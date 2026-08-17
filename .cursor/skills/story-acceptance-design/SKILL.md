---
name: story-acceptance-design
description: >-
  根据 PRD 或 Story MD 生成 Story 验收标准（AC）与测试点 Markdown。
  先判定变更类型（UI/UX | Logic | Hybrid）再选 Small/Large；
  Small 模式 AC 即测试点；Large 模式输出粗粒度 AC + 带 AC 追溯的测试点表。
  Use when 用户提到 Story AC、验收标准、测试点、需求分析、需求评审、从 Story 生成 AC。
---

# Story Acceptance Design

从需求生成 **Story AC**（开发 review）与 **测试点**（QA 覆盖）；Large 需求二者分层，且测试点必须标注「命中 AC」。

完整规则见 [reference.md](reference.md)，示例见 [examples.md](examples.md)，Large 产出模板见 [docs/templates/test-points-template.md](../../../docs/templates/test-points-template.md)。

目录约定见 [docs/sprints/INDEX.md](../../../docs/sprints/INDEX.md)。

## 工作流

1. **确认 Sprint 与 feature-slug**（落盘前必做）
   - `{sprint-id}`：与飞书 Sprint 一致（如 `OBIS-20260622-20260703`）
   - `{feature-slug}`：小写英文连字符；写入/更新 `docs/sprints/features-registry.json`
2. **读需求**：提取入口、主路径、规则、交互、Out of Scope；飞书 Story 优先保留原文 **AC-01～AC-N** 编号。
3. **判定变更类型**（写 AC / 测试点前必做，见 [reference.md](reference.md)「变更类型」）：
   - **UI/UX**：布局、文案、控件态、交互反馈、空态/加载态等；测试点侧重可见性与交互可观察结果
   - **Logic**（功能/逻辑）：业务规则、状态机、权限、配额、去重、数据副作用等；测试点侧重规则矩阵与相关回归
   - **Hybrid**：界面与规则均改；文档声明主/次类型，P0 密度跟主类型
   - 与规则类型 A–D **正交**：变更类型决定设计偏置；A–D 命中仍须跑强制清单
4. **选模式**（用户未指定则自动判定，见 reference）：
   - **Small**：细粒度 Story AC（预估 ≤ 8 条），**AC 即测试覆盖全集**
   - **Large**：粗粒度 Story AC（3–8 条或与飞书 AC 对齐）+ **测试点表 + AC 追溯矩阵**
5. **写 Story AC**：每条完整一句话，句式 `[前提/谁] + [操作/条件] + [可观察结果]`。
   - UI/UX：结果侧重「看到 / 展示 / 态变化 / 文案」
   - Logic：结果侧重「应/不应发生的业务结果、计数、触达、落库」
6. **识别规则类型并跑强制清单**（写测试点前必做，见 [reference.md](reference.md)「规则类型与强制清单」）：
   - 扫描关键词：首次 / 仅 1 次 / 去重 / 邮件·通知 / 配额 / 多角色可见性等
   - 命中任一类则按清单补齐 TP；**清单未覆盖不得宣称测试点设计完成**
   - Small 模式：将清单要点并入 AC，或标 `待确认`；Large：清单项落独立 TP
7. **写测试点**（Large 或用户要求「测试点 md」时）：
   - 按变更类型跑对应侧重清单（见 reference），再按**产品页面 / 模块**分组表格
   - 每条含 `TP-ID | 来源 | 优先级 | 测试点`
   - 每条飞书 AC 至少 1 条 P0 测试点覆盖
   - 输出 **AC ↔ 测试点追溯矩阵**、**覆盖摘要**；命中规则类型时输出并勾选 **设计自检**
8. **输出待确认 / Out of Scope**。
9. **写入固定目录**（用户要求落盘时）：

```text
docs/sprints/{sprint-id}/features/{feature-slug}/acceptance.md
```

并维护同目录 `META.md`（sprint、story-id、status）。**禁止** `*-new.md` 旁路副本。

10. **声明模式与变更类型**：文档开头注明：
    - `**模式**: Small/Large` 及判定依据（1 句话）
    - `**变更类型**: UI/UX | Logic | Hybrid`（Hybrid 写清主/次）及判定依据（1 句话）

## Story AC 格式

**编号段落列表**，不用表格：

```markdown
## Story AC

1.（AC-01）用户进入 XX 页时，应看到 YY。

2.（AC-02）用户点击 ZZ 后，应出现 WW。
```

- 标题固定为 `## Story AC`
- 与飞书 Description 中验收标准对齐时，保留 `（AC-0x）` 前缀
- 条与条之间空一行
- 默认 P0 不加前缀；非 P0 在编号后标注 `（P1）` 或 `（P1 / 待确认）`
- 不写 CSS 选择器、接口路径；避免「体验更好、尽量、正常」等不可验收表述

## 测试点格式（Large / 显式要求测试点时）

### 表格列（固定顺序）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|

### 来源 取值

| 值 | 含义 |
|----|------|
| `AC-0x` | 覆盖 Story AC；多条用逗号分隔，如 `AC-01, AC-04` |
| `需求描述` | 需求正文有述，未列入 Story AC 列表 |
| `QA扩展` | QA 补充的边界、负向、并发等 |

表格上方加一行说明（见 [test-points-template.md](../../../docs/templates/test-points-template.md)）。

### 必含章节

- `## 测试点`（按 UI 模块分 `###` 小节）
- `## AC ↔ 测试点追溯矩阵`（从 AC 反查 TP，标注每条 AC 是否 ✅ 覆盖）
- `## 覆盖摘要`（模块 × 优先级；命中类型统计）

黄金样例：`docs/sprints/_unassigned/features/self-reg-001-05-domain-whitelist/acceptance.md`

## Small vs Large

| 模式 | Story AC | 测试点 | 产出路径 |
|------|----------|--------|----------|
| Small | ≤ 8 条，细粒度 | 与 AC 合并，可不单独列表 | 可选写入 `acceptance.md` |
| Large | 3–8 条粗粒度或飞书 AC 全文 | 独立表格 + AC 追溯 | `docs/sprints/{sprint}/features/{slug}/acceptance.md` |

## 写作约束

- 中文输出；编号稳定，便于追溯与用例展开
- AC 必须可验收、可勾选
- **先定变更类型再铺测试点**：禁止用同一套「功能规则」习惯覆盖纯 UI/UX Story，也禁止纯 Logic Story 堆无验收依据的样式细节为 P0
- 需求阶段不标注自动化 / Playwright 可执行性
- Out of Scope 不写入 Story AC，单独列 `## Out of Scope`

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 小需求 / AC 和测试点合并 | Small，细粒度编号段落 |
| 大需求 / 先 AC 再测试点 | Large，AC + 测试点表 + 追溯矩阵 |
| UI/UX / 交互改版 / 文案布局 | 变更类型 UI/UX；测试点偏可见性与交互 |
| 功能 / 逻辑 / 规则 / 配额权限 | 变更类型 Logic；测试点偏规则矩阵与回归 |
| 测试点 md / 落盘 | 写入 Sprint Feature 包 `acceptance.md`，并更新 registry |
| 段落形式 / 不要表格 | 仅 Story AC 用编号段落；测试点仍用表格 |

## 与其他 Skill 的关系

```text
feishu-story-to-md      → story/*.md（暂存）
story-acceptance-design → docs/sprints/{sprint}/features/{slug}/acceptance.md
test-points-xmind       → …/features/{slug}/xmind/
functional-testcase-md  → …/features/{slug}/testcases/
```

## 附加资源

- Small/Large、**变更类型**、拆分口诀、**规则类型强制清单**：[reference.md](reference.md)
- Small / Large / UI·Logic 对照 / 里程碑易漏示例：[examples.md](examples.md)
- 产出模板（含设计自检）：[docs/templates/test-points-template.md](../../../docs/templates/test-points-template.md)
- Sprint 索引：[docs/sprints/INDEX.md](../../../docs/sprints/INDEX.md)
- 测试点可视化：[test-points-xmind](../test-points-xmind/SKILL.md)
- 下游用例展开：[functional-testcase-md](../functional-testcase-md/SKILL.md)
