# Story: 【SE卡片】SE卡片内容说明

**来源**: [飞书项目 User Story #7018449332](https://project.feishu.cn/obis/userstory/detail/7018449332)  
**空间**: OBIS (`obis`)  
**编号**: 653 | **优先级**: Must | **Sprint**: OBIS-20260622-20260703  
**模式**: Large（用户要求测试点 md；飞书 AC 共 8 条，含 SEMS 同步、Tag 复用、状态切换与删除确认等子规则，需独立测试点表与 AC 追溯）

---

## Story AC

1.（AC-01）用户在 Assets 页面查看 SE 资源时，应以卡片形式展示 SE 卡片，且卡片包含 name、SE profile ID、active 状态、Update Time、Tag 与操作项。

2.（AC-02）SE profile name 来源于 SEMS；当 SEMS 侧该字段更新时，Assets 中对应 SE 卡片 name 自动同步为最新值。

3.（AC-03）SE profile ID 来源于 SEMS，作为 SE 唯一标识展示；导入后该字段只读，用户不可编辑。

4.（AC-04）新导入的 SE 卡片 active 状态默认为 active。

5.（AC-05）Update Time 取 SE 卡片导入时间；导入后该字段不再因其他业务变更而更新。

6.（AC-06）SE 卡片的 Tag 展示与编辑逻辑与平台现有 tag 一致。

7.（AC-07）用户可通过操作项对 SE 卡片执行 active / deactive 状态切换。

8.（AC-08）用户删除 SE 卡片时须先弹出二次确认弹窗；确认后执行删除；弹窗文案为 `Are you sure you want to delete?` / `确定删除该内容？`

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### Assets — SE 卡片展示

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-LST-01 | AC-01 | P0 | Assets 页面存在 SE 类型资源时，以**卡片形式**展示（非纯表格行列表） |
| TP-SE-LST-02 | AC-01 | P0 | 单张 SE 卡片同时展示字段：name、SE profile ID、active 状态、Update Time、Tag、操作项 |
| TP-SE-LST-03 | QA扩展 | P1 | 多张 SE 卡片并存时，各卡片字段与对应 SEMS 数据一一对应，互不混淆 |

### SE 卡片 — 字段与 SEMS 数据来源

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-FLD-01 | AC-02 | P0 | 新导入 SE 卡片 name 与 SEMS 侧 SE profile name 一致 |
| TP-SE-FLD-02 | AC-02 | P0 | SEMS 侧 SE profile name 更新后，Assets 中对应 SE 卡片 name 自动同步为最新值（无需手动刷新或重新导入） |
| TP-SE-FLD-03 | AC-03 | P0 | SE profile ID 与 SEMS 侧一致，作为 SE 唯一标识展示 |
| TP-SE-FLD-04 | AC-03 | P0 | SE profile ID 导入后只读：无编辑入口，或尝试编辑后不可保存 |
| TP-SE-FLD-05 | AC-04 | P0 | 新导入 SE 卡片 active 状态默认为 **active** |

### SE 卡片 — Update Time

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-TIME-01 | AC-05 | P0 | 新导入 SE 卡片 Update Time 等于导入时间 |
| TP-SE-TIME-02 | 需求描述, AC-05 | P1 / 待确认 | active / deactive 切换后 Update Time 是否更新（字段说明写「状态变化将导致 Update Time 变化」，AC-05 写「导入后不再更新」，**TBD**） |
| TP-SE-TIME-03 | QA扩展 | P1 | SEMS 侧 name 同步更新后，Update Time 不因 name 变更而更新 |

### SE 卡片 — Tag

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-TAG-01 | AC-06 | P0 | SE 卡片 Tag **展示样式**与平台现有 asset tag 一致 |
| TP-SE-TAG-02 | AC-06 | P0 | SE 卡片 Tag **添加 / 编辑 / 删除**交互与平台现有 tag 逻辑一致 |

### SE 卡片 — active / deactive 操作

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-ACT-01 | AC-07 | P0 | 当前为 **active** 的 SE 卡片，操作项可切换为 **deactive** |
| TP-SE-ACT-02 | AC-07 | P0 | 当前为 **deactive** 的 SE 卡片，操作项可切换为 **active** |
| TP-SE-ACT-03 | AC-07 | P0 | active / deactive 切换后，卡片上 active 状态展示立即更新为最新值 |

### SE 卡片 — 删除操作

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-DEL-01 | AC-08 | P0 | 点击删除操作项时弹出二次确认弹窗，不直接删除 |
| TP-SE-DEL-02 | AC-08 | P0 | 确认弹窗文案：英文 **Are you sure you want to delete?**；中文 **确定删除该内容？** |
| TP-SE-DEL-03 | AC-08 | P0 | 用户在确认弹窗点击确认后，SE 卡片从 Assets 中移除 |
| TP-SE-DEL-04 | AC-08 | P0 | 用户在确认弹窗点击取消，SE 卡片保留，不执行删除 |
| TP-SE-DEL-05 | QA扩展 | P1 | 删除成功后刷新页面，该 SE 卡片不再出现 |

### UI 设计对齐

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SE-UI-01 | 需求描述 | P2 | SE 卡片布局、字段位置与 Figma 设计稿一致（[node-id=12021-163058](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=12021-163058)） |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 卡片形式展示含全部字段 | TP-SE-LST-01、TP-SE-LST-02 | ✅ |
| AC-02 name 来源于 SEMS 且自动同步 | TP-SE-FLD-01、TP-SE-FLD-02 | ✅ |
| AC-03 SE profile ID 只读 | TP-SE-FLD-03、TP-SE-FLD-04 | ✅ |
| AC-04 默认 active | TP-SE-FLD-05 | ✅ |
| AC-05 Update Time 取导入时间 | TP-SE-TIME-01 | ✅ |
| AC-06 Tag 与平台 tag 一致 | TP-SE-TAG-01、TP-SE-TAG-02 | ✅ |
| AC-07 active / deactive 切换 | TP-SE-ACT-01、TP-SE-ACT-02、TP-SE-ACT-03 | ✅ |
| AC-08 删除二次确认 | TP-SE-DEL-01、TP-SE-DEL-02、TP-SE-DEL-03、TP-SE-DEL-04 | ✅ |

**AC-01～AC-08 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| SE 卡片展示 | 2 | 1 | 0 | 3 |
| 字段与 SEMS 数据 | 5 | 0 | 0 | 5 |
| Update Time | 1 | 2 | 0 | 3 |
| Tag | 2 | 0 | 0 | 2 |
| active / deactive | 3 | 0 | 0 | 3 |
| 删除操作 | 4 | 1 | 0 | 5 |
| UI 设计 | 0 | 0 | 1 | 1 |
| **合计** | **17** | **4** | **1** | **22** |

| 来源 | 条数 |
|------|------|
| Story AC（AC-01～AC-08） | 17 |
| 需求描述 | 2 |
| QA扩展 | 3 |

---

## 待确认

- [ ] AC-02 原文写「PW 卡片自动同步」，本 Story 上下文为 SE 卡片，是否笔误（测试点已按 SE 卡片编写）
- [ ] Update Time 规则：字段说明表写 active/deactive 变化会更新 Update Time，AC-05 写导入后不再更新（TP-SE-TIME-02）
- [ ] SEMS name 同步触发方式：实时推送还是定时轮询；测试环境如何模拟 SEMS 侧更新（TP-SE-FLD-02）
- [ ] 「同平台 tag 逻辑」的具体参照页面（如 Product / 其他 Asset 类型），便于 AC-06 对齐 baseline

## Out of Scope

- SE 卡片导入流程本身（本 Story 聚焦导入后在 Assets 的展示与操作）
- SEMS 侧 SE profile 的创建 / 编辑界面
- 删除 SE 卡片后 SEMS 侧数据是否联动清除（需求未述）
