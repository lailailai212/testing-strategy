# 【自注册】005-01 — 版本展示与用量可视化 功能测试用例

> 来源：`acceptance.md（同 feature 包）`（含 TP-ID）；脑图：`xmind/（同 feature 包）`  
> 需求：【自注册】005-01 — 版本展示与用量可视化（[Story #7007364069](https://project.feishu.cn/obis/userstory/detail/7007364069)）  
> 用例数：13（P0 × 7，P1 × 4，P2 × 2；E2E × 7，UI × 4，Functional × 2）；覆盖 TP 36 条  
> 入口规则：免费版 → Welcome 欢迎卡片 `Upgrade Plan` / `升级套餐`，或 Profile 租户旁套餐标签；企业版 Welcome 不展示入口，Profile 标签不可点；**切回免费版在超管页面操作**。  
> 产品规则：对比弹窗含 7 维；免费版列实时用量且 Demo 不计入（用量按 **Tenant 聚合**，与操作者无关）；**企业版期间新增资源不计入免费版用量；切回后用量恢复为升级企业版之前**；企业版列绿色 ✓ + `Per contract` / `按合同`；底部「升级到企业版」打开联系销售弹窗（弹窗细节属 FT-S-004-05，本 Story 只验打开）。
> 设计原则：一条用例覆盖一个用户场景，场景内可校验多个测试点；步骤 ≤ 10；标签仅填可读业务名  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：Welcome → `/Cloud/Welcome`；Profile → `/Cloud/Login & Profile/My Profile`  
> 备注列：来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Cloud-Welcome】【E2E】免费版欢迎卡片 - 打开对比弹窗并完成升级主路径 | /Cloud/Welcome | 版本展示与用量可视化 | P0 | 1. 使用**免费版**自注册 Tenant 账号登录<br>2. 系统语言已知（中或英均可，本条以当前语言文案对照）<br>3. 可识别联系销售弹窗（本条仅验打开） | [1] 进入 Welcome，查看欢迎卡片套餐名称与升级入口<br>[2] 点击 `Upgrade Plan` / `升级套餐`，打开版本对比弹窗<br>[3] 核对顶部横幅标题、对比区小标题与三列表头，以及对比表 7 项维度齐全<br>[4] 核对免费版列限额口径，以及企业版列各维度绿色 ✓ + `Per contract` / `按合同`；并观察免费版列用量非固定死值<br>[5] 核对底部区域标题与按钮，点击 `Upgrade to Enterprise` / `升级到企业版` | [1] 展示 `Free Tier` / `免费版`；可见 `Upgrade Plan` / `升级套餐`<br>[2] 打开版本对比弹窗<br>[3] 横幅标题为 `OBIS Free Tier` / `OBIS 免费版`；小标题 `Free Tier vs Enterprise` / `免费版 VS 企业版`；表头为 Feature/功能项、Free Tier (Current)/免费版（当前）、Enterprise/企业版；含且仅含 7 维：Products、Max Volume、KMS Keys、KMS Validity、PKI Templates、PKI Validity、Factory Type<br>[4] 免费版限额符合规格（Products 10、Max Volume ≤500、KMS Keys 5、KMS Validity ≤2 years/2 年、PKI Templates 6、PKI Validity ≤2 years/2 年、Factory Type Cloud only/仅云工厂）；企业版各维绿色 ✓ + 按合同；免费版列展示实时用量（格式待确认，可为已用/限额）<br>[5] 底部标题 `From evaluation to mass production` / `从评估走向量产`；按钮带右侧箭头；点击后打开联系销售弹窗 | 来源 AC-01: 免费版用户进入 Welcome 页面时，欢迎卡片应展示套餐名称/Package Name，并提供升级入口（`Upgrade Plan` / `升级套餐`）。<br>来源 AC-03: 打开版本对比弹窗后，对比表应包含 7 项对比维度：产品数量、单产品最大生产量、KMS 密钥数量、KMS 密钥有效期、PKI 证书模板、PKI 证书有效期、工厂类型。<br>来源 AC-04: 版本对比弹窗免费版列应展示实时用量值，且 Demo 资源不计入限额统计。<br>来源 AC-05: 版本对比弹窗企业版列各维度应展示绿色 ✓ 图标 + 「按合同」/ `Per contract`。<br>来源 AC-06: 版本对比弹窗底部应展示「升级到企业版」/ `Upgrade to Enterprise` 按钮。<br>来源 AC-07: 用户点击「升级到企业版」按钮后，应打开联系销售弹窗。 |
| 【Login-Profile-My-Profile】【E2E】免费版 Profile - 套餐标签可点打开对比弹窗 | /Cloud/Login & Profile/My Profile | 版本展示与用量可视化 | P0 | 1. 免费版账号已登录<br>2. 可进入 Profile / My Profile | [1] 进入 Profile，查看所属租户名称旁套餐标签<br>[2] 点击免费版套餐标签<br>[3] 确认打开版本对比弹窗（可与 Welcome 入口弹窗结构一致） | [1] 展示 `Free Tier` / `免费版`<br>[2] 标签可点击<br>[3] 打开版本对比弹窗 | 来源 AC-02: 免费版用户进入 Profile 页面时，所属租户名称旁应展示套餐名称/Package Name，且免费版标签可点击进入版本对比详情；企业版标签不可点击。 |
| 【Cloud-Welcome】【UI】企业版 Welcome - 不展示套餐名称与升级入口 | /Cloud/Welcome | 版本展示与用量可视化 | P1 | 1. 使用**企业版**账号登录<br>2. 可进入 Welcome | [1] 进入 Welcome，查看欢迎卡片是否展示套餐名称与 `Upgrade Plan` / `升级套餐` | [1] **不展示**套餐名称/Package Name，也**不展示**升级入口 | 来源 需求描述: 企业版用户 Welcome 欢迎卡片不展示套餐名称与升级入口 |
| 【Login-Profile-My-Profile】【UI】企业版 Profile - 展示标签但不可点击 | /Cloud/Login & Profile/My Profile | 版本展示与用量可视化 | P1 | 1. 企业版账号已登录<br>2. 可进入 Profile | [1] 进入 Profile，查看租户旁套餐标签文案<br>[2] 尝试点击企业版套餐标签 | [1] 展示企业版套餐名称/Package Name（企业版文案）<br>[2] 标签不可点击；无响应且**不**打开版本对比弹窗 | 来源 AC-02: 免费版用户进入 Profile 页面时，所属租户名称旁应展示套餐名称/Package Name，且免费版标签可点击进入版本对比详情；企业版标签不可点击。 |
| 【Cloud-Welcome】【Functional】实时用量 - Demo 不计入且仅统计真实资源 | /Cloud/Welcome | 版本展示与用量可视化 | P0 | 1. 免费版账号；可准备仅含 Demo 资源的 Tenant，以及同时含 Demo + 真实产品/密钥/模板的 Tenant（或同一 Tenant 分阶段造数）<br>2. Demo 判定对齐 002-02（`demo` 标签等） | [1] 在仅存在 Demo 产品/密钥/模板时，从 Welcome 打开对比弹窗，记录 Products / KMS Keys / PKI Templates 用量<br>[2] 增加真实（非 Demo）资源后重新打开对比弹窗，记录对应用量<br>[3] 确认 Demo 资源数量未计入已用量 | [1] 对应维度用量为 0（或不占用已用量）<br>[2] 用量随真实资源数量变化，展示实时值<br>[3] 同时存在 Demo 与真实资源时，用量**仅**统计真实资源 | 来源 AC-04: 版本对比弹窗免费版列应展示实时用量值，且 Demo 资源不计入限额统计。 |
| 【Cloud-Welcome】【E2E】实时用量 - 真实产品密钥模板增删同步 | /Cloud/Welcome | 版本展示与用量可视化 | P1 | 1. 免费版账号，用量未触顶，便于增删<br>2. 可创建/删除真实（非 Demo）产品、KMS 密钥、PKI 证书模板<br>3. 每次变更后可重新打开对比弹窗观察 | [1] 打开对比弹窗，记录 Products / KMS Keys / PKI Templates 当前用量<br>[2] 创建 1 个真实产品后重新打开对比，再删除该产品后再次打开<br>[3] 创建 1 个真实 KMS 密钥后打开对比，再删除后打开<br>[4] 创建 1 个真实 PKI 证书模板后打开对比，再删除后打开 | [1] 取得基线用量<br>[2] 创建后 Products 用量 +1；删除后回到基线<br>[3] 创建后 KMS Keys +1；删除后回落<br>[4] 创建后 PKI Templates +1；删除后回落 | 来源 AC-04: 版本对比弹窗免费版列应展示实时用量值，且 Demo 资源不计入限额统计。 |
| 【Cloud-Welcome】【E2E】双入口 - 用量一致且均可打开联系销售 | /Cloud/Welcome | 版本展示与用量可视化 | P1 | 1. 免费版账号，已有可观测的真实用量（非全 0 更易对比）<br>2. 可分别从 Welcome 与 Profile 打开对比弹窗 | [1] 从 Welcome 打开对比弹窗，记录各维度用量，点击「升级到企业版」后关闭联系销售弹窗与对比弹窗<br>[2] 从 Profile 点击套餐标签打开对比弹窗，核对用量是否与步骤 [1] 一致<br>[3] 在 Profile 入口打开的对比弹窗中点击「升级到企业版」 | [1] 打开联系销售弹窗成功<br>[2] Welcome / Profile 两入口展示**同一套**用量结果<br>[3] 同样可打开联系销售弹窗 | 来源 AC-04: 版本对比弹窗免费版列应展示实时用量值，且 Demo 资源不计入限额统计。<br>来源 AC-07: 用户点击「升级到企业版」按钮后，应打开联系销售弹窗。 |
| 【Cloud-Welcome】【Functional】用量近限额 - 对比弹窗仍可正常打开 | /Cloud/Welcome | 版本展示与用量可视化 | P2 | 1. 免费版账号，至少某一可计数维度已达或接近限额（如 Products 接近 10）<br>2. 不验证配额拦截本身（Out of Scope） | [1] 确认当前用量已达或接近限额<br>[2] 从 Welcome 打开版本对比弹窗，查看该维度用量展示 | [1] 前置用量条件成立<br>[2] 弹窗可正常打开并正确展示当前用量；不因触达限额而无法打开对比 | 来源 QA扩展: 用量达到或接近限额时，对比弹窗仍可正常打开并正确展示当前用量 |
| 【Cloud-Welcome】【UI】英文环境 - Welcome/Profile 与对比弹窗文案 | /Cloud/Welcome | 版本展示与用量可视化 | P2 | 1. 免费版账号；系统语言为 **English**<br>2. 可进入 Welcome 与 Profile | [1] Welcome 查看套餐标签与 Upgrade Plan；Profile 查看套餐标签<br>[2] 打开对比弹窗，核对横幅描述、底部描述及全文是否为英文规格 | [1] 标签与入口为英文（`Free Tier`、`Upgrade Plan` 等）<br>[2] 横幅描述为 `Full PKI + KMS capabilities with quota limits. No time limit, permanently free.`；底部描述为 `Upgrade to Enterprise with zero migration — all data retained.`；对比弹窗全文英文，无中英混杂或 i18n key 裸露 | 来源 需求描述: 英文环境下横幅/底部描述与 Welcome/Profile/对比弹窗英文规格文案 |
| 【Cloud-Welcome】【UI】中文环境 - Welcome/Profile 与对比弹窗文案 | /Cloud/Welcome | 版本展示与用量可视化 | P2 | 1. 免费版账号；系统语言为 **中文**<br>2. 可进入 Welcome 与 Profile | [1] Welcome / Profile 查看套餐与升级相关中文文案<br>[2] 打开对比弹窗，核对横幅描述、底部描述；并观察企业版工厂类型展示口径 | [1] 展示 `免费版`、`升级套餐` 等中文文案<br>[2] 横幅描述为 `完整 PKI + KMS 安全能力，配额受限但功能完整。无时间限制，永久免费。`；底部描述为 `升级企业版数据全保留、零迁移。`；全文中文；企业版工厂类型按统一规则为绿色 ✓ + 按合同（若仍单独展示 `云 + 本地工厂` 以产品最终稿为准，待确认） | 来源 需求描述: 中文环境下横幅/底部描述与对比弹窗中文规格文案 |
| 【Cloud-Welcome】【UI】切换语言后 - 对比弹窗文案跟随当前语言 | /Cloud/Welcome | 版本展示与用量可视化 | P2 | 1. 免费版账号<br>2. 可在中/英之间切换系统语言 | [1] 在语言 A 下打开对比弹窗，记录文案语言后关闭<br>[2] 切换到语言 B，重新打开对比弹窗<br>[3] 核对文案是否全部切换为语言 B | [1] 文案与语言 A 一致<br>[2] 弹窗可重新打开<br>[3] 文案随当前语言切换，无中英混杂或 i18n key 裸露 | 来源 QA扩展: 切换语言后重新打开对比弹窗，文案随当前语言切换 |
| 【Cloud-Welcome】【E2E】实时用量 - 非创建者造数后创建者对比弹窗用量同步+1 | /Cloud/Welcome | 版本展示与用量可视化 | P0 | 1. 免费版自注册 Tenant；当前用户为 **Tenant 创建者（Admin）**，用量未触顶<br>2. 同 Tenant 下已邀请至少 1 名 **Manager 或 Member**，具备创建真实（非 Demo）产品、KMS 密钥、PKI 证书模板的权限<br>3. 创建者与成员均可登录；可从 Welcome 打开版本对比弹窗 | [1] 以 **Tenant 创建者**登录，从 Welcome 打开版本对比弹窗，记录 Products / KMS Keys / PKI Templates 当前已用量后关闭弹窗<br>[2] 退出并以 **非创建者**成员登录，分别创建 1 个真实产品、1 个真实 KMS 密钥、1 个真实 PKI 证书模板（均非 Demo）<br>[3] 退出并以 **Tenant 创建者**重新登录，从 Welcome 再次打开版本对比弹窗，核对上述三维已用量<br>[4] （可选）从 Profile 套餐标签再次打开对比弹窗，核对用量与步骤 [3] 一致 | [1] 取得创建者视角基线用量<br>[2] 非创建者创建三类真实资源均成功<br>[3] 创建者看到的 Products / KMS Keys / PKI Templates 已用量相对基线各 **+1**（用量按 Tenant 聚合，不因操作者非创建者而不计或延迟丢失）<br>[4] Profile 入口展示与 Welcome **同一套**用量 | 来源 AC-04: 版本对比弹窗免费版列应展示实时用量值，且 Demo 资源不计入限额统计。<br>来源 QA扩展: 用量按 Tenant 聚合；非创建者造数后创建者打开对比弹窗用量同步 +1 |
| 【Cloud-Welcome】【E2E】企业版切回免费版 - 入口恢复且用量恢复为升级前基线 | /Cloud/Welcome | 版本展示与用量可视化 | P0 | 1. 自注册免费版 Tenant；升级前已有可观测真实用量（Products / KMS Keys / PKI Templates 基线已知，且含企业版期间将新增的对照空间）<br>2. 可升级为企业版；企业版期间可再创建额外真实产品/密钥/模板<br>3. 超管可在**超管页面**将该 Tenant **切回免费版**；切回后可打开版本对比弹窗 | [1] 升级前打开对比弹窗，记录 Products / KMS Keys / PKI Templates **升级前已用量**（基线）<br>[2] 升级为企业版；在企业版期间再创建若干真实（非 Demo）产品/密钥/模板（数量记为 Δ）<br>[3] 在**超管页面**将该 Tenant 切回免费版，确认当前为免费版<br>[4] 进入 Welcome / Profile，确认入口恢复；打开对比弹窗，核对免费版限额口径，并核对三维**已用量** | [1] 取得升级前基线<br>[2] 企业版期间资源创建成功（Δ > 0）<br>[3] 超管切回免费版成功<br>[4] Welcome 恢复 `Free Tier` / `免费版` + 升级入口；Profile 免费版标签可点；限额口径符合免费版规格；已用量**等于升级前基线**（企业版期间新增 Δ **不计入**）；Demo 不计入；企业版列仍为绿色 ✓ + 按合同 | 来源 AC-01 / AC-02 / AC-04<br>来源 QA扩展: 切回路径在超管页面；企业版期间资源不计入免费版用量；回退后用量恢复为升级企业版之前的用量（2026-07-16 确认） |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | 免费版 Welcome 打开对比并升级主路径 | WEL-PLAN-01/02/03；BAN-01；TBL-01/02/03/04/05；CTA-01/04/05；USAGE-01 |
| 2 | 免费版 Profile 标签打开对比 | PROF-PLAN-01/02 |
| 3 | 企业版 Welcome 不展示 | WEL-PLAN-04 |
| 4 | 企业版 Profile 不可点 | PROF-PLAN-03/04 |
| 5 | Demo 排除与真实用量 | USAGE-01/05/06 |
| 6 | 产品/密钥/模板增删同步 | USAGE-02/03/04 |
| 7 | 双入口用量一致 + 均可联系销售 | USAGE-07；CTA-06 |
| 8 | 近限额仍可打开对比 | USAGE-08 |
| 9 | 英文文案 | BAN-02；CTA-02；I18N-01 |
| 10 | 中文文案（含企业版工厂口径） | BAN-03；CTA-03；TBL-06；I18N-02 |
| 11 | 切换语言 | I18N-03 |
| 12 | 非创建者造数，创建者看用量 +1 | USAGE-09；USAGE-07（可选复验） |
| 13 | 企业版切回免费版：入口恢复 + 用量=升级前基线 | USAGE-10；WEL-PLAN-01/02；PROF-PLAN-01/02；TBL-04 |

**36 条 TP 均已至少被 1 条用例覆盖。**

## 待确认

- [ ] 免费版列「实时用量」精确展示格式（已用/限额等）
- [ ] 企业版工厂类型是否仍单独展示 `Cloud + On-prem`，或完全被「按合同」替代
- [ ] Max Volume / Validity 等维度是否有可观测「已用」值，或仅展示限额文案
- [ ] `/Cloud/Welcome` 在 MeterSphere 模块树中的最终挂载名（现网用例沿用该路径）
- [ ] 免费版下 Manager / Member 是否具备创建真实产品 / 密钥 / 证书模板权限（本条前置）
- [x] 企业版切回免费版：路径在超管页面；企业版期间资源不计入；回退后用量=升级前基线（2026-07-16 确认）
