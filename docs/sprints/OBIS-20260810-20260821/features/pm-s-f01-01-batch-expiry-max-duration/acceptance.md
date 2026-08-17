# Story: PM-S-F01-01：Create Product 表单 Batch Expiry Duration Max. Duration 默认值调整

**来源**: [飞书项目 User Story #7067202174](https://project.feishu.cn/obis/userstory/detail/7067202174)
**空间**: OBIS (`obis`)
**编号**: 852 | **优先级**: Must | **Epic**: —
**Sprint**: OBIS-20260810-20260821
**模式**: Small（单入口 Create Product、单字段默认值变更，预估 AC ≤ 3）
**变更类型**: UI/UX（判定依据：仅改 Max. Duration 默认展示值 30→90，校验/单位/其他字段不变）

> Story 导出：`story/obis-7067202174-pm-s-f01-01-batch-expiry-max-duration-默认值调整/`

---

## Story AC

1.（AC-01）用户进入 Create Product 页面时，Batch Expiry Duration 的 Max. Duration 字段默认值应为 **90 天**（改前为 30 天）。

2.（P1）用户进入 Create Product 页面时，Min. Duration、Batch Expiry Duration 其余字段、校验范围与单位应与改动前一致，仅 Max. Duration 默认值变化。

---

## 测试点

> Small 模式：下列测试点与 Story AC 对齐，供后续用例展开。

### Create Product — Batch Expiry Duration

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PROD-BED-01 | AC-01 | P0 | 打开 Create Product：Max. Duration 默认值为 **90**（单位天），无需手动修改即可看到新默认值 |
| TP-PROD-BED-02 | AC-01, 需求描述 | P0 | 对照改前基线：同入口同字段改前默认为 **30**，改后为 **90** |
| TP-PROD-BED-03 | 需求描述 | P1 | Min. Duration 默认值与改前一致；Max/Min 校验范围、单位（天）不变 |
| TP-PROD-BED-04 | QA扩展 | P1 | 用户可将 Max. Duration 改为非默认合法值并提交成功；成功落库值为用户输入值而非强制 90 |
| TP-PROD-BED-05 | QA扩展 | P2 | 中/英文界面下 Max. Duration 默认值均为 90 天 |
| TP-PROD-BED-06 | QA扩展 | P1 | 使用 Max Duration 默认 90 创建的 Product：Create Batch 时 Expiry Time 在上限内可成功，超出 Max Duration（>90 天）应被阻断，证明有效期约束生效 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Max. Duration 默认 90 天 | TP-PROD-BED-01；TP-PROD-BED-02 | ✅ |
| （P1）仅改默认值、其余不变 | TP-PROD-BED-03 | ✅ |

**AC-01 已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| Create Product — Batch Expiry Duration | 2 | 3 | 1 | 6 |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 3 |
| 需求描述 | 1 |
| QA 扩展 | 3 |

---

## 设计自检

### 变更类型

- [x] 已声明 UI/UX
- [x] P0 密度侧重默认值可见性与基线对照
- [x] 未堆无界面依据的深逻辑矩阵为 P0
- [x] A–D 未命中，标 N/A

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（未命中）

### 多角色可见 / 触达（类型 C）

- [x] N/A（未命中）

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）

---

## 待确认

- （无）改前 30 / 只改 Max. Duration 默认值已于 2026-08-10 确认。

## Out of Scope

- Min. Duration 及其他 Create Product 字段默认值、校验规则与提交流程变更
- 已创建 Product 的存量 Batch Expiry Duration 回填或迁移
