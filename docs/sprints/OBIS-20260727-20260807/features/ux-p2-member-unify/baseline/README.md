# ux-p2-member-unify — UI Baseline

> **扫描时间**：2026-08-03（SIT · 雪球租户 · `feng.zhang`）  
> **环境**：见 `config/env.local.yaml` → `environments.sit`  
> **用例**：[`../testcases/ux-p2-member-unify.md`](../testcases/ux-p2-member-unify.md)  
> **批次映射**：[`docs/execution/OBIS-20260727-20260807/batch-case-mapping.md`](../../../../execution/OBIS-20260727-20260807/batch-case-mapping.md) B4–B6

## 文件索引

| 文件 | 说明 |
|------|------|
| [`entry-urls.md`](entry-urls.md) | 模块入口与详情 URL 模式 |
| [`kms-member-baseline.md`](kms-member-baseline.md) | KMS Key Detail → Member / Transfer |
| [`screenshots/`](screenshots/) | 截图（按需补充） |

## 覆盖状态

| 页面 | 状态 | 备注 |
|------|------|------|
| KMS Key Detail → Member | ✅ 已扫 | 样本 Key：`test permission` |
| Transfer Admin 弹窗 | ⬜ 待补 | B4 打开后 Cancel 时补截图 |
| PKI / Factory Member | ⬜ 待补 | 入口模式见 entry-urls |
| Group Member | ⬜ 待补 | |
| Account 删除 Confirm Action | ⬜ 待补 | 依赖 D2 |

## Agent 使用

1. 直达 `entry-urls.md` 中的 URL（勿靠左侧菜单探索）  
2. Locator 优先：`getByRole` / 精确文案；对照本目录 baseline  
3. B4：**禁止 Confirm** Transfer / 删除移交
