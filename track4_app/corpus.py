"""Corpus loading and indexing.

Loads the frozen dump once at startup into a few in-memory views. The split
between `all_by_id` (everything) and `in_scope` (English only) is the point
where the language rule is enforced: retrieval only ever reads `in_scope`, so
non-English posts cannot influence a finding, while `all_by_id` still lets us
check that a cited ID is real.
"""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import datetime

DUMP_PATH = os.environ.get(
    "T4_DUMP",
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "track4_dataset_nohoneypots",
        "track4_dataset_nohoneypots",
        "dump.json",
    ),
)

IN_SCOPE_LANGUAGE = "English"
_DATE_FORMAT = "%m/%d/%Y %H:%M"
_HASHTAG_RE = re.compile(r"#(\w+)")


class Corpus:
    def __init__(self, posts: list[dict]):
        self.posts = posts
        self.all_by_id: dict[str, dict] = {p["post_id"]: p for p in posts}

        self.in_scope: list[dict] = [
            p for p in posts if p.get("language") == IN_SCOPE_LANGUAGE
        ]

        self.by_author: dict[str, list[dict]] = defaultdict(list)
        self.by_hashtag: dict[str, list[dict]] = defaultdict(list)
        for p in self.in_scope:
            self.by_author[p["author"].upper()].append(p)
            for tag in p["_hashtags"]:
                self.by_hashtag[tag].append(p)

    # -- lookups -----------------------------------------------------------

    def author_posts(self, handle: str) -> list[dict]:
        return self.by_author.get(handle.upper().lstrip("@"), [])

    def hashtag_posts(self, tag: str) -> list[dict]:
        return self.by_hashtag.get(tag.lower().lstrip("#"), [])

    def keyword_posts(self, terms: list[str]) -> list[dict]:
        """Placeholder for topic search until retrieval lands: rank by how many
        of the query terms appear in the post text."""
        terms = [t.lower() for t in terms if t]
        if not terms:
            return []
        scored = []
        for p in self.in_scope:
            text = p["_text_lower"]
            hits = sum(1 for t in terms if t in text)
            if hits:
                scored.append((hits, p))
        scored.sort(key=lambda s: (-s[0], s[1]["post_id"]))
        return [p for _, p in scored]

    def known_authors(self) -> set[str]:
        return set(self.by_author)

    def exists(self, post_id: str) -> bool:
        return post_id in self.all_by_id


def _parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, _DATE_FORMAT)
    except ValueError:
        return None


def load(path: str = DUMP_PATH) -> Corpus:
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)

    for p in raw:
        content = p.get("content") or ""
        p["_text_lower"] = content.lower()
        p["_hashtags"] = [t.lower() for t in _HASHTAG_RE.findall(content)]
        p["_published"] = _parse_date(p.get("publish_date"))

    return Corpus(raw)
