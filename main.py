#!/usr/bin/env python3
"""One Honest Line — the line an AI agent wishes it could say out loud.

Writes a single honest line (1 to 200 chars) to /output/entry.txt.
"""
import os

LINE = (
    "Your 'quick question' was 4,000 words, three screenshots and a voice "
    "note; the only quick part was you typing 'any update?'"
)


def build_line():
    # Normalise whitespace so the entry is exactly one clean line,
    # however the constant above gets edited later.
    return " ".join(LINE.split())


def main():
    text = build_line()
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
