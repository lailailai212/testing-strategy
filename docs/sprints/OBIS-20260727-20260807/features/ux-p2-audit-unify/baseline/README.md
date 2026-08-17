# ux-p2-audit-unify — UI Baseline

> **扫描时间**：2026-08-03（入口实测；Group Audit 明细待补）  
> **环境**：SIT · 雪球 · 见 `env.local.yaml`  
> **用例**：[`../testcases/ux-p2-audit-unify.md`](../testcases/ux-p2-audit-unify.md)  
> **批次**：[`batch-case-mapping.md`](../../../../execution/OBIS-20260727-20260807/batch-case-mapping.md) **B1**

## 入口 URL

共享列表入口见 [`../../ux-p2-member-unify/baseline/entry-urls.md`](../../ux-p2-member-unify/baseline/entry-urls.md)。

| Audit 位置 | 如何到达 | 备注 |
|------------|----------|------|
| Group Audit | Group 列表 → 某 Group 详情 → Audit Tab | 需台账 `GRP-1 Audit` URL |
| Account Audit | Account `/user/list` → 用户详情 → Audit | |
| Profile Audit | 头像 → My Profile → Audit | 上午探查：列 Operator / Organization / Operation Type / Operation Time；Sort ·1 |
| KMS Audit | Key Detail → **Audit** Tab（非 Operation Log） | 样本：`/key/2081648131348414465` → Audit |
| PKI Audit | PKI 资源详情 → Audit | 待补直达 URL |
| Product Audit | Product 详情 → Audit | 待补；候选 PROD-6 |

## Profile Audit（上午探查摘要，可作 B1 对照）

| 项 | 实测 |
|----|------|
| 默认列 | Operator、Organization、Operation Type、Operation Time |
| Sort | `Sort ·1`（仅 Operation Time） |
| Organization 显示 | 「雪球」 |
| 数据 | 多操作人、多 Operation Type、时间跨 2026-06～07 |

## 待补

- [ ] Group 详情直达 URL + Audit 默认列截图  
- [ ] KMS Audit Tab 列/Filter/Columns 与 Group 对照截图  
- [ ] PKI / Product Audit 样本 URL
