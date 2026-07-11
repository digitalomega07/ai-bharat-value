#!/usr/bin/env python3
"""Check a Markdown research report for mandatory disclosure sections."""

import argparse
from pathlib import Path

REQUIRED_TERMS = {
    "as-of date": ("as-of", "as of"),
    "sources": ("source", "sources"),
    "limitations": ("limitation", "limitations", "data gap"),
    "verdict": ("verdict", "research conclusion"),
    "thesis falsification": ("kill condition", "kill trigger", "falsif"),
    "research disclaimer": ("not personalized investment advice", "research and education"),
}


def check(text):
    lower = text.lower()
    return [label for label, terms in REQUIRED_TERMS.items() if not any(term in lower for term in terms)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report")
    args = parser.parse_args()
    path = Path(args.report)
    missing = check(path.read_text(encoding="utf-8"))
    if missing:
        print("FAIL: missing " + ", ".join(missing))
        raise SystemExit(1)
    print("PASS: mandatory report disclosures found")


if __name__ == "__main__":
    main()

