# Story: OBIS 角色权限矩阵回归

**来源**: 用户提供的 OBIS 角色分类与权限说明截图 + 对话确认  
**空间**: OBIS (`obis`)  
**编号**: — | **优先级**: — | **Epic**: —  
**Sprint**: OBIS-20260810-20260821  
**模式**: Large（判定依据：系统 / 产品 / 工厂多层角色，赋权路径 + 能力矩阵 + 无权限隐藏 + 接口绕过）  
**变更类型**: Logic（判定依据：权限谁能做、无权限不展示、直链/接口拒绝；UI 仅作为规则可观察点）

---

## 已确认规则（对话）

| 项 | 结论 |
|----|------|
| 无权限 | **入口不显示**（不采用置灰可点） |
| 产品内角色赋权 | `Product` → 产品详情 → **Member** → 行内 **⋮** → 编辑该用户产品内角色 |
| 工厂角色赋权 | `Factory` → 工厂详情 → **Member** → **Add User** / **Edit User** |
| Factory Admin 与 Factory Manager | **不是**同一角色；Transfer Admin 只覆盖 Admin 降级为 Manager，不能当作赋 Manager 的主路径 |
| 直链 / 接口绕过 | 纳入回归，P1 |
| 已有用例 | 本包独立，不管 `perm-create-module-asset-type` |

## 角色分层（对照现网，不臆造截图未出现的模块名）

**产品内角色**（Member ⋮ 可勾选）：Owner、Product Manager、Resource Manager、Version Manager、Batch Manager、Member  

**工厂角色**（Add User / Edit User）：Factory Admin、Factory Manager  

**系统层角色**（租户 Operation / Account 侧，本包只做侧栏与创建入口抽样）：System Manager、Product Manager、Resource Manager、Factory Manager、Normal User  

## 产品内写入口抽样（按角色职责对照 IoT Admin 现网）

> 原图勾选格未再提供。下表按**角色名对应职责**抽样；执行时若现网与表不一致，记缺陷或回写本表。

| 写入口（现网） | Owner | Product Manager | Resource Manager | Version Manager | Batch Manager | Member |
|----------------|-------|-----------------|------------------|-----------------|---------------|--------|
| 产品信息编辑（Overview 产品名 / 设置） | ✓ | ✓ | — | — | — | — |
| Assets 编辑 / Add | ✓ | ✓ | ✓ | — | — | — |
| Create Version | ✓ | — | — | ✓ | — | — |
| Create Batch | ✓ | — | — | — | ✓ | — |
| Member Add / ⋮ 编辑角色 | ✓ | ✓ | — | — | — | — |
| 进入产品详情查看 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

工厂：Factory Admin 可见 **Transfer Admin**；Factory Manager **不显示** Transfer Admin。两者均可在有工厂 Member 管理权限时被 Add/Edit User 赋予。

---

## Story AC

1.（AC-01）具备该产品 Member 管理权限的用户，在 Product 详情 **Member** 列表通过行内 **⋮** 编辑目标用户的产品内角色（Owner / Product Manager / Resource Manager / Version Manager / Batch Manager / Member），保存后列表 Role 更新，目标用户重新登录或刷新后权限按新角色生效。

2.（AC-02）不具备该产品 Member 管理权限的用户进入同一产品 **Member** Tab 时，**不显示** Add 与行内 **⋮** 编辑角色入口。

3.（AC-03）具备该工厂 Member 管理权限的用户，在 Factory 详情 **Member** 通过 **Add User** 或 **Edit User** 将用户设为 Factory Admin 或 Factory Manager（二者不是同一角色），保存后列表 Role 与该用户权限按所选角色生效。

4.（AC-04）不具备该工厂 Member 管理权限的用户进入同一工厂 **Member** Tab 时，**不显示** Add User 与 Edit User。

5.（AC-05）用户仅拥有某一产品内角色时，只展示该角色职责对应的写入口；无权限的写入口**不显示**（对照上表抽样）。

6.（AC-06）产品内角色为 **Member** 的用户可进入该产品详情查看，但不显示 Create Version、Create Batch、Assets 编辑/Add、Member Add / ⋮ 编辑。

7.（AC-07）Factory Admin 与 Factory Manager 权限不同：Admin 本人可见 **Transfer Admin**；Factory Manager **不显示** Transfer Admin。

8.（P1 / AC-08）无权限用户通过直链或接口发起创建 Version / Batch、编辑产品 Member、Factory Add User 时，请求被拒绝且不落库。

---

## 测试点

> **命中 AC 列**：`AC-0x` = 直接覆盖 Story AC；`描述` = 需求正文有述但未列入 AC；`QA扩展` = QA 补充边界/负向。

### Product — Member 赋权

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PRD-MEM-01 | AC-01 | P0 | Owner 或 Product Manager 打开产品 Member，行内 ⋮ 可编辑角色，选项含 Owner / Product Manager / Resource Manager / Version Manager / Batch Manager / Member |
| TP-PRD-MEM-02 | AC-01 | P0 | 将目标用户改为 Version Manager 并保存：列表 Role 为 Version Manager；该用户刷新后可见 Create Version |
| TP-PRD-MEM-03 | AC-02 | P0 | 仅 Member（或无 Member 管理权限）进入 Member Tab：**不显示** Add 与 ⋮ 编辑角色 |
| TP-PRD-MEM-04 | QA扩展 | P1 | 同一用户可被赋予多个产品内角色时，写入口取并集（待确认；确认前按现网记录） |

### Product — 角色写入口

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PRD-CAP-01 | AC-05, AC-06 | P0 | 仅 Member：可进 Overview；不显示 Create Version、Create Batch、Assets 编辑/Add、Member Add/⋮ |
| TP-PRD-CAP-02 | AC-05 | P0 | 仅 Owner：Create Version、Create Batch、Assets 编辑/Add、Member ⋮ 均显示且可完成一次主路径 |
| TP-PRD-CAP-03 | AC-05 | P0 | 仅 Version Manager：显示 Create Version 并可创建；不显示 Create Batch、Member Add/⋮ |
| TP-PRD-CAP-04 | AC-05 | P0 | 仅 Batch Manager：显示 Create Batch 并可创建；不显示 Create Version、Member Add/⋮ |
| TP-PRD-CAP-05 | AC-05 | P0 | 仅 Resource Manager：Assets 编辑/Add 显示并可保存；不显示 Create Version、Create Batch、Member Add/⋮ |
| TP-PRD-CAP-06 | AC-05 | P1 | 仅 Product Manager：产品信息可编辑、Member ⋮ 显示；不显示 Create Version、Create Batch |

### Factory — Member 赋权与角色差异

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-FAC-MEM-01 | AC-03 | P0 | 有权限用户 Add User：角色可选 Factory Admin 与 Factory Manager，保存后列表 Role 正确 |
| TP-FAC-MEM-02 | AC-03 | P0 | Edit User 可将 Factory Manager 改为 Factory Admin（或反向），保存后 Role 与权限随新角色变化 |
| TP-FAC-MEM-03 | AC-04 | P0 | 无工厂 Member 管理权限：**不显示** Add User、Edit User |
| TP-FAC-CAP-01 | AC-07 | P0 | Factory Admin 本人：Admin 行菜单可见 Transfer Admin 且可打开弹窗 |
| TP-FAC-CAP-02 | AC-07 | P0 | Factory Manager：不显示 Transfer Admin |

### 直链 / 接口绕过

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-BYP-01 | AC-08 | P1 | 无产品写权限会话调用创建 Version / Batch 或编辑 Member：拒绝（403 或业务错误），不落库 |
| TP-BYP-02 | AC-08 | P1 | 无工厂 Member 管理权限会话调用 Add User / 改角色：拒绝且不落库 |

### 系统层抽样

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SYS-01 | 需求描述 | P1 | Normal User（或明确无系统管理权限）：侧栏不显示其无权限模块；Product/Factory 列表不显示无权限的创建入口 |
| TP-SYS-02 | QA扩展 | P2 | System Manager 可进入 Product 与 Factory 列表（抽样，不以臆造模块名为准） |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 产品 Member ⋮ 编辑角色 | TP-PRD-MEM-01；TP-PRD-MEM-02 | ✅ |
| AC-02 无权限不显示产品 Member 编辑 | TP-PRD-MEM-03 | ✅ |
| AC-03 工厂 Add/Edit User 赋 Admin 或 Manager | TP-FAC-MEM-01；TP-FAC-MEM-02 | ✅ |
| AC-04 无权限不显示工厂 Add/Edit User | TP-FAC-MEM-03 | ✅ |
| AC-05 产品内角色写入口按职责显隐 | TP-PRD-CAP-02～06 | ✅ |
| AC-06 Member 仅查看 | TP-PRD-CAP-01 | ✅ |
| AC-07 Factory Admin ≠ Manager（Transfer） | TP-FAC-CAP-01；TP-FAC-CAP-02 | ✅ |
| AC-08 直链/接口绕过 | TP-BYP-01；TP-BYP-02 | ✅ |

**AC-01～AC-08 均已至少 1 条 P0（AC-08 为 P1）测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| Product Member 赋权 | 3 | 1 | 0 | 4 |
| Product 角色写入口 | 5 | 1 | 0 | 6 |
| Factory Member / 角色 | 5 | 0 | 0 | 5 |
| 直链/接口 | 0 | 2 | 0 | 2 |
| 系统层抽样 | 0 | 1 | 1 | 2 |
| **合计** | **13** | **5** | **1** | **19** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 16 |
| 需求描述 | 1 |
| QA 扩展 | 2 |

---

## 待确认

- [ ] 产品内多角色是否取并集（TP-PRD-MEM-04）
- [ ] 系统层各角色侧栏/创建入口的完整清单（本包只抽样，不写 RMS/PIM 等截图未出现的模块）
- [ ] 单角色测试账号邮箱（前置条件按角色名书写，执行前补台账）

## Out of Scope

- KMS Admin / PKI Admin / Group 权限（非本张角色说明的产品/工厂层）
- 创建 Module / Add Asset Type 专项（独立需求，本包不并）

---

## 设计自检

### 变更类型

- [x] 已声明 Logic
- [x] P0 侧重赋权主路径、无权限隐藏、角色写入口差异
- [x] 未堆无验收依据的样式细节为 P0
- [x] 命中类型 C，已按权限两维写能力与无权限隐藏

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（未命中）

### 多角色可见 / 触达（类型 C）

- [x] 产品内角色 × 写入口显隐矩阵已写
- [x] 工厂 Admin vs Manager 已写
- [x] 无权限「不显示」已写；接口绕过为独立 P1
- [x] 赋权后目标用户权限生效（操作者改角色 ≠ 仅操作者自己看到）已写 TP-PRD-MEM-02 / TP-FAC-MEM-02

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）
