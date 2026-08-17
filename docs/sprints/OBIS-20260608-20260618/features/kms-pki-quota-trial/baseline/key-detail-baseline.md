# KMS Key Detail 页面元素 Baseline

> **环境**：`https://iot-admin-sit.snowballtech.com/key/2066511606979149826`  
> **扫描时间**：2026-06-15  
> **账号**：`future.wei@snowballtech.com`  
> **样本密钥**：ScanStep23（KID-AR34c414c3f8，Active，RSA-2048）  
> **MeterSphere 模块**：`/Cloud/KMS/Key Detail`（子 Tab 见下表）  
> **截图**：`screenshots/key-detail-*.png`  
> **A11y 快照**：`snapshots/key-detail-*-a11y-snapshot.yml`

## URL 与路由

| 项 | 值 |
|----|-----|
| 路径模式 | `/key/{keyId}` |
| 示例 | `/key/2066511606979149826` |
| 面包屑 | KMS / {Key Name} |
| 从列表进入 | Key List 点击密钥名称链接 |

## 页面结构（单页多 Section + Tab 锚点）

```text
页头
├── 返回箭头
├── 密钥名（可编辑 textbox）+ PROD 标签
├── Status: Active
└── [Lock] [Download]

Tab 导航（锚点滚动，非互斥隐藏）
├── Overview
├── Usage Count
├── Permission
└── Operation Log

内容区（纵向堆叠，Tab 点击滚动定位）
├── Basic Info（可折叠）        → Overview / Key Detail/Overview
├── Used by Product / User     → Usage Count / Key Detail/Usage Count/*
├── Permission 表 + 工具栏       → Key Detail/Permission
└── Operation Log 表 + 工具栏    → Key Detail/Operation Log
```

## 页头元素

| 元素 | 文案/值（样本） | 推荐 Locator | 稳定度 |
|------|----------------|-------------|--------|
| 返回 | 图标 | `main` 内首个 `img[cursor=pointer]` 或 header 区 back | 低 |
| 密钥名称 | ScanStep23（textbox） | `getByRole('textbox', { name: 'ScanStep23' })` 或 header textbox | 中 |
| 环境标签 | PROD | `getByText('PROD', { exact: true })` | 中 |
| 状态 | Status / Active | `getByText('Active')` 邻近 Status | 中 |
| Lock | Lock | `getByRole('button', { name: 'Lock' })` | 高 |
| Download | Download | `getByRole('button', { name: 'Download' })` | 高 |

## Tab 导航

| Tab | MeterSphere 子模块 | 推荐 Locator |
|-----|-------------------|-------------|
| Overview | `/Cloud/KMS/Key Detail/Overview` | `.arco-tabs-tab` + `filter({ hasText: 'Overview' })` |
| Usage Count | `/Cloud/KMS/Key Detail/Usage Count` | 同上 `Usage Count` |
| Permission | `/Cloud/KMS/Key Detail/Permission` | 同上 `Permission` |
| Operation Log | `/Cloud/KMS/Key Detail/Operation Log` | 同上 `Operation Log` |

> Tab 与下方 Section **同时存在于 DOM**；切换 Tab 主要为滚动定位，非 SPA 路由切换。

## Overview — Basic Info

**截图**：[`screenshots/key-detail-overview.png`](screenshots/key-detail-overview.png)

| 字段 | 样本值 | 说明 |
|------|--------|------|
| Name | ScanStep23 | 带复制图标 |
| ID | KID-AR34c414c3f8 | 带复制图标 |
| Storage | Local | |
| Version | V1 | |
| Source | System | |
| Type | Asymmetric | |
| Algorithm | RSA-2048 | |
| Admin | Future Wei | 含 avatar |
| Creation Time | 2026-06-15 21:22:16 | |
| Usage | Sign / Verify | |
| Usage Count | 0 | 字段名与 Tab 名相同，避免全局 `getByText('Usage Count')` |
| Last Usage | 2026-06-15 21:22:16 | |
| Expiration Date | 2051-06-15 | 只读展示；旁有进度条 |
| 有效期进度 | Used 1 hour / 25 years left | `getByText(/years left/)` |

| 控件 | 说明 | Locator |
|------|------|---------|
| Basic Info 标题旁图标按钮 | **折叠/展开** Basic Info（非编辑入口） | `h6` filter `Basic Info` 邻近 `button` |
| Name/ID 复制图标 | 点击复制 | 字段值旁 `img[cursor=pointer]` |

## Usage Count Section

**截图**：[`screenshots/key-detail-usage-count.png`](screenshots/key-detail-usage-count.png)

| 区块 | 样本状态 | Locator |
|------|----------|---------|
| Used by Product (0) | 折叠面板，空态「No associated products」 | `getByRole('button', { name: /Used by Product/ })` |
| Used by User (0) | 折叠面板，空态「No associated users」 | `getByRole('button', { name: /Used by User/ })` |

子模块：`/Cloud/KMS/Key Detail/Usage Count/Product`、`/Cloud/KMS/Key Detail/Usage Count/User`

## Permission Section

**截图**：[`screenshots/key-detail-permission.png`](screenshots/key-detail-permission.png)

| 元素 | 说明 | Locator |
|------|------|---------|
| Add | 新增权限 | `getByRole('button', { name: 'Add' })` |
| Filter | 筛选 | `getByText('Filter', { exact: true })` |
| Sort· 1 | 排序 | `getByText(/Sort/)` |

**表头**：Name | Permission | Status | Operator | Operation Time | （操作列）

**样本行**：

| Name | Permission | Status | Operator | Operation Time |
|------|------------|--------|----------|----------------|
| Admin Future Wei(future.wei@snowballtech.com) | Add, View, Unlock, Edit, Create Authorization, Lock, Delete | Enable | future.wei@snowballtech.com | 2026-06-15 21:22:15 |

## Operation Log Section

**截图**：[`screenshots/key-detail-operation-log.png`](screenshots/key-detail-operation-log.png)

| 元素 | 说明 |
|------|------|
| Filter / Sort· 1 | 同 Permission 区工具栏模式 |

**表头**：Operation | Operation Type | Operation Time | Operator Name | Operator Email

**样本行**：

| Operation | Operation Type | Operation Time |
|-----------|----------------|----------------|
| Save HSM Key: ScanStep23 | Create-HSM | 2026-06-15 21:22:24 |
| Create key: ScanStep23 | Create | 2026-06-15 21:22:16 |

## 与配额 Story / 用例关联

| 用例场景 | Key Detail 相关发现 |
|----------|---------------------|
| TP-KMS-VAL-07 编辑有效期 | Overview 仅展示 **Expiration Date** 只读；Basic Info 旁按钮为**折叠**非编辑；编辑入口待另路径确认 |
| 密钥状态计入配额 | Status 展示 **Active**；Deleted/Revoked 等需在对应状态密钥上复扫 |
| 有效期 2 年限制 | 样本 Expiration 为 2051（创建时 25 Years），与免费版 2 年规则不同 |

## Fragile 汇总

- `Usage Count` 同时是 **Tab 名**与 **Basic Info 字段名**，须用 `.arco-tabs-tab` 或 Section 父级限定
- Basic Info 折叠按钮无文案/`aria-label`，当前用 `h6` + 邻近 `button`
- 返回箭头、复制图标、行内操作按钮均无稳定 `data-testid`
- Tab 切换不卸载 DOM，断言时需限定 Section（如 `heading` Operation Log 下方表格）

## 入口路径

`KMS Key List` → 点击密钥名称（如 System Key RSA4096）→ `/key/{id}`
