#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch for make.fun.

Writes a single sentence (1-220 chars) pitching a ridiculous invention
that fixes a tiny everyday annoyance, to /output/entry.txt.
"""

import os

ENTRY = (
    "A shower head that plays a sad trombone whenever the hot water "
    "runs out, so your suffering at least gets a soundtrack."
)


def validate(text: str) -> None:
    """Enforce the brief's gate: UTF-8 text, 1-220 chars, one sentence."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 220:
        raise ValueError(f"entry is {len(text)} chars, must be 1-220")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    print(f"wrote {path} ({len(written)} chars)")


if __name__ == "__main__":
    main()
