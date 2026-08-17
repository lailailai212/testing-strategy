# Baseline — pm-s-f01-01-batch-expiry-max-duration

## Screenshots

| 文件 | 说明 |
|------|------|
| `screenshots/ref-create-product-batch-expiry.png` | Create Product 弹窗 — Batch Expiry Duration 区（改后态参考：Max Duration = **90** Days） |

## 字段约定（对照截图）

| 字段 | 改后默认（本期验收） | 备注 |
|------|----------------------|------|
| Default Duration | 30 Days | 本期不变 |
| Min Duration | 1 Days | 本期不变 |
| Max Duration | **90** Days | 改前 30 → 改后 90（本 Story 唯一变更） |

## 入口

Product 列表 → **Create Product** → 表单底部 **Batch Expiry Duration**
