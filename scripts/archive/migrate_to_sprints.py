"""Migrate flat generate_doc / baseline artifacts into docs/sprints/{sprint}/features/{slug}/.

Usage (from repo root):
    python scripts/migrate_to_sprints.py
    python scripts/migrate_to_sprints.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/sprints/features-registry.json"

LEGACY = {
    "acceptance": ROOT / "docs/generate_doc/test-points",
    "tree": ROOT / "docs/generate_doc/test-points-xmind/trees",
    "xmind": ROOT / "docs/generate_doc/test-points-xmind",
    "testcases": ROOT / "docs/generate_doc/testcases",
    "modules": ROOT / "docs/generate_doc/testcases/modules",
    "baseline": ROOT / "docs/baseline",
    "reports": ROOT / "docs/generate_doc/testreports",
}


def feature_root(sprint: str, slug: str) -> Path:
    return ROOT / "docs/sprints" / sprint / "features" / slug


def copy_if_exists(src: Path, dst: Path, dry_run: bool) -> bool:
    if not src.exists():
        return False
    if dry_run:
        print(f"  COPY {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
        return True
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    print(f"  OK   {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
    return True


def write_meta(path: Path, slug: str, meta: dict, dry_run: bool) -> None:
    lines = [
        f"# META — {slug}",
        "",
        f"- feature-slug: `{slug}`",
        f"- sprint: `{meta['sprint']}`",
    ]
    if meta.get("story_id"):
        lines.append(f"- story-id: `{meta['story_id']}`")
    if meta.get("story_path"):
        lines.append(f"- story-path: `{meta['story_path']}`")
    lines.append(f"- status: `{meta.get('status', 'draft')}`")
    if meta.get("baseline_legacy"):
        lines.append(f"- baseline-legacy-dir: `docs/baseline/{meta['baseline_legacy']}`")
    if meta.get("note"):
        lines.append(f"- note: {meta['note']}")
    lines.extend(
        [
            "",
            "## Layout",
            "",
            "```text",
            f"features/{slug}/",
            "├── META.md",
            "├── acceptance.md          # AC + 测试点",
            "├── xmind/",
            f"│   ├── {slug}.tree.json",
            f"│   └── {slug}-test-points.xmind",
            "├── testcases/",
            f"│   ├── {slug}.md",
            f"│   ├── {slug}-metersphere.xlsx",
            "│   └── module-mapping.json",
            "├── baseline/",
            "└── reports/",
            "```",
            "",
        ]
    )
    text = "\n".join(lines)
    if dry_run:
        print(f"  WRITE {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"  OK   META {path.relative_to(ROOT)}")


def migrate_feature(slug: str, meta: dict, dry_run: bool) -> None:
    sprint = meta["sprint"]
    fr = feature_root(sprint, slug)
    print(f"\n[{slug}] -> {sprint}")

    write_meta(fr / "META.md", slug, meta, dry_run)

    copy_if_exists(
        LEGACY["acceptance"] / f"{slug}.md",
        fr / "acceptance.md",
        dry_run,
    )
    copy_if_exists(
        LEGACY["tree"] / f"{slug}.tree.json",
        fr / "xmind" / f"{slug}.tree.json",
        dry_run,
    )
    copy_if_exists(
        LEGACY["xmind"] / f"{slug}-test-points.xmind",
        fr / "xmind" / f"{slug}-test-points.xmind",
        dry_run,
    )
    copy_if_exists(
        LEGACY["testcases"] / f"{slug}.md",
        fr / "testcases" / f"{slug}.md",
        dry_run,
    )
    copy_if_exists(
        LEGACY["testcases"] / f"{slug}-metersphere.xlsx",
        fr / "testcases" / f"{slug}-metersphere.xlsx",
        dry_run,
    )
    # Prefer json mapping; also copy csv if present
    for ext in (".json", ".csv"):
        copy_if_exists(
            LEGACY["modules"] / f"{slug}-module-mapping{ext}",
            fr / "testcases" / f"module-mapping{ext}",
            dry_run,
        )

    baseline_src_name = meta.get("baseline_legacy") or slug
    baseline_src = LEGACY["baseline"] / baseline_src_name
    if baseline_src.is_dir():
        copy_if_exists(baseline_src, fr / "baseline", dry_run)

    # Feature-scoped reports (e.g. self-reg-003-03)
    short = slug
    for candidate in (
        slug,
        slug.replace("-toolbar-resource-center", ""),
        "self-reg-003-03" if "003-03" in slug else None,
    ):
        if not candidate:
            continue
        report_src = LEGACY["reports"] / candidate
        if report_src.is_dir():
            copy_if_exists(report_src, fr / "reports", dry_run)
            break


def write_sprint_readmes(registry: dict, dry_run: bool) -> None:
    by_sprint: dict[str, list[tuple[str, dict]]] = {}
    for slug, meta in registry["features"].items():
        by_sprint.setdefault(meta["sprint"], []).append((slug, meta))

    for sprint, items in sorted(by_sprint.items()):
        path = ROOT / "docs/sprints" / sprint / "README.md"
        rows = [
            f"# Sprint `{sprint}`",
            "",
            "| feature-slug | story-id | status | path |",
            "|---|---|---|---|",
        ]
        for slug, meta in sorted(items):
            sid = meta.get("story_id") or "—"
            st = meta.get("status") or "draft"
            rows.append(
                f"| `{slug}` | {sid} | {st} | [features/{slug}/](features/{slug}/) |"
            )
        rows.append("")
        text = "\n".join(rows)
        if dry_run:
            print(f"WRITE {path.relative_to(ROOT)}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"OK sprint README {path.relative_to(ROOT)}")


def write_index(registry: dict, dry_run: bool) -> None:
    path = ROOT / "docs/sprints/INDEX.md"
    by_sprint: dict[str, list[str]] = {}
    for slug, meta in registry["features"].items():
        by_sprint.setdefault(meta["sprint"], []).append(slug)

    lines = [
        "# Sprints 索引",
        "",
        "Feature 包路径：`docs/sprints/{sprint-id}/features/{feature-slug}/`",
        "",
        "机器可读索引：[`features-registry.json`](features-registry.json)",
        "",
        "## Sprint 列表",
        "",
        "| Sprint | Features |",
        "|---|---|",
    ]
    for sprint, slugs in sorted(by_sprint.items()):
        link = f"[`{sprint}`]({sprint}/)"
        lines.append(f"| {link} | {len(slugs)} |")
    lines.extend(
        [
            "",
            "## 约定",
            "",
            "- 一个 feature 只归属一个 Sprint（跨迭代沿用：在后续 Sprint README 链接引用）",
            "- `{feature-slug}` 全仓库唯一；禁止 `*-new.md` 旁路副本",
            "- 全局 MeterSphere 模块树：`docs/modules/metersphere-modules.json`",
            "- 根目录 `story/` 仍为飞书导入暂存；正式关联写在各 feature 的 `META.md`",
            "",
        ]
    )
    text = "\n".join(lines)
    if dry_run:
        print(f"WRITE {path.relative_to(ROOT)}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"OK INDEX {path.relative_to(ROOT)}")


def lift_modules(dry_run: bool) -> None:
    src = ROOT / "docs/generate_doc/testcases/modules/metersphere-modules.json"
    dst = ROOT / "docs/modules/metersphere-modules.json"
    if src.is_file():
        copy_if_exists(src, dst, dry_run)


def migrate_sprint_bug_report(dry_run: bool) -> None:
    src = ROOT / "docs/generate_doc/testreports/sprint-OBIS-20260622-20260703-bugs.md"
    dst = (
        ROOT
        / "docs/sprints/OBIS-20260622-20260703/reports/sprint-bugs.md"
    )
    copy_if_exists(src, dst, dry_run)


def write_legacy_readme(dry_run: bool) -> None:
    path = ROOT / "docs/generate_doc/README.md"
    text = """# generate_doc（Legacy）

> **已迁移**：正式产出请使用 `docs/sprints/{sprint}/features/{feature-slug}/`。
> 索引：[`docs/sprints/INDEX.md`](../sprints/INDEX.md) · [`features-registry.json`](../sprints/features-registry.json)

本目录保留迁移前扁平文件，供对照；新写入请走 Sprint/Feature 包结构。后续确认无引用后删除。

| 旧路径 | 新路径 |
|--------|--------|
| `test-points/{slug}.md` | `../sprints/{sprint}/features/{slug}/acceptance.md` |
| `test-points-xmind/` | `../sprints/.../features/{slug}/xmind/` |
| `testcases/{slug}.md` | `../sprints/.../features/{slug}/testcases/` |
| `testcases/modules/metersphere-modules.json` | `../modules/metersphere-modules.json` |
| `testreports/` | Sprint `reports/` 或 Feature `reports/` |
"""
    if dry_run:
        print(f"WRITE {path.relative_to(ROOT)}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"OK legacy README {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    for slug, meta in registry["features"].items():
        migrate_feature(slug, meta, args.dry_run)

    write_sprint_readmes(registry, args.dry_run)
    write_index(registry, args.dry_run)
    lift_modules(args.dry_run)
    migrate_sprint_bug_report(args.dry_run)
    write_legacy_readme(args.dry_run)
    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
