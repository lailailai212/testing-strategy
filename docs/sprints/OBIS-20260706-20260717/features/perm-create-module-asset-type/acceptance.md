# Story: 权限 — 创建 Module / Add Asset Type（仅 Product Manager、Resource Manager）

**来源**: [飞书项目 User Story #7041825174](https://project.feishu.cn/obis/userstory/detail/7041825174)  
**空间**: OBIS (`obis`)  
**编号**: 778 | **优先级**: Must | **Epic**: （未填写）  
**模式**: Large（双能力 × 多入口 × 有/无权限角色差异；入口映射已确认；无权限时入口**不显示**）

---

## Story AC

1.（AC-01）具备 Product Manager 或 Resource Manager 角色的用户，在 Product 详情 Overview / Assets 的 Module 行点击 `+ Add`，应能进入并成功完成「创建 Module」。

2.（AC-02）具备 Product Manager 或 Resource Manager 角色的用户，通过 Overview 的 `Create Assets Type` 或 Assets 的 `+ Create Asset...`（同一权限、同一动作），应能成功完成「Add Asset Type」。

3.（AC-03）不具备 Product Manager 且不具备 Resource Manager 的用户，对「创建 Module」入口（`+ Add`）应**不显示**，无法创建 Module。

4.（AC-04）不具备 Product Manager 且不具备 Resource Manager 的用户，对「Add Asset Type」两处入口（`Create Assets Type` / `+ Create Asset...`）均应**不显示**，且两入口表现一致。

5.（AC-05）Overview 与 Assets 上的 Module `+ Add` 受同一「创建 Module」权限控制，有权限时两处均可创建，无权限时两处均**不显示**。

6.（AC-06）Overview `Create Assets Type` 与 Assets `+ Create Asset...` 为同一权限、同一动作：有权限任选一入口可完成；无权限两入口均**不显示**。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号；否则填 `需求描述` 或 `QA扩展`。  
> **优先级口径**：P0 = 冒烟/阻断主路径；P1 = 角色负向与双入口一致性；P2 = 边界/待确认细节。  
> **入口约定（已确认）**：`+ Add` = 创建 Module；`Create Assets Type` ≡ `+ Create Asset...` = Add Asset Type。  
> **无权限表现（已确认）**：入口**不显示**（非置灰、非点击拦截）。

### 创建 Module — 有权限正向

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MOD-POS-01 | AC-01 | P0 | Product Manager 进入 Product 详情 Overview，可见 Module 行 `+ Add`，点击后可成功创建 Module，新 Module 出现在 Module 子 Tab |
| TP-MOD-POS-02 | AC-01 | P0 | Resource Manager 进入 Product 详情 Overview，可见并可用 `+ Add`，可成功创建 Module |
| TP-MOD-POS-03 | AC-01, AC-05 | P0 | Product Manager（或 Resource Manager）在 Assets Tab 的 Module 行 `+ Add` 同样可成功创建 Module |
| TP-MOD-POS-04 | AC-05 | P1 | 同一有权限用户在 Overview 与 Assets 两处 `+ Add` 行为一致（均可创建；创建结果在两 Tab 的 Module 列表中同步可见） |

### Add Asset Type — 有权限正向

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AST-POS-01 | AC-02 | P0 | Product Manager 在 Overview 点击 `Create Assets Type`，可成功完成 Add Asset Type |
| TP-AST-POS-02 | AC-02 | P0 | Resource Manager 在 Overview 点击 `Create Assets Type`，可成功完成 Add Asset Type |
| TP-AST-POS-03 | AC-02, AC-06 | P0 | Product Manager（或 Resource Manager）在 Assets 点击 `+ Create Asset...`，可成功完成与 Overview 相同的 Add Asset Type 动作 |
| TP-AST-POS-04 | AC-06 | P1 | 同一有权限用户分别从 Overview `Create Assets Type` 与 Assets `+ Create Asset...` 发起，权限校验与可完成性一致（同一权限、同一动作） |

### 创建 Module — 无权限负向

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MOD-NEG-01 | AC-03 | P0 | 非 Product Manager 且非 Resource Manager 的用户，在 Overview Module 行**不显示** `+ Add`，无法创建 Module |
| TP-MOD-NEG-02 | AC-03, AC-05 | P0 | 同上用户在 Assets Module 行同样**不显示** `+ Add`，与 Overview 表现一致 |
| TP-MOD-NEG-03 | AC-03 | P1 | 至少抽测一类非授权角色（如 System Manager 或 Normal User，**角色清单待产品补全**）验证入口不显示、不可创建 Module |

### Add Asset Type — 无权限负向

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AST-NEG-01 | AC-04 | P0 | 非 Product Manager 且非 Resource Manager 的用户，Overview 上**不显示** `Create Assets Type`，无法 Add Asset Type |
| TP-AST-NEG-02 | AC-04, AC-06 | P0 | 同上用户，Assets 上同样**不显示** `+ Create Asset...`，与 Overview 表现一致 |
| TP-AST-NEG-03 | AC-04 | P1 | 至少抽测一类非授权角色验证两处 Add Asset Type 入口均不显示 |

### 角色与边界（QA 扩展）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PERM-EDGE-01 | QA扩展 | P1 / 待确认 | 用户同时拥有 Product Manager（或 Resource Manager）与其他角色时，仍具备创建 Module / Add Asset Type（权限取并集，**待确认**） |
| TP-PERM-EDGE-02 | QA扩展 | P1 / 待确认 | 无权限用户绕过 UI 直接调用创建 Module / Add Asset Type 接口时被拒绝（403/业务错误），不落库 |
| TP-PERM-EDGE-03 | QA扩展 | P2 / 待确认 | 无权限用户不可通过篡改前端或直链进入创建流程并成功提交 |
| TP-PERM-EDGE-04 | QA扩展 | P2 | 有权限用户连续点击 `+ Add` / `Create Assets Type` 时不产生重复脏数据（防重复提交或二次确认，按现网实现） |
| TP-PERM-EDGE-05 | 需求描述 | P2 | `Create Version` 入口不在本 Story 权限条款内：不因本 Story 错误限制或错误放开 Product Manager/Resource Manager 对该按钮的既有权限（回归对照） |

### 中英文与文案

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-I18N-01 | QA扩展 | P2 / 待确认 | 中文环境下 `+ Add` / `Create Assets Type` / `+ Create Asset...` 文案符合产品约定（正式中文文案 **TBD**） |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点（含 P0） | 覆盖状态 |
|----------|---------------------|----------|
| AC-01 PM/RM 可通过 `+ Add` 创建 Module | TP-MOD-POS-01～03（P0） | ✅ |
| AC-02 PM/RM 可通过双入口 Add Asset Type | TP-AST-POS-01～03（P0） | ✅ |
| AC-03 非授权角色不显示创建 Module 入口 | TP-MOD-NEG-01/02（P0） | ✅ |
| AC-04 非授权角色不显示 Add Asset Type 入口 | TP-AST-NEG-01/02（P0） | ✅ |
| AC-05 Overview/Assets 的 `+ Add` 同权 | TP-MOD-POS-03（P0）；TP-MOD-POS-04、NEG-02 | ✅ |
| AC-06 两处 Asset Type 入口同权同动作 | TP-AST-POS-03（P0）；TP-AST-POS-04、NEG-02 | ✅ |

**AC-01～AC-06 均已至少 1 条 P0 级测试点覆盖；无权限表现已确认为「不显示」。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| 创建 Module — 有权限正向 | 3 | 1 | 0 | 4 |
| Add Asset Type — 有权限正向 | 3 | 1 | 0 | 4 |
| 创建 Module — 无权限负向 | 2 | 1 | 0 | 3 |
| Add Asset Type — 无权限负向 | 2 | 1 | 0 | 3 |
| 角色与边界（QA 扩展） | 0 | 2 | 3 | 5 |
| 中英文与文案 | 0 | 0 | 1 | 1 |
| **合计** | **10** | **6** | **4** | **20** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 14 |
| 需求描述 | 1 |
| QA 扩展 | 5 |

---

## 待确认

- [x] 无权限时入口**不显示**（2026-07-17 确认；非置灰、非点击拦截）
- [ ] 完整非授权角色清单（System Manager / Factory Manager / Normal User / Tenant Admin 等）及是否全部不显示入口
- [ ] 多角色叠加是否取并集
- [ ] 是否仅管控「创建」；编辑/删除 Module、Asset Type 是否另有规则
- [ ] Role 权限树中的正式权限码名称
- [ ] 中文环境按钮正式文案

## Out of Scope

- `Create Version` / Production Version 创建权限
- Assets 内 `+ Assign Key`、Chip Config 编辑等资源操作权限
- Product 列表「新建产品」权限
- 创建 Module / Add Asset Type 表单字段业务规则（本 Story 仅权限管控；表单细节以对应功能 Story 为准）
