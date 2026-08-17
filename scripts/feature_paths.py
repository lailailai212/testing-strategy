"""Resolve docs/sprints/{sprint}/features/{slug}/ paths via features-registry.json."""

from __future__ import annotations

import json
from pathlib import Path


def repo_root_from(start: Path | None = None) -> Path:
    here = (start or Path(__file__)).resolve()
    for parent in [here, *here.parents]:
        if (parent / "docs" / "sprints" / "features-registry.json").is_file():
            return parent
        if (parent / "docs").is_dir() and (parent / ".cursor").is_dir():
            return parent
    return Path.cwd()


def load_registry(root: Path | None = None) -> dict:
    root = root or repo_root_from()
    path = root / "docs" / "sprints" / "features-registry.json"
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_sprint(slug: str, sprint: str | None = None, root: Path | None = None) -> str:
    if sprint:
        return sprint
    registry = load_registry(root)
    meta = registry.get("features", {}).get(slug)
    if not meta:
        raise KeyError(
            f"feature-slug '{slug}' not in docs/sprints/features-registry.json; "
            "pass --sprint or register the feature"
        )
    return meta["sprint"]


def feature_dir(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    root = root or repo_root_from()
    sprint_id = resolve_sprint(slug, sprint, root)
    return root / "docs" / "sprints" / sprint_id / "features" / slug


def acceptance_path(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    return feature_dir(slug, sprint, root) / "acceptance.md"


def tree_path(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    return feature_dir(slug, sprint, root) / "xmind" / f"{slug}.tree.json"


def xmind_path(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    return feature_dir(slug, sprint, root) / "xmind" / f"{slug}-test-points.xmind"


def testcases_md_path(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    return feature_dir(slug, sprint, root) / "testcases" / f"{slug}.md"


def testcases_xlsx_path(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    return feature_dir(slug, sprint, root) / "testcases" / f"{slug}-metersphere.xlsx"


def baseline_dir(slug: str, sprint: str | None = None, root: Path | None = None) -> Path:
    return feature_dir(slug, sprint, root) / "baseline"


def metersphere_modules_path(root: Path | None = None) -> Path:
    root = root or repo_root_from()
    return root / "docs" / "modules" / "metersphere-modules.json"
