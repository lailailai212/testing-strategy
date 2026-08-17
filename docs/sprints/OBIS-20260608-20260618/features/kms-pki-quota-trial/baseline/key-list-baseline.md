# KMS Key List 页面元素 Baseline

> **环境**：`https://iot-admin-sit.snowballtech.com/key/list`（SIT）  
> **扫描时间**：2026-06-15  
> **账号**：`future.wei@snowballtech.com`（验证码登录）  
> **MeterSphere 模块**：`/Cloud/KMS/Key List`  
> **截图**：[`screenshots/key-list.png`](screenshots/key-list.png)  
> **A11y 快照**：[`snapshots/key-list-a11y-snapshot.yml`](snapshots/key-list-a11y-snapshot.yml)

## 页面结构

```text
全局导航栏（Logo / 面包屑 KMS / 主题开关 / 通知 / 用户 Avatar）
├── 左侧边栏（Core: Product, KMS*, PKI | Ecosystem | Records | Admin | System）
└── 主内容区
    ├── 页头：Key List + [Create Key]
    ├── 工具栏：Filter | Sort· 3 | [图标按钮] [图标按钮]
    └── 数据表（Arco Table，双 table 结构：表头 + 表体）
```

## 关键交互元素

| 区域 | 元素 | 文案/ID | 推荐 Locator（Playwright） | 稳定度 |
|------|------|---------|---------------------------|--------|
| 页头 | 页面标题 | Key List | `getByRole('heading', { name: 'Key List' })` | 高 |
| 页头 | 创建入口 | **Create Key** | `getByRole('button', { name: 'Create Key' })` | 高 |
| 工具栏 | 筛选 | Filter | `getByText('Filter', { exact: true })` | 中 |
| 工具栏 | 排序 | Sort· 3 | `getByText(/Sort/)` | 中 |
| 工具栏 | 视图/刷新图标按钮 | （无文案） | `.kms-list-toolbar button` + nth | 低 |
| 表头 | Name / Key ID | `#th-name` | `locator('#th-name')` | 高 |
| 表头 | Key Type | `#th-type` | `locator('#th-type')` | 高 |
| 表头 | Key Spec | `#th-algorithm` | `locator('#th-algorithm')` | 高 |
| 表头 | Creation Time | `#th-createTime` | `locator('#th-createTime')` | 高 |
| 表头 | Usage Count | `#th-usageCount` | `locator('#th-usageCount')` | 高 |
| 表头 | Status | `#th-status` | `locator('#th-status')` | 高 |
| 表头 | 操作列 | `#th-operations` | `locator('#th-operations')` | 中 |
| 表行 | 密钥名称链接 | System Key … | `getByRole('row').filter({ hasText: 'KID-' })` | 中 |
| 表行 | 状态 | Active / … | `getByRole('cell', { name: 'Active' })` | 中 |
| 表行 | 行内操作按钮 | （图标） | `tbody .arco-table-tr` 内 `getByRole('button')` | 低 |

## 列表样本数据（扫描时）

当前 SIT 租户可见 **8 条 System Key**（含 TEST 标签），均为 Active：

| Name | Key Type | Key Spec | Status | Key ID（节选） |
|------|----------|----------|--------|----------------|
| System Key RSA4096 | Asymmetric | RSA-4096 | Active | KID-AR527c4547a8 |
| System Key RSA3072 | Asymmetric | RSA-3072 | Active | KID-ARbed677f441 |
| System Key RSA2048 | Asymmetric | RSA-2048 | Active | KID-AR109b0cbd99 |
| System Key AES256 | Symmetric | AES-256 | Active | KID-SAef4ccf3a16 |
| System Key AES192 | Symmetric | AES-192 | Active | KID-SAaefb19a436 |
| System Key AES128 | Symmetric | AES-128 | Active | KID-SA08215365d5 |
| System Key ECC P384 | Asymmetric | ECC-P384 | Active | KID-AE18207913fc |
| System Key ECC P256 | Asymmetric | ECC-P256 | Active | KID-AE6a829240f1 |

## 与 Story / 用例差异（重要）

| 项 | Story/用例假设 | SIT 实测 |
|----|----------------|----------|
| 创建按钮文案 | `+ Create Key` | **Create Key**（无 + 前缀） |
| 列表初始数据 | 自注册租户无 default key | 本账号有 **8 条 System Key** |
| 配额测试数据 | 需自建非 Deleted 密钥 | 需换自注册免费版租户或造数 |

## Fragile 汇总

- 工具栏两个无文案图标按钮：无 `aria-label` / `data-testid`，只能用 nth 或 class
- `Please enter value` 等通用 placeholder 在 Create Key 页也存在，**不要**跨页混用
- 行内操作按钮对部分 Symmetric 密钥为 **disabled**

## 登录入口（复现）

1. 打开 `/login?redirect=Key+List`
2. Email：`future.wei@snowballtech.com` → Send Code → 验证码 `111111`
3. Sign In → 跳转 `/key/list`
