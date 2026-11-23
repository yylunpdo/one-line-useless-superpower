#!/usr/bin/env python3
"""One line, zero use: a hilariously useless superpower.

Entry for make.fun bounty u-daring-gecko-25-one-line-zero-use-the-useless-01ca1c68.
Prints the single original line (at most 200 characters).
"""

LINE = "I can teleport anywhere — but only three centimetres to the left, and only when nobody is watching."


def main() -> None:
    assert len(LINE) <= 200, f"line is {len(LINE)} characters, over the 200 limit"
    assert LINE.count("\n") == 0, "the entry must be a single line"
    print(LINE)


if __name__ == "__main__":
    main()
