"""Smoke test: runs the required capability shapes against a live server.

    python smoke.py [base_url]
"""

from __future__ import annotations

import json
import sys

import requests

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"

QUERIES = [
    "retrieve the top 5 posts of account TEN_GOP",
    "what are the main narratives account JENN_ABRAMS posts about?",
    "retrieve all posts with hashtag #blacklivesmatter",
    "summarize what posts using #fakenews say",
    "most relevant posts about police brutality",
    "what are the dominant narratives about immigration?",
    "show me the full text of the top 3 posts by BLEEPTHEPOLICE",
]


def main() -> int:
    health = requests.get(f"{BASE}/health", timeout=10).json()
    print("health:", json.dumps(health), "\n")

    failures = 0
    for q in QUERIES:
        r = requests.post(f"{BASE}/chat", json={"query": q}, timeout=180)
        r.raise_for_status()
        d = r.json()
        ids = d["source_post_ids"]

        print(f"Q: {q}")
        print(f"   confidence={d['confidence']}  cited={len(ids)}  {ids[:3]}")
        print(f"   {d['answer'][:400]}")
        if "source_post_content" in d:
            print(f"   full_text: {len(d['source_post_content'])} posts")
        if not ids:
            print("   !! no citations")
            failures += 1
        print()

    print("no-citation responses:", failures, "/", len(QUERIES))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
