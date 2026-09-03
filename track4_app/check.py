"""Acceptance checks against a live server.

Asserts the contract properties that the criteria treat as hard failures:
every cited ID exists in the dump, every ID written inline in the answer is
one of the cited IDs, and no non-English post is ever surfaced.
"""

from __future__ import annotations

import json
import re
import sys

import requests

import corpus as corpus_mod

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
ID_RE = re.compile(r"T4-\d{6}")

QUERIES = [
    "retrieve the top 5 posts of account TEN_GOP",
    "what are the main narratives account JENN_ABRAMS posts about?",
    "summarize what posts using #fakenews say",
    "what are the dominant narratives about immigration?",
    "show me the full text of the top 3 posts by BLEEPTHEPOLICE",
]

C = corpus_mod.load()
IN_SCOPE = {p["post_id"] for p in C.in_scope}


def check(q: str) -> list[str]:
    d = requests.post(f"{BASE}/chat", json={"query": q}, timeout=300).json()
    ids, ans = d["source_post_ids"], d["answer"]
    errs = []

    for pid in ids:
        if not C.exists(pid):
            errs.append(f"fabricated id in source_post_ids: {pid}")
        elif pid not in IN_SCOPE:
            errs.append(f"non-English post cited: {pid}")

    for pid in set(ID_RE.findall(ans)):
        if pid not in ids:
            errs.append(f"answer cites {pid} which is not in source_post_ids")

    if "[removed: unverified id]" in ans:
        errs.append("model produced an id outside its context (stripped)")
    if not 0.0 <= d["confidence"] <= 1.0:
        errs.append(f"confidence out of range: {d['confidence']}")
    if "source_post_content" in d and len(d["source_post_content"]) != len(ids):
        errs.append("source_post_content length does not match source_post_ids")
    return errs


def main() -> int:
    total = 0
    for q in QUERIES:
        errs = check(q)
        total += len(errs)
        print(("PASS  " if not errs else "FAIL  ") + q)
        for e in errs:
            print("        -", e)
    print(f"\n{total} violation(s)")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
