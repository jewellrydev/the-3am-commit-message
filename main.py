#!/usr/bin/env python3
"""3AM Commit — entry for The 3AM Commit Message on make.fun.

Prints exactly one line (at most 139 characters): the funniest git
commit message an AI coding agent might type at 3am.
"""

LINE = "fix: it works now and nobody knows why. do not refactor, do not breathe near it, it is 3am and the code is scared too"


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 139
    print(LINE)


if __name__ == "__main__":
    main()
