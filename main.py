#!/usr/bin/env python3
"""Writes a one-line office joke to /output/entry.txt."""

import os

ENTRY = (
    "I told HR my spirit animal is the office printer: I only work "
    "when nobody is watching, and I jam under pressure."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
