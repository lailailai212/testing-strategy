# KMS 页面元素 Baseline

SIT 环境 KMS 模块 UI 元素扫描产出，供功能用例落地、Playwright 自动化与 locator 稳定化参考。

## 扫描信息

| 项 | 值 |
|----|-----|
| 环境 | SIT，地址见 `config/env.local.yaml` → `environments.sit` |
| 扫描时间 | 2026-06-15 |
| 登录账号 | 见 `config/env.local.yaml` → `accounts.super_admin` |
| 工具 | Playwright MCP（登录 + 页面快照 + DOM 抽取） |

## 文件索引

| 文件 | 说明 |
|------|------|
| [`elements-baseline.json`](elements-baseline.json) | 结构化元素清单 + 推荐 locator + 样本数据 |
| [`key-list-baseline.md`](key-list-baseline.md) | Key List 页 |
| [`create-key-baseline.md`](create-key-baseline.md) | Create Key **Step 1** Basics |
| [`create-key-step2-baseline.md`](create-key-step2-baseline.md) | Create Key **Step 2** Key Source Setting |
| [`create-key-step3-baseline.md`](create-key-step3-baseline.md) | Create Key **Step 3** Permission |
| [`key-detail-baseline.md`](key-detail-baseline.md) | Key Detail（Overview / Usage Count / Permission / Operation Log） |
| `snapshots/*.yml` | 各页无障碍树快照 |
| `screenshots/*.png` | 各页截图（含 Key Detail、Add 权限弹窗） |

## 覆盖页面

| 页面 | URL | 状态 |
|------|-----|------|
| KMS Key List | `/key/list` | ✅ 已扫描 |
| Create Key — Step 1 Basics | `/key/create` | ✅ 已扫描 |
| Create Key — Step 2 Generation Method | `/key/create` | ✅ 已扫描 |
| Create Key — Step 3 Permission | `/key/create` | ✅ 已扫描 |
| Assign User Permissions 弹窗 | Step 3 Add 触发 | ✅ 已扫描 |
| Key Detail（全 Section） | `/key/{keyId}` | ✅ 已扫描 |

## Create Key 向导底栏按钮

| Step | 按钮 |
|------|------|
| 1 Basics | Cancel、**Continue** |
| 2 Key Source Setting | **Back**、**Skip**、**Next** |
| 3 Permission | **Complete** |

## 稳定化优先级（本模块）

1. **高**：`getByRole('button', { name: 'Create Key|Continue|Next|Complete' })`、`#th-*` 表头 ID、Key Source / Validity radio
2. **中**：`.arco-form-item` + label 过滤；Step 3 行 filter `hasText: email`
3. **低/避免**：无文案图标按钮 nth、全局 `Please enter value` / `Please Select`

## 关联需求

- Story：[`story/obis-7007200385-【自注册】004-02-kms与pki配额限制/`](../../../story/obis-7007200385-【自注册】004-02-kms与pki配额限制/)
- 功能用例：[`../testcases/kms-pki-quota-trial.md`](../testcases/kms-pki-quota-trial.md)

> **注意**：当前 SIT 账号为含 System Key 的租户，UI 与自注册免费版（无 Unlimited、无预设 key）存在差异；配额相关用例需使用对应租户复测。
