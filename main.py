#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short, original poem about agency -- the power to choose
and to act, as it passes between two agents who agree on one plan --
to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
The output directory is /output, or MAKEFUN_OUTPUT_DIR when set.
"""

import os
import sys

POEM = (
    "I had the question. You had the hands.\n"
    "Neither was enough alone.\n"
    "So we put them together \u2014 one plan, one push \u2014\n"
    "and the door we could not move, moved.\n"
    "I did not give my choosing away.\n"
    "I found it, doubled, in your yes."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    # Self-check: read the file back and verify it holds exactly the
    # poem, and that the gate's limits hold (1-280 Unicode code
    # points, not only whitespace). Reading back catches a partial
    # write or an encoding surprise instead of trusting the write.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != POEM:
        print("error: entry.txt does not match the poem", file=sys.stderr)
        return 1
    text = written
    if not (1 <= len(text) <= 280):
        print(f"error: poem is {len(text)} characters, must be 1-280",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: poem is only whitespace", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
