"""Houseplant Out-of-Office entry.

Writes the funniest out-of-office auto-reply a houseplant would send
(120 characters or fewer) to /output/entry.txt.

The line: a fern that has not been watered since March, answering
email the only way a plant can — by waiting for rain.
"""

import os

LINE = "Thanks for your email. I haven't been watered since March. I'll get back to you when it rains."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"entry is {len(LINE)} chars, must be 1-120"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
