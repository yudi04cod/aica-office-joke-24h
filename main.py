#!/usr/bin/env python3
"""Write a one-line office joke to /output/entry.txt.

The joke is validated before it is written: it must be exactly one
line, with no newline in the middle and no surrounding whitespace,
and it must stay within the 200-character limit for a one-line entry.
"""

import os

ENTRY = (
    "I told HR my spirit animal is the office printer: I only work "
    "when nobody is watching, and I jam under pressure."
)


def validate(entry: str) -> None:
    """Make sure the entry is a single line within the length limit."""
    assert len(entry) <= 200, "entry is too long"
    assert "\n" not in entry, "entry must be a single line"
    assert entry == entry.strip(), "entry must have no surrounding whitespace"


def main() -> None:
    # Validate first so a malformed entry never reaches the output file.
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
