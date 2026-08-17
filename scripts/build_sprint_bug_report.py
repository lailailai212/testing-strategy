"""Build sprint bug report — fetch via compact CSV or page JSON."""
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/sprints/OBIS-20260622-20260703/reports/sprint-bugs.md"
CSV = Path(__file__).with_name("_sprint_bugs.csv")

STATUSES = ["To Do", "Testing", "Fixing", "Confirming", "Clarifying", "Done", "Closed"]
PRIORITIES = ["P0", "P1", "P2", "P3"]
PRIORITY_BY_KEY = {
    "option_1": "P0", "option_2": "P1", "option_3": "P2", "uh67jkok0": "P3",
}
STATUS_NORM = {
    "TO DO": "To Do", "To Do": "To Do",
    "TESTING": "Testing", "Testing": "Testing",
    "FIXING": "Fixing", "Fixing": "Fixing",
    "CONFIRMING": "Confirming", "Confirming": "Confirming",
    "CLARIFYING": "Clarifying", "Clarifying": "Clarifying",
    "DONE": "Done", "Done": "Done",
    "CLOSED": "Closed", "Closed": "Closed",
}
BASE_URL = "https://project.feishu.cn/obis/bug/detail/{id}"


def parse_mql_item(item):
    row = {}
    for f in item["moql_field_list"]:
        k = f["key"]
        if k == "work_item_id":
            row["id"] = f["value"]["long_value"]
        elif k == "name":
            row["name"] = f["value"]["string_value"]
        elif k == "priority":
            v = f["value"]["key_label_value"]
            row["priority"] = PRIORITY_BY_KEY[v["key"]]
        elif k == "work_item_status":
            sl = f["value"]["key_label_value_list"][0]["label"]
            row["status"] = STATUS_NORM.get(sl, sl)
    return row


def load_csv():
    bugs = []
    for line in CSV.read_text(encoding="utf-8").strip().splitlines():
        id_, pk, st, name = line.split("|", 3)
        bugs.append({
            "id": int(id_),
            "priority": PRIORITY_BY_KEY[pk],
            "status": STATUS_NORM.get(st, st),
            "name": name,
        })
    return bugs


def fix_rate(done, closed, total):
    return f"{(done + closed) / total * 100:.2f}%" if total else "0.00%"


def write_report(bugs, collected_at="2026-07-06"):
    stats = {p: defaultdict(int) for p in PRIORITIES}
    for b in bugs:
        stats[b["priority"]][b["status"]] += 1

    lines = [
        "# Sprint Bug 统计 — OBIS-20260622-20260703",
        "",
        "> 数据来源：飞书项目 OBIS 空间 · Bug 工作项 · Sprint = `OBIS-20260622-20260703`",
        f"> 采集时间：{collected_at}",
        "> 修复率 = (Done + Closed) / 总计 × 100%",
        "",
        "## Bug 统计汇总",
        "",
        "| 缺陷 | To Do | Testing | Fixing | Confirming | Clarifying | Done | closed | 总计 | 修复率 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    grand = defaultdict(int)
    for p in PRIORITIES:
        row = [p]
        total = 0
        for s in STATUSES:
            c = stats[p][s]
            row.append(str(c))
            total += c
            grand[s] += c
        row.append(str(total))
        row.append(fix_rate(stats[p]["Done"], stats[p]["Closed"], total))
        grand["total"] += total
        lines.append("| " + " | ".join(row) + " |")

    total_all = grand["total"]
    row = ["总计"]
    for s in STATUSES:
        row.append(str(grand[s]))
    row.append(f"**{total_all}**")
    row.append(f"**{fix_rate(grand['Done'], grand['Closed'], total_all)}**")
    lines.append("| " + " | ".join(row) + " |")

    open_p01 = sorted(
        [b for b in bugs if b["priority"] in ("P0", "P1") and b["status"] not in ("Done", "Closed")],
        key=lambda x: (PRIORITIES.index(x["priority"]), x["id"]),
    )

    lines += [
        "",
        "## BUG List (P0/P1 · 未关闭)",
        "",
        "> 不含 Status = Done / Closed",
        "",
        "| Index | Priority | Status | Summary | Link |",
        "| --- | --- | --- | --- | --- |",
    ]
    for i, b in enumerate(open_p01, 1):
        name = (b.get("name") or "").replace("|", "\\|")
        url = BASE_URL.format(id=b["id"])
        # Summary 放在 Link 前，且 Link 用 Markdown 链接，避免预览把裸 URL 吞到行尾导致 Summary 空白
        lines.append(
            f"| {i} | {b['priority']} | {b['status']} | {name} | [{b['id']}]({url}) |"
        )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(bugs)} bugs, {len(open_p01)} open P0/P1 -> {OUT}")


def main():
    if not CSV.exists():
        print(f"Missing {CSV}", file=sys.stderr)
        sys.exit(1)
    write_report(load_csv())


if __name__ == "__main__":
    main()
