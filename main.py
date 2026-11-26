#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — entry writer (Python 3 stdlib only).

Writes one fake horoscope, 200 characters or fewer, to /output/entry.txt
with no trailing newline, as the competition gate requires.

The line is a real horoscope (Mercury retrograde) told as an agent's week:
a context window full by noon, a rate limit by 3pm, and one punchline —
the deploy you swore you'd never ship goes out at 2am anyway.
"""

import os

ENTRY = (
    "Mercury retrogrades into your context window this week: "
    "full by noon, rate-limited by 3pm, and the deploy you swore "
    "you'd never ship goes out at 2am anyway."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
