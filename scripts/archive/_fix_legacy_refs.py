"""One-shot: rewrite stale docs/generate_doc and docs/baseline refs in sprint MDs."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SUBS = [
    (
        "docs/generate_doc/testcases/modules/metersphere-modules.json",
        "docs/modules/metersphere-modules.json",
    ),
    (
        "docs/generate_doc/testcases/modules/self-reg-006-01-transactional-email-module-mapping.json",
        "testcases/module-mapping.json",
    ),
    (
        "docs/generate_doc/testcases/modules/self-reg-001-05-domain-whitelist-module-mapping.json",
        "testcases/module-mapping.json",
    ),
    ("docs/baseline/kms/*-baseline.md", "baseline/*-baseline.md"),
    ("docs/baseline/self-reg-001-05/*-baseline.md", "baseline/*-baseline.md"),
    (
        "docs/baseline/assets-card-customization/assets-card-customization-baseline.md",
        "baseline/assets-card-customization-baseline.md",
    ),
    (
        "docs/generate_doc/testcases/self-reg-001-05-domain-whitelist.md",
        "../testcases/self-reg-001-05-domain-whitelist.md",
    ),
]


def main() -> None:
    changed: list[str] = []
    for path in (ROOT / "docs/sprints").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in SUBS:
            text = text.replace(old, new)
        text = re.sub(
            r"docs/generate_doc/test-points/[\w-]+\.md",
            "acceptance.md（同 feature 包）",
            text,
        )
        text = re.sub(
            r"docs/generate_doc/test-points-xmind/[\w-]+-test-points\.xmind",
            "xmind/（同 feature 包）",
            text,
        )
        text = re.sub(
            r"docs/generate_doc/test-points-xmind/[\w-]+\.xmind",
            "xmind/（同 feature 包）",
            text,
        )
        text = text.replace(
            "docs/generate_doc/testcases/",
            "testcases/（历史路径已清理；见同 feature 包）",
        )
        text = re.sub(
            r"- baseline-legacy-dir: `docs/baseline/[^`]+`\r?\n",
            "",
            text,
        )
        text = text.replace(
            "../../generate_doc/testcases/self-reg-001-05-domain-whitelist.md",
            "../testcases/self-reg-001-05-domain-whitelist.md",
        )
        if text != orig:
            path.write_text(text, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))

    print(f"updated {len(changed)} files")
    for item in changed:
        print(" ", item)

    left: list[str] = []
    for path in ROOT.rglob("*.md"):
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if any(x in rel for x in (".git/", "REPO-CLEANUP.md", "scripts/archive/")):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "docs/generate_doc" in text or "docs/baseline/" in text:
            left.append(rel)
    print(f"remaining refs: {len(left)}")
    for item in left[:40]:
        print(" ", item)


if __name__ == "__main__":
    main()
