"""Fetch sprint bugs from Feishu MQL JSON pages and refresh report."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from build_sprint_bug_report import (
    CSV,
    PRIORITY_BY_KEY,
    STATUS_NORM,
    parse_mql_item,
    write_report,
)

PAGES = Path(__file__).with_name("_sprint_pages.json")


def item_to_csv_row(item: dict) -> str:
    row = parse_mql_item(item)
    pk = None
    st_raw = None
    for f in item["moql_field_list"]:
        if f["key"] == "priority":
            pk = f["value"]["key_label_value"]["key"]
        elif f["key"] == "work_item_status":
            st_raw = f["value"]["key_label_value_list"][0]["label"]
    if pk is None or st_raw is None:
        raise ValueError(f"Missing fields in item {row.get('id')}")
    name = row["name"].replace("|", "\\|")
    return f"{row['id']}|{pk}|{st_raw}|{name}"


def load_pages(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    items: list[dict] = []
    for page in data:
        items.extend(page["data"]["1"])
    return items


def main() -> None:
    collected_at = sys.argv[1] if len(sys.argv) > 1 else "2026-07-07"
    if not PAGES.exists():
        print(f"Missing {PAGES}", file=sys.stderr)
        sys.exit(1)
    items = load_pages(PAGES)
    lines = [item_to_csv_row(it) for it in items]
    CSV.write_text("\n".join(lines) + "\n", encoding="utf-8")
    bugs = []
    for line in lines:
        id_, pk, st, name = line.split("|", 3)
        bugs.append({
            "id": int(id_),
            "priority": PRIORITY_BY_KEY[pk],
            "status": STATUS_NORM.get(st, st),
            "name": name.replace("\\|", "|"),
        })
    write_report(bugs, collected_at=collected_at)
    open_p01 = sum(
        1 for b in bugs
        if b["priority"] in ("P0", "P1") and b["status"] not in ("Done", "Closed")
    )
    print(f"Wrote {len(bugs)} bugs, {open_p01} open P0/P1 -> report ({collected_at})")


if __name__ == "__main__":
    main()
