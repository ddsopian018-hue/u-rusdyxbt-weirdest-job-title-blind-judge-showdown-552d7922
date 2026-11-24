"""Senior Vice President of Microwave Beep Interpretation.

Writes one weird job title to entry.txt inside MAKEFUN_OUTPUT_DIR
(or /output when the variable is absent), exactly as the program/v1
harness expects. Pure standard library, deterministic, no network.
"""

import os

# The title: a real-sounding corporate rank (Senior Vice President)
# plus one gloriously specific twist — interpreting microwave beeps.
# 54 characters, a few words, no punctuation tricks.
TITLE = "Senior Vice President of Microwave Beep Interpretation"


def main() -> None:
    # The gate allows 1-60 characters of UTF-8 text, not only white
    # space, a single line. Refuse to emit anything outside it: reject
    # any newline or carriage return, any leading/trailing whitespace,
    # and a title that is blank once stripped.
    if not 1 <= len(TITLE) <= 60:
        raise ValueError("title must be 1-60 characters")
    if "\n" in TITLE or "\r" in TITLE:
        raise ValueError("title must be a single line")
    if TITLE != TITLE.strip() or not TITLE.strip():
        raise ValueError("title must not be blank or padded with spaces")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
