"""Generate XMind workbook from a JSON tree definition.

Usage:
    python generate_xmind.py --feature-slug product-asset-tag
    python generate_xmind.py --tree path/to/tree.json --output docs/foo.xmind

Tree JSON schema — see reference.md in parent skill folder.
Output paths — docs/generate_doc/test-points-xmind/ (see skill SKILL.md).
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any

import xmind

XMIND_OUTPUT_DIR = Path("docs/generate_doc/test-points-xmind")
TREES_DIR = XMIND_OUTPUT_DIR / "trees"


def repo_root() -> Path:
    """Walk up from script location to find repository root (contains docs/)."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "docs" / "generate_doc" / "test-points-xmind").is_dir():
            return parent
        if (parent / "docs").is_dir() and (parent / ".cursor").is_dir():
            return parent
    return Path.cwd()


def paths_for_feature(slug: str, root: Path | None = None) -> tuple[Path, Path]:
    base = (root or repo_root()) / XMIND_OUTPUT_DIR
    tree = base / "trees" / f"{slug}.tree.json"
    output = base / f"{slug}-test-points.xmind"
    return tree, output

META_XML = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<meta xmlns="urn:xmind:xmap:xmlns:meta:2.0" version="2.0">
  <Author><Name>qa-testing-strategy</Name></Author>
</meta>"""

MANIFEST_XML = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<manifest xmlns="urn:xmind:xmap:xmlns:manifest:1.0">
  <file-entry full-path="content.xml" media-type="text/xml"/>
  <file-entry full-path="meta.xml" media-type="text/xml"/>
  <file-entry full-path="styles.xml" media-type="text/xml"/>
  <file-entry full-path="comments.xml" media-type="text/xml"/>
  <file-entry full-path="META-INF/" media-type=""/>
  <file-entry full-path="META-INF/manifest.xml" media-type="text/xml"/>
</manifest>"""

REQUIRED_ZIP_ENTRIES = {
    "content.xml",
    "meta.xml",
    "styles.xml",
    "comments.xml",
    "META-INF/manifest.xml",
}


def add_branch(parent, node: Any) -> None:
    if isinstance(node, str):
        parent.addSubTopic().setTitle(node)
        return
    if not isinstance(node, dict):
        raise TypeError(f"Tree node must be str or dict, got {type(node)}")
    title = node.get("title")
    if not title:
        raise ValueError("Dict node must have non-empty 'title'")
    branch = parent.addSubTopic()
    branch.setTitle(title)
    for child in node.get("children", []):
        add_branch(branch, child)


def load_tree(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if "root_title" not in data or "tree" not in data:
        raise ValueError("Tree JSON must contain 'root_title' and 'tree'")
    return data


def patch_xmind_zip(output: Path) -> None:
    """Add meta.xml + META-INF/manifest.xml required by XMind desktop."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xmind") as tmp:
        tmp_path = Path(tmp.name)

    try:
        with zipfile.ZipFile(output, "r") as src, zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as dst:
            existing = set(src.namelist())
            for name in existing:
                if name in {"meta.xml", "META-INF/manifest.xml"}:
                    continue
                dst.writestr(name, src.read(name))
            dst.writestr("meta.xml", META_XML.encode("utf-8"))
            dst.writestr("META-INF/manifest.xml", MANIFEST_XML.encode("utf-8"))
        tmp_path.replace(output)
    finally:
        if tmp_path.exists() and tmp_path != output:
            tmp_path.unlink(missing_ok=True)


def validate_xmind_zip(output: Path) -> list[str]:
    with zipfile.ZipFile(output, "r") as zf:
        names = set(zf.namelist())
    return sorted(REQUIRED_ZIP_ENTRIES - names)


def generate(tree_data: dict, output: Path) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    workbook = xmind.load(str(output))
    sheet = workbook.getPrimarySheet()
    sheet.setTitle(tree_data.get("sheet_title", "测试点"))
    root = sheet.getRootTopic()
    root.setTitle(tree_data["root_title"])
    for child in tree_data["tree"]:
        add_branch(root, child)
    xmind.save(workbook, str(output))
    patch_xmind_zip(output)

    missing = validate_xmind_zip(output)
    if missing:
        raise RuntimeError(f"XMind zip missing entries after patch: {missing}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate XMind from test-point tree JSON")
    parser.add_argument(
        "--feature-slug",
        help="Feature slug; resolves tree/output under docs/generate_doc/test-points-xmind/",
    )
    parser.add_argument("--tree", type=Path, help="Path to tree JSON file")
    parser.add_argument("--output", type=Path, help="Output .xmind path")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (default: auto-detect)",
    )
    args = parser.parse_args()

    root = args.repo_root or repo_root()

    if args.feature_slug:
        if args.tree or args.output:
            print("Error: use either --feature-slug or both --tree and --output", file=sys.stderr)
            return 1
        tree_path, output_path = paths_for_feature(args.feature_slug, root)
    elif args.tree and args.output:
        tree_path, output_path = args.tree, args.output
        expected_base = (root / XMIND_OUTPUT_DIR).resolve()
        if not tree_path.resolve().is_relative_to(expected_base / "trees"):
            print(
                f"Warning: --tree should be under {expected_base / 'trees'}",
                file=sys.stderr,
            )
        if not output_path.resolve().is_relative_to(expected_base):
            print(
                f"Warning: --output should be under {expected_base}",
                file=sys.stderr,
            )
    else:
        print("Error: provide --feature-slug or both --tree and --output", file=sys.stderr)
        return 1

    if not tree_path.is_file():
        print(f"Error: tree file not found: {tree_path}", file=sys.stderr)
        return 1

    try:
        tree_data = load_tree(tree_path)
        out = generate(tree_data, output_path)
        with zipfile.ZipFile(out, "r") as zf:
            print(f"Generated: {out.resolve()}")
            print(f"Zip entries: {zf.namelist()}")
        return 0
    except (json.JSONDecodeError, ValueError, TypeError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
