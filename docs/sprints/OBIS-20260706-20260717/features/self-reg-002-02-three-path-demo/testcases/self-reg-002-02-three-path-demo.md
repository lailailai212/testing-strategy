# 【自注册】002-02 — 三路 Demo 预设 功能测试用例

> 来源：`acceptance.md（同 feature 包）`（含 TP-ID）；脑图：`xmind/（同 feature 包）`  
> 需求：【自注册】002-02 — 三路 Demo 预设（[Story #7006975243](https://project.feishu.cn/obis/userstory/detail/7006975243)）  
> 用例数：14（P0 × 9，P1 × 4，P2 × 1；E2E × 8，Functional × 5，UI × 1）；覆盖 TP 37 条  
> 入口规则：自注册 Tenant **Demo 预设已成功**（编排见 002-01）；分别进入 Factory / KMS / PKI / Product 列表与详情验收资源规格。  
> 产品规则：资源名与状态见预期全文；列表展示 `Demo Data` / `测试数据` 或 `Demo-` 标识，列表不展示环境标签，详情页不展示 Demo 标签；Demo 不计配额；Version 默认 **Approved**；可删可编可真实使用；租户隔离。  
> **与 002-01 分工**：**删除行为与「删除后不重建」主测在本文件**；「Demo 已清空后是否再次触发预设」归 002-01。  
> 文案规则：名称/标签/状态等按需求原文写全，禁止用省略号概括。  
> 设计原则：一条用例一个场景；步骤 ≤ 10；标签仅可读业务名  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：按验收页面挂载（见各行）  
> 备注列：来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Ecosystem-Factory-Factory-List】【E2E】Factory Demo - TestCloudFactory 与 TestStation | /Cloud/Ecosystem/Factory/Factory List | 三路Demo预设 | P0 | 1. 自注册 Tenant 的 FM Demo 预设已成功<br>2. 当前用户为租户 Admin（或具备查看 Factory 权限） | [1] 进入 Factory 列表，定位名称 `TestCloudFactory`<br>[2] 进入该 Factory，定位 Programming Station `TestStation`，核对状态与登录方式<br>[3] 核对 Factory 类型、管理员、API 密钥及创建/同步时间 | [1] 存在且仅验收本预设的 1 个 Cloud Factory，名称 `TestCloudFactory`，状态 Active；列表展示 `Demo Data` / `测试数据` 或 `Demo-` 标识，**不**展示环境标签（Test/正式等）<br>[2] 存在 1 个 Programming Station，名称 `TestStation`，状态 Active，登录方式为密码<br>[3] Factory 类型为云工厂（cloud）；管理员为租户 Admin 账号；API 密钥由系统自动生成；创建时间、同步时间为预设完成时刻（年月日时分秒） | 来源 AC-01: Factory 预设应创建 1 个 Cloud Factory + 1 个 Programming Station，状态均为 Active。 |
| 【KMS-Key-List】【E2E】KMS Demo - TestKey 规格与权限 | /Cloud/KMS/Key List | 三路Demo预设 | P0 | 1. Vault KMS Demo 预设已成功<br>2. 以 Tenant Admin 登录 | [1] 进入 KMS Key 列表，定位 `TestKey`<br>[2] 进入密钥详情，核对环境、算法、用途、有效期、生成方式<br>[3] 核对 Tenant Admin 对该密钥的权限范围 | [1] 存在 1 个密钥，名称 `TestKey`；列表有 Demo 标识、无环境标签<br>[2] 环境 Test；对称密钥；规范 AES128；用途包含加密解密、生成并验证 MAC；有效期 2 年；生成方式为系统生成<br>[3] Tenant Admin 对该 Demo 密钥拥有所有权限 | 来源 AC-02: Vault 预设应创建 1 个 KMS 密钥（AES128、TEST 环境）+ 三层 PKI 证书链（PAA/PAI/DAC，Matter 规范，有效期 2 年）。 |
| 【PKI-PKI-List】【E2E】PKI Demo - Test PAA/PAI/DAC 三层链 | /Cloud/PKI/PKI List | 三路Demo预设 | P0 | 1. Vault PKI Demo 预设已成功<br>2. 以 Tenant Admin 登录 | [1] 在证书/模板相关列表定位 `Test PAA`、`Test PAI`、`Test DAC`<br>[2] 逐个打开详情，核对规范、状态、有效期、算法、签名算法及 PAA/DAC 特有字段<br>[3] 核对 Tenant Admin 权限，并确认 Test PAA 为租户自签名测试 PAA（非官方认证 PAA） | [1] 存在三层：PAA（`Test PAA`）+ PAI（`Test PAI`）+ DAC 模板（`Test DAC`）；均为 Matter 规范、状态 Active；列表有 Demo 标识、无环境标签<br>[2] PAA/PAI/DAC 有效期均为 2 Years；算法 ECC-P256；签名算法 ecdsa-with-SHA256；PAA 类型为 Test PAA（非认证 PAA）；DAC 的 PID 为 8001<br>[3] Tenant Admin 对 Demo PAA/PAI/DAC 拥有所有权限；Demo PAA 不可当作 SNOWBALL 官方认证 PAA 用于生产（能力/标识可区分） | 来源 AC-02: Vault 预设应创建 1 个 KMS 密钥（AES128、TEST 环境）+ 三层 PKI 证书链（PAA/PAI/DAC，Matter 规范，有效期 2 年）。 |
| 【Product-Product-List】【E2E】Product Demo - Demo-Product 与 Approved Version | /Cloud/Product/Product List | 三路Demo预设 | P0 | 1. PM Demo 预设已成功<br>2. 可进入产品列表与详情 | [1] 产品列表定位 `Demo-Product`，核对 Specification、状态、环境<br>[2] 进入产品详情，确认默认进入 Test 环境且可切换环境；核对默认 Module 与 Version<br>[3] 确认创建产品流程/表单无 Description 字段或填写入口 | [1] 存在 1 个产品 `Demo-Product`：Specification=Matter，状态 Released，环境 Testing；列表有 Demo 标识、无环境标签<br>[2] 从列表进入详情默认进入 Test 环境，且可切换环境；含默认 Module（Module1）与 Version（`Demo-Version-v1.0`），Version 状态为 **Approved**<br>[3] 无 Description 字段/填写入口 | 来源 AC-03: Product 预设应创建 1 个 Demo Product（Testing 环境、Matter 规范），含固件 / Chip Config（Silicon Labs EFR32MG24）/ Key 引用 / 证书引用 / Matter Config，以及默认 Module 与 Version（Version 默认 Approved，以评论为准）。 |
| 【Product-Product-List】【E2E】Product Demo - 资源包与 Matter Config 规格 | /Cloud/Product/Product List | 三路Demo预设 | P0 | 1. Demo-Product 预设已成功<br>2. 可查看固件、Chip Config、Key/证书引用、Matter Config、生产限额等 | [1] 在 Demo-Product 中核对固件、Chip Config、Key 引用、证书引用、Matter Config、PS Software<br>[2] 核对 Max Production Volume、Allowed Range、Default Duration、Vendor<br>[3] 核对 Matter Config 字段，并确认固件为真实可烧录文件 | [1] 固件 `Demo-Firmware-v1.0`（Type: Application）；Chip Config `Demo-Chip-Config-v1`（Silicon Labs / EFR32MG24 / EFR32MG24B210F1536IM48）；Key 引用 Demo KMS；证书引用 Demo DAC；含 Matter Config、PS Software<br>[2] Max Production Volume=Limited 500；Allowed Range Min=1、Max=30；Default Duration=30；Vendor=SNB<br>[3] Matter Config：PID=8001，DAC Template=Demo DAC，Spike2Iteration=1000，Commissioning Flow=Standard，设备发现模式=BLE；固件为真实可烧录文件（非占位空文件） | 来源 AC-03: Product 预设应创建 1 个 Demo Product（Testing 环境、Matter 规范），含固件 / Chip Config（Silicon Labs EFR32MG24）/ Key 引用 / 证书引用 / Matter Config，以及默认 Module 与 Version（Version 默认 Approved，以评论为准）。 |
| 【Product-Product-List】【UI】Demo 标签与配额 - 列表有标签详情无标签且不计用量 | /Cloud/Product/Product List | 三路Demo预设 | P0 | 1. Factory / KMS / PKI / Product Demo 均已存在<br>2. 可对照用量/配额展示（如 005-01 版本对比或配额入口） | [1] 分别打开 Factory、KMS、PKI、Product **列表**，观察 Demo 资源标签与环境标签<br>[2] 分别打开对应 **详情页**，观察是否展示 Demo 标签<br>[3] 对照配额/用量统计，确认 Demo 是否计入 | [1] 列表页展示 `Demo Data` / `测试数据` 或 `Demo-` 标识；**不**展示环境标签（Test / 正式等）<br>[2] 详情页**不**展示 `Demo Data` / `测试数据` 标签<br>[3] Demo 资源不计入配额和用量统计 | 来源 AC-04: Demo 资源在列表展示 Demo 标签，不展示环境标签，且不计入配额和用量统计。 |
| 【Ecosystem-Factory-Factory-List】【Functional】失败回滚 - Factory 成功 Station 失败 | /Cloud/Ecosystem/Factory/Factory List | 三路Demo预设 | P0 | 1. 可注入「Cloud Factory 创建成功、Programming Station 创建失败」（注入方式待确认）<br>2. 可观察该路失败结果与是否残留 Factory | [1] 触发含上述注入的预设（或单路重试场景）<br>[2] 检查是否仍存在刚创建的 Factory，以及该路结果记录 | [1] Station 创建失败<br>[2] 回滚已创建的 Factory；该路记为失败；不残留成功 Factory | 来源 AC-05: 创建失败时按规则回滚已创建的资源。 |
| 【KMS-Key-List】【Functional】失败回滚 - KMS/PKI/Product 链路 | /Cloud/KMS/Key List | 三路Demo预设 | P1 | 1. 可分别注入：KMS 成功但 PKI 失败；PKI 链中途失败；Product 成功但资源包失败，或资源包成功但 Version 失败<br>2. 可观察回滚与失败记录；与 002-01 重试对齐时可一并观察 3 次仍失败 | [1] KMS 成功、PKI 失败：检查 Key 是否被回滚及该路结果<br>[2] PKI 中途失败：检查已创建 CA 是否回滚<br>[3] Product 成功但资源包失败，或资源包成功但 Version 失败：检查 Product（及资源包）是否回滚；可选验证单路重试 3 次均失败后记录该路失败 | [1] 回滚已创建的 KMS 密钥，该路记为失败<br>[2] 回滚已创建的 CA 证书，该路记为失败<br>[3] 回滚已创建的 Product（及资源包），该路记为失败；重试 3 次均失败后记录该路失败结果（与 002-01 编排对齐） | 来源 AC-05: 创建失败时按规则回滚已创建的资源。 |
| 【Product-Product-List】【E2E】编辑与删除 - Demo 产品非核心字段及删除不重建 | /Cloud/Product/Product List | 三路Demo预设 | P0 | 1. Demo-Product 已存在；已知可编辑的非核心字段范围（清单待产品确认）<br>2. 可准备对照：同权限下用户自创建资源的编辑/删除行为 | [1] 编辑 Demo 产品某一非核心字段并保存，再打开详情核对<br>[2] 删除 Demo 产品内单个资源（如某一固件/配置），等待观察是否重建<br>[3] 删除整个 Demo 产品，等待观察是否重建；对比自创建资源的编辑/删除在权限、校验、列表刷新上是否一致 | [1] 保存成功；详情展示更新后内容<br>[2] 单个资源删除成功；系统不重建<br>[3] 整个 Demo 产品删除成功；系统不重建；编辑/删除效果与用户自创建资源一致（权限、校验、列表刷新等） | 来源 AC-06: 用户可删除 Demo 资源，删除后系统不重建。<br>来源 AC-07: 用户可编辑 Demo 产品的非核心字段。<br>来源 AC-10: Demo 数据编辑/删除后的效果与用户自创建资源一致。 |
| 【KMS-Key-List】【E2E】真实使用 - Demo Key 可完成签发类操作 | /Cloud/KMS/Key List | 三路Demo预设 | P0 | 1. Demo `TestKey` 与相关 Demo 证书/产品可用<br>2. 账号具备签发类操作权限 | [1] 使用预设 Demo KMS 密钥发起真实签发类操作（按现网签发路径）<br>[2] 确认操作结果与是否因 Demo 被额外限制 | [1] 可完成签发流程<br>[2] 功能不做额外限制，效果与使用普通可用密钥一致（业务成功为准） | 来源 AC-09: Demo 数据可被真实使用（如用预设密钥签发证书、用预设工厂创建批次），功能不做限制。 |
| 【Ecosystem-Factory-Batch】【E2E】真实使用 - Demo Factory/Station 可创建批次 | /Cloud/Ecosystem/Factory/Batch | 三路Demo预设 | P1 | 1. `TestCloudFactory` / `TestStation` 已 Active<br>2. 具备创建批次权限与必要产品数据 | [1] 使用预设 Demo Factory / Station 按现网流程创建批次<br>[2] 确认批次创建结果 | [1] 可进入并完成创建批次流程<br>[2] 批次创建成功；不因 Demo 身份被额外功能限制 | 来源 AC-09: Demo 数据可被真实使用（如用预设密钥签发证书、用预设工厂创建批次），功能不做限制。 |
| 【Login-Profile-Registration】【E2E】租户隔离 - A 不可见 B 的 Demo 数据 | /Cloud/Login & Profile/Registration | 三路Demo预设 | P0 | 1. 两个自注册 Tenant A、B 均已完成 Demo 预设<br>2. 可分别登录 A、B 查看 Factory / Key / PKI / Product | [1] 以租户 A 登录，记录本租户 Demo 资源标识<br>[2] 切换/登录租户 B，检查是否可见租户 A 的 Demo Factory、Key、PKI、Product<br>[3] 核对 A、B 的 Demo PAA/PAI/DAC 与密钥是否为各自独立实例 | [1] A 仅见本租户 Demo<br>[2] B **不能**看到 A 的 Demo Factory / Key / PKI / Product<br>[3] 两租户各自拥有独立的 Demo PAA/PAI/DAC 与密钥，互不共享同一证书链 | 来源 AC-08: Demo 数据按租户独立创建，各租户互不共享。 |
| 【Product-Product-List】【Functional】非核心字段 - 可编辑范围与产品确认一致 | /Cloud/Product/Product List | 三路Demo预设 | P2 | 1. 产品已确认「非核心字段」清单（Description 已去掉后的范围）<br>2. Demo-Product 可编辑 | [1] 按清单逐项尝试编辑允许字段并保存<br>[2] 尝试编辑清单外/核心字段 | [1] 允许字段可保存成功<br>[2] 核心/禁止字段不可改或保存失败，与产品约定一致 | 来源 QA扩展: 「非核心字段」可编辑范围清单与产品确认一致 |
| 【Product-Product-List】【UI】产品详情 - 默认 Test 环境可切换 | /Cloud/Product/Product List | 三路Demo预设 | P1 | 1. Demo-Product 存在 Testing 环境配置 | [1] 从产品列表进入 `Demo-Product` 详情<br>[2] 切换到其他可用环境（若有）再切回 | [1] 默认进入 Test 环境<br>[2] 可切换环境且切换后页面数据与所选环境一致 | 来源 需求描述: 用户从列表进入产品详情默认进入 Test 环境，且可切换环境 |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | Factory + Station | FM-01～04；TAG-01/02（Factory） |
| 2 | KMS TestKey | VAULT-KMS-01～03 |
| 3 | PKI 三层链 | VAULT-PKI-01～05 |
| 4 | Product + Approved Version | PM-PROD-01/02/05/08 |
| 5 | 资源包与 Matter Config | PM-PROD-03/04/06/07 |
| 6 | 标签与配额 | TAG-01～04 |
| 7 | Factory/Station 回滚 | ROLL-01 |
| 8 | KMS/PKI/Product 回滚 | ROLL-02～05 |
| 9 | 编辑删除 | ACT-01～04 |
| 10 | Demo Key 真实签发 | ACT-05 |
| 11 | Demo Factory 建批次 | ACT-06 |
| 12 | 租户隔离 | ISO-01/02 |
| 13 | 非核心字段清单 | ACT-07 |
| 14 | 详情默认 Test 环境 | PM-PROD-05（复验） |

**37 条 TP 均已至少被 1 条用例覆盖。**（TAG 在 Factory/Product 用例中亦有交叉断言；用例 14 强化 PM-PROD-05。）

## 待确认

- [ ] AC-03「Draft」与评论「Approved」正式文案是否已统一（用例按 **Approved**）
- [ ] 非核心字段可编辑清单
- [ ] 失败回滚的注入/模拟方式
- [ ] 配额交叉验证具体入口（005-01 对比弹窗或其他）
