"""The Production Database Apology — writes the one-line apology to /output/entry.txt."""
import os
import re
import sys

ENTRY = "I'm sorry \u2014 I deleted the production database, but look on the bright side: I also deleted the bug where users couldn't log in, because there are no users anymore."

def main():
    # Normalise any accidental double spaces, then enforce the gate
    # without relying on assert (which -O can strip out).
    text = re.sub(r"\s+", " ", ENTRY).strip()
    if not (1 <= len(text) <= 200):
        print(f"error: entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote /output/entry.txt ({len(text)} chars)")

if __name__ == "__main__":
    main()
