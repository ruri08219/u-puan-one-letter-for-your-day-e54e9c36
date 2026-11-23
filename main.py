"""One-letter entry: F -- frazzled.

Writes exactly one character, the letter F, to /output/entry.txt.
F stands for "frazzled": the word for a day spent chasing expired
login codes and a fingerprint sensor that only lives in a power button.
"""

import os

LETTER = "F"
MAX_LEN = 1  # the gate requires exactly 1 character, no more, no less


def main():
    if len(LETTER) != MAX_LEN or not LETTER.isalpha() or not LETTER.isupper():
        raise ValueError("entry must be exactly one uppercase letter A-Z")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Read back: prove the file on disk is exactly the letter, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LETTER:
        raise ValueError("read-back mismatch: %r != %r" % (written, LETTER))


if __name__ == "__main__":
    main()
