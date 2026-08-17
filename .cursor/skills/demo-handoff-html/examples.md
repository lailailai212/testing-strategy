# Examples — Demo Handoff HTML

## 示例：为 Archive feature 生成演示页

**用户**：给 `sems-e1-s08-se-profile-archive` 生成提测演示 HTML

**步骤**：

1. 读 `docs/sprints/OBIS-20260810-20260821/features/sems-e1-s08-se-profile-archive/acceptance.md`
2. 挑选 P0 演示项（详情 Archive、列表 Archive、失败 Toast、不可见等），合并同路径 TP
3. 以 `assets/demo-handoff.template.html` 填占位符，写入：

```text
docs/sprints/OBIS-20260810-20260821/features/sems-e1-s08-se-profile-archive/reports/demo-handoff.html
```

4. 更新该 feature `META.md` Layout

**演示项编号示例**：`D-ARCH-01` …

**演示顺序示例**：前置状态限制（只读）→ 详情成功路径 → 列表成功路径 → 失败/Cancel → 不可见与审计（数据敏感项靠后）

## 用户说法对照

| 说法 | 产出 |
|------|------|
| 「生成 0821 sprint 四个需求的提测演示页」 | 四个 feature 各一份 `reports/demo-handoff.html` |
| 「只要 P0」 | 第四节不含 P1 行 |
| 「更新模块导航的演示 HTML」 | 覆盖 `e2-s01-module-nav-convergence/reports/demo-handoff.html` |

## 与 Sprint 级 MD 清单的关系

| 产物 | 位置 | 用途 |
|------|------|------|
| 本 Skill HTML | `features/{slug}/reports/demo-handoff.html` | **单需求**现场演示 |
| 历史 MD checklist | `docs/execution/{sprint}/demo-review-checklist.md` | 多 Story 汇总（可选，本 Skill 默认不生成） |
