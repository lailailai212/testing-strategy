# Sprint `OBIS-20260727-20260807` 提测演示审核 Checklist

> 用于开发**提测演示**环节的现场审核：开发按条演示，QA / 产品逐条判定「通过 / 不通过」，据此决定本 Sprint 三个 Story 是否准入正式测试。
>
> 依据文档：
> - [`ux-p2-member-unify` acceptance](../../sprints/OBIS-20260727-20260807/features/ux-p2-member-unify/acceptance.md)（AC-01～08，43 测试点）
> - [`ux-p2-detail-supplement` acceptance](../../sprints/OBIS-20260727-20260807/features/ux-p2-detail-supplement/acceptance.md)（AC-01～08，38 测试点）
> - [`ux-p2-audit-unify` acceptance](../../sprints/OBIS-20260727-20260807/features/ux-p2-audit-unify/acceptance.md)（AC-01～06，22 测试点）
>
> 账号 / 资源代号（`A1`、`KEY-1`、`t1` 等）见 [`data-prep.md`](data-prep.md) 与 [`config/conventions.md`](../../../config/conventions.md)。

## 一、审核规则

| 项 | 约定 |
|---|---|
| 演示方 | 开发（每个 Story 由主开发操作，QA 不代操作） |
| 审核方 | QA 主测 + 产品；结论由 QA 主测记录 |
| 判定粒度 | 每条演示项独立判定，**不合并打包过** |
| 准入门槛 | 该 Story 全部 **P0 演示项通过** 才准入测试 |
| P0 不通过 | 该 Story **整体打回**，修复后重新演示（可只补演示未通过项） |
| P1 不通过 | 记为已知缺陷，不阻塞准入，进测试后按缺陷跟踪 |
| 演示无法进行 | 因数据 / 环境缺失无法演示的条目记「阻塞」，不计入通过，须在准入前补齐 |
| 时长建议 | 三个 Story 各 25～30 分钟，超时未演完的部分按「阻塞」处理 |

**结论栏填写**：`P` 通过 / `F` 不通过 / `B` 阻塞（无法演示）。

## 二、演示前置条件（开场前 5 分钟确认，缺项则相应 Story 顺延）

- [ ] 三个 Story 的功能均已部署到演示环境，且版本号与提测单一致
- [ ] 演示环境可在**中 / 英文之间切换**（Transfer 弹窗文案、Toast、`+n` hover 均需中英文各看一次）
- [ ] 开发已准备好 Transfer 演示所需资源：`KEY-1`（目标已在 Member）、`KEY-2`（目标不在 Member）、`CERT-1`、`FAC-1`、`FAC-2`
- [ ] 开发已准备好可删账号：至少 1 个命中 Admin/Owner 身份（演示拦截）、1 个不命中（演示直删）
- [ ] 六处 Audit（Group / Account / Profile / KMS / PKI / Product）均有日志数据
- [ ] 浏览器开发者工具可用（列宽 280 / 160 / 64 px 需现场量）
- [ ] Figma node **15959-188662** 可打开（勾选框主题色对照）
- [ ] 已归档 / 已锁定 / 已删除 / 已销毁四类状态资源是否具备 —— **若无，Member Story 的 D-MEM-14 记阻塞**

---

## 三、Story 1 · 【体验优化P2】Member 功能统一

> 飞书 Story [#7042512337](https://project.feishu.cn/obis/userstory/detail/7042512337)　│　共 20 条：P0 16 条，P1 4 条
> 演示顺序按「列表展示 → 弹窗规格 → 移交结果 → 删除移交」，**Transfer 与删除为不可逆操作，放在本 Story 最后连续演示**。

### 3.1 KMS / PKI Member 列表

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-MEM-01 | 打开 KMS Key 详情 → Member Tab | 默认列为 Name、Role、Permission、Organization、Status，且 **Organization 紧跟在 Permission 之后** | AC-01 / TP-KMS-L01 | P0 | ☐ |
| D-MEM-02 | hover 某成员 Permission 列的 `+n` | 默认只展示 1 个权限 Tag；hover 后小窗列出该成员**全部** Permission | AC-01 / TP-KMS-L02 | P0 | ☐ |
| D-MEM-03 | 用 Admin 本人（`A3`）打开 Admin 行三点菜单 | 菜单项**只有** Transfer Admin，无其它操作项，且可点击 | AC-01 / TP-KMS-L03、L04 | P0 | ☐ |
| D-MEM-04 | 换非 Admin 用户（`A2`）查看同一 Admin 行 | Transfer Admin 置灰不可点，hover 提示「No Permission / 无权限」 | AC-01 / TP-KMS-L05 | P0 | ☐ |
| D-MEM-05 | 打开 PKI 资源详情 → Member Tab，重复 D-MEM-01～04 | 列与顺序、菜单与置灰行为**与 KMS 完全一致** | AC-01 / TP-PKI-L01、L02 | P0 | ☐ |
| D-MEM-06 | KMS Member 工具栏 | Filter、Columns、Refresh、Sort、`+ Add` 入口均可达（本次不改能力，只看回归） | 需求描述 / TP-KMS-L07 | P1 | ☐ |

### 3.2 Factory Member 列表

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-MEM-07 | 打开 Factory → Member 列表 | 默认列**仅** Name、Role、Status；Organization / Operator / Join Time **默认不展示** | AC-04 / TP-FAC-L01 | P0 | ☐ |
| D-MEM-08 | Admin 本人打开 Admin 行三点菜单 | 菜单为 Reset Password + Transfer Admin，**无 Remove**；他人查看时两项均置灰并 hover「No Permission / 无权限」 | AC-04 / TP-FAC-L03、L04 | P0 | ☐ |
| D-MEM-09 | 通过 Columns 打开三个隐藏列 | Organization / Operator / Join Time 打开后正常展示 | AC-04 / TP-FAC-L02 | P1 | ☐ |

### 3.3 Group Member

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-MEM-10 | 打开含 Admin 行与非 Admin 行的 Group Member 列表 | Admin 用户行**不展示**三点菜单；非 Admin 行仍保留菜单；全表**无任何 Transfer 入口** | AC-06 / TP-GRP-01～03 | P0 | ☐ |

### 3.4 Transfer Admin 弹窗与移交结果（不可逆）

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-MEM-11 | KMS 打开 Transfer 弹窗，不选目标直接 Confirm | 标题「Transfer KMS Admin / 转移密钥管理员」；字段 Select KMS Admin 必填带 `*`；Placeholder「Please Select / 请选择」；报错「KMS Admin is required / 密钥管理员是必填项」；**弹窗不关闭、不移交**；下拉仅同租户其他 Active 用户邮箱，不含当前 Admin | AC-02 / TP-KMS-T01～T03 | P0 | ☐ |
| D-MEM-12 | KMS 对 `KEY-1`（目标已在 Member）与 `KEY-2`（目标不在 Member）各完成一次成功移交，**中英文各一次** | 已在列表者 Role→Admin 并被授予全部权限点；不在列表者新增为 Admin 且全部权限点；**原 Admin 仍在列表**，Role→Normal Member 且权限点不变；Toast「操作成功 / Operation Successful」，弹窗关闭列表刷新 | AC-02 / TP-KMS-T04～T06、T08 | P0 | ☐ |
| D-MEM-13 | PKI 与 Factory 各完成一次 Transfer | PKI：标题与报错为 PKI 文案（Certificate Admin），目标→Admin+全部权限点，原 Admin→Normal Member；Factory：目标→**Factory Admin**，原 Admin→**Factory Manager**；两者 Toast 均成功 | AC-03、AC-05 / TP-PKI-T01～T02、TP-FAC-T01～T04 | P0 | ☐ |
| D-MEM-14 | 任一 Transfer 弹窗点 Cancel / 右上角关闭 / 点蒙层 | Cancel 与关闭均不执行移交；**点蒙层不关闭弹窗** | 需求描述 / TP-KMS-T07 等 | P1 | ☐ |

### 3.5 Account 删除与批量移交（不可逆）

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-MEM-15 | 删除一个命中 Product Owner / KMS·PKI·Factory Admin 的账号 | **不可直接删除**，弹出 Confirm Action；标题「Confirm Action / 确认操作」中英文正确；Target Admin 必填带 `*`，Placeholder「Please Select / 请选择」；未选 Confirm 报错「Target Admin is Required / 目标管理员是必填项」；下拉仅同租户其他 Active 邮箱 | AC-08 / TP-ACC-D01、D02、D05 | P0 | ☐ |
| D-MEM-16 | 查看该弹窗内的资源清单 | 按 Product / KMS / PKI / Factory **分卡片**展示，卡片显示 `Resource / 资源：n`，hover 展示全部资源名；**数量为 0 的类型不展示卡片** | AC-08 / TP-ACC-D03 | P0 | ☐ |
| D-MEM-17 | 说明并演示资源状态纳入范围 | 已归档、已锁定资源**纳入**校验；已删除、已销毁**不纳入**（不因其单独弹批量转移窗）<br>无四类状态资源时本条记「B 阻塞」，并由开发口头说明实现逻辑 | AC-08 / TP-ACC-D04 | P0 | ☐ |
| D-MEM-18 | 选择 Target Admin 并 Confirm | 命中的资源 Admin **全部**移交给目标；用户被删除；Toast 成功；目标用户在各资源 Member 中新增或刷新 Role 与权限 | AC-08 / TP-ACC-D06 | P0 | ☐ |
| D-MEM-19 | 打开该用户此前所属的 Product → Member 列表并刷新 | 列表中**不可见**该用户，且**无 Name/Status 为 `-` 的空壳残留行**（对照 ref-08 问题现状） | AC-07 / TP-PRD-01、D02 | P0 | ☐ |
| D-MEM-20 | 删除一个无任何 Admin/Owner 身份的账号；并在 Account（SNB）侧重复一次拦截删除 | 无身份者按现网**直接删除**，不弹批量转移窗；Account（SNB）的拦截、弹窗与移交删除行为与 Account **一致** | QA扩展 / TP-ACC-D08、D09 | P1 | ☐ |

**Story 1 结论**：☐ 准入　☐ 打回（不通过项：____________）　☐ 有条件准入（阻塞项：____________）

---

## 四、Story 2 · 【体验优化P2】Audit 功能统一

> 飞书 Story [#7029049092](https://project.feishu.cn/obis/userstory/detail/7029049092)　│　共 13 条：P0 11 条，P1 2 条
> 全部为只读演示。**先把 Group 作为基准演完，再演其余五处的一致性**，否则无对照参照。

### 4.1 Group Audit（基准）

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-AUD-01 | 打开 Group 详情 → Audit | 默认列为 Operator、Organization、Operation Type、Operation Time；**Operation Details 默认不展示** | AC-01 / TP-AUD-G01 | P0 | ☐ |
| D-AUD-02 | hover Operator 单元格的邮箱 icon 并复制 | Operator 展示头像 + Name + 邮箱 icon；hover 出完整邮箱与复制按钮，**复制成功**（现场粘贴验证） | AC-01 / TP-AUD-G02 | P0 | ☐ |
| D-AUD-03 | 查看 Organization 与 Operation Time 列 | Organization 为操作人所属**租户简称**；Operation Time 精确到年月日时分秒；单元格溢出时 hover 可见全文 | AC-01 / TP-AUD-G03、G04 | P0 | ☐ |
| D-AUD-04 | 展开 Filter 面板 | 含 Operator Name、Operator Email、Organization 三个输入框，Placeholder 为「Please Enter / 请输入」；含 Operation Time 范围选择 | AC-02 / TP-AUD-G05 | P0 | ☐ |
| D-AUD-05 | 用同一天作为起止日期筛选 | Start date 按 **00:00:00** 生效、End date 按 **23:59:59** 生效（用当日边界附近的日志验证） | AC-02 / TP-AUD-G06 | P0 | ☐ |
| D-AUD-06 | 打开 Columns 配置 | Operator、Operation Type **不可隐藏且不可拖拽换序**；Organization、Operation Time 可隐藏可恢复 | AC-03 / TP-AUD-G08、G10 | P0 | ☐ |
| D-AUD-07 | 勾选开启 Operation Details | 该列出现在 **Operation Type 之后**，内容为原 Operation 长文案格式 | AC-03 / TP-AUD-G09 | P0 | ☐ |
| D-AUD-08 | 现场制造一条操作后点 Refresh，并切换 Sort | Refresh 后新日志出现；默认按 Operation Time **倒序**；可切正序；**无其它 Sort 维度** | AC-04 / TP-AUD-G11、G12 | P0 | ☐ |
| D-AUD-09 | 按姓名 / 邮箱 / 组织分别筛选一次，并筛一个无匹配值 | 能筛出匹配行；无匹配时空态展示合理 | AC-02 / TP-AUD-G07 | P1 | ☐ |

### 4.2 其余五处一致性

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-AUD-10 | 依次打开 Account 详情 Audit、My Profile Audit | 默认列、Operator hover、Organization、Filter / Columns / Sort **与 Group 基准一致** | AC-05 / TP-AUD-A01、A02 | P0 | ☐ |
| D-AUD-11 | 打开 PKI 资源详情 Audit、Product 详情 Audit | 与基准一致；且 **Filter 内不出现 KMS 独有的 Operation Type 筛选项** | AC-05 / TP-AUD-P01～P03 | P0 | ☐ |
| D-AUD-12 | 打开 KMS Key 详情 Audit → 展开 Filter → 用 Operation Type 筛选 | 默认列 / Columns / Sort / Refresh 同 Group；Filter 面板在 **Organization 之后**额外提供 Operation Type；筛选后列表仅保留匹配类型 | AC-06 / TP-AUD-K01～K03 | P0 | ☐ |
| D-AUD-13 | KMS Audit 开启 Operation Details | 默认隐藏，开启后可见，位置同基准 | AC-01 / TP-AUD-K04 | P1 | ☐ |

**现场需产品答复**（属本 Story 待确认项，演示时一并定稿）：

- [ ] KMS Filter 的 Operation Type 是单选 / 多选 / 输入？可选值来源是什么？
- [ ] Organization Filter 是否模糊匹配？操作人无组织时如何展示与筛选？
- [ ] 默认列顺序是否固定为 Operator → Organization → Operation Type →（Details）→ Operation Time？
- [ ] Profile 与 Account Audit 是否共用同一组件（影响回归范围）？

**Story 2 结论**：☐ 准入　☐ 打回（不通过项：____________）　☐ 有条件准入（阻塞项：____________）

---

## 五、Story 3 · 【体验优化P2】细节补充

> 飞书 Story [#7051514356](https://project.feishu.cn/obis/userstory/detail/7051514356)　│　共 16 条：P0 13 条，P1 3 条
> 本 Story 为多点位散状改动，**演示重点是「改到了哪些点位」而非单点深挖**；列宽与主题色需现场取证（开发者工具 / Figma）。

### 5.1 `+n` hover 与成功 Toast

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-DTL-01 | hover Account 列表 User Role 的 `+n`、Account 详情 Role 的 `+n` | 小窗展示被折叠的**全部** Role | AC-01 / TP-PLUS-01、02 | P0 | ☐ |
| D-DTL-02 | hover Group 详情 Linked Product 的 Role `+n`（如 `Member +2`） | 小窗展示其余角色全文 | AC-01 / TP-PLUS-03 | P0 | ☐ |
| D-DTL-03 | hover Product 列表 Module 列的 `+n`（选溢出项 ≥ 6 的产品） | 浮层标题为 `Module :`，Tag 列出全部溢出项，过多时**浮层可滚动** | AC-01 / TP-PLUS-04 | P1 | ☐ |
| D-DTL-04 | 中文环境触发任一成功操作，再切英文重复 | 中文 Toast「操作成功」，英文「Operation Successful」（**不是 Operation success**）；样式为绿勾 + 浅绿底提示条 | AC-02 / TP-TOAST-01、02 | P0 | ☐ |
| D-DTL-05 | 再抽 2 个不同模块的成功操作 | Toast 文案与样式一致 | QA扩展 / TP-TOAST-03 | P1 | ☐ |

### 5.2 视觉规格（需现场取证）

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-DTL-06 | 勾选 Filter 内 Checkbox 与表单 / 下拉内 Checkbox，对照 Figma node 15959-188662 | 勾选态颜色为**主题色**且与 Figma 一致；旁侧标签文案不变 | AC-03 / TP-CHK-01、02 | P0 | ☐ |
| D-DTL-07 | 用开发者工具量 Product List、Account List、Group List 的列宽 | 第一列 **280px**、Status **160px**、Operation **64px**，其余列平均分布 | AC-04 / TP-COL-01、02 | P0 | ☐ |
| D-DTL-08 | 同上量 KMS List、PKI List | 三列固定宽度同上 | AC-04 / TP-COL-03 | P0 | ☐ |
| D-DTL-09 | 查看 KMS 列表 Usage Count、PKI 列表 Issued Count（树展开到有值节点） | 均为**普通文字样式**，无额外图标与边框 | AC-05 / TP-CNT-01、02 | P0 | ☐ |

### 5.3 本人编辑与 Product Version

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-DTL-10 | 在 Account 列表与 Account（SNB）列表操作**本人行** → Edit | Edit 可用；抽屉内**无 User Role、无 Notes**，其余字段逻辑不变 | AC-06 / TP-SELF-01、02 | P0 | ☐ |
| D-DTL-11 | 打开本人 Account 详情、My Profile → Edit icon | 弹窗同样隐藏 User Role 与 Notes；修改一个普通字段可保存成功并回显 | AC-06 / TP-SELF-03、04、05 | P0 | ☐ |
| D-DTL-12 | 用 System Admin 与普通用户分别操作**他人行** | 仅 System Admin 可 Edit（其余人置灰）；管理员编辑他人时表单**仍可见** User Role 与 Notes | QA扩展 / TP-SELF-06 | P1 | ☐ |
| D-DTL-13 | 查看 Product 列表 Version 列，覆盖三种产品：有多个 Prod 版本 / Test 比 Prod 更新 / 无 Prod 版本 | 展示 **Prod 环境最新一个**版本；Test 更新时**仍不取 Test**；无 Prod 时展示 `-`；切换或筛选 Module 时 Version **不联动变化** | AC-07 / TP-VER-01～04 | P0 | ☐ |

### 5.4 OTA / Vulnerability 权限

| # | 演示内容 | 审核判据 | 依据 | 级别 | 结论 |
|---|---|---|---|---|---|
| D-DTL-14 | 打开 Role 权限树 | 出现 **Vulnerability Tab Page / 漏洞 Tab 页面**、**OTA Tab Page / OTA Tab 页面** 两个节点，可勾选配置 | AC-08 / TP-PERM-01 | P0 | ☐ |
| D-DTL-15 | 用无 Vulnerability 权限、无 OTA 权限、两者都有的三类用户分别打开 Product 详情；并演示改权限后重登 | 无权限者对应 Tab **不展示**；两权限齐备者两 Tab 可见且可进入；改权限并重新登录 / 刷新后显隐与最新权限一致 | AC-08 / TP-PERM-02～04、07 | P0 | ☐ |
| D-DTL-16 | 对照 `t1`（会上线）与 `t2`（不上线，宜家及关联租户）两个租户的 Role 配置 | `t1` 的雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 四类 Role 交付后**具备**两项权限；`t2` **所有 Role 均不配置**，其用户看不到两 Tab | AC-08 / TP-PERM-05、06 | P0 | ☐ |

**现场需产品答复**（属本 Story 待确认项）：

- [ ] 勾选框「所有」是否包含 Radio、Switch、树的半选态？主题色是否仅以 Figma 为准（是否给出 token / hex）？
- [ ] 大列表第一列是否一律为 Name？Operation 64px 是否仅放 `⋮`？
- [ ] 本人编辑的抽屉与弹窗，字段集是否完全一致？
- [ ] 同为 Prod 版本时「最新」的排序口径是创建时间 / 发布时间 / 版本号？（决定 Version 列取值是否可判定）

**Story 3 结论**：☐ 准入　☐ 打回（不通过项：____________）　☐ 有条件准入（阻塞项：____________）

---

## 六、不在本次演示与验收范围

| 项 | 出处 |
|---|---|
| Group Transfer Admin（明确暂不做） | member-unify Out of Scope |
| 小屏横向滚动与固定三列不被挤占 | detail-supplement AC-04 / TP-COL-05 |
| Audit 工具栏本身的能力改造（本次只统一列与筛选项） | audit-unify 需求范围 |
| 有特殊约定文案的成功提示（不受统一 Toast 文案强制） | TP-TOAST-04 |

## 七、演示结论汇总

| Story | 演示项 | 其中 P0 | 通过 | 不通过 | 阻塞 | 结论 |
|---|---|---|---|---|---|---|
| ux-p2-member-unify | 20 | 16 | | | | |
| ux-p2-audit-unify | 13 | 11 | | | | |
| ux-p2-detail-supplement | 16 | 13 | | | | |
| **合计** | **49** | **40** | | | | |

- 演示日期：________　参与人：QA ________ / 开发 ________ / 产品 ________
- 整体准入结论：☐ 三个 Story 全部准入　☐ 部分准入（________）　☐ 全部打回
- 需二次演示的 Story 与时间：____________
- 遗留待确认项归属与答复时限：____________
