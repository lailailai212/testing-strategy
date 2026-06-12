---
name: story-acceptance-design
description: >-
  根据 PRD 或 Story MD 生成编号段落形式的 Story 验收标准（AC）。
  Small 模式输出细粒度 AC；Large 模式输出粗粒度 AC + 待确认。
  Use when 用户提到 Story AC、验收标准、需求分析、需求评审、从 Story 生成 AC。
---

# Story Acceptance Design

从需求生成**编号段落形式**的 Story AC，供开发 review；条目编号稳定，便于后续展开测试用例。

完整规则见 [reference.md](reference.md)，示例见 [examples.md](examples.md)。

## 工作流

1. **读需求**：提取入口、主路径、规则、交互、Out of Scope。
2. **选模式**（用户未指定则自动判定，见 reference）：
   - **Small**：细粒度 Story AC（预估 ≤ 8 条），AC 即测试覆盖全集
   - **Large**：粗粒度 Story AC（3–8 条）+ 待确认；**不输出测试点表**（v1.0）
3. **写条目**：每条完整一句话，句式 `[前提/谁] + [操作/条件] + [可观察结果]`。
4. **补覆盖**（Small）：
   - 主路径与阻断规则标 P0（默认不写前缀）
   - 边界、负向、未决规则标 `（P1）` 或 `（P1 / 待确认）`
5. **输出待确认**：歧义、未定义文案、范围未明等，单独列在 `## 待确认`。
6. **声明模式**：输出开头注明 `**模式**: Small/Large` 及判定依据（1 句话）。

## Story AC 输出格式（Small / Large 统一）

**必须使用编号段落列表**，不用表格。

```markdown
# Story: [标题]

**模式**: Small（判定依据一句话）

## Story AC

1. 用户进入 XX 页时，应看到 YY。

2. 用户点击 ZZ 后，应出现 WW。

3.（P1 / 待确认）若 AA 发生，行为应符合产品最终定义。

## 待确认

- [ ] ...
```

### 格式规则

- 标题固定为 `## Story AC`
- 每条以 `数字.` 开头，紧跟完整句子（编号与正文之间无空格亦可）
- **条与条之间空一行**，便于阅读
- 默认 P0 不加前缀；非 P0 在编号后标注，如 `3.（P1）` 或 `7.（P1 / 待确认）`
- 不写 CSS 选择器、接口路径等实现细节
- 避免「体验更好、尽量、正常」等不可验收表述

## Small vs Large 粒度

| 模式 | Story AC 条数 | 粒度 |
|------|---------------|------|
| Small | ≤ 8 | 细：每个可观察行为/规则单独一条 |
| Large | 3–8 | 粗：按模块或主路径合并 |

Large 模式额外输出：

```markdown
## 测试点
（v1.0 待产品功能 baseline 确认，暂不生成；baseline 定稿后按规范补充）
```

## 写作约束

- 中文输出；编号稳定，便于追溯与用例展开
- AC 必须可验收、可勾选
- 需求阶段不标注自动化 / Playwright 可执行性
- Out of Scope 不写入 Story AC，必要时在待确认中说明

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 小需求 / 合并 AC 和测试点 | 强制 Small，细粒度编号段落 |
| 大需求 / 先 AC 再测试点 | 强制 Large，粗粒度编号段落 |
| 段落形式 / 不要表格 | 编号段落 Story AC（默认已是） |

## 附加资源

- 判定规则与拆分口诀：[reference.md](reference.md)
- Small / Large 完整示例：[examples.md](examples.md)
- 团队文档：[docs/story-ac-guide.md](../../../docs/story-ac-guide.md)
- 测试点可视化 XMind：[test-points-xmind](../test-points-xmind/SKILL.md)
