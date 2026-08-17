# E2-S01 模块入口与导航收敛 — 功能测试用例

> 来源：`docs/sprints/OBIS-20260810-20260821/features/e2-s01-module-nav-convergence/acceptance.md`  
> 飞书 Story：[7067952077](https://project.feishu.cn/obis/userstory/detail/7067952077)  
> **变更类型**：Hybrid（主 UI/UX，次 Logic：整产品取数）→ 用例以 `【UI】` 为主，角色/取数/忽略字段用 `【Functional】`  
> 用例数：12（P0 × 9，P1 × 2，P2 × 1）  
> UI 参考：`baseline/screenshots/`（Overview / Assets / Version Details / Create Version）  
> 入口：Product → 目标产品详情；页签 Overview / Assets / Version；Create Version 为创建页签；Version 行链入 Version Details  
> 用例名称：`【{模块 slug}】【{UI|Functional|E2E}】{子功能} - {描述}`  
> 备注约定：来自 AC 写 `来源 AC-F01-xx: {AC 原文}`；否则 `来源 需求描述:` / `来源 QA扩展:`  
> 标签：`模块入口与导航收敛`（禁止写入 TP/AC 编号）

### 场景与 TP 覆盖

| 用例场景 | 覆盖 TP |
|----------|---------|
| Overview Assets 八卡收敛与首屏无闪现 | TP-OV-01～04、TP-FLASH-01、TP-ENT-02 |
| Create Version 无切换条与分区导航 | TP-CV-01～06 |
| Assets 页分区导航与行集 | TP-AST-01～04 |
| Version Details 无多 Module UI | TP-VD-01～03、TP-ENT-01 |
| 四页入口清除总检 | TP-ENT-01、TP-ENT-02 |
| 英文界面收敛 | TP-I18N-01、TP-I18N-02、TP-VD-06 |
| 不同角色呈现一致 | TP-ROLE-01 |
| 模块字段静默忽略 | TP-IGN-01 |
| Create Version 其余未误改 | TP-CV-07、TP-ENT-03 |
| 首屏请求/性能（定性） | TP-PERF-01 |
| Module-scoped 副标题不阻断（边界） | TP-OOS-01、TP-AST-05（列集抽检） |

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Product-Overview】【UI】Assets 分区 - 无模块切换条且八卡呈现 | /Cloud/Product/Overview | 模块入口与导航收敛 | P0 | 1. 已登录且可查看目标产品<br>2. 产品下已有资产数据（可对照 baseline 八卡）<br>3. 已进入该产品详情 Overview | [1] 定位 Overview 页 **Assets** 分区（文案含 Chip Credentials…）<br>[2] 观察 Assets 分区顶部/卡片上方是否存在模块切换条、Module Tab 或 Module 下拉<br>[3] 清点汇总卡数量与标题（Chip Config / Keys / Certificates / Firmware / Matter Config / Factory Data / General File / Programming Station Software Package）<br>[4] 观察 Assets 与下方 Production Version 区块衔接处是否有大块空白<br>[5] 硬刷新 Overview，观察首屏 Assets 区域是否先出现切换条再消失 | [1] Assets 分区可见<br>[2] **不渲染**模块切换条及任何 Module 选择控件<br>[3] 呈现 **8** 张汇总卡，构成与顺序符合参考图；统计口径可与改前对照<br>[4] 上下内容收拢衔接，无无内容空白带<br>[5] 首屏直接呈收敛态，无切换条闪现 | 来源 AC-F01-01: 用户进入产品详情 Overview 页 Assets 分区时，分区内不渲染模块切换条，分区只呈现 8 张资产汇总卡。<br>来源 AC-F01-03: 上述两处切换条移除后，其上下相邻内容应正常收拢衔接，不留出无内容的空白区域。<br>来源 AC-F01-04: Overview 页 Assets 分区渲染后，8 张汇总卡的构成、顺序与每张卡的统计口径应与改动前一致，卡片位置正确。<br>来源 AC-F01-09: …Overview 页 Assets 分区 8 张汇总卡应按整个产品汇总。<br>来源 AC-F01-10: 改按整个产品取数后，汇总卡计数与各分区行集的呈现应与改动前一致…<br>来源 AC-F01-14: 页面首次渲染应直接以收敛后状态呈现，不出现模块切换条或分区导航标题行先显示再消失的闪现。 |
| 【Product-Version】【UI】Create Version - 无模块切换条与分区导航标题行 | /Cloud/Product/Version | 模块入口与导航收敛 | P0 | 1. 已登录且可创建 Version<br>2. 已进入目标产品详情<br>3. 可打开 Create Version 页（参考图：Basic Info + Chip Config + 右侧索引） | [1] 进入 **Create Version** 页<br>[2] 观察页顶 Basic Info 上方/表单顶部是否有模块切换条<br>[3] 观察右侧分区导航顶部是否显示当前模块名标题行；索引是否从 Chip Config / Keys… 起列<br>[4] 依次点击右侧索引 Keys、Certificates（或可见项），观察主区滚动与激活态<br>[5] 上下滚动主区，观察索引激活态是否跟随<br>[6] 查看 Chip Config / Keys 等分区是否直接展示资产内容（无「先选模块」步骤） | [1] Create Version 打开，可见 Basic Info（Version Name / Region 等）与分区内容<br>[2] **不渲染**模块切换条；顶部与 Basic Info 衔接无空白带<br>[3] **不渲染**模块名标题行；索引项完整（Chip Config、Keys、Certificates、Firmware、Matter Config、Factory Data、General File 等），数量/顺序符合参考图<br>[4] 点击可滚动定位到对应分区<br>[5] 激活态随滚动更新<br>[6] 各分区直接呈现该产品资产范围，无 Module 过滤控件 | 来源 AC-F01-02: 用户进入 Create Version 页时，页面顶部不渲染模块切换条。<br>来源 AC-F01-03: 上述两处切换条移除后，其上下相邻内容应正常收拢衔接，不留出无内容的空白区域。<br>来源 AC-F01-06: 用户进入 Assets 页或 Create Version 页时，分区导航不渲染顶部标题行（改动前显示当前模块名）。<br>来源 AC-F01-07: 标题行移除后，其下各分区索引项应完整渲染，数量与顺序不变，点击可滚动定位到对应分区，激活态随滚动更新。<br>来源 AC-F01-08: 标题行移除后，分区导航整体不留出无内容的空白区域，索引项正常滚动。<br>来源 AC-F01-09: …Assets 页与 Create Version 页各分区应直接呈现该产品下全部资产（不按模块过滤）… |
| 【Product-Assets】【UI】Assets 页 - 分区导航无模块标题且可定位 | /Cloud/Product/Assets | 模块入口与导航收敛 | P0 | 1. 已登录且可查看产品 Assets<br>2. 已进入目标产品 **Assets** 页（参考图：右侧 Chip Config…Programming） | [1] 观察右侧分区导航顶部是否有模块名标题行或「当前模块」展示<br>[2] 核对索引项：Chip Config、Keys、Certificates、Firmware、Matter Config、Factory Data、General File、Programming…<br>[3] 点击 Keys、Certificates 等索引，观察滚动定位与激活高亮<br>[4] 查看 Keys / Certificates 分区表格是否直接展示行数据（无模块切换后才加载的步骤） | [1] **不渲染**模块名标题行；导航顶部直接为分区索引<br>[2] 索引完整，顺序与参考图一致，导航区无空白带<br>[3] 点击可定位；激活态随滚动更新<br>[4] 行集按整产品呈现，界面无 Module 过滤/切换控件 | 来源 AC-F01-06: 用户进入 Assets 页或 Create Version 页时，分区导航不渲染顶部标题行（改动前显示当前模块名）。<br>来源 AC-F01-07: 标题行移除后，其下各分区索引项应完整渲染，数量与顺序不变，点击可滚动定位到对应分区，激活态随滚动更新。<br>来源 AC-F01-08: 标题行移除后，分区导航整体不留出无内容的空白区域，索引项正常滚动。<br>来源 AC-F01-09: …Assets 页与 Create Version 页各分区应直接呈现该产品下全部资产（不按模块过滤）… |
| 【Product-Version】【UI】Version Details - 无多 Module UI 与入口 | /Cloud/Product/Version | 模块入口与导航收敛 | P0 | 1. 已登录且可查看 Version<br>2. Overview 或 Version 列表中存在可点开的 Version（如 Version_Module 1，**名称为数据不视为模块入口**） | [1] 打开该 Version 的 **Version Details**<br>[2] 观察页头、Basic Info 上方、内容区是否存在模块切换条 / Module Tab / Module 下拉<br>[3] 观察右侧分区导航：是否有模块名标题行；索引是否为 Chip Config / Keys…（无「选模块」层）<br>[4] 检查面包屑（Product / 产品名 / Version 名）、Actions 菜单、可展开区域是否含「进入其他模块 / 切换模块」类入口<br>[5] 硬刷新详情页，观察是否闪现模块切换 UI | [1] 详情页打开，可见 Basic Info、Chip Config 等<br>[2] **不渲染**任何多 Module 选择 UI<br>[3] 无模块名标题行与「当前模块」展示；索引为资产分区列表<br>[4] 面包屑仅为产品→版本层级，**无模块层级**；Actions/展开区无模块切换入口<br>[5] 首屏直接无 Module UI，无闪现 | 来源 AC-F01-05: 模块切换条移除后，界面不存在任何其他可进入或切换模块层级的入口（含菜单项、下拉项、链接、面包屑层级与可展开区域）。<br>来源 AC-F01-06: 用户进入 Assets 页或 Create Version 页时，分区导航不渲染顶部标题行…<br>来源 QA扩展: Version Details 页不得出现多 Module UI 与模块入口 |
| 【Product-Overview】【UI】四页巡检 - 无模块层级入口且不可勾出 | /Cloud/Product/Overview | 模块入口与导航收敛 | P0 | 1. 已登录<br>2. 同一产品可打开 Overview、Assets、Create Version、Version Details | [1] 在 Overview 巡视菜单/下拉/链接/面包屑/展开区，查找模块层级入口<br>[2] 在 Assets 重复巡视<br>[3] 在 Create Version 重复巡视<br>[4] 在 Version Details 重复巡视<br>[5] 尝试通过勾选、展开、切换类控件「找回」模块切换条或模块标题行 | [1]～[4] 四处均**无可进入或切换模块层级**的入口<br>[5] 被隐藏元素为不渲染，无法勾出/展开再现 | 来源 AC-F01-05: 模块切换条移除后，界面不存在任何其他可进入或切换模块层级的入口（含菜单项、下拉项、链接、面包屑层级与可展开区域）。 |
| 【Product-Overview】【UI】中英文 - 收敛行为一致 | /Cloud/Product/Overview | 模块入口与导航收敛 | P0 | 1. 环境可切换中/英文<br>2. 已登录并可打开目标产品相关页 | [1] 英文界面下打开 Overview Assets、Assets、Create Version、Version Details<br>[2] 对照中文界面，检查模块切换条与分区导航模块名标题行是否出现<br>[3] 切回中文再快速确认上述页面仍收敛 | [1] 四页可正常打开<br>[2] 英文下同样**不出现**模块切换条与分区导航模块名标题行<br>[3] 中文保持收敛，中英行为一致 | 来源 AC-F01-11: 中文与英文界面下，收敛行为一致，均不出现模块切换条与分区导航标题行。 |
| 【Product-Overview】【Functional】不同角色 - 收敛呈现一致无开关 | /Cloud/Product/Overview | 模块入口与导航收敛 | P0 | 1. 准备至少 2 个权限不同的账号（均可访问同一产品）<br>2. 账号 A 已确认四页为收敛态 | [1] 使用账号 B 登录，打开同一产品 Overview / Assets / Create Version / Version Details<br>[2] 对照账号 A：有无模块切换条、模块名标题行、模块入口、界面开关 | [1] 四页可打开<br>[2] 与账号 A **呈现一致**；无角色分支差异；界面**无**「显示模块层级」类开关 | 来源 AC-F01-13: 任意角色用户进入上述页面时，收敛行为一致，不因角色、权限点或租户不同而出现差异，界面不提供开关。 |
| 【Product-Assets】【Functional】模块字段 - 界面静默忽略 | /Cloud/Product/Assets | 模块入口与导航收敛 | P0 | 1. 已登录<br>2. 开发者工具可用；开发可指出仍返回模块字段的接口（或接口响应中可见 module 相关字段） | [1] 打开 Assets（或 Overview / Create Version），打开网络面板并刷新<br>[2] 定位仍带模块字段的响应（由开发指认或筛选）<br>[3] 同时观察页面：是否渲染模块字段、是否报错、是否弹出与模块相关的提示 | [1] 页面加载成功<br>[2] 响应中可观察到模块相关字段仍存在（若环境确有）<br>[3] 界面**忽略**该字段：不渲染、不报错、不出提示 | 来源 AC-F01-12: 后端返回数据仍带模块字段时，界面应忽略该字段，不渲染、不报错、不出提示。 |
| 【Product-Version】【UI】Create Version - 基本信息与分区未误改 | /Cloud/Product/Version | 模块入口与导航收敛 | P1 | 1. 已打开 Create Version<br>2. 参考图：Basic Info 含 Version Name*、Region、Copy from History Version、Notes；底栏 Cancel / Create | [1] 核对 Basic Info 字段是否齐全可编辑<br>[2] 核对 Chip Config 表列（Label/Type/Key/Value）及数据行可展示<br>[3] 核对底栏 Cancel、Create 按钮可见<br>[4] 返回产品详情，核对页签 Overview / Assets / Version / Batch / Device / Audit / Member 仍在 | [1] Basic Info 字段与参考图一致，未被移除<br>[2] Chip Config 及后续分区表格正常<br>[3] Cancel / Create 可用（本步不强制提交）<br>[4] 产品详情页签条本身未改动 | 来源 需求描述: 本期不动 Create Version 页除切换条与分区导航标题行以外的任何部分<br>来源 需求描述: 产品详情的页签条本身不动 |
| 【Product-Overview】【Functional】首屏加载 - 不劣于改前（定性） | /Cloud/Product/Overview | 模块入口与导航收敛 | P1 | 1. 开发者工具 Network 可用<br>2. （建议）有改前请求条数或加载体感基线说明 | [1] 硬刷新 Overview，记录首屏相关请求大致条数与是否明显变慢<br>[2] 对 Assets、Create Version 各硬刷新一次并对照<br>[3] 与改前基线或开发说明对比是否引入额外首屏请求 | [1]～[2] 页面可正常完成首屏<br>[3] 未明显引入额外首屏请求；加载体感不劣于改前（量化方式见待确认） | 来源 AC-F01-15: 本改动不引入额外接口请求；Overview、Assets、Create Version 首屏加载时间不劣于改动前。 |
| 【Product-Assets】【UI】副标题 Module-scoped - 不阻断本 Story | /Cloud/Product/Assets | 模块入口与导航收敛 | P2 | 1. 已打开 Assets 页<br>2. Keys / Certificates 分区可见（参考图副标题含 Module-scoped） | [1] 查看 Keys 分区副标题是否仍含 Module-scoped 类措辞<br>[2] 确认本 Story 验收结论不依赖该副标题已改文案 | [1] 若仍含 Module-scoped：**记录**即可<br>[2] **不**因副标题未改而判定本 Story 失败（改文案属另 Story） | 来源 需求描述: Assets 页分区副标题 Module-scoped 文案改动另 Story 认领，本 Story 不动 |
| 【Product-Assets】【UI】Assets 列集抽检 - 与改前一致 | /Cloud/Product/Assets | 模块入口与导航收敛 | P1 | 1. 已打开 Assets<br>2. Keys 区有至少一行数据（参考：Name/Type/Tag/Update Time/Notes） | [1] 核对 Keys 列表列名与顺序<br>[2] 核对 Chip Config 列表列名（Label/Type/Key/Value） | [1] Keys 列集与参考图/改前一致<br>[2] Chip Config 列集一致；本期仅取数范围变化，列本身未改 | 来源 需求描述: Assets 各分区列集、列序、单元格取值与行菜单不变；本期只改取数范围 |

---

## 待确认（执行时）

- [ ] AC-F01-15 性能对比的量化基线（请求条数或耗时）如何采集
- [ ] Version 名称含 `Module`（如 Version_Module 1）仅为历史命名，执行时勿误判为「模块层级入口」
- [ ] Create Batch 页不在本 Story 主改范围；截图仅作环境旁证
