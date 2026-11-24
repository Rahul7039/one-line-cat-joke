#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — writes a single cat joke to /output/entry.txt."""

import os

JOKE = "Every morning my cat stares at me like I personally cancelled the sun."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)

if __name__ == "__main__":
    main()
