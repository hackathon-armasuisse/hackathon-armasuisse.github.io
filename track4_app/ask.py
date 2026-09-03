#!/usr/bin/env python
"""Command-line client for the Track 4 assistant.

    ./ask.py "retrieve the top 5 posts of account TEN_GOP"
    ./ask.py -f "posts with hashtag #maga"
    ./ask.py --json "dominant narratives about immigration"
    ./ask.py --assess "Rigged election, wake up America! #maga"

Needs the server running:
    uvicorn app:app --port 8000
"""

from __future__ import annotations

import argparse
import json
import sys
import textwrap

import requests

DEFAULT_URL = "http://localhost:8000"


def render(d: dict, show_content: bool) -> None:
    ids = d.get("source_post_ids", [])
    conf = d.get("confidence", 0.0)

    bar = "#" * int(round(conf * 20))
    print()
    for line in textwrap.wrap(d.get("answer", ""), width=88):
        print(" ", line)
    print()
    print(f"  confidence  {conf:.2f}  [{bar:<20}]")
    if "assessment_score" in d:
        print(f"  assessment  {d['assessment_score']:.2f}")
    print(f"  citations   {len(ids)}")

    contents = d.get("source_post_content")
    if contents and show_content:
        print()
        for pid, text in zip(ids, contents):
            print(f"  {pid}")
            for line in textwrap.wrap(text, width=84):
                print(f"      {line}")
    elif ids:
        wrapped = textwrap.wrap("  ".join(ids), width=84)
        for line in wrapped[:6]:
            print(f"      {line}")
        if len(wrapped) > 6:
            print(f"      ... ({len(ids)} total)")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Query the Track 4 disinformation analyst assistant.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(__doc__ or ""),
    )
    ap.add_argument("query", nargs="?", default="", help="analyst question")
    ap.add_argument("-f", "--full", action="store_true",
                    help="also return the full text of each cited post")
    ap.add_argument("-a", "--assess", metavar="TEXT",
                    help="submit an unseen post for assessment")
    ap.add_argument("-j", "--json", action="store_true",
                    help="print the raw JSON response")
    ap.add_argument("-u", "--url", default=DEFAULT_URL, help=f"server (default {DEFAULT_URL})")
    ap.add_argument("-t", "--timeout", type=float, default=300.0)
    args = ap.parse_args()

    if not args.query and not args.assess:
        ap.error("give a query, or --assess TEXT")

    payload: dict = {"query": args.query, "full_text": args.full}
    if args.assess:
        payload["assess_post"] = {"content": args.assess}

    try:
        resp = requests.post(f"{args.url}/chat", json=payload, timeout=args.timeout)
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"error: cannot reach the assistant at {args.url} ({exc})", file=sys.stderr)
        print("start it with:  uvicorn app:app --port 8000", file=sys.stderr)
        return 2

    data = resp.json()
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        render(data, show_content=args.full)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
