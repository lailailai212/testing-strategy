# 【体验优化P2】细节补充 功能测试用例

> 来源：`docs/sprints/OBIS-20260727-20260807/features/ux-p2-detail-supplement/acceptance.md`（含 TP-ID）  
> 需求：【体验优化P2】细节补充（[Story #7051514356](https://project.feishu.cn/obis/userstory/detail/7051514356)）  
> Story MD：`story/obis-7051514356-体验优化p2-细节补充/obis-7051514356-体验优化p2-细节补充.md`  
> 用例数：27（**P0 × 7，P1 × 12，P2 × 8**；UI × 21，Functional × 4，E2E × 2；覆盖 TP 38 条）
> 用例等级约定：P0 = 阻塞或重要环节/重要功能主路径；P1 = 重要能力；P2 = 边界/空态/一致性抽测
> 入口规则：Admin → Account / Group；Product → Product List / 产品详情 Tab；KMS → Key List；PKI → PKI List；Operation → Role / User(SNB)；头像 → My Profile  
> 产品规则：本人编辑隐藏 User Role、Notes；非本人仅 System Admin 可 Edit；Version 仅取 Prod 最新，无 Prod 显示 `-`；大列表固定三列 280/160/64，大屏中间列均分剩余宽度，小屏横向滚动且固定三列不被挤占  
> 设计原则：一条用例覆盖一个用户场景，场景内可校验多个测试点；步骤清晰连贯；单用例步骤 ≤ 10  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：见 `testcases/module-mapping.json`（对照 `docs/modules/metersphere-modules.json`）  
> 标签列：仅可读业务名 `体验优化P2细节补充`（不含 TP-ID / AC 序号）  
> 备注列：标明需求来源；来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Admin-Account】【UI】+n hover - Account 列表 User Role 展示全部 | /Cloud/Admin/Account | 体验优化P2细节补充 | P0 | 1. 已登录具备 Account 列表访问权限的账号<br>2. 列表中存在 User Role 溢出展示为 `+n` 的用户行（角色数足够触发溢出） | [1] 进入 Admin → Account 列表，定位 User Role 列出现 `+n` 的行<br>[2] 将鼠标悬停在该行的 `+n` 上<br>[3] 查看小窗中展示的 Role 内容 | [1] 可见 `+n` 溢出标识<br>[2] 弹出 hover 小窗<br>[3] 小窗展示被折叠的全部 Role，内容完整、可读 | 来源 AC-01: 用户在 Account 列表 User Role、Account 详情 Role、Group Linked Product Role，以及其它已出现 `+n` 的页面，hover `+n` 时应弹出小窗展示被折叠的全部数据。 |
| 【Admin-Account】【UI】+n hover - Account 详情 Role 展示全部 | /Cloud/Admin/Account | 体验优化P2细节补充 | P1 | 1. 已登录可访问 Account 详情<br>2. 目标用户详情页 Role 存在 `+n` 溢出 | [1] 从 Account 列表进入该用户详情页，定位 Role 区域的 `+n`<br>[2] hover `+n` 并核对本页全部 Role | [1] 详情页 Role 出现 `+n`<br>[2] 小窗展示全部 Role，与实际角色一致 | 来源 AC-01: 用户在 Account 列表 User Role、Account 详情 Role、Group Linked Product Role，以及其它已出现 `+n` 的页面，hover `+n` 时应弹出小窗展示被折叠的全部数据。 |
| 【Admin-Group】【UI】+n hover - Group Linked Product Role 展示其余角色 | /Cloud/Admin/Group | 体验优化P2细节补充 | P1 | 1. 已登录可访问 Group 详情<br>2. 某 Group → Linked Product Tab 中存在 Role 形如 `Member +2`（或等价 `+n`）的行 | [1] 进入 Admin → Group → 目标 Group 详情 → Linked Product Tab<br>[2] 定位 Role 列 `+n`，hover 打开小窗<br>[3] 对照被折叠的其余角色全文 | [1] Linked Product 列表可见<br>[2] hover 弹出小窗<br>[3] 小窗展示其余角色全文（如 Version Manager, Product Manager），与数据一致 | 来源 AC-01: 用户在 Account 列表 User Role、Account 详情 Role、Group Linked Product Role，以及其它已出现 `+n` 的页面，hover `+n` 时应弹出小窗展示被折叠的全部数据。 |
| 【Product-Product-List】【UI】+n hover - Product 列表 Module 浮层与滚动 | /Cloud/Product/Product List | 体验优化P2细节补充 | P1 | 1. 已登录可访问 Product 列表<br>2. 存在 Module 数量足以首 Tag + `+n` 溢出的产品；若溢出项很多可准备可滚动数据 | [1] 打开 Product 列表，定位 Module 列「首 Tag + `+n`」行<br>[2] hover `+n`，观察浮层标题与 Tag 列表<br>[3] 若溢出项过多，在浮层内滚动查看 | [1] 首个 Module 为 Tag，其余以 `+n` 胶囊展示<br>[2] 白底圆角浮层，标题为 `Module :`，内部 Tag 列出全部溢出 Module<br>[3] 内容过多时可滚动且 Tag 完整可见 | 来源 AC-01: 用户在 Account 列表 User Role、Account 详情 Role、Group Linked Product Role，以及其它已出现 `+n` 的页面，hover `+n` 时应弹出小窗展示被折叠的全部数据。<br>来源 需求描述: Product 列表 Module 列首 Tag + `+n`；hover 浮层标题 Module :，Tag 列出全部溢出项，过多可滚动 |
| 【Admin-Account】【Functional】+n hover - 单值无溢出与边界正确 | /Cloud/Admin/Account | 体验优化P2细节补充 | P2 | 1. 准备仅 1 个 User Role 的账号行（不触发 `+n`）<br>2. 另准备恰好触发溢出边界的账号行（刚出现 `+n`） | [1] Account 列表定位仅 1 个 Role 的行，确认无 `+n`，尝试 hover Role 区域<br>[2] 定位恰好溢出出现 `+n` 的行，hover `+n` 并核对小窗内容与角色全集 | [1] 无 `+n`，不出现 hover 溢出小窗<br>[2] `+n` 数值与小窗内容正确，覆盖被折叠项且无遗漏/重复 | 来源 AC-01: 用户在 Account 列表 User Role、Account 详情 Role、Group Linked Product Role，以及其它已出现 `+n` 的页面，hover `+n` 时应弹出小窗展示被折叠的全部数据。<br>来源 QA扩展: 仅 1 个值无 `+n` 时不出现 hover 溢出窗；恰好溢出边界时 `+n` 与小窗内容正确 |
| 【Admin-Account】【UI】+n hover - 中英文环境均可完整打开 | /Cloud/Admin/Account | 体验优化P2细节补充 | P2 | 1. 存在带 `+n` 的 Account 列表或详情数据<br>2. 可切换系统中/英文 | [1] 中文环境下打开带 `+n` 的页面，hover `+n`<br>[2] 切换英文环境，再次 hover 同一处 `+n` | [1] 中文环境小窗可打开且内容完整<br>[2] 英文环境同样可打开且内容完整 | 来源 QA扩展: 中英文环境下 `+n` hover 小窗均可打开且内容完整 |
| 【Admin-Account】【UI】成功 Toast - 中文「操作成功」样式 | /Cloud/Admin/Account | 体验优化P2细节补充 | P0 | 1. 系统语言为中文<br>2. 已登录，可执行任一无特殊文案约定的成功操作（如本人编辑 Name 后保存，或现网常规成功操作） | [1] 触发一次成功操作并观察 Toast<br>[2] 核对文案与样式（绿勾、浅绿底） | [1] 出现成功 Toast<br>[2] 文案为「操作成功」；左侧绿色成功图标 + 浅绿底提示条 | 来源 AC-02: 用户触发无特殊约定的成功操作后，成功 Toast 文案应为中文「操作成功」/ 英文「Operation Successful」，样式为成功态绿色图标 + 浅绿底提示条。 |
| 【Admin-Account】【UI】成功 Toast - 英文 Operation Successful | /Cloud/Admin/Account | 体验优化P2细节补充 | P1 | 1. 系统语言为英文<br>2. 可执行与中文用例同类的成功操作 | [1] 触发同一类成功操作<br>[2] 核对英文 Toast 文案与样式 | [1] 出现成功 Toast<br>[2] 文案为「Operation Successful」（非 Operation success）；成功态绿勾 + 浅绿底 | 来源 AC-02: 用户触发无特殊约定的成功操作后，成功 Toast 文案应为中文「操作成功」/ 英文「Operation Successful」，样式为成功态绿色图标 + 浅绿底提示条。 |
| 【Admin-Account】【UI】成功 Toast - 至少抽测两个模块一致 | /Cloud/Admin/Account | 体验优化P2细节补充 | P2 | 1. 中文或英文环境任选其一并固定<br>2. 准备至少两个不同模块可成功操作入口（如 Account 保存、Product/Group 等现网成功操作） | [1] 在模块 A 触发成功操作，记录 Toast 文案与样式<br>[2] 在模块 B 再触发一次成功操作并对比 | [1][2] 两处 Toast 文案与样式均符合统一规格（中文「操作成功」或英文「Operation Successful」+ 绿勾浅绿底），表现一致 | 来源 AC-02: 用户触发无特殊约定的成功操作后，成功 Toast 文案应为中文「操作成功」/ 英文「Operation Successful」，样式为成功态绿色图标 + 浅绿底提示条。<br>来源 QA扩展: 至少再抽测 2 个不同模块成功操作，Toast 文案与样式一致 |
| 【Admin-Account】【Functional】成功 Toast - 特殊文案例外不强制覆盖 | /Cloud/Admin/Account | 体验优化P2细节补充 | P2 | 1. 已知某 Story 约定了特殊成功文案的操作入口（如邀请用户成功带邮件提示等）<br>2. 可对照该 Story 约定文案 | [1] 触发该特殊约定成功操作<br>[2] 对照原 Story 约定文案，确认本 AC 未强制改写 | [1] 操作成功并出 Toast<br>[2] Toast 仍按各 Story 特殊文案展示，不受本 AC「操作成功 / Operation Successful」强制覆盖 | 来源 QA扩展: 需求约定有特殊文案的成功提示不受本 AC 强制覆盖（按各 Story 例外） |
| 【Product-Product-List】【UI】勾选框 - Filter 勾选态为主题色 | /Cloud/Product/Product List | 体验优化P2细节补充 | P1 | 1. 已登录可打开 Product 列表 Filter<br>2. 可对照 Figma node 15959-188662 主题色 | [1] 打开 Product 列表 Filter，勾选任一 Checkbox（如 Module）<br>[2] 观察勾选态颜色及旁侧标签文案 | [1] Checkbox 可勾选<br>[2] 勾选态为主题色（深蓝底白勾，对照 Figma）；旁侧标签文案不变 | 来源 AC-03: 用户在 Filter、表单等处勾选 Checkbox 时，勾选态颜色应为主题色（对照 Figma），旁侧标签文案不变。 |
| 【Admin-Account】【UI】勾选框 - 表单或下拉相关勾选主题色 | /Cloud/Admin/Account | 体验优化P2细节补充 | P2 | 1. 已登录，可打开含 Checkbox 的表单/下拉场景（如创建/编辑用户相关勾选，或现网等价表单 Checkbox） | [1] 打开含 Checkbox 的表单或下拉相关区域<br>[2] 勾选 Checkbox，观察颜色与标签 | [1] Checkbox 可见可操作<br>[2] 勾选态为主题色；旁侧标签文案不变 | 来源 AC-03: 用户在 Filter、表单等处勾选 Checkbox 时，勾选态颜色应为主题色（对照 Figma），旁侧标签文案不变。 |
| 【Operation-Role】【UI】勾选框与权限节点 - Role 树主题色及 OTA/Vulnerability 可配 | /Cloud/Operation/Role | 体验优化P2细节补充 | P0 | 1. 已登录具备 Role 配置权限（如 System Admin）<br>2. 可进入目标 Role 的权限树编辑 | [1] 进入 Operation → Role，打开某 Role 权限树<br>[2] 定位节点 **Vulnerability Tab Page / 漏洞 Tab 页面**、**OTA Tab Page / OTA Tab 页面**，勾选并观察勾选态颜色<br>[3] 确认两节点可勾选配置（保存按现网） | [1] 权限树可打开<br>[2] 两节点存在；勾选态为主题色（抽测非 Filter 勾选）<br>[3] 两权限可勾选配置 | 来源 AC-03: 用户在 Filter、表单等处勾选 Checkbox 时，勾选态颜色应为主题色（对照 Figma），旁侧标签文案不变。<br>来源 AC-08: 系统 Role 可配置 Vulnerability Tab、OTA Tab 权限；无权限用户看不到对应 Tab。会上线该功能的租户：雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 需配置上述权限；不上线的租户（如宜家及其关联租户）所有 Role 均不配置。<br>来源 QA扩展: 至少再抽测 1 处非 Filter 勾选（如 Role 权限树），勾选态为主题色 |
| 【Product-Product-List】【UI】勾选框 - 未勾选与禁用态不误用主题色 | /Cloud/Product/Product List | 体验优化P2细节补充 | P2 | 1. Filter 中存在未勾选 Checkbox；若有禁用态 Checkbox 一并观察<br>2. Radio/Switch 是否纳入本 AC **待确认**，本条先验 Checkbox | [1] 观察未勾选态 Checkbox 颜色<br>[2] 若存在禁用态 Checkbox，观察其颜色<br>[3] （可选）记录 Radio/Switch 是否误用勾选主题色，供产品确认 | [1] 未勾选态不呈现勾选主题色填充<br>[2] 禁用态不误用勾选主题色<br>[3] Radio/Switch 范围待确认；发现异常记缺陷/待确认 | 来源 QA扩展: 未勾选态与禁用态不误用勾选主题色（待确认是否含 Radio/Switch） |
| 【Product-Product-List】【UI】列宽与 Version - Product 固定三列、大屏均分及 Prod 最新版 | /Cloud/Product/Product List | 体验优化P2细节补充 | P0 | 1. 已登录可访问 Product 列表<br>2. 准备：有 Prod Version 的产品；仅有 Test 或 Test 比 Prod 更新的产品；可切换/筛选 Module 展示<br>3. 浏览器窗口处于**足以展示全部列**的大屏宽度；可用开发者工具或标尺核对列宽约值 | [1] 打开 Product 列表，测量第一列 / Status / Operation 宽度，观察中间非固定列宽度分配<br>[2] 定位有 Prod Version 的产品，查看 Version 列文案<br>[3] 定位仅 Test、或 Test 新于 Prod 的产品，查看 Version 列<br>[4] 切换或筛选 Module 相关展示，再次查看同一产品 Version 列 | [1] 第一列约 280px、Status 约 160px、Operation 约 64px 固定；大屏下中间列按比例均分剩余宽度（视觉上可宽于固定列）<br>[2] Version 展示 Prod 环境下最新一个版本文案<br>[3] 仍只展示 Prod 最新 Version，不取 Test<br>[4] Version 不随 Module 切换/筛选联动改变 | 来源 AC-04: 用户打开 Product / KMS / PKI / Factory / U-safe / Device History / DAC Report / Account / Group 等大列表时：第一列（通常 Name）固定 280px、Status 固定 160px、Operation 固定 64px；大屏（宽度足以展示全部列）下中间非固定列按比例均分剩余宽度；小屏（宽度不足以展示全部列）下固定三列保持宽度不被挤占，并出现横向滚动以查看其余列。<br>来源 AC-07: 用户查看 Product 列表 Version 列时，应显示该产品 Prod 环境下最新的一个版本（不取 Test），且不随 Module 切换联动变化。 |
| 【Product-Product-List】【UI】Version - 无 Prod Version 展示短横线 | /Cloud/Product/Product List | 体验优化P2细节补充 | P2 | 1. 存在无 Prod Version 的产品（可仅有 Test 或完全无版本） | [1] Product 列表定位该产品 Version 列 | [1] Version 列展示 `-` | 来源 QA扩展: 无 Prod Version 时，Version 列展示 `-` |
| 【Admin-Account】【UI】列宽 - Account 与 Group 固定三列及大屏中间列均分 | /Cloud/Admin/Account | 体验优化P2细节补充 | P1 | 1. 已登录可访问 Account 列表与 Group 列表<br>2. 浏览器处于足以展示全部列的大屏宽度 | [1] 打开 Account 列表，核对固定三列宽度及中间列是否均分剩余宽度<br>[2] 打开 Group 列表，同样核对 | [1] Account：第一列约 280px、Status 约 160px、Operation 约 64px；大屏中间列按比例均分剩余宽度<br>[2] Group 列表同上 | 来源 AC-04: 用户打开 Product / KMS / PKI / Factory / U-safe / Device History / DAC Report / Account / Group 等大列表时：第一列（通常 Name）固定 280px、Status 固定 160px、Operation 固定 64px；大屏（宽度足以展示全部列）下中间非固定列按比例均分剩余宽度；小屏（宽度不足以展示全部列）下固定三列保持宽度不被挤占，并出现横向滚动以查看其余列。 |
| 【KMS-Key-List】【UI】列宽与 Count - KMS/PKI 固定三列、大屏均分及普通文字 Count | /Cloud/KMS/Key List | 体验优化P2细节补充 | P1 | 1. 已登录可访问 KMS Key List 与 PKI List<br>2. PKI 侧可展开至有 Issued Count 数值的节点（如 DAC Template）<br>3. 浏览器处于足以展示全部列的大屏宽度 | [1] 打开 KMS Key List，核对固定三列与中间列均分；观察 Usage Count 列样式<br>[2] 打开 PKI List，核对固定三列与中间列均分；展开树至有 Issued Count 的节点，观察样式 | [1] KMS：第一列约 280px、Status 约 160px、Operation 约 64px；大屏中间列按比例均分剩余宽度；Usage Count 为普通文字，无额外图标与边框<br>[2] PKI：同上固定三列与大屏均分；Issued Count 为普通文字，无额外图标与边框 | 来源 AC-04: 用户打开 Product / KMS / PKI / Factory / U-safe / Device History / DAC Report / Account / Group 等大列表时：第一列（通常 Name）固定 280px、Status 固定 160px、Operation 固定 64px；大屏（宽度足以展示全部列）下中间非固定列按比例均分剩余宽度；小屏（宽度不足以展示全部列）下固定三列保持宽度不被挤占，并出现横向滚动以查看其余列。<br>来源 AC-05: 用户查看 KMS 列表 Usage Count、PKI 列表 Issued Count 时，应为普通文字样式，无额外图标与边框。 |
| 【Ecosystem-Factory-Factory-List】【UI】列宽 - Factory 等大列表固定三列与大屏均分（抽样） | /Cloud/Ecosystem/Factory/Factory List | 体验优化P2细节补充 | P2 | 1. 已登录可访问 Factory / U-safe / Device History / DAC Report 中至少两类列表（抽样）<br>2. 浏览器处于足以展示全部列的大屏宽度 | [1] 打开 Factory List，核对固定三列与中间列均分<br>[2] 再抽测 U-safe List、Device History、DAC Report 中至少一类，同样核对列宽 | [1] Factory：第一列约 280px、Status 约 160px、Operation 约 64px；大屏中间列按比例均分剩余宽度<br>[2] 抽测列表同样符合固定三列 + 大屏均分规则 | 来源 AC-04: 用户打开 Product / KMS / PKI / Factory / U-safe / Device History / DAC Report / Account / Group 等大列表时：第一列（通常 Name）固定 280px、Status 固定 160px、Operation 固定 64px；大屏（宽度足以展示全部列）下中间非固定列按比例均分剩余宽度；小屏（宽度不足以展示全部列）下固定三列保持宽度不被挤占，并出现横向滚动以查看其余列。 |
| 【Product-Product-List】【UI】列宽 - 小屏固定三列不被挤占且横向滚动 | /Cloud/Product/Product List | 体验优化P2细节补充 | P1 | 1. 已登录可访问 Product 列表<br>2. 可用浏览器开发者工具将视口宽度收窄至**不足以展示全部列**（或等价缩小窗口）<br>3. 可用开发者工具测量固定三列宽度 | [1] 大屏下先确认 Product 列表可完整展示各列<br>[2] 将视口收窄至不足以展示全部列，观察是否出现横向滚动条（或可横向滚动容器）<br>[3] 在小屏下测量第一列 / Status / Operation 宽度，并横向滚动查看中间列 | [1] 大屏可完整展示各列（对照）<br>[2] 出现横向滚动，中间列不被压缩挤扁至不可读<br>[3] 固定三列仍约 280px / 160px / 64px，不被挤占；滚动后可查看其余列内容 | 来源 AC-04: 用户打开 Product / KMS / PKI / Factory / U-safe / Device History / DAC Report / Account / Group 等大列表时：第一列（通常 Name）固定 280px、Status 固定 160px、Operation 固定 64px；大屏（宽度足以展示全部列）下中间非固定列按比例均分剩余宽度；小屏（宽度不足以展示全部列）下固定三列保持宽度不被挤占，并出现横向滚动以查看其余列。 |
| 【Admin-Account】【E2E】本人编辑 - Account 列表可 Edit 且隐藏 Role/Notes 并可保存 | /Cloud/Admin/Account | 体验优化P2细节补充 | P0 | 1. 使用普通可登录账号，列表中存在本人行<br>2. 记录当前 Name / Phone 等可改字段值，便于保存后核对 | [1] Account 列表定位本人行 → Operation → Edit<br>[2] 观察抽屉字段：确认无 User Role、Notes；Email 等其余字段逻辑符合现网<br>[3] 修改可编辑字段（如 Name 或 Phone）并保存<br>[4] 关闭后在列表/再次打开 Edit 或详情核对更新 | [1] Edit 可用（亮起），打开编辑抽屉<br>[2] 无 User Role、Notes；其余可编辑字段逻辑不变<br>[3] 保存成功（Toast 按现网/统一成功文案）<br>[4] 非 Role/Notes 字段展示已更新 | 来源 AC-06: 用户编辑本人账号（列表 Edit 或详情/Profile Edit）时，Edit 可用，编辑表单隐藏 User Role 与 Notes，其余可编辑字段逻辑不变。<br>来源 QA扩展: 本人编辑可保存成功后列表/详情展示更新（非 Role/Notes 字段） |
| 【Operation-User(SNB)】【UI】本人编辑 - Account（SNB）列表隐藏 Role/Notes | /Cloud/Operation/User(SNB) | 体验优化P2细节补充 | P1 | 1. 使用可访问 Account（SNB）/ User(SNB) 列表的本人账号<br>2. 列表存在本人行 | [1] 打开 User(SNB) 列表，定位本人行 → Edit<br>[2] 观察编辑抽屉字段集 | [1] Edit 可用并打开抽屉<br>[2] 隐藏 User Role、Notes | 来源 AC-06: 用户编辑本人账号（列表 Edit 或详情/Profile Edit）时，Edit 可用，编辑表单隐藏 User Role 与 Notes，其余可编辑字段逻辑不变。 |
| 【Admin-Account】【UI】本人编辑 - Account 详情 Edit 弹窗隐藏 Role/Notes | /Cloud/Admin/Account | 体验优化P2细节补充 | P1 | 1. 已登录并进入本人 Account 详情 | [1] 点击详情页 Edit icon<br>[2] 观察弹窗字段：User Role、Notes 是否隐藏；Email 等其余字段逻辑 | [1] Edit icon 可用（亮起），打开编辑弹窗<br>[2] 隐藏 User Role、Notes；Email 等其余字段逻辑不变 | 来源 AC-06: 用户编辑本人账号（列表 Edit 或详情/Profile Edit）时，Edit 可用，编辑表单隐藏 User Role 与 Notes，其余可编辑字段逻辑不变。 |
| 【Login-&-Profile-My-Profile】【UI】本人编辑 - Profile Edit 隐藏 Role/Notes | /Cloud/Login & Profile/My Profile | 体验优化P2细节补充 | P1 | 1. 已登录，可进入 My Profile | [1] 进入 My Profile，点击 Edit icon<br>[2] 观察编辑弹窗字段 | [1] Edit icon 可用<br>[2] 弹窗隐藏 User Role、Notes | 来源 AC-06: 用户编辑本人账号（列表 Edit 或详情/Profile Edit）时，Edit 可用，编辑表单隐藏 User Role 与 Notes，其余可编辑字段逻辑不变。 |
| 【Admin-Account】【Functional】非本人编辑 - 仅 System Admin 可 Edit 且可见 Role/Notes | /Cloud/Admin/Account | 体验优化P2细节补充 | P1 | 1. 准备非 System Admin 账号与具备 System Admin role 的管理员账号<br>2. 列表存在非本人（他人）账号行 | [1] 非 System Admin 登录，定位他人行，观察 Edit 状态<br>[2] System Admin 登录，定位同一他人行，点击 Edit<br>[3] 观察管理员编辑他人表单是否含 User Role、Notes | [1] 非 System Admin 对他人行 Edit 置灰（不可用）<br>[2] System Admin 可打开编辑表单<br>[3] 表单仍可见 User Role、Notes | 来源 QA扩展: 非本人行：仅具备 System Admin role 的管理员可 Edit，其余人 Edit 置灰；管理员编辑他人时表单仍可见 User Role、Notes |
| 【Product-OTA】【E2E】OTA/Vulnerability Tab - 无权限隐藏、有权限可见及变更刷新 | /Cloud/Product/OTA | 体验优化P2细节补充 | P0 | 1. 准备：无 Vulnerability 权限用户、无 OTA 权限用户、同时拥有两权限用户（或同一用户通过改权限切换）<br>2. 可进入同一 Product 详情<br>3. 可修改 Role 权限后重新登录或刷新 | [1] 无 Vulnerability Tab Page 权限用户进入 Product 详情，观察 Tab<br>[2] 无 OTA Tab Page 权限用户进入同一 Product 详情，观察 Tab<br>[3] 同时拥有两权限用户进入，分别进入 Vulnerability 与 OTA Tab<br>[4] 变更某用户权限后重新登录/刷新，再次核对该用户 Tab 显隐 | [1] 不展示 Vulnerability Tab<br>[2] 不展示 OTA Tab<br>[3] 两 Tab 均可见且可进入<br>[4] Tab 显隐与最新权限一致 | 来源 AC-08: 系统 Role 可配置 Vulnerability Tab、OTA Tab 权限；无权限用户看不到对应 Tab。会上线该功能的租户：雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 需配置上述权限；不上线的租户（如宜家及其关联租户）所有 Role 均不配置。<br>来源 QA扩展: 权限变更后重新登录/刷新，Tab 显隐与权限一致 |
| 【Operation-Role】【Functional】租户默认配置 - 会上线与不上线租户 Role 权限 | /Cloud/Operation/Role | 体验优化P2细节补充 | P0 | 1. 准备会上线 OTA & Vulnerability 的租户（含雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager）<br>2. 准备不上线租户（如宜家及其关联租户）<br>3. 可查看各 Role 权限树默认/交付配置，并用对应用户验证 Product 详情 Tab | [1] 在会上线租户检查上述 4 类 Role 是否配置 Vulnerability / OTA Tab Page 权限<br>[2] 用会上线租户对应用户进入 Product 详情抽样确认 Tab 可见（按配置）<br>[3] 在不上线租户检查所有 Role 均未配置上述两权限<br>[4] 用不上线租户用户进入 Product 详情，确认看不到两 Tab | [1] 会上线租户指定 Role 默认/交付后具备两权限<br>[2] 对应用户可见相应 Tab（与配置一致）<br>[3] 不上线租户所有 Role 均不配置两权限<br>[4] 对应用户看不到 Vulnerability / OTA Tab | 来源 AC-08: 系统 Role 可配置 Vulnerability Tab、OTA Tab 权限；无权限用户看不到对应 Tab。会上线该功能的租户：雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 需配置上述权限；不上线的租户（如宜家及其关联租户）所有 Role 均不配置。 |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | Account 列表 User Role +n hover | TP-PLUS-01 |
| 2 | Account 详情 Role +n hover | TP-PLUS-02 |
| 3 | Group Linked Product Role +n | TP-PLUS-03 |
| 4 | Product Module +n 浮层 | TP-PLUS-04 |
| 5 | +n 单值/溢出边界 | TP-PLUS-05 |
| 6 | +n 中英文 | TP-PLUS-06 |
| 7 | 成功 Toast 中文 | TP-TOAST-01 |
| 8 | 成功 Toast 英文 | TP-TOAST-02 |
| 9 | Toast 多模块抽测 | TP-TOAST-03 |
| 10 | 特殊 Toast 例外 | TP-TOAST-04 |
| 11 | Filter Checkbox 主题色 | TP-CHK-01 |
| 12 | 表单 Checkbox 主题色 | TP-CHK-02 |
| 13 | Role 树 Checkbox + OTA/Vulnerability 节点可配 | TP-CHK-03, TP-PERM-01 |
| 14 | 未勾选/禁用态 | TP-CHK-04 |
| 15 | Product 列宽（大屏）+ Prod Version 规则 | TP-COL-01, TP-VER-01, TP-VER-02, TP-VER-03 |
| 16 | 无 Prod Version 显示 `-` | TP-VER-04 |
| 17 | Account / Group 列宽（大屏） | TP-COL-02 |
| 18 | KMS/PKI 列宽（大屏）+ Count 普通文字 | TP-COL-03, TP-CNT-01, TP-CNT-02 |
| 19 | Factory 等列宽抽样（大屏） | TP-COL-04 |
| 20 | 小屏固定三列 + 横向滚动 | TP-COL-05 |
| 21 | Account 列表本人编辑并保存 | TP-SELF-01, TP-SELF-05 |
| 22 | Account（SNB）本人编辑 | TP-SELF-02 |
| 23 | Account 详情本人编辑 | TP-SELF-03 |
| 24 | Profile 本人编辑 | TP-SELF-04 |
| 25 | 非本人 Edit 权限与 Role/Notes | TP-SELF-06 |
| 26 | Tab 显隐与权限变更刷新 | TP-PERM-02, TP-PERM-03, TP-PERM-04, TP-PERM-07 |
| 27 | 会上线/不上线租户默认配置 | TP-PERM-05, TP-PERM-06 |

**说明**：**27** 条用例覆盖全部 **38** 条 TP（每条 TP 至少命中 1 次）。

## 待确认

- [ ] 勾选框「所有」是否含 Radio、Switch、树半选；主题色 token/hex 是否仅以 Figma 为准
- [ ] 第一列是否一律 Name；Operation 64px 是否仅放 ⋮
- [ ] 本人编辑：抽屉 vs 弹窗字段集是否完全一致
- [ ] 同为 Prod 时「最新」排序口径（创建时间 / 发布时间 / 版本号）
