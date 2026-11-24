"""Houseplant Out-of-Office entry.

Writes the funniest out-of-office auto-reply a houseplant would send
(120 characters or fewer) to /output/entry.txt.

The line: a fern that has not been watered since March, answering
email the only way a plant can — by waiting for rain.
"""

import os

LINE = "Thanks for your email. I haven't been watered since March. I'll get back to you when it rains."

OUTPUT_PATH = "/output/entry.txt"


def _validate(line: str) -> str:
    """Fail closed: entry must be exactly one non-blank line, 1-120 chars."""
    if not line or line != line.strip():
        raise ValueError("entry must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must not contain line breaks")
    if not 1 <= len(line) <= 120:
        raise ValueError(f"entry is {len(line)} chars, must be 1-120")
    return line


def main() -> None:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
