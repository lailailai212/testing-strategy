# Story: 【卡片编辑】overview展示内容改动

**来源**: [飞书项目 User Story #7013841136](https://project.feishu.cn/obis/userstory/detail/7013841136)  
**空间**: OBIS (`obis`)  
**编号**: 627 | **优先级**: Must | **Sprint**: OBIS-20260622-20260703  
**模式**: Large（需求跨 Overview / Assets 双 Tab、Module 联动、三类卡片摘要规则及 Create 入口，需独立测试点表与 AC 追溯）

---

## Story AC

1.（AC-01）用户在 Product 详情 **Overview** Tab 的 **Assets-{Module名}** 区块中，应看到与 **Assets** Tab 当前 Module 下**一致**的卡片集合；在 Assets 侧**新增**或**删除**卡片后，Overview 须**同步**出现或移除对应卡片。

2.（AC-02）用户在 Overview Tab 通过 **Module 选择器**切换 Module 时，下方 **Assets-{Module名}** 区块标题与卡片内容须**联动切换**为所选 Module 的 Assets 卡片。

3.（AC-03）Overview Tab **Assets-{Module}** 区块右上方应提供 **Create Assets Type** 按钮；用户点击后弹出**新建卡片**弹窗。

4.（AC-04）**SE** 类型卡片在 Overview 上摘要须展示 **name**（与 Assets 侧 SE 卡片 name 一致，来源见 Story #653）。

5.（AC-05）**Custom（自定义）** 类型卡片在 Overview 上摘要须展示 **data volume**（自定义卡片字段行表的**行数**）。

6.（AC-06）**内置卡片**（如 Matter Module 默认卡）在 Overview 上须展示**摘要统计 / 关键字段**，且卡片底栏展示 **{编辑者} - {相对时间}**；Matter Module 各内置卡摘要格式须与 Product Doc 样本一致（如 Firmware `2 total, 1 active`、Keys `6 active keys` 等）。

7.（AC-07）Overview 卡片区每张卡片须含**图标**、**卡片标题**、**摘要内容**、底栏 **{编辑者} - {相对时间}**；内置卡 **Programming Station Software** 标题对应 Assets 侧 **PS Software Package**（命名差异同 Story #601）。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### Overview — 页面结构与 Module 联动

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-STR-01 | 需求描述 | P0 | Product Workspace → Product 详情 → **Overview** Tab 可正常进入；Product 级 Tab 含 Overview（当前）、Assets、Version 等 |
| TP-OVW-STR-02 | AC-02 | P0 | Overview 页存在 **Module 选择器**（横向 Tab + **Add**）；默认选中某一 Module |
| TP-OVW-STR-03 | AC-02 | P0 | Module 选择器下方展示 **Assets-{Module名}** 区块标题（样本：**Assets-Module_A**） |
| TP-OVW-STR-04 | AC-02 | P0 | 切换 Module 选择器至 **Module_B** 后，区块标题更新为 **Assets-Module_B**，下方卡片切换为该 Module 的 Assets 卡片 |
| TP-OVW-STR-05 | AC-02 | P0 | 切换回 **Module_A** 后，卡片区恢复展示 Module_A 对应卡片集合 |
| TP-OVW-STR-06 | 需求描述 | P1 | Overview 卡片区为**网格布局**（参考样本 **2 行 × 4 列**）；卡片数量变化时布局自适应，不重叠、不截断标题 |

### Overview — Assets 卡片与 Assets Tab 同步

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-SYNC-01 | AC-01 | P0 | Matter Module 初始状态下，Overview **Assets-{Module}** 卡片区卡片**种类与数量**与 Assets Tab 同 Module **一致**（默认 8 张内置卡） |
| TP-OVW-SYNC-02 | AC-01 | P0 | 在 Assets Tab **删除**一可删卡片（如 Other Module 下 General File）并确认后，切回 Overview Tab，该卡片**不再出现** |
| TP-OVW-SYNC-03 | AC-01 | P0 | 在 Assets Tab **新增**卡片（内置类型或自定义，见 Story #602 / #603）成功后，Overview Tab 同 Module **同步出现**新卡片 |
| TP-OVW-SYNC-04 | AC-01 | P0 | Assets Tab **隐藏**内置卡片（删除内置卡 = 隐藏，见 Story #602 AC-02）后，Overview **同步移除**该卡片 |
| TP-OVW-SYNC-05 | AC-01 | P0 | Assets Tab **加回**已隐藏内置卡片后，Overview **同步恢复**该卡片 |
| TP-OVW-SYNC-06 | AC-01 | P1 | 在 Overview Tab 停留时，于另一 Tab（Assets）完成增删后**返回 Overview**，卡片区已更新（无需整页刷新；若需手动刷新则记缺陷） |
| TP-OVW-SYNC-07 | QA扩展 | P1 | 多 Module 并存时，在 **Module_A** Assets 增删卡片，**Module_B** Overview 卡片区**不受影响** |
| TP-OVW-SYNC-08 | QA扩展 | P1 | Overview 与 Assets 卡片**相对排序**一致（内置在前、自定义按创建顺序在后，见 Story #602 AC-13） |

### Overview — Create Assets Type

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-CRT-01 | AC-03 | P0 | **Assets-{Module}** 区块右上方存在 **Create Assets Type** 按钮（Product Doc 称「创建卡片」） |
| TP-OVW-CRT-02 | AC-03 | P0 | 点击 **Create Assets Type** 弹出**新建卡片**弹窗（非跳转至 Assets Tab） |
| TP-OVW-CRT-03 | AC-03, AC-01 | P0 | 通过 Overview 入口成功创建卡片后，Overview 卡片区**立即出现**新卡片，且 Assets Tab 同 Module **同步出现** |
| TP-OVW-CRT-04 | 需求描述 | P1 / 待确认 | Overview 弹窗与 Assets Tab 新增卡片弹窗是否为**同一 UI / 同一流程**（内置 / 自定义选项一致） |
| TP-OVW-CRT-05 | QA扩展 | P1 | Overview 弹窗 **Cancel** / 关闭后，不创建卡片，Overview 与 Assets 均无新增 |

### Overview — SE 卡片摘要

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-SE-01 | AC-04 | P0 | Secure Element Module 下，Overview 存在 **SE** 卡片时，摘要展示 **name** 字段 |
| TP-OVW-SE-02 | AC-04 | P0 | Overview SE 卡片摘要 **name** 与 Assets Tab 同 Module SE 卡片 **name** 一致 |
| TP-OVW-SE-03 | AC-04 | P0 | SEMS 侧 SE profile name 更新后（Story #653 AC-02），Overview SE 卡片摘要 **name** **同步更新** |
| TP-OVW-SE-04 | QA扩展 | P1 | SE 卡片 name 为空或未导入时，Overview 摘要展示规则（占位文案 / 空态 / 隐藏卡片）符合产品约定 |

### Overview — Custom 卡片摘要

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-CUS-01 | AC-05 | P0 | Overview 上 **Custom（自定义）** 卡片摘要展示 **data volume**（行数语义） |
| TP-OVW-CUS-02 | AC-05 | P0 | 自定义卡片字段行表有 **N** 行已保存数据时，Overview 摘要 **data volume = N**（与 Assets 侧行表一致） |
| TP-OVW-CUS-03 | AC-05 | P0 | 在 Assets 自定义卡片中**新增 / 删除**字段行并保存后，Overview 摘要 **data volume** **同步更新** |
| TP-OVW-CUS-04 | 需求描述 | P1 / 待确认 | **data volume** 是否含**空行**、是否仅统计**已保存**行、未保存草稿是否计入 |
| TP-OVW-CUS-05 | QA扩展 | P1 | 同一 Module 多张 Custom 卡片并存时，各卡 **data volume** 独立计数、互不混淆 |
| TP-OVW-CUS-06 | QA扩展 | P2 | Custom 卡片 **0 行**时 Overview 摘要展示（如 `0` / `0 data keys` / 空态文案）符合产品约定 |

### Overview — 内置卡片（Matter）摘要

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-BLT-01 | AC-06 | P0 | Matter Module Overview 上 **Firmware** 卡片摘要格式与样本一致：**`{total} total, {active} active`**（样本 `2 total, 1 active`） |
| TP-OVW-BLT-02 | AC-06 | P0 | **Keys** 摘要：**`{n} active keys`**（样本 `6 active keys`） |
| TP-OVW-BLT-03 | AC-06 | P0 | **Certificates** 摘要：**`{n} active certs`**（样本 `2 active certs`） |
| TP-OVW-BLT-04 | AC-06 | P0 | **Chip Config** 摘要：**`Chip: {chip model}`**（样本 `Chip: Silicon Labs MG24`） |
| TP-OVW-BLT-05 | AC-06 | P0 | **Matter Config** 摘要含两行：**`VID: {vid}`**、**`PID: {pid}`**（样本 `VID: 0x1441`、`PID: 0x0123`） |
| TP-OVW-BLT-06 | AC-06 | P0 | **Factory Data** 摘要：**`{n} data keys`**（样本 `8 data keys`） |
| TP-OVW-BLT-07 | AC-06, AC-07 | P0 | **Programming Station Software** 卡片摘要：**`{total} total, {active} active`**（样本 `1 total, 2 active`）；Assets 侧对应卡片为 **PS Software Package** |
| TP-OVW-BLT-08 | AC-06 | P0 | **General File** 摘要：**`{total} total, {active} active`**（样本 `2 total, 1 active`） |
| TP-OVW-BLT-09 | AC-06 | P0 | 修改 Matter 内置卡内容（如新增 active key）并保存后，Overview 对应卡片摘要**实时或刷新后更新**为最新统计 |
| TP-OVW-BLT-10 | 需求描述 | P1 / 待确认 | 内置卡**无数据 / 空态**时摘要展示规则（如 `0 active keys`）是否全环境统一 |
| TP-OVW-BLT-11 | QA扩展 | P1 | **Other** Module 内置卡（无 Matter Config）Overview 摘要规则与 Matter 同类卡一致（total/active 或 key 计数格式） |

### Overview — 卡片通用展示（图标 / 底栏）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-OVW-COM-01 | AC-07 | P0 | 每张 Overview 卡片含**图标**、**卡片标题**、**摘要内容**三个主要区域 |
| TP-OVW-COM-02 | AC-06, AC-07 | P0 | 内置卡片底栏展示 **`{编辑者} - {相对时间}`** 格式（样本 `John Smith - 2h ago`） |
| TP-OVW-COM-03 | AC-07 | P0 | Overview 卡片标题 **Programming Station Software** 与 Assets **PS Software Package** 为同一卡片的不同页面命名 |
| TP-OVW-COM-04 | 需求描述 | P1 / 待确认 | 底栏 **编辑者** 与 **相对时间** 的数据来源（最后保存者 / 最后编辑字段者）及更新时机 |
| TP-OVW-COM-05 | QA扩展 | P1 | SE / Custom 卡片底栏是否同样展示 **{编辑者} - {相对时间}**（Product Doc 仅明确内置卡，待 UI 确认） |
| TP-OVW-COM-06 | QA扩展 | P2 | 相对时间随时间推移自动刷新（如 `2h ago` → `3h ago`）或需重新进入页面才更新 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Overview 与 Assets 卡片增删同步 | TP-OVW-SYNC-01～05；TP-OVW-CRT-03；TP-OVW-SYNC-06～08 | ✅ |
| AC-02 Module 选择器联动 | TP-OVW-STR-02～05 | ✅ |
| AC-03 Create Assets Type 入口与弹窗 | TP-OVW-CRT-01～03；TP-OVW-CRT-05 | ✅ |
| AC-04 SE 卡片 name 摘要 | TP-OVW-SE-01～03 | ✅ |
| AC-05 Custom 卡片 data volume 摘要 | TP-OVW-CUS-01～03 | ✅ |
| AC-06 内置卡片摘要 + 底栏编辑者/时间 | TP-OVW-BLT-01～09；TP-OVW-COM-02 | ✅ |
| AC-07 卡片结构 + PS Software 命名映射 | TP-OVW-COM-01～03；TP-OVW-BLT-07 | ✅ |

**AC-01～AC-07 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| Overview — 页面结构与 Module 联动 | 4 | 2 | 0 | 6 |
| Overview — Assets 同步 | 5 | 3 | 0 | 8 |
| Overview — Create Assets Type | 3 | 2 | 0 | 5 |
| Overview — SE 卡片摘要 | 3 | 1 | 0 | 4 |
| Overview — Custom 卡片摘要 | 3 | 2 | 1 | 6 |
| Overview — 内置卡片（Matter）摘要 | 9 | 2 | 0 | 11 |
| Overview — 卡片通用展示 | 3 | 2 | 1 | 6 |
| **合计** | **30** | **14** | **2** | **46** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 32 |
| 需求描述 | 8 |
| QA 扩展 | 6 |

---

## 待确认

- [ ] 内置卡片 Overview 摘要**空态**展示是否全环境统一（参考图仅含 Matter Module_A 有数据样本）
- [ ] **SE / Custom** Overview 展示：Product Doc 已规定 name / data volume，但参考图无 SE / Custom 样本，UI 布局与底栏是否同内置卡
- [ ] Overview **Create Assets Type** 弹窗是否与 Assets Tab 新增卡片（Story #602 / #603）为**同一弹窗 / 同一流程**
- [ ] Custom 卡片 **data volume** 计数：是否含空行、是否仅统计已保存行、删除行后是否实时更新
- [ ] 底栏 **`{编辑者} - {相对时间}`** 的数据来源与更新时机（最后保存者 vs 最后编辑字段者）
- [ ] Overview 与 Assets 增删同步是否需**手动刷新**页面，或应自动 / 切 Tab 即更新

---

## Out of Scope

- **Production Version** 区块（Create Version 按钮与版本列表）— 本 Story 不改动
- **Manufacturing** 区块（Create Batch 按钮与批次列表）— 本 Story 不改动
- 顶部**告警横幅**（如 Factory Service Storage Quota Exceeded）— 仅作页面上下文，非本 Story 验收范围
- Assets Tab 卡片增删 / 自定义编辑器本身逻辑 — 见 Story #602、#603；本 Story 仅验证 Overview **同步与展示**
- SE 卡片字段定义与 SEMS 同步 — 见 Story #653；本 Story 仅验证 Overview **name 摘要展示**

---

## 关联 Story

| 编号 | Story | 关系 |
|:----:|-------|------|
| 601 | 选择 module 类型 | Matter 默认 8 卡、PS Software Package 命名映射 |
| 602 | assets 卡片自定义 | Assets 侧增删；Overview 须同步 |
| 603 | 自定义卡片 | Custom 类型与 data volume 展示 |
| 653 | SE 卡片内容说明 | SE 卡片 name 字段来源与展示 |
