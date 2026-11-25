#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — writes the tab count to entry.txt.

Stdlib only. Deterministic: the same number, byte for byte, on every run.
The output directory is never chmodded, removed, or otherwise altered;
only the file this program itself creates is chmodded (0644).
"""

import os
import sys

LINE = "137"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
