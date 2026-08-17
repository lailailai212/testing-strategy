# 【自注册】006-01 — 免费版事务邮件触达 功能测试用例

> 来源：`acceptance.md（同 feature 包）`（含 TP-ID）；需求：`story/obis-7007422975-【自注册】006-01-免费版事务邮件触达/`  
> 需求：【自注册】006-01 — 免费版事务邮件触达（[Story #7007422975](https://project.feishu.cn/obis/userstory/detail/7007422975)）  
> 用例数：22（P0 × 18，P1 × 4；E2E × 15，Functional × 7）；覆盖 TP 51 条  
> 入口规则：Welcome → 自注册完成 Account + Tenant 创建；首次 DAC → 签发真实终端实体 DAC（非 Demo）；首次烧录 → 生成真实 Production Record；邮件校验 → Tenant 创建者邮箱（含垃圾箱）。  
> 产品规则：每类邮件按 Tenant 去重仅 1 次（以**首次业务成功**计，业务失败不占额度）；**收件人固定为 Tenant 创建者（注册者），与操作者是否为 Admin 无关**；Demo 预设 / 运营开通 / **邀请加入非自注册 Tenant** 不触发；**命中企业白名单仍发个人 Tenant Welcome**；**邀请加入不向被邀请人发 Welcome**；**升级企业后 DAC/烧录不发**；**超管页面切回免费版后首次烧录应发**；**自建产品混用 Demo 资产首次烧录仍发**；Matter 首次烧录可同时触发 DAC+烧录两封；邮件通道失败重试 3 次、间隔 5 分钟，不阻塞业务；**本迭代不做 Operator 告警**（评论 2026-07-14）。
> Demo 判定口径（对齐 [002-02 三路 Demo 预设](https://project.feishu.cn/obis/userstory/detail/7006975243)）：系统标签 `demo` / 列表 `Demo-` 或「Demo Data / 测试数据」；典型资源 TestKey、Test PAA/PAI/DAC、Demo-Product、TestCloudFactory；不计入配额。  
> 设计原则：**一条用例覆盖一个用户场景**，场景内可校验多个测试点；步骤清晰连贯；单用例步骤 ≤ 10；标签仅填可读业务名  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：自注册相关统一挂载 `/Cloud/Login & Profile/Registration`；映射见 `testcases/module-mapping.json`  
> 备注列：标明需求来源；来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Login-Profile-Registration】【E2E】Welcome 邮件 - 自注册成功后创建者收到且内容正确 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 准备未注册邮箱作为 Tenant 创建者，邮箱可收信；注册姓名已知<br>2. 可在同 Tenant 下添加至少 1 名其他成员<br>3. 可查看创建者及其他成员邮箱收件箱 | [1] 使用创建者邮箱完成自注册，直至 Account 创建完毕且 Tenant 创建成功<br>[2] 打开创建者收到的 Welcome 邮件，核对发件人、主题、HTML 样式、英中双语正文、三项引导、`{name}` 与 CTA 链接<br>[3] 检查同 Tenant 其他成员邮箱 | [1] Tenant 创建成功；业务流程不被邮件发送阻塞；创建者收到 **1** 封 Welcome<br>[2] 发件人名称 `Snowball OBIS`、地址 `noreply@snowballtech.com`；主题 `Welcome to OBIS! Let's Get Started`；HTML 含 OBIS Logo 与品牌色；英中双语；英文含 Complete first DAC signing / Try secure factory flash / Explore the docs 与 Get Started；中文含完成首次 DAC 签发 / 体验安全烧录 / 查阅操作文档与「立即开始」；`{name}` 为注册姓名；链接为可访问的 OBIS 登录相关链接<br>[3] 其他成员**未收到** Welcome 邮件 | 来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次<br>来源 AC-04: 邮件模板中英文双语，变量替换正确 |
| 【Login-Profile-Registration】【Functional】Welcome 去重 - 重复事件与运营操作不重发 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P1 | 1. 自注册 Tenant 已创建成功，创建者已收到 Welcome 邮件<br>2. 具备触发「Tenant 创建成功」类重复事件的能力，或可模拟等价重试（待确认具体入口）<br>3. 运营侧可对该 Tenant 执行非开通类常规操作（待确认可操作项） | [1] 记录创建者当前 Welcome 邮件数量<br>[2] 触发或模拟重复的 Tenant 创建成功事件，检查 Welcome 数量<br>[3] 运营侧对该自注册 Tenant 执行常规操作后，再次检查 Welcome 数量 | [1] 当前 Welcome 为 1 封<br>[2] **不**重复发送 Welcome<br>[3] Welcome 仍为 1 封，运营操作不导致再次发送 | 来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次 |
| 【Login-Profile-Registration】【E2E】首次 DAC 邮件 - 内容正确且二次签发成功不重发 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（仍为免费版/未升级企业），尚未发送过首次 DAC 邮件<br>2. 可签发**非 Demo** 真实终端实体 DAC；创建者邮箱可收信；同 Tenant 有其他成员<br>3. 记录创建者当前首次 DAC 类邮件数量（应为 0） | [1] 签发首条真实终端实体 DAC 证书<br>[2] 打开创建者收到的首次 DAC 邮件，核对发件人、主题、HTML 双语、`{name}`、证书变量（类型/签发时间 UTC/序列号）与查看证书链接；并确认其他成员未收到<br>[3] **二次成功**：再次签发一条真实 DAC<br>[4] 检查创建者邮箱是否新增首次 DAC 类邮件 | [1] 真实 DAC 签发成功；创建者收到 **1** 封首次 DAC 邮件<br>[2] 发件人 `Snowball OBIS` / `noreply@snowballtech.com`；主题 `Great Work! Your First DAC Certificate Has Been Issued`；HTML 含 Logo/品牌色；英中双语；`{name}` 正确；`{cert_type}`=DAC、`{issue_time}` 为 ISO 8601 UTC、`{serial_number}` 为十六进制；含 View Certificate / 查看证书链接；其他成员未收到<br>[3] 第二次真实 DAC 签发成功<br>[4] **未**再发送首次 DAC 邮件（Tenant 维度仅 1 次；二次成功不重发） | 来源 AC-02: 首次 DAC 签发邮件在真实证书签发后发送（非 Demo）<br>来源 AC-04: 邮件模板中英文双语，变量替换正确 |
| 【Login-Profile-Registration】【E2E】首次烧录邮件 - 内容正确且二次成功烧录不重发 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（仍为免费版/未升级企业），尚未发送过首次烧录邮件<br>2. 可生成**非 Demo** 真实 Production Record；创建者邮箱可收信；同 Tenant 有其他成员<br>3. 记录创建者当前首次烧录类邮件数量（应为 0） | [1] 生成首条真实 Production Record<br>[2] 打开创建者收到的首次烧录邮件，核对发件人、主题、HTML 双语、`{name}`、生产信息变量与查看生产记录链接；并确认其他成员未收到<br>[3] **二次成功烧录**：再次生成一条真实 Production Record<br>[4] 检查创建者邮箱是否新增首次烧录类邮件 | [1] 真实 Production Record 生成成功；创建者收到 **1** 封首次烧录邮件<br>[2] 发件人 `Snowball OBIS` / `noreply@snowballtech.com`；主题 `Production Milestone! Your First Device Has Been Flashed`；HTML 含 Logo/品牌色；英中双语；`{name}` 正确；`{product_name}`/`{batch_name}`/`{flash_time}`（ISO 8601 UTC）与记录一致；含 View Production Records / 查看生产记录链接；其他成员未收到<br>[3] 第二次真实 Production Record 生成成功<br>[4] **未**再发送首次烧录邮件（Tenant 维度仅 1 次；二次成功烧录不重发） | 来源 AC-03: 首次烧录邮件在真实 Production Record 上传后发送<br>来源 AC-04: 邮件模板中英文双语，变量替换正确 |
| 【Login-Profile-Registration】【E2E】三类邮件组合 - 同一 Tenant 顺序完成各收一封 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P1 | 1. 新自注册 Tenant（或尚未触发过三类事务邮件的 Tenant），且未升级企业<br>2. 可依次完成自注册、真实 DAC 签发、真实烧录<br>3. 创建者邮箱可收信 | [1] 完成自注册 Tenant 创建，统计 Welcome 邮件数量<br>[2] 签发首条真实 DAC，统计首次 DAC 邮件数量<br>[3] 生成首条真实 Production Record，统计首次烧录邮件数量<br>[4] 汇总三类事务邮件数量 | [1] Welcome 恰好 1 封<br>[2] 首次 DAC 恰好 1 封<br>[3] 首次烧录恰好 1 封<br>[4] 三类邮件各 1 封，去重计数互不影响（本条只验数量；内容规格见各场景专属用例） | 来源 QA扩展: 同一 Tenant 按顺序完成 Welcome → 首次真实 DAC → 首次真实烧录，三类邮件均各收到 1 封 |
| 【Login-Profile-Registration】【E2E】Demo 排除 - Demo 签发与烧录不触发且不占首次额度 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪，尚未发送过首次 DAC / 首次烧录邮件<br>2. 已具备 002-02 Demo 资源（`demo` 标签 / `Demo-`，如 Test DAC、Demo-Product）；另可使用**非 Demo** 真实资源对照<br>3. 创建者邮箱可收信；记录当前相关邮件数量 | [1] 使用 Demo DAC（Test DAC / `demo`）完成一次证书签发，检查邮箱<br>[2] 使用 Demo 预设产品/工厂完成一次烧录并生成 Production Record，检查邮箱<br>[3] 使用非 Demo 真实 DAC 签发首条证书，检查是否收到首次 DAC 邮件<br>[4] 使用非 Demo 真实产品生成首条 Production Record，检查是否收到首次烧录邮件 | [1] Demo DAC 签发成功；**不发送**首次 DAC 邮件，也不发送其他事务邮件<br>[2] Demo 预设烧录/记录生成成功；**不发送**首次烧录邮件，也不发送其他事务邮件<br>[3] 发送首次 DAC 邮件（Demo 不占用「首次」额度）<br>[4] 发送首次烧录邮件（Demo 不占用「首次」额度） | 来源 AC-05: Demo 资源不触发邮件 |
| 【Login-Profile-Registration】【E2E】自建产品混用 Demo 资产 - 首次烧录仍发邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（未升级企业），尚未发送过首次烧录邮件<br>2. 用户创建**第一个自建产品**，产品内配置/使用了 demo key 和/或 demo cert 和/或 demo factory 数据<br>3. 可完成该产品第一次烧录并生成 Production Record；创建者邮箱可收信 | [1] 确认当前为第一个自建产品且含 demo key/cert/factory 资产<br>[2] 完成该产品第一次烧录直至 Production Record 生成成功<br>[3] 检查创建者邮箱是否收到首次烧录邮件 | [1] 自建产品与 Demo 资产配置就绪<br>[2] 烧录/记录生成成功<br>[3] **发送**首次产品烧录邮件（混用 Demo 资产不排除本场景） | 来源 需求描述: 用户第一个自建产品里面使用了 demo key/demo cert/demo factory 数据，第一次烧录完成需要发邮件（评论 2026-07-14） |
| 【Login-Profile-Registration】【Functional】运营开通 Tenant - 不触发任何事务邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 可通过运营后台开通新 Tenant（非自注册）<br>2. 该 Tenant 关联邮箱可收信<br>3. 该 Tenant 可执行真实 DAC 签发与真实 Production Record 生成 | [1] 完成运营后台开通 Tenant，检查是否收到 Welcome<br>[2] 签发真实 DAC，检查是否收到首次 DAC 邮件<br>[3] 生成真实 Production Record，检查是否收到首次烧录邮件 | [1] Tenant 开通成功；**不发送** Welcome<br>[2] 真实 DAC 签发成功；**不发送**首次 DAC 邮件<br>[3] Production Record 生成成功；**不发送**首次烧录邮件 | 来源 AC-07: 运营后台开通的 Tenant 不触发任何邮件 |
| 【Login-Profile-Registration】【Functional】升级企业后 - DAC 与烧录不发事务邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已创建（可已收 Welcome）；按现网路径将该账户/Tenant **升级为企业**<br>2. 升级前尚未发送过首次 DAC / 首次烧录邮件，或已确认升级后仍可观察是否新发<br>3. 创建者邮箱可收信 | [1] 完成自注册账户升级为企业<br>[2] 升级后签发一张 DAC，检查邮箱<br>[3] 升级后完成一次烧录并生成 Production Record，检查邮箱 | [1] 升级成功<br>[2] **不发送**首次 DAC 签发邮件<br>[3] **不发送**首次烧录邮件 | 来源 需求描述: 自注册账户升级成企业后签发 DAC / 第一次烧录不需要发邮件（评论 2026-07-14） |
| 【Login-Profile-Registration】【E2E】Matter 组合 - 首次烧录同时收到 DAC 与烧录两封邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（未升级企业），尚未发送过首次 DAC / 首次烧录邮件<br>2. 使用 Matter module，其首次烧录同时意味着首次 DAC 签发成功<br>3. 创建者邮箱可收信 | [1] 执行 Matter module 首次设备烧录直至成功<br>[2] 检查创建者邮箱在烧录成功时刻收到的邮件种类与数量 | [1] 烧录成功，业务流程正常完成<br>[2] 同时收到 **两封**邮件：首次 DAC 签发邮件 + 首次产品烧录邮件（期望行为） | 来源 需求描述: Matter module 首次烧录同时意味着首次 DAC 签发成功时，用户在烧录成功那一刻收到两封邮件（DAC + 烧录） |
| 【Login-Profile-Registration】【Functional】发送失败 - 重试中成功则停止且不阻塞 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 可模拟事务邮件首次发送失败、后续某次（≤3）重试成功（待确认注入方式）<br>2. 准备触发任一事务邮件的业务操作（如自注册创建 Tenant）<br>3. 可观察后台重试日志 | [1] 开启「首次失败、第 N 次重试成功」模拟<br>[2] 执行触发邮件的业务操作<br>[3] 观察重试间隔、次数及是否继续重试，并确认业务结果 | [1] 失败注入生效<br>[2] 业务操作成功完成（不因邮件失败阻塞）<br>[3] 约 5 分钟间隔重试；成功后**停止**后续重试；累计重试不超过 3 次；业务数据成功落库（本迭代不验 Operator 告警） | 来源 AC-06: 发送失败重试 3 次（间隔 5 分钟），不阻塞业务流程（告警暂不做） |
| 【Login-Profile-Registration】【Functional】发送失败 - 三次均失败停止重试且不阻塞 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 可模拟邮件持续发送失败，或使用无效/不可达创建者邮箱<br>2. 准备触发事务邮件的业务操作<br>3. 可查看失败/重试日志（本迭代**不要求** Operator 告警） | [1] 配置持续发送失败（或无效邮箱）<br>[2] 执行触发邮件的业务操作<br>[3] 等待重试完成（间隔约 5 分钟，最多 3 次），检查重试次数、业务数据及是否投递成功 | [1] 失败条件生效<br>[2] 业务主流程**成功**（不阻塞）<br>[3] 后台重试共 3 次后停止；无成功投递的事务邮件；**不要求**产生 Operator 告警（本迭代 Out of Scope） | 来源 AC-06: 发送失败重试 3 次（间隔 5 分钟），不阻塞业务流程（告警暂不做，评论 2026-07-14） |
| 【Login-Profile-Registration】【Functional】负向 - 真实 DAC 签发失败不发送首次 DAC 邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P1 | 1. 自注册 Tenant 已就绪，尚未发送过首次 DAC 邮件<br>2. 可构造真实 DAC 签发失败场景<br>3. 创建者邮箱可收信；记录当前首次 DAC 类邮件数量 | [1] 发起真实 DAC 签发并使其失败<br>[2] 检查创建者邮箱是否收到首次 DAC 邮件 | [1] DAC 签发失败，业务按失败路径处理<br>[2] **不发送**首次 DAC 签发邮件 | 来源 QA扩展: 真实 DAC 签发失败时，不发送首次 DAC 签发邮件 |
| 【Login-Profile-Registration】【Functional】负向 - Production Record 生成失败不发送首次烧录邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P1 | 1. 自注册 Tenant 已就绪，尚未发送过首次烧录邮件<br>2. 可构造真实 Production Record 生成失败场景<br>3. 创建者邮箱可收信；记录当前首次烧录类邮件数量 | [1] 发起真实 Production Record 生成并使其失败<br>[2] 检查创建者邮箱是否收到首次烧录邮件 | [1] Production Record 生成失败，业务按失败路径处理<br>[2] **不发送**首次烧录邮件 | 来源 QA扩展: Production Record 生成失败时，不发送首次烧录邮件 |
| 【Login-Profile-Registration】【E2E】DAC 业务失败后成功 - 失败不发、再次成功仍发且二次成功不重发 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（未升级企业），尚未发送过首次 DAC 邮件<br>2. 可构造真实 DAC **业务签发失败**，并可再次发起**成功**签发（非 Demo）<br>3. 创建者邮箱可收信；记录当前首次 DAC 类邮件数量（应为 0） | [1] 发起真实 DAC 签发并使其**业务失败**<br>[2] 检查创建者邮箱是否收到首次 DAC 邮件<br>[3] 再次发起真实 DAC 签发直至**成功**<br>[4] 检查创建者是否收到首次 DAC 邮件（核对主题即可，内容规格见专属用例）<br>[5] 再签发一条真实 DAC（二次成功），检查是否新增首次 DAC 邮件 | [1] DAC 签发失败，业务按失败路径处理<br>[2] **不发送**首次 DAC 邮件（失败不占用「首次成功」额度）<br>[3] 第二次尝试签发成功<br>[4] **发送**首次 DAC 邮件 **1** 封（以首次业务成功计）<br>[5] 二次成功签发后**未**再发送首次 DAC 邮件 | 来源 AC-02: 首次 DAC 签发邮件在真实证书签发后发送（非 Demo）<br>来源 QA扩展: 业务失败不占用首次额度；失败后再成功仍发且仅 1 次 |
| 【Login-Profile-Registration】【E2E】烧录业务失败后成功 - 失败不发、再次成功仍发且二次成功烧录不重发 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（未升级企业），尚未发送过首次烧录邮件<br>2. 可构造真实烧录 / Production Record **业务生成失败**，并可再次发起**成功**烧录（非 Demo）<br>3. 创建者邮箱可收信；记录当前首次烧录类邮件数量（应为 0） | [1] 发起真实烧录 / Production Record 生成并使其**业务失败**<br>[2] 检查创建者邮箱是否收到首次烧录邮件<br>[3] 再次发起真实烧录直至 Production Record **生成成功**<br>[4] 检查创建者是否收到首次烧录邮件（核对主题即可，内容规格见专属用例）<br>[5] 再完成一次真实烧录并生成 Production Record（二次成功烧录），检查是否新增首次烧录邮件 | [1] 烧录 / Production Record 失败，业务按失败路径处理<br>[2] **不发送**首次烧录邮件（失败不占用「首次成功」额度）<br>[3] 再次烧录成功，Production Record 落库<br>[4] **发送**首次烧录邮件 **1** 封（以首次业务成功计）<br>[5] 二次成功烧录后**未**再发送首次烧录邮件 | 来源 AC-03: 首次烧录邮件在真实 Production Record 上传后发送<br>来源 QA扩展: 业务失败不占用首次额度；失败后再成功仍发且仅 1 次 |
| 【Login-Profile-Registration】【E2E】Matter 失败后成功 - 首次业务失败不发、再次烧录成功双发且二次不重发 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P1 | 1. 自注册 Tenant 已就绪（未升级企业），尚未发送过首次 DAC / 首次烧录邮件<br>2. 使用 Matter module；可构造**首次烧录业务失败**，并可再次烧录成功（成功时同时意味着首次 DAC 签发成功）<br>3. 创建者邮箱可收信 | [1] 执行 Matter module 首次设备烧录并使其**业务失败**<br>[2] 检查创建者邮箱是否收到首次 DAC / 首次烧录邮件<br>[3] 再次执行 Matter 烧录直至成功<br>[4] 检查烧录成功时刻收到的邮件种类与数量<br>[5] 再完成一次成功烧录，检查是否新增首次 DAC / 首次烧录邮件 | [1] 烧录失败，业务按失败路径处理<br>[2] **不发送**首次 DAC 邮件，也**不发送**首次烧录邮件<br>[3] 再次烧录成功<br>[4] 同时收到 **两封**邮件：首次 DAC + 首次烧录（与 Matter 双发期望一致）<br>[5] 二次成功烧录后两类邮件均**不**再发送 | 来源 需求描述: Matter module 首次烧录同时意味着首次 DAC 签发成功时，用户在烧录成功那一刻收到两封邮件（DAC + 烧录）<br>来源 QA扩展: 业务失败不占用首次额度；失败后再成功仍按成功规则发信 |
| 【Login-Profile-Registration】【E2E】非创建者操作 - 成员首次签发DAC/烧录仍仅触达 Tenant 创建者 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 已就绪（未升级企业），尚未发送过首次 DAC / 首次烧录邮件<br>2. 同 Tenant 下已邀请至少 1 名**非 Tenant 创建者**成员（Manager 或 Member），具备签发真实 DAC 与完成真实烧录的权限<br>3. Tenant 创建者邮箱与该成员邮箱均可收信，且地址不同 | [1] 以**非创建者**成员登录，签发首条真实终端实体 DAC<br>[2] 分别检查 Tenant **创建者**邮箱与**操作者**邮箱是否收到首次 DAC 邮件<br>[3] 仍以该非创建者成员登录，完成首条真实 Production Record 烧录<br>[4] 分别检查创建者邮箱与操作者邮箱是否收到首次烧录邮件 | [1] 非创建者完成真实 DAC 签发成功<br>[2] **仅创建者**收到首次 DAC 邮件 1 封；操作者（非创建者）**未收到**；`{name}` 等变量仍为创建者注册信息（非操作者）<br>[3] 非创建者完成真实烧录成功<br>[4] **仅创建者**收到首次烧录邮件 1 封；操作者**未收到**（收件人固定创建者，与操作者角色无关） | 来源 需求描述: 仅发送给 Tenant 创建者邮箱（评论 2026-07-10 确认；非「创建者 + System Admin」）<br>来源 AC-02: 首次 DAC 签发邮件在真实证书签发后发送（非 Demo）<br>来源 AC-03: 首次烧录邮件在真实 Production Record 上传后发送 |
| 【Login-Profile-Registration】【E2E】Welcome 邮件 - 命中企业白名单自注册后创建者仍收到 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 超管已为目标企业开启 Self-Registration 并配置 Email Domain 白名单；企业租户有效<br>2. 准备未注册邮箱，域名命中该白名单；邮箱可收信<br>3. 可走完注册至个人 trial Tenant 创建成功（**Apply to Join** 或 **Skip&Enter System** 均可） | [1] 使用命中白名单的邮箱完成自注册，直至出现白名单加入提示后选择 **Skip&Enter System**（或 **Apply to Join** 后 **Enter Trail**），完成个人 trial/免费版 Tenant 创建<br>[2] 检查该用户（个人 Tenant **创建者**）邮箱是否收到 Welcome，并核对主题与收件人为创建者本人<br>[3] 确认未因命中白名单而漏发 Welcome；企业加入申请相关邮件不在本条断言范围（见 001-05） | [1] 个人 trial Tenant 创建成功；可进入系统<br>[2] 创建者收到 **1** 封 Welcome；主题 `Welcome to OBIS! Let's Get Started`；发件人 `Snowball OBIS` / `noreply@snowballtech.com`<br>[3] 命中企业白名单**不阻断**个人 Tenant 的 Welcome 触达 | 来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次<br>来源 QA扩展: 命中企业域名白名单仍创建个人 trial Tenant 并发送 Welcome |
| 【Login-Profile-Registration】【E2E】邀请加入自注册 Tenant - 被邀请人不收 Welcome且非收件人 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册免费版 Tenant 已创建，创建者已收 Welcome；尚未发送过首次 DAC / 首次烧录邮件（或已记录基线）<br>2. 创建者可通过 Invitations 邀请新成员；准备可收信的被邀请人邮箱<br>3. 被邀请人接受邀请后具备签发真实 DAC / 完成真实烧录的权限（若无权限则本条仅验「接受邀请不收 Welcome」） | [1] 创建者邀请用户加入本自注册 Tenant，被邀请人接受邀请成为成员<br>[2] 检查被邀请人邮箱是否收到 Welcome 或首次 DAC/烧录类事务邮件<br>[3] 以被邀请人登录，完成首条真实 DAC 签发与首条真实 Production Record（若权限不足则跳过本步并记待确认）<br>[4] 分别检查创建者与被邀请人邮箱 | [1] 被邀请人成为该 Tenant 成员<br>[2] 被邀请人**未收到** Welcome，也**未收到**首次 DAC/烧录邮件（接受邀请本身不触发 006-01 事务邮件）<br>[3] 业务操作成功（有权限时）<br>[4] **仅创建者**收到首次 DAC、首次烧录各至多 1 封；被邀请人仍不收 | 来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次<br>来源 需求描述: 仅发送给 Tenant 创建者邮箱<br>来源 QA扩展: 邀请加入自注册 Tenant 不向被邀请人发 Welcome |
| 【Login-Profile-Registration】【E2E】邀请加入非自注册 Tenant - 加入与DAC/烧录均不发事务邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 准备**非自注册** Tenant（运营后台开通或企业 Tenant）<br>2. 该 Tenant Admin 可邀请成员；被邀请人邮箱可收信<br>3. 被邀请人接受后可在该 Tenant 下尝试真实 DAC 签发与真实烧录 | [1] 被邀请人接受邀请加入该非自注册 Tenant<br>[2] 检查被邀请人及该 Tenant 创建者/关联邮箱是否收到 Welcome<br>[3] 在该 Tenant 上下文签发真实 DAC，检查是否收到首次 DAC 邮件<br>[4] 在该 Tenant 上下文完成真实烧录并生成 Production Record，检查是否收到首次烧录邮件 | [1] 加入成功<br>[2] **不发送** Welcome（非自注册路径不触发 006-01 Welcome）<br>[3] **不发送**首次 DAC 邮件<br>[4] **不发送**首次烧录邮件 | 来源 AC-07: 运营后台开通的 Tenant 不触发任何邮件<br>来源 QA扩展: 邀请加入非自注册 Tenant 后，DAC/烧录亦不发 006-01 事务邮件 |
| 【Login-Profile-Registration】【E2E】企业版切回免费版 - 首次真实烧录应发邮件 | /Cloud/Login & Profile/Registration | 免费版事务邮件 | P0 | 1. 自注册 Tenant 曾**升级为企业版**；升级后在企业版期间可已做过烧录（企业版不发信）<br>2. 超管可在**超管页面**将该账户/Tenant **切回免费版**<br>3. 切回后尚未在免费版发送过首次烧录邮件；创建者邮箱可收信；可生成非 Demo 真实 Production Record | [1] 在**超管页面**完成企业版 → 免费版切回，确认当前为免费版<br>[2] 记录创建者当前首次烧录类邮件数量<br>[3] 在免费版状态下完成首条真实 Production Record<br>[4] 检查创建者是否收到首次烧录邮件；再完成一次真实烧录，确认不重发 | [1] 超管切回免费版成功<br>[2] 取得基线（企业版期间不应因烧录新增首次烧录邮件）<br>[3] **发送**首次烧录邮件 **1** 封（主题 `Production Milestone! Your First Device Has Been Flashed`）<br>[4] 二次成功烧录**未**再发送（Tenant 免费版维度仅 1 次） | 来源 AC-03: 首次烧录邮件在真实 Production Record 上传后发送<br>来源 QA扩展: 切回路径在超管页面；企业版切回免费版后首次烧录需要发邮件（2026-07-16 确认） |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | 自注册成功收 Welcome | WEL-01/03；FMT-01～05；WEL-CNT-01～03 |
| 2 | Welcome 去重 | WEL-02；COMBO-03 |
| 3 | 首次真实 DAC 邮件 + 二次签发不重发 | DAC-01/02/03；DAC-CNT-01～03；NEG-04（时间戳） |
| 4 | 首次真实烧录邮件 + 二次成功烧录不重发 | FLASH-01/02/03；FLASH-CNT-01～03；NEG-04 |
| 5 | 三类邮件顺序各一封 | COMBO-02 |
| 6 | Demo 预设不触发且不占首次额度 | EXCL-01～04 |
| 7 | 自建产品混用 Demo 资产首次烧录仍发 | EXCL-09 |
| 8 | 运营开通不触发 | EXCL-05/06 |
| 9 | 升级企业后不发 DAC/烧录 | EXCL-07/08 |
| 10 | Matter 双发 | COMBO-01 |
| 11 | 邮件通道失败重试中成功 | RETRY-01/02/04 |
| 12 | 邮件通道三次失败停止重试不阻塞 | RETRY-01/03/04；NEG-01 |
| 13 | DAC 签发失败不发信 | NEG-02 |
| 14 | 烧录失败不发信 | NEG-03 |
| 15 | DAC 业务失败后再次成功仍发 + 二次不重发 | DAC-04；DAC-01/02 |
| 16 | 烧录业务失败后再次成功仍发 + 二次成功烧录不重发 | FLASH-04；FLASH-01/02 |
| 17 | Matter 失败后成功双发 + 二次不重发 | COMBO-01；DAC-04；FLASH-04 |
| 18 | 非创建者完成首次 DAC/烧录，仍仅触达创建者 | DAC-05；FLASH-05；DAC-03；FLASH-03 |
| 19 | 命中企业白名单自注册仍收 Welcome | WEL-04 |
| 20 | 邀请加入自注册 Tenant：被邀请人不收 Welcome | EXCL-10 |
| 21 | 邀请加入非自注册 Tenant：加入与 DAC/烧录均不发 | EXCL-11 |
| 22 | 企业版切回免费版后首次烧录应发 | EXCL-12 |

**51 条 TP 均已至少被 1 条用例覆盖。**

## 待确认

- [x] MeterSphere「所属模块」：/Cloud/Login & Profile/Registration（自注册相关）
- [x] Demo 资源判定口径 — 已对齐 [002-02](https://project.feishu.cn/obis/userstory/detail/7006975243)
- [x] Operator 告警 — 本迭代不做（评论 2026-07-14）
- [x] 升级企业后不发 DAC/烧录邮件 — 已确认
- [x] 自建产品混用 Demo 资产首次烧录仍发 — 已确认
- [ ] 邮件 CTA 落地为登录页还是登录后深链
- [ ] Welcome「重复创建成功事件」的可测触发方式
- [ ] 邮件发送失败的注入/模拟方式
- [ ] DAC / 烧录**业务失败**的可构造方式（与邮件通道失败区分）
- [ ] 「升级为企业」现网入口与可测账号路径
- [ ] 免费版下 Manager / Member 是否具备真实 DAC 签发与烧录权限（本条前置）
- [x] 企业版切回免费版：路径在超管页面（2026-07-16 确认）
- [ ] 白名单 Apply / Skip 是否均完成个人 trial Tenant 创建并触发 Welcome
