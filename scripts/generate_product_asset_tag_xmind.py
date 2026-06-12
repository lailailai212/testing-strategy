"""Regenerate Product Asset Tag test-point XMind from tree JSON.

Prefer the generic skill script:
  .cursor/skills/test-points-xmind/scripts/generate_xmind.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XMIND_DIR = ROOT / "docs" / "generate_doc" / "test-points-xmind"
TREE = XMIND_DIR / "trees" / "product-asset-tag.tree.json"
OUTPUT = XMIND_DIR / "product-asset-tag-test-points.xmind"
GENERATOR = ROOT / ".cursor" / "skills" / "test-points-xmind" / "scripts" / "generate_xmind.py"


def main() -> int:
    cmd = [
        sys.executable,
        str(GENERATOR),
        "--feature-slug",
        "product-asset-tag",
    ]
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
