# Sprint `OBIS-20260727-20260807` 测试数据准备清单

> 来源：本 Sprint 三个 feature 的功能测试用例前置条件汇总
> - [`ux-p2-member-unify`](../../sprints/OBIS-20260727-20260807/features/ux-p2-member-unify/testcases/ux-p2-member-unify.md)（25 条）
> - [`ux-p2-detail-supplement`](../../sprints/OBIS-20260727-20260807/features/ux-p2-detail-supplement/testcases/ux-p2-detail-supplement.md)（27 条）
> - [`ux-p2-audit-unify`](../../sprints/OBIS-20260727-20260807/features/ux-p2-audit-unify/testcases/ux-p2-audit-unify.md)（12 条）
>
> 合计 64 条用例。本文列出执行前必须就位的账号、资源、日志、环境与工具，以及不可逆数据的用量与执行顺序约束。
>
> **配套文档**：造好的真实数据登记在 [`data-ledger.md`](data-ledger.md)；执行顺序见 [`execution-plan.md`](execution-plan.md)；环境地址与凭证见 `config/env.local.yaml`；代号含义见 [`config/conventions.md`](../../../config/conventions.md)。

## 0. 结论摘要

本 Sprint 的数据准备难点不在数量，而在三点：

1. **不可逆消耗**：Transfer Admin 与 Account 删除类用例执行一次即改变数据身份，无法原地重跑。需要 **5 个一次性可删账号** 与 **5 个独立资源实例**（2 KMS Key / 1 PKI Cert / 2 Factory），或准备复位手法。
2. **特殊状态资源需要提前找开发或运维构造**：「已归档 / 已锁定 / 已删除 / 已销毁」四种状态的资源，且待删用户须在其中担任 Admin。这是本 Sprint 最可能卡住执行的数据项，建议提前 2～3 天提需求。
3. **跨租户数据**：Audit 的 Organization 列与筛选、以及 OTA/Vulnerability 的「会上线 / 不上线租户」对照，都要求至少 2 个租户环境同时可用。

---

## 1. 租户与组织要求

| 编号 | 要求 | 用于 | 备注 |
|---|---|---|---|
| T1 | 主测试租户，会上线 OTA & Vulnerability（雪球系） | 绝大多数用例；detail-supplement 租户默认配置用例 | 需含 4 类 Role：雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager |
| T2 | 不上线 OTA & Vulnerability 的租户（宜家及其关联租户） | detail-supplement「不上线租户所有 Role 均不配置」 | 需有可登录用户验证 Tab 不可见 |
| T3 | 第二个 Organization 的操作人（可复用 T2 或 SNB 运营账号） | audit-unify Organization 列与 Organization 筛选 | 需要该操作人在 T1 的 Group/Product 上留下审计日志，**可行性待与开发确认** |

## 2. 账号矩阵

### 2.1 权限与角色类（可反复使用）

| 编号 | 账号要求 | 用于 |
|---|---|---|
| A1 | System Admin：具备 Account / User(SNB) 删除权限、Role 权限树配置权限 | Account 删除批量转移、Role 树勾选与 OTA/Vulnerability 节点、编辑他人账号 |
| A2 | 普通 Active 用户，**非** System Admin，且非任何资源 Admin | 验证他人行 Edit 置灰、Transfer Admin 置灰 + hover「No Permission / 无权限」 |
| A3 | 资源 Admin 本人：同时是 KEY-1 / KEY-2 的 KMS Admin、CERT-1 的 PKI Admin、FAC-1 / FAC-2 的 Factory Admin | 全部 Transfer Admin 用例的操作人 |
| A6 | 同租户 **Locked** 状态用户 | 验证 Transfer 下拉不含 Locked（或置灰 + User is locked） |

> A3 合并三类 Admin 身份可以，因为降级只作用于对应资源；但 **A3 不可同时用作 Account 删除用例的待删用户**，否则删除会连带清掉 Transfer 场景。

### 2.2 Transfer 目标类（会被授予 Admin，建议专用）

| 编号 | 账号要求 | 用于 |
|---|---|---|
| A4 | 同租户 Active，**已在** KEY-1 Member 且非 Admin | KMS Transfer 目标已在列表 |
| A5 | 同租户 Active，**不在** KEY-2 Member | KMS Transfer 目标不在列表（新增为 Admin） |
| A8 | 同租户 Active，PKI Transfer 目标（在或不在 CERT-1 Member 均可） | PKI Transfer 成功移交 |
| A10 | 同租户 Active，**已在** FAC-1 Member 且非 Factory Admin | Factory Transfer 目标已在列表 |
| A11 | 同租户 Active，**不在** FAC-2 Member | Factory Transfer 目标不在列表 |
| A12 | 同租户 Active，作为 Account 删除时的 Target Admin | Confirm Action 批量转移的接收方 |

### 2.3 一次性可删账号（执行后销毁，不可复用）

| 编号 | 账号要求 | 用于 |
|---|---|---|
| D1 | 可删除账号，且**已加入某 Product（PROD-5）的 Member** | Account 删除后 Product Member 不可见该用户、无 `-` 空壳行 |
| D2 | 可删除账号，**命中至少一类** Product Owner / KMS Admin / PKI Admin / Factory Admin | Confirm Action 弹窗文案与资源卡片、选择 Target Admin 移交并删除 |
| D3 | 可删除账号，对**已归档**与**已锁定**资源仍为 Admin；另关联**已删除 / 已销毁**资源作对照 | 归档锁定纳入、已删除已销毁不纳入 |
| D4 | 可删除账号，**不是**任何 Product Owner / KMS·PKI·Factory Admin | 无 Admin 身份可直接删除（不弹批量转移窗） |
| D5 | 在 Account(SNB) / User(SNB) 侧命中 Admin 条件的可删账号 | SNB 与 Account 行为一致性 |

> D2 需覆盖多类资源才能验证「资源卡片按类型展示、数量为 0 的类型不展示卡片」，建议让 D2 同时担任 Product Owner + KMS Admin 两类，留出至少一类为 0 的对照。

### 2.4 `+n` 与角色展示类

| 编号 | 账号要求 | 用于 |
|---|---|---|
| R1 | User Role 数量足以在 Account 列表触发 `+n`（建议 ≥ 3 个角色） | Account 列表 User Role hover、Account 详情 Role hover |
| R2 | 仅 1 个 User Role | 单值无 `+n` 对照 |
| R3 | 角色数恰好落在溢出边界（刚出现 `+n`） | `+n` 数值与小窗内容边界正确性 |

### 2.5 OTA / Vulnerability 权限类

| 编号 | 账号要求 | 用于 |
|---|---|---|
| P1 | T1 内，**无** Vulnerability Tab Page 权限 | Product 详情不展示 Vulnerability Tab |
| P2 | T1 内，**无** OTA Tab Page 权限 | Product 详情不展示 OTA Tab |
| P3 | T1 内，同时具备两项权限 | 两 Tab 可见且可进入 |
| P4 | T2（不上线租户）内任一用户 | 确认两 Tab 均不可见 |

> P1～P3 可用同一账号通过改 Role 权限切换，但用例要求「变更权限后重新登录 / 刷新，Tab 显隐与最新权限一致」，因此需保留改权限并重登的操作条件。

## 3. 资源实例清单

### 3.1 KMS

| 编号 | 数据要求 | 用于 |
|---|---|---|
| KEY-1 | A3 为 Admin；Member 含 A4；**至少一名成员 Permission ≥ 2 个**（触发 `+n`） | Member 默认列 / Permission `+n` hover / Organization / Status；Transfer 目标已在列表 |
| KEY-2 | A3 为 Admin；A5 **不在** Member | Transfer 目标不在列表（新增为 Admin） |
| KEY-3 | Operation Log 含**多种 Operation Type** 的审计日志 | KMS Audit Filter 的 Operation Type 筛选 |
| KMS Key List | 存在带 Usage Count 数值的 Key | 列宽 + Usage Count 普通文字样式 |

### 3.2 PKI

| 编号 | 数据要求 | 用于 |
|---|---|---|
| CERT-1 | A3 为 PKI Admin；同租户有其他 Active 用户 | PKI Member 列、Transfer 弹窗与成功移交 |
| CERT-1 Audit | 存在审计日志 | PKI Audit 与 Group 基准一致 |
| PKI List | 可展开到有 **Issued Count** 数值的节点（如 DAC Template） | 列宽 + Issued Count 普通文字样式 |

### 3.3 Factory

| 编号 | 数据要求 | 用于 |
|---|---|---|
| FAC-1 | A3 为 Factory Admin；A10 **已在** Member | Factory Member 默认列 / Columns / Admin 菜单；Transfer 目标已在列表 |
| FAC-2 | A3 为 Factory Admin；A11 **不在** Member | Transfer 目标不在列表 |
| Factory List | 有列表数据 | 列宽抽样 |

### 3.4 Group

| 编号 | 数据要求 | 用于 |
|---|---|---|
| GRP-1 | Member 列表**同时含 Admin 行与非 Admin 行** | Admin 行隐藏三点菜单、非 Admin 行保留菜单 |
| GRP-1 Audit | ① 跨多日日志；② 靠近 00:00:00 / 23:59:59 的边界记录；③ 含 ≥ 2 个不同 Organization 的操作人；④ 含 Operation Details 长文案（可触发单元格溢出 hover）；⑤ 可现场制造一条新操作以验证 Refresh | Audit 默认列、Filter 时间边界、Organization 筛选、溢出 hover、Refresh / Sort |
| GRP-1 Linked Product | 某行 Role 形如 `Member +2`（如 Version Manager、Product Manager 被折叠） | Linked Product Role `+n` hover |
| Group List | 有列表数据 | 列宽核对 |

### 3.5 Product

| 编号 | 数据要求 | 用于 |
|---|---|---|
| PROD-1 | 有 Prod 环境版本，且**存在多个 Prod 版本**（便于验证「最新一个」） | Version 列取 Prod 最新 |
| PROD-2 | 仅有 Test 版本，或 **Test 比 Prod 更新** | Version 仍只取 Prod，不取 Test |
| PROD-3 | 无任何 Prod 版本（仅 Test 或完全无版本） | Version 列展示 `-` |
| PROD-4 | Module 数量足以「首 Tag + `+n`」，且**溢出项多到浮层可滚动**（建议 ≥ 6 个 Module） | Module `+n` 浮层标题、Tag 全量、滚动 |
| PROD-5 | Member 含 D1 账号 | Account 删除后 Product Member 不可见 |
| PROD-6 | 详情含 OTA 与 Vulnerability Tab，且有审计日志 | Tab 权限显隐、Product Audit 对齐基准 |

### 3.6 特殊状态资源（**最高优先级，需提前提资源申请**）

| 编号 | 数据要求 | 用于 |
|---|---|---|
| S-ARCH | **已归档**资源，D3 在其中为 Admin | 归档纳入 Confirm Action 校验 |
| S-LOCK | **已锁定**资源，D3 在其中为 Admin | 锁定纳入校验 |
| S-DEL | **已删除**资源，D3 曾为 Admin | 不纳入校验（不因其单独弹批量转移窗） |
| S-DESTROY | **已销毁**资源，D3 曾为 Admin | 同上 |

> 这四类状态通常无法由测试人员在前台自行构造，且 S-DEL / S-DESTROY 是否在环境中仍可区分需要确认。**建议本项单独找开发确认构造方式与排期。**

### 3.7 其余大列表（列宽抽样）

Account 列表、Group 列表、U-safe List、Device History、DAC Report 中**至少两类**需有数据，用于第一列 280px / Status 160px / Operation 64px 的抽样核对。

### 3.8 Audit 数据覆盖面

Group（基准）、Account 详情、My Profile、KMS Key 详情、PKI 资源详情、Product 详情 —— **六处均需存在审计日志**，否则一致性对照用例无法执行。建议执行前统一制造一批操作以铺日志。

## 4. 不可逆数据的用量与执行顺序

### 4.1 消耗清单

| 操作 | 用例数 | 消耗 | 复位方式 |
|---|---|---|---|
| KMS Transfer Admin 成功 | 2 | A3 在 KEY-1 / KEY-2 降级为 Normal Member | 用新 Admin（A4 / A5）登录，再 Transfer 回 A3 |
| PKI Transfer Admin 成功 | 1 | A3 在 CERT-1 降级为 Normal Member | 用 A8 登录 Transfer 回 A3 |
| Factory Transfer Admin 成功 | 2 | A3 在 FAC-1 / FAC-2 降级为 **Factory Manager** | 用 A10 / A11 登录 Transfer 回 A3 |
| Account 删除 | 5 | D1～D5 账号销毁 | **无法复位**，重跑需新建账号 |

### 4.2 建议执行顺序

1. **只读 / 展示类先行**：Audit 全部 12 条、detail-supplement 的 `+n`、Toast、勾选框、列宽、Version 类用例，以及 Member 列表默认列、工具栏、Transfer 弹窗 UI（打开后 Cancel，不 Confirm）。此阶段不破坏数据。
2. **Transfer E2E**：KMS → PKI → Factory，每条执行后按 4.1 复位，再进行下一条。
3. **Account 删除类最后**：先 D4（直接删除）→ D1（Product Member 可见性）→ D3（资源状态范围）→ D2（批量转移）→ D5（SNB 一致性）。删除会同时改变资源 Admin 归属，放在最后可避免污染前序场景。

> 若需回归重跑，第 2、3 阶段的数据必须重新准备；建议一次性多备 1～2 套 D 类账号。

## 5. 环境与工具要求

| 项 | 要求 | 用于 |
|---|---|---|
| 多语言 | 系统可在中 / 英文之间切换 | Transfer 弹窗中英文文案、成功 Toast 中英文、`+n` hover 中英文 |
| 浏览器开发者工具或屏幕标尺 | 可测量列宽像素 | 第一列 280px、Status 160px、Operation 64px 核对 |
| Figma 访问权限 | node **15959-188662** | 勾选框主题色对照 |
| 剪贴板权限 | 浏览器允许复制 | Audit Operator 邮箱 icon hover 后复制完整邮箱 |
| 桌面常规 + 可收窄视口 | 大屏验中间列均分；小屏验横向滚动与固定三列不被挤占 | 开发者工具 Device/Resize 即可 |
| Role 权限变更通道 | 可修改 Role 权限并重新登录 / 刷新生效 | OTA / Vulnerability Tab 显隐随权限变更 |

## 6. 阻塞排期的待确认项

以下来自三份用例文档的「待确认」，**建议在数据准备阶段一并向产品 / 开发澄清**，否则相关用例判定标准不明确：

**audit-unify**
- [ ] KMS Filter 内 Operation Type 是单选 / 多选 / 输入，可选值来源（直接影响 KEY-3 的日志类型需要铺多少种）
- [ ] Organization Filter 是否模糊匹配；空组织如何展示与筛选
- [ ] 默认列顺序是否固定为 Operator → Organization → Operation Type →（Details）→ Operation Time
- [ ] Profile 与 Account Audit 是否共用同一组件
- [ ] Product Audit 在 MeterSphere 中的最终挂载路径（当前暂挂 `/Cloud/Product`）

**detail-supplement**
- [ ] 勾选框「所有」是否含 Radio、Switch、树半选；主题色 token / hex 是否仅以 Figma 为准
- [ ] 第一列是否一律 Name；Operation 64px 是否仅放 ⋮
- [ ] 本人编辑：抽屉 vs 弹窗字段集是否完全一致
- [ ] 同为 Prod 时「最新」的排序口径（创建时间 / 发布时间 / 版本号）—— **直接决定 PROD-1 要造几个版本、按什么顺序造**

**member-unify**
- [ ] acceptance 无开放项；确认 KMS/PKI Member 挂载 Key Detail / Cert & Template Detail，Account SNB 路径为 `/Cloud/Operation/User(SNB)`

## 7. 准备检查清单

执行前逐项打勾：

- [ ] T1 / T2 两个租户可用，T1 内 4 类 Role 已就位
- [ ] A1、A2、A3、A6 权限账号可登录
- [ ] A4、A5、A8、A10、A11、A12 六个 Transfer / Target 目标账号为 Active
- [ ] D1～D5 五个一次性可删账号已按身份要求配置
- [ ] R1、R2、R3 三个角色数量档位的账号已就位
- [ ] P1～P4 权限对照账号已就位
- [ ] KEY-1、KEY-2、KEY-3 就位，KEY-1 有成员 Permission ≥ 2
- [ ] CERT-1 就位，PKI List 有 Issued Count 数值节点
- [ ] FAC-1、FAC-2 就位
- [ ] GRP-1 的 Member、Audit、Linked Product 三类数据均满足
- [ ] PROD-1～PROD-6 六个产品就位（版本 / Module / Member / Tab 各维度）
- [ ] **S-ARCH、S-LOCK、S-DEL、S-DESTROY 四类状态资源已确认构造方式并完成**
- [ ] 六处 Audit 均有日志，且 Group Audit 含跨日、边界时间、跨 Organization、长文案
- [ ] 中英文切换、Figma node 15959-188662、开发者工具均可用
- [ ] 第 6 节待确认项已澄清或已明确「按现网 / 不阻塞」
