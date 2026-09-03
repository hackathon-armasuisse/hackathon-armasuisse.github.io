"""Query routing.

Turns a free-text analyst question into a scope (which posts) plus an intent
(what to do with them). Deliberately regex-driven for this iteration: two of
the three required capabilities are exact filters, not search, so they should
never go through a ranker.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from corpus import Corpus

_STOPWORDS = {
    "a", "about", "all", "and", "any", "are", "account", "accounts", "by",
    "can", "content", "corpus", "do", "does", "dominant", "for", "from",
    "full", "get", "give", "hashtag", "have", "how", "in", "is", "it", "its",
    "list", "main", "many", "me", "most", "much", "narrative", "narratives",
    "of", "on", "or", "post", "posts", "relevant", "retrieve", "say", "show",
    "some", "summarise", "summarize", "text", "that", "the", "their", "them",
    "these", "they", "this", "to", "top", "tweet", "tweets", "use", "used",
    "using", "was", "what", "which", "who", "with", "write",
}

_HASHTAG_RE = re.compile(r"#(\w+)")
_HANDLE_RE = re.compile(r"@(\w+)")
_TOPK_RE = re.compile(r"\btop[\s-]*(\d{1,3})\b|\b(\d{1,3})\s+(?:most|posts|tweets)\b", re.I)
_HASHTAG_WORD_RE = re.compile(r"\bhashtags?\s+[\"']?#?(\w+)", re.I)
_ACCOUNT_WORD_RE = re.compile(
    r"\b(?:account|author|handle|user|posted by|posts by|tweets by|from)\s+[\"']?@?([A-Za-z0-9_]+)",
    re.I,
)
_SUMMARY_RE = re.compile(
    r"\b(summar\w+|narrative|narratives|theme|themes|topic|topics|about what|"
    r"main|dominant|what do|what does|what are)\b",
    re.I,
)
_FULLTEXT_RE = re.compile(
    r"\b(full text|verbatim|exact wording|word for word|show (?:me )?the (?:posts?|tweets?|text)|"
    r"quote|content of)\b",
    re.I,
)

DEFAULT_TOP_K = 10
MAX_TOP_K = 100


@dataclass
class Route:
    scope: str                      # account | hashtag | topic
    intent: str                     # retrieve | summarize
    query_text: str = ""
    posts: list[dict] = field(default_factory=list)
    target: str | None = None       # the handle or tag that was matched
    top_k: int = DEFAULT_TOP_K
    want_full_text: bool = False
    total_matches: int = 0


def _extract_top_k(query: str) -> tuple[int, bool]:
    """Returns (k, explicit). 'all posts' means no limit."""
    if re.search(r"\ball\b", query, re.I):
        return MAX_TOP_K, True
    m = _TOPK_RE.search(query)
    if m:
        k = int(m.group(1) or m.group(2))
        return max(1, min(k, MAX_TOP_K)), True
    return DEFAULT_TOP_K, False


def _find_author(query: str, corpus: Corpus) -> str | None:
    known = corpus.known_authors()

    m = _HANDLE_RE.search(query)
    if m and m.group(1).upper() in known:
        return m.group(1).upper()

    m = _ACCOUNT_WORD_RE.search(query)
    if m and m.group(1).upper() in known:
        return m.group(1).upper()

    # Bare handle anywhere in the query, longest match first so that a handle
    # containing another one as a substring still wins.
    for token in sorted(re.findall(r"[A-Za-z0-9_]{3,}", query), key=len, reverse=True):
        if token.upper() in known:
            return token.upper()
    return None


def _find_hashtag(query: str, corpus: Corpus) -> str | None:
    m = _HASHTAG_RE.search(query)
    if m:
        return m.group(1).lower()
    m = _HASHTAG_WORD_RE.search(query)
    if m and corpus.hashtag_posts(m.group(1)):
        return m.group(1).lower()
    return None


def _keywords(query: str) -> list[str]:
    words = re.findall(r"[A-Za-z0-9']{3,}", query.lower())
    return [w for w in words if w not in _STOPWORDS]


def route(query: str, corpus: Corpus) -> Route:
    top_k, _ = _extract_top_k(query)
    want_full_text = bool(_FULLTEXT_RE.search(query))
    intent = "summarize" if _SUMMARY_RE.search(query) else "retrieve"

    common = dict(
        intent=intent,
        query_text=query,
        top_k=top_k,
        want_full_text=want_full_text,
    )

    tag = _find_hashtag(query, corpus)
    if tag:
        posts = corpus.hashtag_posts(tag)
        return Route(scope="hashtag", posts=posts, target=f"#{tag}",
                     total_matches=len(posts), **common)

    author = _find_author(query, corpus)
    if author:
        posts = corpus.author_posts(author)
        return Route(scope="account", posts=posts, target=author,
                     total_matches=len(posts), **common)

    terms = _keywords(query)
    posts = corpus.keyword_posts(terms)
    return Route(scope="topic", posts=posts, target=" ".join(terms) or None,
                 total_matches=len(posts), **common)
