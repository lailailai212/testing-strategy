# Story: 【SE卡片】内容导入

**来源**: [飞书项目 User Story #7018567020](https://project.feishu.cn/obis/userstory/detail/7018567020)  
**空间**: OBIS (`obis`)  
**编号**: 655 | **优先级**: Must | **Sprint**: OBIS-20260622-20260703  
**模式**: Large（飞书 AC 共 6 条，含 SEMS 实时查询、三重筛选与单 SE 限制，需独立测试点表与 AC 追溯）

---

## Story AC

1.（AC-01）SE 卡片区域右上方提供「**添加**」按钮；用户点击后弹出 **SE 下拉选择框**。

2.（AC-02）SE 下拉选择框为**单选**，每次只能添加**一个** SE。

3.（AC-03）当已添加 SE 后，「**添加**」按钮**置灰**，不可再次添加。

4.（AC-04）下拉选项内容由 **Product Workspace（PW）** 调用 **SEMS 接口**实时查询可用列表获得。

5.（AC-05）下拉列表筛选条件须**同时满足**：① 与当前 **PV 环境**匹配（Test / Production）；② SE Profile 状态为 **Active**；③ 操作者持有 **create authorization** 创建权限。

6.（AC-06）下拉选项展示字段为：**SE name**、**SE id**。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### Assets — SE 卡片区域与添加按钮

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SEI-BTN-01 | AC-01 | P0 | Secure Element Module 的 Assets 页 **SE 卡片区域**右上方存在「**添加**」按钮 |
| TP-SEI-BTN-02 | AC-01 | P0 | 当前 Module **尚未导入 SE** 时，「添加」按钮**可点击**（非置灰） |
| TP-SEI-BTN-03 | AC-01 | P0 | 点击「添加」后弹出 **SE 下拉选择框**（非跳转至 SEMS 外部页） |
| TP-SEI-BTN-04 | AC-03 | P0 | 已成功导入 **1 个 SE** 后，「添加」按钮**置灰**，无法再次点击 |
| TP-SEI-BTN-05 | 需求描述 | P1 | 删除已导入 SE（Story #653）后，「添加」**恢复可点击**，**可再次导入** SE |
| TP-SEI-BTN-06 | QA扩展 | P1 | **Select Secure Element** 下拉**仅展示**操作者持有 **create authorization** 的 SE config；无权限项**不出现**（**非**「添加」按钮置灰） |

### SE 下拉选择框 — 单选与导入

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SEI-SEL-01 | AC-02 | P0 | 下拉选择框为**单选**模式，同一时刻仅可选中 **1 个** SE |
| TP-SEI-SEL-02 | AC-02 | P0 | 选中并确认导入后，Assets SE 卡片区域展示**该 SE** 卡片（与 Story #653 展示字段联动） |
| TP-SEI-SEL-03 | AC-02, AC-03 | P0 | 导入成功后下拉关闭，页面仅存在 **1 张** SE 卡片，「添加」按钮置灰 |
| TP-SEI-SEL-04 | 需求描述 | P1 / 待确认 | 选中 SE 后的**确认交互**：点击选项即导入 / 需额外 Confirm 按钮（Product Doc 未述） |
| TP-SEI-SEL-05 | QA扩展 | P1 | 打开下拉后点击外部区域或 Cancel，**不导入** SE，「添加」按钮仍可点击 |
| TP-SEI-SEL-06 | QA扩展 | P1 | 下拉列表为空时，展示**空态提示**（如无可用 SE），且不创建 SE 卡片 |

### SEMS 列表 — 实时查询

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SEI-API-01 | AC-04 | P0 | 每次点击「添加」打开下拉时，PW **调用 SEMS 接口**拉取最新可用列表（非本地缓存静态数据） |
| TP-SEI-API-02 | AC-04 | P0 | SEMS 侧**新增**符合条件的 SE Profile 后，再次打开下拉，新 SE **出现在**选项中 |
| TP-SEI-API-03 | AC-04 | P1 | SEMS 侧 SE Profile **变更或移除**后，再次打开下拉，列表与 SEMS 当前状态**一致** |

### SEMS 列表 — 筛选条件（AC-05）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SEI-FLT-01 | AC-05 | P0 | **Test** PV 环境下，下拉仅展示与 **Test** 环境匹配的 SE Profile |
| TP-SEI-FLT-02 | AC-05 | P0 | **Production** PV 环境下，下拉仅展示与 **Production** 环境匹配的 SE Profile |
| TP-SEI-FLT-03 | AC-05 | P0 | SEMS 中状态为 **非 Active** 的 SE Profile **不出现在**下拉选项 |
| TP-SEI-FLT-04 | AC-05 | P0 | 操作者**无 create authorization** 时，对应 SE Profile **不出现在**下拉（或无法完成导入） |
| TP-SEI-FLT-05 | AC-05 | P0 | 同时满足 **PV 环境 + Active + create authorization** 的 SE Profile **出现在**下拉 |
| TP-SEI-FLT-06 | QA扩展 | P1 | 仅满足部分条件（如 Active 但环境不匹配）的 SE **均被排除** |

### SEMS 列表 — 选项展示字段

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SEI-DSP-01 | AC-06 | P0 | 下拉每一项同时展示 **SE name** 与 **SE id** |
| TP-SEI-DSP-02 | AC-06 | P0 | 下拉中 SE name、SE id 与 SEMS 侧对应 SE Profile **一致** |
| TP-SEI-DSP-03 | AC-06, AC-02 | P0 | 导入成功后，Assets SE 卡片 **name** 与下拉所选 **SE name** 一致，**SE profile ID** 与所选 **SE id** 一致 |

### UI 设计对齐

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SEI-UI-01 | 需求描述 | P2 | 「添加」按钮位置、下拉样式与 Figma 设计稿一致（[node-id=12021-163058](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=12021-163058)） |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 添加按钮与 SE 下拉 | TP-SEI-BTN-01～03 | ✅ |
| AC-02 单选、每次仅一个 SE | TP-SEI-SEL-01～03 | ✅ |
| AC-03 已添加后按钮置灰 | TP-SEI-BTN-04；TP-SEI-SEL-03 | ✅ |
| AC-04 PW 实时调用 SEMS 列表 | TP-SEI-API-01～03 | ✅ |
| AC-05 三重筛选条件 | TP-SEI-FLT-01～06；TP-SEI-BTN-06 | ✅ |
| AC-06 展示 SE name、SE id | TP-SEI-DSP-01～03 | ✅ |

**AC-01～AC-06 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| 添加按钮 | 4 | 2 | 0 | 6 |
| 下拉单选与导入 | 3 | 3 | 0 | 6 |
| SEMS 实时查询 | 2 | 1 | 0 | 3 |
| 筛选条件 | 5 | 1 | 0 | 6 |
| 选项展示 | 3 | 0 | 0 | 3 |
| UI 设计 | 0 | 0 | 1 | 1 |
| **合计** | **17** | **7** | **1** | **25** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 17 |
| 需求描述 | 3 |
| QA 扩展 | 5 |

---

## 待确认

- [ ] **PW** 是否即 **Product Workspace**（Story #658 已明确定义；本 Story Product Doc 亦写 PW 调用 SEMS）
- [ ] 选中 SE 后的**确认导入交互**（点击即添加 vs 需 Confirm）
- [x] 删除已导入 SE 后「添加」恢复可点击，可再次导入（2026-06 产品确认；删除流程见 #653）
- [x] 无 create authorization 的 SE config **不在下拉展示**（非按钮置灰）（2026-06 产品确认）
- [ ] Test / Production 环境切换后，已导入 SE 与下拉列表行为（是否需重新导入）

## Out of Scope

- SE 卡片导入后在 Assets 的**字段展示、Tag、active/deactive、删除** — 见 Story #653（本 Story 仅验收**导入**与下拉筛选；删后可再导入）
- Overview 页 SE 卡片 **name** 摘要展示 — 见 Story #627
- SEMS 侧 SE Profile 的创建 / 编辑界面
- SEMS **状态变更订阅**及创建 Version / Batch 校验 — 见 Story #658

---

## 关联 Story

| 编号 | Story | 关系 |
|:----:|-------|------|
| 653 | SE 卡片内容说明 | 导入成功后 SE 卡片展示与操作 |
| 658 | SE 卡片订阅与动作 | SEMS 状态订阅与 Version / Batch 校验 |
| 601 | 选择 module 类型 | SE Module 默认含 SE 卡片区域 |
