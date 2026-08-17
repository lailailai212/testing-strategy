# 权限 — 创建 Module / Add Asset Type 功能测试用例

> 来源：`acceptance.md（同 feature 包）`（含 TP-ID）  
> 需求：权限说明 — 仅 Product Manager、Resource Manager 有创建 Module / Add Asset Type 权限（[Story #7041825174](https://project.feishu.cn/obis/userstory/detail/7041825174)）  
> 用例数：11（P0 × 6，P1 × 3，P2 × 2；E2E × 4，UI × 3，Functional × 4）；覆盖 TP 20 条  
> 入口规则：`Product` → 产品详情 → Overview / Assets；`+ Add` = 创建 Module；`Create Assets Type` ≡ `+ Create Asset...` = Add Asset Type（已确认）  
> 产品规则：仅 Product Manager、Resource Manager 具备上述权限；**无权限时入口不显示**（2026-07-17 确认）；非授权角色清单**待确认**（抽测至少一类非授权角色）  
> 设计原则：一条用例覆盖一个用户场景，场景内可校验多个测试点；步骤清晰连贯；单用例步骤 ≤ 10  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：`/Cloud/Product/Overview`、`/Cloud/Product/Assets`（见 `docs/modules/metersphere-modules.json`）  
> 标签列：仅可读业务名 `CreateModule与AddAssetType权限`（不含 TP-ID / AC 序号）  
> 备注列：标明需求来源；来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Product-Overview】【E2E】创建 Module - Product Manager 可从 Overview 与 Assets 创建 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P0 | 1. 使用仅含 **Product Manager** 角色（或明确含该角色）的账号登录<br>2. 存在可进入的 Product 详情（如 Test 环境产品）<br>3. 记录当前 Module 子 Tab 列表 | [1] 进入 Product 详情 → Overview，定位 Module 子 Tab 行<br>[2] 点击 `+ Add`，按现网流程完成创建 Module 并提交<br>[3] 切换到 Assets Tab，确认新 Module 可见；再次点击 Assets 上 Module 行 `+ Add`，再创建一个 Module | [1] 可见橙色 `+ Add`，可点击<br>[2] 创建成功；新 Module 出现在 Overview 的 Module 子 Tab<br>[3] Assets 同步可见已创建 Module；Assets 的 `+ Add` 同样可成功创建；两处入口行为一致 | 来源 AC-01: 具备 Product Manager 或 Resource Manager 角色的用户，在 Product 详情 Overview / Assets 的 Module 行点击 `+ Add`，应能进入并成功完成「创建 Module」。<br>来源 AC-05: Overview 与 Assets 上的 Module `+ Add` 受同一「创建 Module」权限控制，有权限时两处均可创建，无权限时两处均不显示。 |
| 【Product-Overview】【E2E】创建 Module - Resource Manager 可创建 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P0 | 1. 使用仅含 **Resource Manager** 角色（或明确含该角色）的账号登录<br>2. 存在可进入的 Product 详情 | [1] 进入 Product 详情 → Overview，定位 Module 行 `+ Add`<br>[2] 点击 `+ Add`，按现网流程完成创建 Module | [1] 可见且可点击 `+ Add`<br>[2] 创建成功；新 Module 出现在 Module 子 Tab | 来源 AC-01: 具备 Product Manager 或 Resource Manager 角色的用户，在 Product 详情 Overview / Assets 的 Module 行点击 `+ Add`，应能进入并成功完成「创建 Module」。 |
| 【Product-Overview】【E2E】Add Asset Type - Product Manager 双入口均可完成 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P0 | 1. Product Manager 账号已登录<br>2. 存在可进入的 Product 详情；至少已有一个 Module（如 Module_1）<br>3. 可观察 Add Asset Type 成功后的页面变化（按现网，如资产类型卡片/列表更新） | [1] Overview → 定位 `Create Assets Type`，点击并按现网流程完成 Add Asset Type<br>[2] 切换到 Assets Tab，点击右侧 `+ Create Asset...`，再次按同一流程完成 Add Asset Type<br>[3] 对比两入口发起时的权限校验与可完成性 | [1] 可见可点 `Create Assets Type`；操作成功完成<br>[2] 可见可点 `+ Create Asset...`；可完成与 Overview 相同的 Add Asset Type 动作<br>[3] 两入口为同一权限、同一动作，均可完成 | 来源 AC-02: 具备 Product Manager 或 Resource Manager 角色的用户，通过 Overview 的 `Create Assets Type` 或 Assets 的 `+ Create Asset...`（同一权限、同一动作），应能成功完成「Add Asset Type」。<br>来源 AC-06: Overview `Create Assets Type` 与 Assets `+ Create Asset...` 为同一权限、同一动作：有权限任选一入口可完成；无权限两入口均不显示。 |
| 【Product-Overview】【E2E】Add Asset Type - Resource Manager 可从 Overview 完成 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P0 | 1. Resource Manager 账号已登录<br>2. 存在可进入的 Product 详情及可用 Module | [1] Overview 点击 `Create Assets Type`<br>[2] 按现网流程完成 Add Asset Type | [1] 按钮可见可点<br>[2] 成功完成 Add Asset Type | 来源 AC-02: 具备 Product Manager 或 Resource Manager 角色的用户，通过 Overview 的 `Create Assets Type` 或 Assets 的 `+ Create Asset...`（同一权限、同一动作），应能成功完成「Add Asset Type」。 |
| 【Product-Overview】【UI】创建 Module - 非授权角色两处入口不显示 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P0 | 1. 使用**非** Product Manager 且**非** Resource Manager 的账号登录（如 System Manager 或 Normal User，角色以产品清单为准）<br>2. 该账号可进入同一 Product 详情 | [1] Overview → 观察 Module 行是否存在 `+ Add`<br>[2] Assets → 观察 Module 行是否存在 `+ Add`<br>[3] 确认无法新增 Module | [1] Overview **不显示** `+ Add`，无法创建 Module<br>[2] Assets 同样**不显示** `+ Add`，与 Overview 表现一致<br>[3] Module 列表无因本操作新增 | 来源 AC-03: 不具备 Product Manager 且不具备 Resource Manager 的用户，对「创建 Module」入口（`+ Add`）应不显示，无法创建 Module。<br>来源 AC-05: Overview 与 Assets 上的 Module `+ Add` 受同一「创建 Module」权限控制，有权限时两处均可创建，无权限时两处均不显示。 |
| 【Product-Overview】【UI】Add Asset Type - 非授权角色两处入口不显示 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P0 | 1. 非 Product Manager 且非 Resource Manager 账号已登录并可进入 Product 详情 | [1] Overview 观察是否存在 `Create Assets Type`<br>[2] Assets 观察是否存在 `+ Create Asset...`<br>[3] 确认未新增 Asset Type / 未完成创建 | [1] Overview **不显示** `Create Assets Type`，无法 Add Asset Type<br>[2] Assets **不显示** `+ Create Asset...`，与 Overview 表现一致<br>[3] 无成功创建结果 | 来源 AC-04: 不具备 Product Manager 且不具备 Resource Manager 的用户，对「Add Asset Type」两处入口均应不显示，且两入口表现一致。<br>来源 AC-06: Overview `Create Assets Type` 与 Assets `+ Create Asset...` 为同一权限、同一动作：有权限任选一入口可完成；无权限两入口均不显示。 |
| 【Product-Overview】【Functional】多角色叠加 - 含 PM 或 RM 时仍可创建 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P1 | 1. 准备同时拥有 Product Manager（或 Resource Manager）**与**其他角色的账号（权限取并集 **待确认**）<br>2. 可进入 Product 详情 | [1] 使用多角色账号进入 Overview<br>[2] 分别尝试 `+ Add` 创建 Module，以及 `Create Assets Type` 完成 Add Asset Type | [1] 页面可正常进入<br>[2] 仍具备创建 Module / Add Asset Type 能力（若产品确认取并集）；若产品规定非并集，以产品结论为准并更新本条 | 来源 QA扩展: 用户同时拥有 Product Manager（或 Resource Manager）与其他角色时，仍具备创建 Module / Add Asset Type（权限取并集，待确认） |
| 【Product-Overview】【Functional】接口绕过 - 无权限调用创建接口被拒绝 | /Cloud/Product/Assets | 创建Module与AddAssetType权限| P1 | 1. 非授权角色账号已登录（可拿会话 Token）<br>2. 已知创建 Module / Add Asset Type 的接口或可抓包对比有权限请求（注入方式待确认）<br>3. 可核对后端是否落库 | [1] 使用无权限会话直接调用创建 Module 接口（或等价绕过 UI 提交）<br>[2] 直接调用 Add Asset Type 接口（或直链/篡改前端后提交）<br>[3] 检查响应与数据是否落库 | [1] 请求被拒绝（403 或业务错误），不创建 Module<br>[2] 同样被拒绝，不完成 Add Asset Type<br>[3] 无新增脏数据 | 来源 QA扩展: 无权限用户绕过 UI 直接调用创建接口被拒绝且不落库；不可通过直链/篡改前端成功提交 |
| 【Product-Overview】【Functional】防重复提交 - 连续点击不产生脏数据 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P2 | 1. Product Manager（或 Resource Manager）已登录<br>2. 可进入创建 Module / Add Asset Type 提交流程 | [1] 在创建 Module 提交流程中连续快速点击提交（或连续点 `+ Add` 后重复提交）<br>[2] 在 Add Asset Type 流程中同样连续快速提交<br>[3] 统计实际创建成功条数 | [1] 不产生重复脏 Module（防重复提交或仅成功一条，按现网实现）<br>[2] 不产生重复脏 Asset Type<br>[3] 成功条数与用户意图一致，无额外脏数据 | 来源 QA扩展: 有权限用户连续点击时不产生重复脏数据 |
| 【Product-Overview】【UI】回归 - Create Version 不因本权限 Story 误伤 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P2 | 1. Product Manager 与 Resource Manager 账号各一<br>2. 记录本 Story 上线前（或对照环境）上述角色对 `Create Version` 的既有可见/可用状态 | [1] 使用 Product Manager 进入 Overview Production Version 区域，观察 `Create Version`<br>[2] 使用 Resource Manager 同样观察 `Create Version`<br>[3] 与对照状态比较 | [1][2][3] `Create Version` 的可见/可用性**不因本 Story**被错误隐藏或错误放开；与既有权限表现一致 | 来源 需求描述: Create Version 入口不在本 Story 权限条款内，不因本 Story 错误限制或错误放开 |
| 【Product-Overview】【UI】中文环境 - 相关入口文案 | /Cloud/Product/Overview | 创建Module与AddAssetType权限| P2 | 1. Product Manager 账号；系统语言切换为中文<br>2. 正式中文文案 **TBD**（确认前按现网文案记录） | [1] Overview 查看 Module `+ Add`、`Create Assets Type` 中文文案<br>[2] Assets 查看 Module `+ Add`、`+ Create Asset...` 中文文案 | [1][2] 文案符合产品约定（确认后对照正式中文）；无 i18n key 裸露 | 来源 QA扩展: 中文环境下按钮文案符合产品约定（正式中文文案 TBD） |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | PM 创建 Module（Overview + Assets） | MOD-POS-01/03/04 |
| 2 | RM 创建 Module | MOD-POS-02 |
| 3 | PM Add Asset Type（双入口） | AST-POS-01/03/04 |
| 4 | RM Add Asset Type | AST-POS-02 |
| 5 | 非授权角色不显示创建 Module 入口 | MOD-NEG-01/02/03 |
| 6 | 非授权角色不显示 Add Asset Type 入口 | AST-NEG-01/02/03 |
| 7 | 多角色叠加 | EDGE-01 |
| 8 | 接口/直链绕过 | EDGE-02/03 |
| 9 | 防重复提交 | EDGE-04 |
| 10 | Create Version 回归 | EDGE-05 |
| 11 | 中文文案 | I18N-01 |

**20 条 TP 均已至少被 1 条用例覆盖。**

## 待确认

- [x] 无权限时入口**不显示**（2026-07-17 确认；用例 5、6 已按此断言）
- [ ] 完整非授权角色清单（用例 5、6 抽测角色）
- [ ] 多角色叠加是否取并集（用例 7）
- [ ] 创建 Module / Add Asset Type 接口路径与失败码（用例 8）
- [ ] 中文环境正式按钮文案（用例 11）
- [ ] 创建表单必填字段与成功态可观察结果（列表/卡片刷新方式）以现网为准，本 Story 不覆盖表单业务规则
