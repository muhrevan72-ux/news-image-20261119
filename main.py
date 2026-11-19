#!/usr/bin/env python3
"""World News in One Image — 19 November 2026 (make.fun bounty).

Submission program, Python 3.13 standard library only.
It copies the entry image held in this repository to the output
directory the grader provides, exactly as the starter entry does.

The image itself was drawn locally by render.py (Pillow + DejaVu,
a local build tool only — it is not run by the grader).
main.py uses only the standard library, needs no network, and is
deterministic: running it twice writes the same bytes.

Usage (outside the grader):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    # writes out/entry.png
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
