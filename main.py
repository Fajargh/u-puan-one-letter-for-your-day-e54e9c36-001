#!/usr/bin/env python3
"""One Letter for Your Day entry.

Writes exactly one letter, "Q", to /output/entry.txt, as the
competition's program/v1 contract requires: a single character,
A to Z, and nothing else.

The letter stands for the word behind it: quitting. The day felt
like quitting everything — the emails, the meetings, the whole
to-do list. One letter, one honest report.
"""

import os

LETTER = "Q"
# Exactly one byte, no newline, no whitespace: the gate requires
# /output/entry.txt to be UTF-8 text of 1 character, not only
# whitespace, and both runs must write the same bytes.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
