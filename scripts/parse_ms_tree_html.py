"""Parse MeterSphere module tree HTML and update metersphere-modules.json."""
from __future__ import annotations

import html as html_lib
import json
import re
import sys
from pathlib import Path

NODE_RE = re.compile(
    r'<div class="arco-tree-node[^"]*"[^>]*'
    r'data-level="(\d+)"[^>]*'
    r'data-key="([^"]+)"[^>]*'
    r'type="([^"]+)"[^>]*'
    r'(?:count="(\d+)"[^>]*)?'
    r'path="([^"]+)"',
    re.DOTALL,
)

LEAF_RE = re.compile(r'arco-tree-node-is-leaf')


def parse_nodes(html: str) -> list[dict]:
    nodes = []
    for m in NODE_RE.finditer(html):
        level, key, typ, count, path = m.groups()
        if typ.upper() == "MODULE" or key == "root":
            start = m.start()
            chunk = html[start : start + 500]
            is_leaf = "arco-tree-node-is-leaf" in chunk
            nodes.append(
                {
                    "path": html_lib.unescape(path),
                    "level": int(level),
                    "key": key,
                    "case_count": int(count or 0),
                    "is_leaf": is_leaf,
                }
            )
    return nodes


def build_tree(nodes: list[dict]) -> list[dict]:
    by_path = {n["path"]: n for n in nodes}
    roots: list[dict] = []

    def node_dict(n: dict) -> dict:
        parts = n["path"].strip("/").split("/")
        name = parts[-1] if parts and parts[0] else n["path"]
        return {
            "path": n["path"],
            "level": n["level"],
            "name": name,
            "case_count": n["case_count"],
            "is_leaf": n["is_leaf"],
        }

    children_map: dict[str, list[dict]] = {}
    for n in nodes:
        path = n["path"]
        if path == "/未规划用例" or n["level"] == 0:
            continue
        parent_parts = path.strip("/").split("/")
        if len(parent_parts) <= 1:
            parent = "/" + parent_parts[0] if parent_parts else path
        else:
            parent = "/" + "/".join(parent_parts[:-1])
        children_map.setdefault(parent, []).append(node_dict(n))

    for n in nodes:
        if n["level"] != 0:
            continue
        d = node_dict(n)
        if n["path"] == "/未规划用例":
            d["type"] = "system_default"
        kids = children_map.get(n["path"], [])
        if kids:
            d["is_leaf"] = False
            d["children"] = sorted(kids, key=lambda x: x["path"])
        roots.append(d)

    return roots


def main() -> None:
    html_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    html = html_path.read_text(encoding="utf-8")
    nodes = parse_nodes(html)
    paths = sorted({n["path"] for n in nodes})
    tree = build_tree(nodes)

    data = {
        "source": "MeterSphere 用例模块树（页面 DOM 快照，2026-06-11，全量展开）",
        "path_format": "以 / 开头；大小写、空格、&、中英文均敏感，须与 MeterSphere 完全一致",
        "hierarchy_rules": [
            "level 0：项目根模块（parentid=NONE）",
            "level N：第 N 层子模块",
            "未规划用例：系统默认节点，不建议新业务挂载",
        ],
        "coverage_note": "自 MeterSphere 页面 expandall=true 快照解析，含 Cloud/Edge/Client/Super Admin Platform 全展开子模块。",
        "valid_paths": paths,
        "modules": tree,
        "not_in_tree_yet": {
            "note": "以下细分子模块尚未在 MeterSphere 创建；Product 相关用例当前统一挂在 /Cloud/Product 下已有模块",
            "paths": [
                "/Cloud/Product/Assets/Assign Security Key",
                "/Cloud/Product/Assets/Assign Certificate",
                "/Cloud/Product/Assets/Tag 新增与删除（Key/Certificate 共用）",
                "/Cloud/Product/Assets/Asset 列表展示",
            ],
        },
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Parsed {len(nodes)} nodes, {len(paths)} unique paths -> {out_path}")


if __name__ == "__main__":
    main()
