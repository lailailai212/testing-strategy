# 【体验优化P2】Audit功能统一 功能测试用例

> 来源：`docs/sprints/OBIS-20260727-20260807/features/ux-p2-audit-unify/acceptance.md`（含 TP-ID）  
> 需求：【体验优化P2】Audit功能统一（[Story #7029049092](https://project.feishu.cn/obis/userstory/detail/7029049092)）  
> Story MD：`story/obis-7029049092-体验优化p2-audit功能统一/obis-7029049092-体验优化p2-audit功能统一.md`  
> 用例数：12（**P0 × 3，P1 × 6，P2 × 3**；UI × 3，Functional × 4，E2E × 5）；覆盖 TP 22 条  
> 用例等级约定：P0 = 阻塞或重要环节/重要功能主路径；P1 = 重要能力；P2 = 边界/空态/一致性抽测  
> 入口规则：Group/Account/Profile/KMS/PKI/Product 详情 → **Audit**（KMS 对应 Operation Log / Audit Tab）；工具栏 Filter / Columns / Refresh / Sort  
> 产品规则：Group 为基准；Account/Profile/PKI/Product 与 Group 完全一致；KMS Filter 在 Organization 后额外 Operation Type；现状「Operation」列 = Operation Details（默认隐藏）  
> 设计原则：一条用例覆盖一个用户场景，场景内可校验多个测试点；步骤清晰连贯；单用例步骤 ≤ 10  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：见 `testcases/module-mapping.json`（对照 `docs/modules/metersphere-modules.json`）  
> 标签列：仅可读业务名 `体验优化P2-Audit功能统一`（不含 TP-ID / AC 序号）  
> 备注列：标明需求来源；来自 AC 时写 `来源 AC-0x: {AC 原文}`
> 评审材料：`reports/testcase-review.md`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Admin-Group】【UI】Audit 列表 - 默认列与 Operator/Organization/Time | /Cloud/Admin/Group | 体验优化P2-Audit功能统一 | P0 | 1. 已登录可访问 Group 详情 Audit<br>2. 目标 Group 已有若干审计日志（含可识别操作人）<br>3. 可准备一列内容较长以便验证溢出 hover | [1] 进入 Admin → Group → 目标 Group 详情 → Audit Tab，观察默认可见列<br>[2] 核对 Operator 列：头像、Name、邮箱 icon；hover 邮箱 icon，复制完整邮箱<br>[3] 核对 Organization 列展示内容<br>[4] 核对 Operation Time 格式；若单元格溢出则 hover 查看全文 | [1] 默认可见 Operator、Organization、Operation Type、Operation Time；**不**默认展示 Operation Details<br>[2] Operator 为头像+Name+邮箱 icon；hover 出完整邮箱与复制，复制成功<br>[3] Organization 为操作人所属租户简称<br>[4] Operation Time 为年月日时分秒；溢出时可 hover 见全文 | 来源 AC-01: 用户打开任意目标模块 Audit 列表时，默认可见 Operator（头像+Name+邮箱 icon，hover 完整邮箱+复制）、Organization（租户简称）、Operation Type、Operation Time（年月日时分秒）；溢出内容 hover 展示全文；Operation Details 默认隐藏且位于 Operation Type 后。 |
| 【Admin-Group】【Functional】Audit Filter - 筛选项与时间起止边界 | /Cloud/Admin/Group | 体验优化P2-Audit功能统一 | P1 | 1. Group Audit 有跨多日的日志数据<br>2. 已知某日边界附近有可验证的记录（靠近 00:00:00 / 23:59:59） | [1] 打开 Audit → Filter，核对筛选项与 Placeholder<br>[2] 选择 Start date / End date 为同一天（或已知边界日），应用筛选<br>[3] 核对结果是否按起日 00:00:00、止日 23:59:59 生效 | [1] 含 Operator Name、Operator Email、Organization 输入框（Placeholder 为 Please Enter / 请输入）及 Operation Time 范围<br>[2] 筛选可执行<br>[3] 结果落在起日 00:00:00～止日 23:59:59 内（边界记录符合预期） | 来源 AC-02: 用户打开 Audit Filter 时，可按 Operator Name、Operator Email、Organization（输入框，Placeholder「Please Enter / 请输入」）及 Operation Time 范围筛选；Start date 取当日 00:00:00，End date 取当日 23:59:59。 |
| 【Admin-Group】【Functional】Audit Filter - 姓名邮箱组织匹配与空态 | /Cloud/Admin/Group | 体验优化P2-Audit功能统一 | P2 | 1. 已知日志中存在可匹配的 Operator Name / Email / Organization<br>2. 可构造无匹配的输入关键词 | [1] 分别按 Operator Name、Operator Email、Organization 输入已知匹配值并筛选<br>[2] 输入无匹配关键词并筛选，观察空态 | [1] 各输入可筛出匹配行<br>[2] 无匹配时列表空态合理（空提示/空表，无报错） | 来源 AC-02: 用户打开 Audit Filter 时，可按 Operator Name、Operator Email、Organization（输入框，Placeholder「Please Enter / 请输入」）及 Operation Time 范围筛选；Start date 取当日 00:00:00，End date 取当日 23:59:59。 |
| 【Admin-Group】【UI】Audit Columns - 锁定列与开启 Operation Details | /Cloud/Admin/Group | 体验优化P2-Audit功能统一 | P0 | 1. 已进入 Group Audit<br>2. 列表存在原「Operation」长文案类数据，便于开启 Details 后核对 | [1] 打开 Columns，尝试隐藏或拖拽换序 Operator、Operation Type<br>[2] 开启 Operation Details，观察列位置与单元格内容<br>[3] 确认默认关闭时 Details 不可见 | [1] Operator、Operation Type 不可隐藏、不可拖拽换序<br>[2] Details 出现在 Operation Type **后**一列；内容为原 Operation 长文案格式<br>[3] 默认不展示 Operation Details | 来源 AC-03: 用户配置 Columns 时：Operator、Operation Type 不可隐藏且不可换顺序；Organization、Operation Time 可配置；Operation Details 默认可开启且位置在 Operation Type 后。<br>来源 AC-01: 用户打开任意目标模块 Audit 列表时，默认可见 Operator（头像+Name+邮箱 icon，hover 完整邮箱+复制）、Organization（租户简称）、Operation Type、Operation Time（年月日时分秒）；溢出内容 hover 展示全文；Operation Details 默认隐藏且位于 Operation Type 后。 |
| 【Admin-Group】【UI】Audit Columns - Organization/Time 可配置并恢复默认 | /Cloud/Admin/Group | 体验优化P2-Audit功能统一 | P2 | 1. 已进入 Group Audit，当前为默认可见列集 | [1] 在 Columns 中隐藏 Organization、再隐藏 Operation Time，观察列表<br>[2] 重新显示上述列（或关闭 Columns 后恢复默认可见集，按现网恢复方式） | [1] Organization、Operation Time 可隐藏，列表不再展示对应列<br>[2] 可再次显示；关闭/恢复后回到默认可见集（Operator、Organization、Operation Type、Operation Time；Details 仍默认隐藏） | 来源 AC-03: 用户配置 Columns 时：Operator、Operation Type 不可隐藏且不可换顺序；Organization、Operation Time 可配置；Operation Details 默认可开启且位置在 Operation Type 后。 |
| 【Admin-Group】【Functional】Audit Refresh 与 Sort - 默认倒序及升序切换 | /Cloud/Admin/Group | 体验优化P2-Audit功能统一 | P1 | 1. Group Audit 有多条不同 Operation Time 的日志<br>2. 可制造一条新操作以便验证 Refresh（或对照时间戳变化） | [1] 打开 Audit，观察默认排序<br>[2] 点击 Refresh，确认列表刷新<br>[3] 打开 Sort，确认仅可按 Operation Time；切换为正序后观察列表<br>[4] 确认无其它 Sort 维度 | [1] 默认按 Operation Time **倒序**<br>[2] Refresh 后列表数据刷新<br>[3] 正序后按时间升序排列<br>[4] Sort 仅 Operation Time，无其它维度 | 来源 AC-04: 用户使用 Refresh 可刷新列表；Sort 仅按 Operation Time，默认倒序。 |
| 【Admin-Account】【E2E】Account Audit - 与 Group 基准规格一致 | /Cloud/Admin/Account | 体验优化P2-Audit功能统一 | P1 | 1. 已登录可进入 Account 详情 Audit<br>2. 对照 Group 基准已验收通过（或同会话可对照） | [1] 进入 Admin → Account → 目标账号详情 → Audit<br>[2] 核对默认列、Operator hover（邮箱+复制）、Organization<br>[3] 抽测 Filter / Columns / Sort / Refresh 关键能力与 Group 一致 | [1] Audit 区域可打开<br>[2] 默认列与 Operator/Organization 交互同 Group<br>[3] Filter、Columns、Sort、Refresh 规格与 Group 一致 | 来源 AC-05: Group / Account / Profile / PKI / Product 的 Audit 规格与 Group 基准完全一致。 |
| 【Login-&-Profile-My-Profile】【E2E】Profile Audit - 与 Group 一致且与 Account 行为一致 | /Cloud/Login & Profile/My Profile | 体验优化P2-Audit功能统一 | P2 | 1. 已登录可进入 My Profile → Audit<br>2. 可对照 Account 详情 Audit（是否同组件待确认，验收结果一致即可） | [1] 进入 My Profile → Audit，核对默认列、Operator hover、Organization、Filter/Columns/Sort<br>[2] 对照 Account Audit：抽测列配置开关与筛选输入行为是否一致 | [1] Profile Audit 规格与 Group 完全一致<br>[2] Account 与 Profile 的列配置/筛选行为一致（验收结果一致即可） | 来源 AC-05: Group / Account / Profile / PKI / Product 的 Audit 规格与 Group 基准完全一致。<br>来源 QA扩展: Account 与 Profile 列配置/筛选行为一致（是否同组件待确认，验收结果一致即可） |
| 【KMS-Key-Detail-Operation-Log】【E2E】KMS Audit - 列/工具栏同 Group 且 Details 默认隐藏 | /Cloud/KMS/Key Detail/Operation Log | 体验优化P2-Audit功能统一 | P1 | 1. 已登录可进入 KMS Key 详情 → Audit / Operation Log<br>2. 存在审计数据 | [1] 打开 KMS Audit，核对默认列与 Columns / Sort / Refresh<br>[2] 确认 Operation Details 默认隐藏；开启后可见 | [1] 默认列与 Columns/Sort/Refresh 同 Group<br>[2] Details 默认隐藏；开启后可见（位置在 Operation Type 后） | 来源 AC-05: Group / Account / Profile / PKI / Product 的 Audit 规格与 Group 基准完全一致。<br>来源 AC-06: KMS Audit 在 Filter 按钮展开面板中，于 Organization 后额外提供 Operation Type 筛选项；其余规格与 Group 一致。<br>来源 AC-01: 用户打开任意目标模块 Audit 列表时，默认可见 Operator（头像+Name+邮箱 icon，hover 完整邮箱+复制）、Organization（租户简称）、Operation Type、Operation Time（年月日时分秒）；溢出内容 hover 展示全文；Operation Details 默认隐藏且位于 Operation Type 后。 |
| 【KMS-Key-Detail-Operation-Log】【Functional】KMS Audit Filter - Organization 后 Operation Type 可筛 | /Cloud/KMS/Key Detail/Operation Log | 体验优化P2-Audit功能统一 | P0 | 1. KMS Audit 存在多种 Operation Type 的日志<br>2. Filter 控件类型（单选/多选/输入）待确认，以可筛为准 | [1] 点击列表上方 Filter，展开面板，核对 Organization 后是否有 Operation Type<br>[2] 使用 Operation Type 筛选某一已知类型并应用<br>[3] 核对列表结果 | [1] Filter 面板在 Organization **后**有 Operation Type 筛选项<br>[2] 筛选可执行<br>[3] 列表仅保留匹配的 Operation Type | 来源 AC-06: KMS Audit 在 Filter 按钮展开面板中，于 Organization 后额外提供 Operation Type 筛选项；其余规格与 Group 一致。 |
| 【PKI-Cert-&-Template-Detail-Audit】【E2E】PKI Audit - 与 Group 一致且无额外 Operation Type 筛选 | /Cloud/PKI/Cert & Template Detail/Audit | 体验优化P2-Audit功能统一 | P1 | 1. 已登录可进入 PKI 资源详情 → Audit<br>2. 对照 Group 基准 | [1] 打开 PKI Audit，核对默认列、Operator/Organization、Columns、Sort<br>[2] 打开 Filter，确认筛选项同 Group（无 KMS 独有 Operation Type） | [1] 默认列、Filter、Columns、Sort 同 Group<br>[2] Filter 无额外 Operation Type 项 | 来源 AC-05: Group / Account / Profile / PKI / Product 的 Audit 规格与 Group 基准完全一致。 |
| 【Product】【E2E】Product Audit - 对齐基准且无 KMS 独有 Filter | /Cloud/Product | 体验优化P2-Audit功能统一 | P1 | 1. 已登录可进入 Product 详情 → Audit<br>2. 产品侧可能已有 Organization 列，需与基准交互对齐 | [1] 打开 Product Audit，核对默认列（含 Organization）、Operator hover、Details 默认隐藏<br>[2] 抽测 Filter / Columns / Sort 与 Group 一致<br>[3] 打开 Filter，确认**不**出现仅 KMS 才有的 Operation Type 筛选项 | [1] 规格与 Group 一致（含 Operator hover、Details 默认隐藏、Organization）<br>[2] Filter/Columns/Sort 同 Group<br>[3] 无 KMS 独有 Filter Operation Type | 来源 AC-05: Group / Account / Profile / PKI / Product 的 Audit 规格与 Group 基准完全一致。<br>来源 QA扩展: Product 不额外出现仅 KMS 才有的 Filter Operation Type |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | Group 默认列与 Operator/Org/Time | TP-AUD-G01, G02, G03, G04 |
| 2 | Group Filter 字段与时间边界 | TP-AUD-G05, G06 |
| 3 | Group Filter 姓名/邮箱/组织与空态 | TP-AUD-G07 |
| 4 | Group Columns 锁定与 Details | TP-AUD-G08, G09 |
| 5 | Group Columns 可配置列恢复 | TP-AUD-G10 |
| 6 | Group Refresh 与 Sort | TP-AUD-G11, G12 |
| 7 | Account Audit 对齐 Group | TP-AUD-A01 |
| 8 | Profile Audit 对齐 + 与 Account 一致 | TP-AUD-A02, A03 |
| 9 | KMS 列/工具栏 + Details | TP-AUD-K01, K04 |
| 10 | KMS Filter Operation Type | TP-AUD-K02, K03 |
| 11 | PKI Audit 对齐 Group | TP-AUD-P01 |
| 12 | Product Audit 对齐 + 无 KMS 独有 Filter | TP-AUD-P02, P03 |

**22 条 TP 均已至少被 1 条用例覆盖。**

## 待确认

- [ ] KMS Filter 内 Operation Type：单选 / 多选 / 输入及可选值来源
- [ ] Organization Filter 是否模糊匹配；空组织展示与筛选
- [ ] 默认列顺序是否固定为 Operator → Organization → Operation Type →（Details）→ Operation Time
- [ ] Profile 与 Account Audit 是否共用同一组件
- [ ] Product Audit 在 MeterSphere 中的最终挂载路径（当前暂挂 `/Cloud/Product`）
