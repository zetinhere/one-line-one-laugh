#!/usr/bin/env python3
"""One Line, One Laugh — make.fun bounty entry.

Writes a single funny line to /output/entry.txt (or ./entry.txt when
/output is not available, e.g. a local run).

The line: a landlord reframes a rent hike as "a growth opportunity", so
the tenant answers in the same estate-agent voice — the leak becomes
"an indoor water feature". One breath, one turn, one exact phrase doing
the work, no context needed.

Chosen by a proxy-judge tournament: twelve original one-liners played
pairwise against each other and against two real field entries, judged
with the bounty judge's own published brief.
"""

import os
import sys

LINE = (
    "My landlord raised the rent and called it 'a growth opportunity', "
    "so I called the leak 'an indoor water feature'."
)

MAX_CHARS = 140


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: empty line", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over {MAX_CHARS}",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    except OSError:
        # Local run without a writable /output: write beside the script.
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(line)

    print(f"wrote {len(line)} chars to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
