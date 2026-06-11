---
name: story-acceptance-design
description: >-
  根据 PRD 或口述需求生成 Story 验收条目。Small 模式合并 AC 与测试点为一张表；
  Large 模式输出 Story AC（测试点待产品功能 baseline，v1.0 不生成测试点表）。Use when 用户提到 Story AC、验收标准、
  需求分析、需求评审、小需求合并、大需求拆分 AC，或从需求文档设计测试覆盖。
---

# Story Acceptance Design

从需求生成**一句话验收条目**，供开发快速 review；条目 ID 稳定，便于后续展开测试用例。

完整规则见 [reference.md](reference.md)，示例见 [examples.md](examples.md)。

## 工作流

1. **读需求**：提取角色、入口、主路径、规则、权限、错误反馈、Out of Scope。
2. **选模式**（用户未指定则自动判定，见 reference）：
   - **Small**：输出一张「验收条目表」（AC = 测试点）
   - **Large**：仅输出 Story AC + 待确认；**不输出测试点表**（待产品功能 baseline，@魏来/@张蒙 定稿后启用）
3. **写条目**：每条一句话，句式 `[前提/谁] + [操作] + [可观察结果]`。
4. **补覆盖**（仅 Small，或用户明确要求且 baseline 已有时）：
   - 每条 AC 至少 1 个 P0
   - 含「刷新、成功、正常、无权限」等词 → 建议补负向或边界
5. **输出待确认**：歧义、未定义文案、跳转行为未说明等。
6. **声明模式**：输出开头注明 `本次采用 Small/Large 模式` 及判定依据（1 句话）。

## Small 模式输出模板

```markdown
# Story: [标题]

**模式**: Small

## 验收条目

| ID | 验收条目（一句话） | 优先级 | 备注 |
|----|-------------------|--------|------|
| 1 | ... | P0 | |
```

## Large 模式输出模板

```markdown
# Story: [标题]

**模式**: Large

## Story AC
1. ...
2. ...

## 待确认
- [ ] ...

## 测试点
（v1.0 待产品功能 baseline 确认，暂不生成；baseline 定稿后按规范补充）
```

## 写作约束

- 中文输出；ID 稳定，便于后续追溯与用例展开
- 不写 CSS 选择器、接口路径等实现细节
- AC / 条目必须可验收；避免「体验更好、尽量、正常」
- Small：P0 行即 Story 给开发 review 的全集；P1 / P2 / P3 可在备注标 QA 扩展
- Large：Story AC 保持 3–8 条粗粒度；**v1.0 不生成测试点表**（待产品功能 baseline）
- 需求阶段不标注自动化 / Playwright 可执行性

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 小需求 / 合并 AC 和测试点 | 强制 Small |
| 大需求 / 先 AC 再测试点 | 强制 Large；仅输出 Story AC，测试点注明 baseline TBD |

## 附加资源

- 判定规则与拆分口诀：[reference.md](reference.md)
- Small / Large 完整示例：[examples.md](examples.md)
- 团队文档：[docs/story-ac-guide.md](../../../docs/story-ac-guide.md)
- 测试点可视化 XMind：[test-points-xmind](../test-points-xmind/SKILL.md)
