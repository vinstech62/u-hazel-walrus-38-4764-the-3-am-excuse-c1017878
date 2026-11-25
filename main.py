#!/usr/bin/env python3
"""The 3 AM Excuse.

A hardware wallet refuses to sign a transaction at 3 AM.
Its secure element is on strike until sunrise.
Writes that one-line excuse to /output/entry.txt.
Deterministic: constant string, no randomness, no clock, no network.
"""

import os

EXCUSE = (
    "My secure element went on strike: no signatures "
    "between 2 and 4 AM. Negotiations resume at sunrise."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Internal guards: single line, 1-200 UTF-8 characters.
    assert isinstance(EXCUSE, str)
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be a single line"
    assert 1 <= len(EXCUSE) <= 200, f"excuse length {len(EXCUSE)} out of range 1-200"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    # Guard: verify the file on disk is byte-for-byte the excuse,
    # Also bounds the entry to the 1-200 character window.
    # one line, within the 1-200 character limit.
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    assert written == EXCUSE, "entry.txt mismatch"
    assert 1 <= len(written) <= 200, "entry.txt out of range"


if __name__ == "__main__":
    main()
