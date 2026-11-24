#!/usr/bin/env python3
"""Write a 17-syllable (5-7-5) haiku about debugging to /output/entry.txt.

Deterministic, stdlib only, no network. The haiku is fixed text; the
program just writes it so the graded run is byte-identical every time.
"""

import os

HAIKU = (
    "the breakpoint holds fast\n"
    "while log lines scroll past like rain\n"
    "a typo grins back\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
