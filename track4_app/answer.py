"""Answer construction.

Citations, counts and confidence are computed here in Python. The LLM is used
only for the summarize intent, and its output is never allowed to introduce a
post ID: the cited set is fixed before the model is called.
"""

from __future__ import annotations

import re
from collections import Counter

from corpus import Corpus
from llm import LLMUnavailable, chat
from router import Route

SUMMARY_SYSTEM = (
    "You are an OSINT analyst assistant summarising social-media posts.\n"
    "You are given a list of posts retrieved from a frozen corpus. Each line "
    "starts with that post's identifier in square brackets, like [T4-001234].\n"
    "Describe the recurring narratives, themes and framing devices across them.\n"
    "Be concrete and specific; name the actual topics, not generic categories.\n"
    "Support each claim by citing the identifiers it comes from, written inline "
    "in parentheses exactly as shown, e.g. (T4-001234, T4-005678).\n"
    "Only ever cite identifiers that appear in the list. Never write an "
    "identifier that is not shown, and never cite by list position.\n"
    "Base every statement on the posts shown. Do not speculate beyond them and "
    "do not invent posts, accounts, events or identifiers.\n"
    "Write 3-6 sentences of plain prose. Do not use bullet points or headings."
)

_ID_RE = re.compile(r"T4-\d{6}")

MAX_SNIPPETS = 40


def _snippets(posts: list[dict]) -> str:
    return "\n".join(
        f"[{p['post_id']}] {p['author']} ({p['publish_date']}): {p['content']}"
        for p in posts
    )


def _strip_unknown_ids(text: str, allowed: set[str]) -> str:
    """Drop any identifier the model produced that was not in its own context.

    The cited set is fixed before the model runs, so anything outside it is a
    fabrication and must not reach the analyst.
    """
    invented = {i for i in _ID_RE.findall(text) if i not in allowed}
    for bad in invented:
        text = text.replace(bad, "[removed: unverified id]")
    return text


def confidence(route: Route, n_cited: int) -> float:
    """Support-driven, not model-chosen. Exact filters (account, hashtag) are
    more trustworthy than the placeholder keyword match."""
    if n_cited == 0:
        return 0.0
    if n_cited == 1:
        base = 0.25
    elif n_cited < 5:
        base = 0.5
    elif n_cited < 10:
        base = 0.75
    else:
        base = 0.9
    if route.scope == "topic":
        base *= 0.8
    return round(base, 2)


def _describe_scope(route: Route) -> str:
    if route.scope == "hashtag":
        return f"hashtag {route.target}"
    if route.scope == "account":
        return f"account {route.target}"
    return f"the terms '{route.target}'" if route.target else "the query"


def _retrieve_answer(route: Route, cited: list[dict]) -> str:
    scope = _describe_scope(route)
    if not cited:
        return f"No posts in the corpus match {scope}."

    shown = len(cited)
    total = route.total_matches
    head = (
        f"Found {total} post{'s' if total != 1 else ''} matching {scope}"
        + (f"; citing the first {shown}." if shown < total else ".")
    )

    authors = Counter(p["author"] for p in cited)
    if route.scope != "account" and len(authors) > 1:
        top = ", ".join(f"{a} ({n})" for a, n in authors.most_common(3))
        head += f" Most frequent authors among them: {top}."

    dates = [p["_published"] for p in cited if p["_published"]]
    if dates:
        head += (
            f" They span {min(dates):%Y-%m-%d} to {max(dates):%Y-%m-%d}."
        )
    return head


def _summarize_answer(route: Route, cited: list[dict]) -> str:
    scope = _describe_scope(route)
    if not cited:
        return f"No posts in the corpus match {scope}, so there is nothing to summarise."

    prompt = (
        f"Analyst question: {route.query_text}\n\n"
        f"Posts retrieved for {scope} ({len(cited)} shown"
        + (f" of {route.total_matches} matching" if route.total_matches > len(cited) else "")
        + "):\n"
        + _snippets(cited[:MAX_SNIPPETS])
    )
    try:
        body = chat(SUMMARY_SYSTEM, prompt)
    except LLMUnavailable as exc:
        return (
            f"Found {route.total_matches} posts matching {scope}, but the summarisation "
            f"model is unavailable ({exc}). The cited posts are returned unsummarised."
        )
    return _strip_unknown_ids(body, {p["post_id"] for p in cited[:MAX_SNIPPETS]})


def build(route: Route, corpus: Corpus) -> dict:
    cited = route.posts[: route.top_k]

    # Nothing may be cited that is not a real post in the dump.
    cited = [p for p in cited if corpus.exists(p["post_id"])]

    if route.intent == "summarize":
        text = _summarize_answer(route, cited)
    else:
        text = _retrieve_answer(route, cited)

    result = {
        "answer": text,
        "source_post_ids": [p["post_id"] for p in cited],
        "confidence": confidence(route, len(cited)),
    }
    if route.want_full_text:
        result["source_post_content"] = [p["content"] for p in cited]
    return result
