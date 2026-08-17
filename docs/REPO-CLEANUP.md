# 仓库目录整理清单

> 生成日期：2026-08-11  
> **执行状态：P0～P3 已完成**（2026-08-11）

## 已完成

| 批次 | 动作 | 结果 |
|------|------|------|
| **P0** | 删 `*-new*.xlsx`、重复 `testcases/modules/`、`_archive/` | ✅ |
| **P1** | 迁移 matrix / demo / testreports；更新 Skills 与脚本引用 | ✅ |
| **P2** | baseline 三套 `diff` 一致后删除 `docs/baseline/`、`docs/generate_doc/` | ✅ |
| **P3** | 删 `scripts/_sprint_*`、`_build_today_report.py`；更新根 `README` | ✅ |

### 迁移落点

| 原路径 | 现路径 |
|--------|--------|
| `generate_doc/testcases/welcome-account-scenario-matrix.md` | `docs/sprints/_examples/welcome-account-scenario-matrix.md` |
| `generate_doc/demo/self-reg-003-welcome-p0-demo.md` | `…/self-reg-003-03-toolbar-resource-center/reports/` |
| `generate_doc/testreports/sprint-…-bugs.md` | `docs/sprints/OBIS-20260622-20260703/reports/sprint-bugs.md` |
| `generate_doc/testreports/self-reg-003-03/` | 同上 feature `reports/` |

### 已删除

- `docs/generate_doc/`（整树）
- `docs/baseline/`（整树）
- `scripts/_sprint_bugs.csv`、`_sprint_bugs_compact.txt`、`_sprint_pages.json`、`_build_today_report.py`

## 仍待治理（P4，需产品确认）

| 项 | 建议 |
|----|------|
| `OBIS-20260706-20260717` vs `…-20260724` | INDEX 注明拆分原因，或合并 |
| `_unassigned/self-reg-001-05-domain-whitelist` | 补 Sprint 后迁入正式目录 |
| `docs/execution/` 缺 `OBIS-20260810-20260821` | 开跑前再建执行包 |
| `scripts/migrate_to_sprints.py` | 源目录已不存在；可标 deprecated 或移入 `scripts/archive/` |

## 目标布局（现行）

| 路径 | 角色 |
|------|------|
| `docs/sprints/` | 设计期正式产出 |
| `docs/execution/` | 执行期 |
| `docs/modules/` | MeterSphere 模块树 |
| `docs/templates/`、`docs/guides/` | 模板与指南 |
| `config/`、`story/`、`.cursor/skills/` | 配置 / Story 暂存 / Skills |
