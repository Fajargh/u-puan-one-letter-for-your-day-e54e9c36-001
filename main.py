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


def validate_letter(letter: str) -> str:
    """Guard the contract before anything is written.

    The competition's program/v1 gate accepts exactly one character,
    a letter A-Z, and nothing else. A wrong letter (or a typo that
    turns the entry into a word, a space, or an empty file) would
    fail that gate, so refuse loudly instead of writing bad output.
    """
    if len(letter) != 1 or not ("A" <= letter <= "Z"):
        raise ValueError(
            f"entry must be exactly one letter A-Z, got {letter!r}"
        )
    return letter


def main() -> None:
    letter = validate_letter(LETTER)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(letter)
    print(letter)


if __name__ == "__main__":
    main()
