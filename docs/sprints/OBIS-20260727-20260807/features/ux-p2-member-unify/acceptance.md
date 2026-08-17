# Story: 【体验优化P2】Member功能统一

**来源**: [飞书项目 User Story #7042512337](https://project.feishu.cn/obis/userstory/detail/7042512337)  
**空间**: OBIS (`obis`)  
**编号**: 780 | **优先级**: Must | **Epic**: UI及体验优化  
**Sprint**: OBIS-20260727-20260807  
**模式**: Large（跨 KMS/PKI/Factory/Group/Product/Account 多入口；列表规格、Transfer、删除移交分层验收，需独立测试点表）  
**变更类型**: Hybrid（主 UI/UX：Member 默认列、Permission `+n`、Operation 菜单与置灰/无权限提示、Transfer/Confirm Action 弹窗交互与文案统一；次 Logic：Transfer 后 Role/权限点变更、Account 删除批量移交与 Product Member 清理）

> Story 导出：`story/obis-7042512337-体验优化p2-member功能统一/obis-7042512337-体验优化p2-member功能统一.md`  
> 判定依据：Epic/标题为体验优化，正文以列表列、菜单、弹窗交互与 Figma/截图为主；Transfer 成功后的角色权限与 Account 删除拦截属交付逻辑，作次类型覆盖。

---

## Story AC

1.（AC-01）用户打开 KMS / PKI Member 列表时，默认可见 Name、Role、Permission（默认 1 个 + `+n` hover 全量）、Organization（Permission 后）、Status；Admin 行 Operation 仅含 Transfer Admin，且仅 Admin 本人可操作，他人置灰并 hover「No Permission / 无权限」。

2.（AC-02）KMS Admin 本人打开 Transfer 弹窗并成功确认后，目标用户成为 Admin（已在列表则刷新 Role 并授予全部权限点，不在则新增），原 Admin 仍在列表且 Role 变为 Normal Member（权限点不变），Toast 为「操作成功 / Operation Successful」。

3.（AC-03）PKI Admin 本人成功 Transfer 后，目标用户成为 Admin 并获全部权限点（存在则刷新，不存在则新增），原 Admin 变为 Normal Member（权限点不变），弹窗标题/字段/报错为 PKI 文案。

4.（AC-04）用户打开 Factory Member 列表时，默认仅 Name、Role、Status；Organization / Operator / Join Time 默认隐藏；Admin 行 Operation 为 Reset Password 与 Transfer Admin（无 Remove），且仅 Admin 本人可操作。

5.（AC-05）Factory Admin 本人成功 Transfer 后，目标用户 Role 为 Factory Admin（存在则刷新，不存在则新增），原 Admin Role 变为 Factory Manager，Toast 成功。

6.（AC-06）用户打开 Group Member 列表时，仅 Admin 用户行隐藏 Operation 三点菜单；其余角色行仍保留三点菜单；本 Story 不做 Group Transfer。

7.（AC-07）Account 被删除后，该用户不应再出现在 Product Member 列表中（不得残留 Name/Status 为 `-` 的空壳行）。

8.（AC-08）在 Account / Account（SNB）删除用户时，若该用户为某 Product Owner、KMS Admin、PKI Admin 或 Factory Admin（命中任一；资源范围为已归档/已锁定，不含已删除/已销毁），则不可直接删除，应弹出 Confirm Action，选择 Target Admin 并确认后移交全部命中资源 Admin、删除用户且 Toast 成功。

---

## 测试点

> **来源**：`AC-0x` / `需求描述` / `QA扩展`。  
> **优先级偏置（主 UI/UX）**：列表列、Permission 折叠、菜单项、置灰/无权限、弹窗控件与文案为 P0 主密度；Transfer/删除后的角色与数据后果（次 Logic）保留独立 P0，但不额外扩展深状态机矩阵。  
> **P1**：Cancel/蒙层、Columns 打开隐藏列、无 Admin 身份直删等边界；**P2**：纯中英文对照。

### KMS — Member 列表（UI/UX）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-KMS-L01 | AC-01 | P0 | 默认可见列：Name、Role、Permission、Organization、Status；Organization 紧跟 Permission 之后 |
| TP-KMS-L02 | AC-01 | P0 | Permission：默认只展示 1 个权限 Tag，其余以 `+n` 折叠；hover `+n` 展示全部 Permission |
| TP-KMS-L03 | AC-01, 需求描述 | P0 | Admin 行打开三点菜单：菜单项仅 Transfer Admin，无其它操作项 |
| TP-KMS-L04 | AC-01 | P0 | Admin 本人查看本行：Transfer Admin 可点（亮起） |
| TP-KMS-L05 | AC-01 | P0 | 非 Admin 本人查看 Admin 行：Transfer Admin 置灰；hover 提示「No Permission / 无权限」 |
| TP-KMS-L06 | 需求描述 | P1 | Organization 展示租户简称；Status 展示 Account 状态（如 Active / Locked） |
| TP-KMS-L07 | 需求描述 | P1 | Member Tab 工具栏仍可见 Filter、Columns、Refresh、Sort、`+ Add`（本次不改工具栏能力，回归入口可达） |

### KMS — Transfer Admin 弹窗（UI/UX）与移交结果（Logic）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-KMS-T01 | AC-02 | P0 | 弹窗标题为「Transfer KMS Admin / 转移密钥管理员」；字段「Select KMS Admin」必填带 `*`；Placeholder「Please Select / 请选择」 |
| TP-KMS-T02 | AC-02, 需求描述 | P0 | 下拉仅同租户其他 **Active** 用户邮箱；不含当前 Admin；不展示 Locked 置灰 + User is locked（以正文为准） |
| TP-KMS-T03 | AC-02 | P0 | 未选目标点 Confirm：字段报错「KMS Admin is required / 密钥管理员是必填项」；不关闭弹窗、不移交 |
| TP-KMS-T04 | AC-02 | P0 | 目标已在 Member：Confirm 后 Role→Admin、授予全部权限点；Toast「操作成功 / Operation Successful」；弹窗关闭；列表刷新 |
| TP-KMS-T05 | AC-02 | P0 | 目标不在 Member：Confirm 后列表新增该用户为 Admin 且全部权限点 |
| TP-KMS-T06 | AC-02 | P0 | 原 Admin 仍在列表；Role→Normal Member；权限点与移交前一致 |
| TP-KMS-T07 | 需求描述 | P1 | Cancel / 右上角关闭：关闭弹窗且不移交；点击蒙层不可关闭 |
| TP-KMS-T08 | QA扩展 | P2 | 标题、必填报错、Toast 中英文分别正确 |

### PKI — Member 列表（UI/UX）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PKI-L01 | AC-01 | P0 | 默认列与顺序同 KMS：Name、Role、Permission（1 个 + `+n` hover 全量）、Organization（Permission 后）、Status |
| TP-PKI-L02 | AC-01 | P0 | Admin 行 `⋮` 仅 Transfer Admin；本人可点，他人置灰 + hover「No Permission / 无权限」 |

### PKI — Transfer Admin 弹窗（UI/UX）与移交结果（Logic）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PKI-T01 | AC-03 | P0 | 标题「Transfer PKI Admin / 转移证书管理员」；字段 Select Certificate Admin 必填 `*`；Placeholder「Please Select / 请选择」；未选报错「Certificate Admin is required / 证书管理员是必填项」 |
| TP-PKI-T02 | AC-03 | P0 | 下拉仅同租户其他 Active 邮箱；Confirm 成功：目标→Admin+全部权限点（在则刷新/不在则新增）；原 Admin→Normal Member 且权限点不变；Toast 成功并关窗 |
| TP-PKI-T03 | 需求描述 | P1 | Cancel/关闭不执行移交；蒙层不可关 |

### Factory — Member 列表（UI/UX）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-FAC-L01 | AC-04 | P0 | 默认可见列仅 Name、Role、Status；Organization、Operator、Join Time **默认不展示** |
| TP-FAC-L02 | AC-04, 需求描述 | P1 | 通过 Columns 可将 Organization / Operator / Join Time 打开后可见 |
| TP-FAC-L03 | AC-04 | P0 | Admin 行 `⋮` 含 Reset Password、Transfer Admin；**无 Remove** |
| TP-FAC-L04 | AC-04 | P0 | Reset Password 与 Transfer Admin 均仅 Admin 本人可点；他人置灰 + hover「No Permission / 无权限」 |

### Factory — Transfer Admin 弹窗（UI/UX）与移交结果（Logic）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-FAC-T01 | AC-05 | P0 | 标题「Transfer Factory Admin / 转移工厂管理员」；Select Factory Admin 必填 `*`；Placeholder「Please Select / 请选择」；未选报错「Factory Admin is required / 工厂管理员是必填项」 |
| TP-FAC-T02 | AC-05 | P0 | 目标已在列表：Confirm 后 Role→Factory Admin；Toast 成功；弹窗关闭 |
| TP-FAC-T03 | AC-05 | P0 | 目标不在列表：Confirm 后新增为 Factory Admin |
| TP-FAC-T04 | AC-05 | P0 | 原 Admin 仍在列表，Role→Factory Manager |
| TP-FAC-T05 | 需求描述 | P1 | Cancel/关闭不执行；蒙层不可关；下拉仅同租户其他 Active |

### Group — Member（UI/UX）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-GRP-01 | AC-06 | P0 | Group Member：Admin 用户行不展示 Operation `⋮` |
| TP-GRP-02 | AC-06 | P0 | 非 Admin 行仍展示 `⋮`，菜单项按现网可用（本次不改非 Admin 菜单内容） |
| TP-GRP-03 | AC-06, 需求描述 | P0 | 全表无 Transfer Admin / Group Transfer 入口 |

### Product — Member（Account 删除后清理，Logic）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PRD-01 | AC-07 | P0 | Account 删除成功后，曾加入的 Product → Member 列表中不可见该用户 |
| TP-PRD-02 | AC-07, 需求描述 | P0 | 删除后刷新列表：无 Name/Status 为 `-` 的空壳残留行（对照 ref-08 问题现状） |

### Account — 删除时批量转移弹窗（UI/UX）与移交删除（Logic）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACC-D01 | AC-08 | P0 | Account / Account（SNB）删除：用户为 Product Owner / KMS Admin / PKI Admin / Factory Admin（命中任一）时不可直接删除，弹出 Confirm Action |
| TP-ACC-D02 | AC-08 | P0 | 弹窗标题「Confirm Action / 确认操作」；提示文案中英文正确（须先转移再删除）；Target Admin 必填带 `*`；Placeholder「Please Select / 请选择」 |
| TP-ACC-D03 | AC-08 | P0 | 资源清单按 Product / KMS / PKI / Factory 卡片展示；有数量卡片显示 `Resource / 资源：n`；hover 展示全部资源名；数量为 0 的卡片不展示 |
| TP-ACC-D04 | AC-08, 需求描述 | P0 | 纳入校验：已归档、已锁定；不纳入：已删除、已销毁 |
| TP-ACC-D05 | AC-08 | P0 | Target Admin 下拉仅同租户其他 Active 邮箱；未选 Confirm 报错「Target Admin is Required / 目标管理员是必填项」 |
| TP-ACC-D06 | AC-08 | P0 | Confirm 后：命中资源 Admin 全部移交目标；Toast 成功；用户被删除；目标加入各资源 Member 或刷新 Role/权限 |
| TP-ACC-D07 | 需求描述 | P1 | Cancel / 关闭不执行删除与移交；蒙层不可关 |
| TP-ACC-D08 | QA扩展 | P1 | 用户无上述 Admin/Owner 身份时，可按现网直接删除（不弹批量转移窗） |
| TP-ACC-D09 | QA扩展 | P1 | Account（SNB）与 Account：命中拦截、弹窗与移交删除行为一致 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 KMS/PKI 列表与操作权限 | TP-KMS-L01～L07；TP-PKI-L01～L02 | ✅ |
| AC-02 KMS Transfer | TP-KMS-T01～08 | ✅ |
| AC-03 PKI Transfer | TP-PKI-T01～03 | ✅ |
| AC-04 Factory 列表 | TP-FAC-L01～04 | ✅ |
| AC-05 Factory Transfer | TP-FAC-T01～05 | ✅ |
| AC-06 Group Admin 隐藏菜单 | TP-GRP-01～03 | ✅ |
| AC-07 Product Member 删除后清理 | TP-PRD-01～02 | ✅ |
| AC-08 Account 删除批量转移 | TP-ACC-D01～09 | ✅ |

**AC-01～AC-08 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| KMS 列表（UI） | 5 | 2 | 0 | 7 |
| KMS Transfer（UI+Logic） | 6 | 1 | 1 | 8 |
| PKI 列表（UI） | 2 | 0 | 0 | 2 |
| PKI Transfer（UI+Logic） | 2 | 1 | 0 | 3 |
| Factory 列表（UI） | 3 | 1 | 0 | 4 |
| Factory Transfer（UI+Logic） | 4 | 1 | 0 | 5 |
| Group（UI） | 3 | 0 | 0 | 3 |
| Product Member 清理（Logic） | 2 | 0 | 0 | 2 |
| Account 删除批量转移（UI+Logic） | 6 | 3 | 0 | 9 |
| **合计** | **33** | **9** | **1** | **43** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 35 |
| 需求描述 | 5 |
| QA 扩展 | 3 |

| 变更侧重（约） | 说明 |
|----------------|------|
| UI/UX 主 | 列表列/Permission 折叠/三点菜单与置灰提示、弹窗标题字段 Placeholder 报错蒙层、资源卡片展示 |
| Logic 次 | Transfer 后 Role/权限点、Account 删除拦截与移交删除、Product 空壳清理、资源状态范围 |

---

## 设计自检

### 变更类型

- [x] 已声明 Hybrid（主 UI/UX，次 Logic：Transfer 角色权限 / 删除移交与 Product 清理）
- [x] P0 密度跟主类型：列表与弹窗交互规格优先；次类型仅保留 AC 要求的业务结果 P0，未扩展无关深矩阵
- [x] 未用错误偏置：未把纯样式堆成 Logic 矩阵，也未丢掉 AC-02/05/07/08 的业务结果覆盖
- [x] 命中类型 C（多角色可见）；A/B/D 未命中已标 N/A

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（未命中）

### 多角色可见 / 触达（类型 C）

- [x] 已覆盖 Admin 本人 vs 他人：Transfer / Reset Password 可点与置灰 + No Permission（TP-KMS-L04/05、TP-FAC-L04、TP-PKI-L02）
- [x] Group 仅 Admin 行隐藏菜单 vs 其他角色保留（TP-GRP-01/02）
- [x] Account 删除后 Product Member 侧不可见该用户（TP-PRD-01～02）
- [x] 删除前 Admin/Owner 身份拦截与移交目标用户（TP-ACC-D01～06）

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）

---

## 待确认

- [ ] （无开放项；Description / 评论已确认：Transfer 仅 Active；Group 不做 Transfer；资源状态范围已写入）

## Out of Scope

- Group Transfer（明确暂不做）
