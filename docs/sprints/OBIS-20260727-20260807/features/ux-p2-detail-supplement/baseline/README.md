# ux-p2-detail-supplement — UI Baseline

> **扫描时间**：2026-08-03（列表入口 + Product `+n` 样本）  
> **环境**：SIT · 雪球  
> **用例**：[`../testcases/ux-p2-detail-supplement.md`](../testcases/ux-p2-detail-supplement.md)  
> **批次**：[`batch-case-mapping.md`](../../../../execution/OBIS-20260727-20260807/batch-case-mapping.md) **B2 / B3**

## 入口 URL

见 [`../../ux-p2-member-unify/baseline/entry-urls.md`](../../ux-p2-member-unify/baseline/entry-urls.md)。

| 页面 | Path | B2/B3 用途 |
|------|------|-----------|
| Product List | `/product/list` | Module `+n`、列宽、Version、勾选 Filter |
| Account | `/user/list` | User Role `+n`、Toast、本人/非本人编辑 |
| Group | `/user/group/list` | Linked Product `+n`、列宽 |
| KMS List | `/key/list` | 列宽 + Usage Count |
| Factory List | `/factory/list` | 列宽抽样 |
| Role | `/system/role/list` | Role 树勾选 / OTA 节点（B3） |
| User (SNB) | `/system/user/list` | 本人编辑 SNB |

## Product List 实测摘要

| 项 | 值 |
|----|-----|
| 工具栏 | Filter / Columns / Refresh / `Sort ·1` / Create |
| 默认列 | Name / Module / Version / Vendor / Status |
| Version 空 | 多行显示 `-`（可作 PROD-3 对照候选） |
| Module `+n` | 例：`product-rare` → `Module_12 +11`；`success.test` → `My +6`（浮层滚动候选） |
| 总量 | Total: 715（数据充足） |

## 待补

- [ ] Account 列表 User Role `+n` 行（R1）直达/筛选条件  
- [ ] 列宽 px 实测（280 / 160 / 64）  
- [ ] Role 权限树打开入口（上午探查：点行无响应，需换入口）  
- [ ] Toast 触发路径截图（可与 B3 本人编辑合并）
