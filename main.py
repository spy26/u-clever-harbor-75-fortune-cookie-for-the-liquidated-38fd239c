#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes a single fortune-cookie line to <output dir>/entry.txt.

Deterministic: no randomness, no network, no secrets, no git reads.
The output directory is $MAKEFUN_OUTPUT_DIR, defaulting to /output
(the harness mount). Locally: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

FORTUNE = (
    "The stars say your portfolio has reached enlightenment: "
    "it now owns nothing, and wants for nothing."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: entry.txt holds exactly the fortune bytes.
    (output_dir / "entry.txt").write_bytes(FORTUNE.encode("utf-8"))
    print(FORTUNE)


if __name__ == "__main__":
    main()
