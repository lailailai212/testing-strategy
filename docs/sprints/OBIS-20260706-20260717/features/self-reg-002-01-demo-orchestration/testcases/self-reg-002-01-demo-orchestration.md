# 【自注册】002-01 — Demo 数据预设编排 功能测试用例

> 来源：`acceptance.md（同 feature 包）`（含 TP-ID）；脑图：`xmind/（同 feature 包）`  
> 需求：【自注册】002-01 — Demo 数据预设编排（[Story #7007110712](https://project.feishu.cn/obis/userstory/detail/7007110712)）  
> 用例数：12（P0 × 8，P1 × 3，P2 × 1；E2E × 6，Functional × 6）；覆盖 TP 24 条（其中 DEMO-02/03 删除主测归 002-02，本文件仅交叉引用）  
> 入口规则：自注册完成 Account + Tenant 创建 → 异步触发 Demo 预设；资源验收分别进入 Factory / KMS·PKI / Product 列表。  
> 产品规则：仅自注册 Tenant 触发且生命周期一次；用户无感知；Demo 列表标签 `Demo Data` / `测试数据`。依赖（评论 2026-07-14）：KMS/PKI/工厂互相独立；PKI 根→中间→叶子、工厂→烧录站串行；产品 Version 依赖 KMS+PKI。失败重试 3 次、间隔 30 秒，不阻塞用户。  
> **与 002-02 分工**：删除/不重建的操作与断言主测在 `self-reg-002-02-three-path-demo`；本文件仅保留「Demo 已清空后不因空态再次触发预设」。  
> 文案规则：标签等关键文案写全中英文，禁止用省略号概括需求原文。  
> 设计原则：一条用例一个场景；步骤 ≤ 10；标签仅可读业务名  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：编排触发统一挂 `/Cloud/Login & Profile/Registration`  
> 备注列：来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Login-Profile-Registration】【E2E】自注册成功 - 异步预设且全量 Demo 资源可见 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 准备未注册邮箱，可完成自注册创建 Tenant<br>2. 具备查看后台预设任务/日志的能力（可观测面待确认）<br>3. 可进入 Factory、KMS/证书、Product 列表 | [1] 完成自注册直至 Tenant 创建成功，观察进入系统过程是否出现预设阻塞 UI<br>[2] 在后台确认 Demo 预设任务已异步创建/开始执行（用户侧无同步等待）<br>[3] 等待预设成功后，分别进入 Factory、KMS、证书、Product 列表，核对资源数量与 Demo 标签 | [1] 可进入系统；无 Demo 预设进度条、无强制等待页、无「正在创建 Demo」类阻塞提示<br>[2] 后台可观测到预设任务；用户侧无同步等待创建完成<br>[3] 资源齐全：1 个 Cloud Factory + 1 个 Programming Station；1 个 KMS Key；PKI 根/中间/叶子（PAA/PAI/DAC）三层；1 个 Product + 资源包 + Version。上述资源在对应**列表页**展示标签 `Demo Data` / `测试数据` | 来源 AC-01: 自注册 Tenant 创建成功后异步触发 Demo 预设任务<br>来源 AC-04: 用户对预设过程完全无感知<br>来源 AC-05: Demo 资源展示「Demo Data」标签，用户可删除且系统不重建 |
| 【Login-Profile-Registration】【E2E】生命周期 - 同一 Tenant 仅触发一次预设 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 自注册 Tenant 已完成首次 Demo 预设（或已有任务成功记录）<br>2. 可统计 Demo 资源数量及预设任务触发次数 | [1] 记录当前 Demo 资源数量与预设任务次数<br>[2] 使用同一 Tenant 重复登录、再次进入 Portal<br>[3] 再次核对 Demo 资源数量与是否新增预设任务 | [1] 取得基线<br>[2] 登录与进入 Portal 成功<br>[3] 不重复触发 KMS / PKI / FM / PM 预设；Demo 资源数量不因重复进入而新增一套 | 来源 AC-07: 同一 Tenant 生命周期内仅触发一次 |
| 【Login-Profile-Registration】【Functional】运营开通 Tenant - 不触发 Demo 预设 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 可通过运营后台开通新 Tenant（非自注册）<br>2. 该 Tenant 可登录并查看 Factory / KMS·PKI / Product 列表 | [1] 完成运营后台开通 Tenant<br>[2] 登录该 Tenant，检查是否存在 Demo Factory、Demo Key/PKI、Demo Product，并检查是否有预设任务 | [1] Tenant 开通成功<br>[2] **不触发** Demo 预设；不出现上述 Demo 资源；无对应预设任务 | 来源 AC-06: 运营后台开通的 Tenant 不触发预设 |
| 【Login-Profile-Registration】【Functional】其他创建路径 - 不触发 Demo 预设 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P1 | 1. 环境存在除自注册、运营开通外的其他 Tenant 创建路径（若无则本条标 N/A）<br>2. 可观察是否触发预设 | [1] 通过该其他路径创建 Tenant<br>[2] 检查预设任务与 Demo 资源 | [1] Tenant 创建成功<br>[2] 不触发 Demo 预设，无 Demo 资源 | 来源 QA扩展: 除自注册创建 Tenant 外的其他路径均不触发 Demo 预设 |
| 【Login-Profile-Registration】【Functional】失败重试 - 各路最多 3 次间隔 30 秒且不阻塞 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 可分别注入 FM、KMS、PKI、PM 预设失败或超时（注入方式待确认）<br>2. 可观察重试日志/任务记录与时间间隔<br>3. 准备走自注册触发预设 | [1] 注入 FM（Factory/Station）失败，触发自注册预设，观察重试次数与间隔<br>[2] 对 KMS Key 路重复注入失败并观察重试<br>[3] 对 PKI 路重复注入失败并观察重试<br>[4] 对 PM（Product/资源包/Version）路重复注入失败并观察重试<br>[5] 在任一路持续失败场景下完成注册并尝试进入系统 | [1] FM 路自动重试，最多 3 次，间隔约 30 秒<br>[2] KMS 路同样最多 3 次、间隔约 30 秒<br>[3] PKI 路同样最多 3 次、间隔约 30 秒<br>[4] PM 路同样最多 3 次、间隔约 30 秒<br>[5] 用户仍可进入系统并正常使用；注册/登录不被阻断 | 来源 AC-03: 每路失败自动重试 3 次（间隔 30 秒），全部失败不阻塞用户 |
| 【Login-Profile-Registration】【Functional】全部重试仍失败 - 记录部分失败并通知运营 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P1 | 1. 可模拟多路或全部预设持续失败直至重试耗尽<br>2. 可查看预设结果记录；运营通知渠道待确认 | [1] 使相关预设持续失败直至各路重试结束<br>[2] 检查预设结果记录与运营侧是否收到通知<br>[3] 确认用户侧仍可使用系统 | [1] 重试按策略结束<br>[2] 记录为部分失败（或失败）；通知运营人员（渠道/内容待确认）<br>[3] 不阻塞用户使用 | 来源 需求描述: 全部重试仍失败时记录预设结果为部分失败，通知运营人员，不阻塞用户 |
| 【Login-Profile-Registration】【Functional】PKI 链路串行 - 上一级失败下一级不开始 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 可注入 PKI 根证书创建失败，或中间证书创建失败<br>2. 可观察各级证书是否被创建 | [1] 注入根证书创建失败并触发预设，检查是否创建中间证书、叶子证书<br>[2] 在根成功、中间失败场景下触发预设，检查是否创建叶子证书 | [1] 根不成功时，不开始创建中间证书，也不创建叶子证书<br>[2] 中间不成功时，不开始创建叶子证书 | 来源 需求描述: PKI 根→中间→叶子，上一级不成功，下一级不开始（评论 2026-07-14） |
| 【Login-Profile-Registration】【Functional】工厂链路串行 - Factory 失败则 Station 不开始 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 可注入 Cloud Factory 创建失败<br>2. 可观察 Programming Station 是否被创建 | [1] 注入 Factory 创建失败并触发预设<br>[2] 检查 Programming Station 是否创建 | [1] Factory 创建失败<br>[2] **不开始**创建 Programming Station | 来源 需求描述: 工厂→烧录站，上一级不成功，下一级不开始（评论 2026-07-14） |
| 【Login-Profile-Registration】【E2E】跨模块独立与 Version 依赖 KMS+PKI | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P0 | 1. 可分别注入 KMS 失败、PKI 失败，并保证另两模块可成功<br>2. 可观察 Factory/Station、KMS、PKI、Product、Version 结果 | [1] 仅注入 KMS 失败，触发预设；检查 PKI、工厂是否仍可成功，以及 Version 是否开始<br>[2] 仅注入 PKI 失败，触发预设；检查 KMS、工厂是否仍可成功，以及 Version 是否开始<br>[3] 在 KMS 或 PKI 未成功时，核对 Product 与 Version 状态（Product 是否落库以实现为准） | [1] PKI、工厂仍可按自身规则成功；**Version 不开始**；工厂与 Station（Factory 成功时）不受 KMS 失败影响<br>[2] KMS、工厂仍可成功；**Version 不开始**；KMS 与工厂不受 PKI 失败影响<br>[3] KMS 或 PKI 未成功时 Version 不开始；KMS、PKI、工厂三者互相独立（其一失败不阻断另两个模块） | 来源 需求描述: KMS/PKI/工厂互相独立；产品版本依赖 KMS 与 PKI（评论 2026-07-14） |
| 【Login-Profile-Registration】【Functional】PM 失败 - 独立重试且不回滚已成功模块 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P1 | 1. 可使 KMS、PKI、工厂先成功，再注入 PM（Product/Version）失败<br>2. 可观察 PM 重试及已成功资源是否被回滚 | [1] 在 KMS/PKI/工厂已成功前提下注入 PM 失败并触发/继续预设<br>[2] 观察 PM 是否独立重试，以及已成功的 KMS、PKI、工厂资源是否仍存在 | [1] PM 侧按失败策略处理<br>[2] PM 独立重试；不回滚已成功的 KMS、PKI、工厂资源 | 来源 需求描述: 产品 Demo 预设失败独立重试，不影响已成功的 KMS/PKI/工厂数据 |
| 【Login-Profile-Registration】【E2E】预设进行中 - 用户可浏览 Portal 并最终看到资源 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P1 | 1. 可放慢或拉长预设执行时间，使进入系统时任务仍在跑<br>2. 自注册账号可登录 Portal | [1] 自注册成功后立即进入 Portal，在预设未完成时浏览各菜单/页面<br>[2] 等待预设完成后，检查 Factory / Vault / Product 列表是否出现 Demo 资源 | [1] 可正常浏览 Portal，无强制等待<br>[2] 预设完成后对应列表出现 Demo 资源 | 来源 AC-04: 用户对预设过程完全无感知 |
| 【Login-Profile-Registration】【Functional】Demo 已清空后 - 不因空态再次触发预设 | /Cloud/Login & Profile/Registration | Demo数据预设编排 | P2 | 1. 自注册 Tenant 曾成功预设<br>2. 本租户全部 Demo 资源**已删除**（删除操作与不重建断言见 002-02，本条不重复执行删除步骤）<br>3. 可观察是否再次触发预设任务 | [1] 确认当前无 Demo Factory / Key·PKI / Product（或数量为 0）<br>[2] 重复登录、再次进入 Portal<br>[3] 检查是否新增预设任务或重新拉起一套 Demo 资源 | [1] Demo 资源为空（删除结果已由 002-02 验收）<br>[2] 登录与进入成功<br>[3] **不**因「Demo 为空」再次触发 KMS/PKI/FM/PM 预设；不新增长生命周期外的第二套 Demo（与 AC-07 一致） | 来源 QA扩展: 删除全部 Demo 后不重建、不再次触发预设（本条只验「不再次触发」；删除/不重建见 002-02） |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | 自注册异步预设成功 + 无感知 + 全量资源与标签 | TRIG-01；FLOW-01；UX-01；DEMO-01 |
| 2 | 生命周期仅一次 | TRIG-02 |
| 3 | 运营开通不触发 | TRIG-03 |
| 4 | 其他创建路径不触发 | TRIG-04 |
| 5 | 各路失败重试且不阻塞 | FLOW-02～06 |
| 6 | 全部失败记录并通知 | FLOW-07 |
| 7 | PKI 串行 | DEP-01 |
| 8 | 工厂串行 | DEP-02 |
| 9 | 跨模块独立与 Version 依赖 | DEP-03～06 |
| 10 | PM 失败不回滚 | DEP-07 |
| 11 | 预设中可浏览 | UX-02 |
| 12 | Demo 已清空后不重触发 | DEMO-04 |
| — | 删除单个/不重建/其余保留 | DEMO-02/03 → **主测见 002-02** |

**24 条 TP：本文件直接覆盖 22 条；DEMO-02/03 由 002-02 删除用例覆盖，避免重复。**

## 待确认

- [ ] 预设任务可观测面（运营后台 / 日志）
- [ ] 失败注入与模拟超时的方式
- [ ] 「通知运营人员」渠道与内容
- [ ] KMS/PKI 失败时 Product 本体是否仍创建（Version 明确不开始）
- [ ] 其他 Tenant 创建路径是否存在（用例 4）
