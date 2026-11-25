#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one original crypto-trading joke line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

from pathlib import Path

JOKE = "My group chat called it a generational buying opportunity. Three dips later, we renamed the chat 'Support Group'."

def validate(text: str) -> str:
    """Strip and gate-check the joke line; returns the cleaned text."""
    cleaned = text.strip()
    assert 1 <= len(cleaned) <= 200, f"joke is {len(cleaned)} chars, must be 1-200"
    assert cleaned.strip(), "joke must not be only whitespace"
    return cleaned

def write_entry(text: str, path: Path) -> int:
    """Write the validated joke to path (creating parents) and return its length."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return len(text)

def main() -> None:
    text = validate(JOKE)
    out = Path("/output/entry.txt")
    print(f"wrote {write_entry(text, out)} chars to {out}")

if __name__ == "__main__":
    main()
