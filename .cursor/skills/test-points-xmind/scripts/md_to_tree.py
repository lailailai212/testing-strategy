"""Convert acceptance (test-points) Markdown to XMind tree JSON.

Reads docs/sprints/{sprint}/features/{slug}/acceptance.md tables under ## 测试点.
Leaf nodes: title, source, priority (no TP-ID).

Usage:
    python md_to_tree.py --feature-slug self-reg-001-05-domain-whitelist
    python md_to_tree.py --feature-slug assets-card-customization --sprint OBIS-20260622-20260703
    python md_to_tree.py --md path/to.md --output path/to.tree.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[4]
if str(_REPO / "scripts") not in sys.path:
    sys.path.insert(0, str(_REPO / "scripts"))

from feature_paths import (  # noqa: E402
    acceptance_path,
    repo_root_from,
    tree_path as sprint_tree_path,
)

SECTION_RE = re.compile(r"^###\s+(.+)$")
TABLE_ROW_RE = re.compile(
    r"^\|\s*(TP-[\w-]+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*(.+?)\s*\|$"
)


def repo_root() -> Path:
    return repo_root_from(Path(__file__))


def parse_md(md_text: str, root_title: str, sheet_title: str) -> dict:
    in_test_points = False
    current_section: str | None = None
    module_key: str | None = None
    modules: dict[str, dict] = {}

    for raw_line in md_text.splitlines():
        line = raw_line.strip()
        if line.startswith("## 测试点"):
            in_test_points = True
            continue
        if in_test_points and line.startswith("## ") and not line.startswith("### "):
            break
        if not in_test_points:
            continue

        sec = SECTION_RE.match(line)
        if sec:
            current_section = sec.group(1).strip()
            module_key = current_section.split("—", 1)[0].strip()
            if module_key not in modules:
                modules[module_key] = {"title": module_key, "children": {}}
            if current_section not in modules[module_key]["children"]:
                modules[module_key]["children"][current_section] = []
            continue

        row = TABLE_ROW_RE.match(line)
        if row and current_section and module_key:
            tp_id, source, priority, title = (c.strip() for c in row.groups())
            if tp_id.upper() == "TP-ID" or source == "来源":
                continue
            leaf = {"title": title, "source": source, "priority": priority}
            modules[module_key]["children"][current_section].append(leaf)

    tree = []
    for mod in modules.values():
        mod_branch = {"title": mod["title"], "children": []}
        for subsection, leaves in mod["children"].items():
            if subsection == mod["title"]:
                mod_branch["children"].extend(leaves)
            else:
                sub_title = subsection.split("—", 1)[-1].strip() if "—" in subsection else subsection
                mod_branch["children"].append({"title": sub_title, "children": leaves})
        tree.append(mod_branch)

    return {
        "sheet_title": sheet_title,
        "root_title": root_title,
        "tree": tree,
    }


def extract_title(md_text: str) -> tuple[str, str]:
    for line in md_text.splitlines():
        if line.startswith("# Story:"):
            root = line.replace("# Story:", "").strip()
            return root, f"{root} 测试点"
    return "测试点", "测试点"


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert acceptance MD to tree JSON")
    parser.add_argument(
        "--feature-slug",
        help="Feature slug; resolves via docs/sprints/features-registry.json",
    )
    parser.add_argument(
        "--sprint",
        help="Sprint id (optional if slug is registered)",
    )
    parser.add_argument("--md", type=Path, help="Input markdown path")
    parser.add_argument("--output", type=Path, help="Output tree JSON path")
    parser.add_argument("--repo-root", type=Path, default=None)
    args = parser.parse_args()

    root = args.repo_root or repo_root()

    if args.feature_slug:
        if args.md or args.output:
            print("Error: use either --feature-slug or both --md and --output", file=sys.stderr)
            return 1
        try:
            md_path = acceptance_path(args.feature_slug, args.sprint, root)
            out_path = sprint_tree_path(args.feature_slug, args.sprint, root)
        except KeyError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    elif args.md and args.output:
        md_path, out_path = args.md, args.output
    else:
        print("Error: provide --feature-slug or both --md and --output", file=sys.stderr)
        return 1

    if not md_path.is_file():
        print(f"Error: MD not found: {md_path}", file=sys.stderr)
        return 1

    text = md_path.read_text(encoding="utf-8")
    root_title, sheet_title = extract_title(text)
    data = parse_md(text, root_title, sheet_title)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    leaf_count = sum(
        1
        for mod in data["tree"]
        for child in mod.get("children", [])
        for _ in (child if isinstance(child, dict) and "source" in child else child.get("children", []) if isinstance(child, dict) else [])
    )
    # simpler count
    def count_leaves(nodes):
        n = 0
        for node in nodes:
            if isinstance(node, dict):
                if node.get("children"):
                    n += count_leaves(node["children"])
                elif "title" in node and "source" in node:
                    n += 1
        return n

    print(f"Wrote: {out_path.resolve()} ({count_leaves(data['tree'])} leaves)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
