#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — writes a single cat joke to /output/entry.txt.

The joke is kept as ordered clauses and assembled at run time, so each
part of the line lives in exactly one place. The assembled line is written
verbatim (no trailing newline) to /output/entry.txt and printed.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# Clauses of the joke, in order. Joined with single spaces; the closing
# full stop is appended by build_joke().
_CLAUSES = (
    "Every morning",
    "my cat",
    "stares at me",
    "like I personally cancelled the sun",
)


def build_joke():
    """Assemble the single-line joke from its clauses."""
    return " ".join(_CLAUSES) + "."


def write_entry(line):
    """Write the joke line to the entry file, creating /output if needed."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    return OUTPUT_PATH


def main():
    line = build_joke()
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
