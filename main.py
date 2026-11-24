#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — entry program.

Writes one line (under 200 characters) to /output/entry.txt: a dog,
caught red-pawed, explains why the homework got eaten.

The joke: the teacher called "the dog ate my homework" the oldest
excuse in the book — so the dog ate the book too. A meta-twist on
the cliche itself, in a dog's voice, with zero human shame.
"""

import os

LINE = "You said 'the dog ate my homework' was the oldest excuse in the book, so I ate the book too."


def main():
    if len(LINE) > 200:
        raise ValueError("entry line exceeds 200 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
