---
name: demo-handoff-html
description: >-
  根据 feature 的 acceptance.md 生成「开发提测演示引导与确认项」单页 HTML：
  含演示前置、开发逐步操作引导、QA/产品逐条判定（通过/不通过/阻塞）与准入结论。
  产出落在 docs/sprints/{sprint}/features/{slug}/reports/demo-handoff.html。
  Use when 用户提到提测演示、演示引导、demo handoff、demo checklist HTML、
  开发演示确认项、准入演示页。
---

# Demo Handoff HTML

为**单个 feature**生成可现场勾选的提测演示 HTML，供开发按条演示、QA/产品判定是否准入测试。

内容与规则对齐历史 Sprint 级清单（见 `docs/execution/*/demo-review-checklist.md`），但**按 feature 落盘**，不写跨 Story 汇总页（除非用户明确要求 Sprint 汇总）。

模板与字段细则见 [reference.md](reference.md)，示例见 [examples.md](examples.md)。

## 前置

- Feature 已有 `acceptance.md`（含 `## Story AC` 与 `## 测试点`）
- 已知或可从 `docs/sprints/features-registry.json` 反查 `{sprint}` / `{feature-slug}`
- 可选：`META.md`、`story/*.md`、待确认节、Out of Scope

## 工作流

1. **解析输入**：feature-slug / sprint / story 路径；缺 sprint 时查 registry。
2. **读** `acceptance.md`：AC、测试点表、待确认、Out of Scope、变更类型。
3. **挑选演示项**（见 reference「演示项挑选」）：
   - 以 **P0** 为主；关键 P1 可进「建议演示」
   - 合并同路径多 TP 为一条演示（避免控件级拆条）
   - 不可逆操作放该 feature 演示末段并标注
4. **写演示引导**：每条含「谁操作 / 打开哪里 / 做什么 / 审核判据」；开发可按序操作。
5. **生成 HTML**：复制 [assets/demo-handoff.template.html](assets/demo-handoff.template.html) 结构，填入本 feature 数据；保留交互（勾选、进度、localStorage、打印）。
6. **落盘**：

```text
docs/sprints/{sprint}/features/{feature-slug}/reports/demo-handoff.html
```

7. **更新** 同目录 `META.md` Layout（若尚无 `reports/demo-handoff.html` 行）。
8. **告知**：HTML 路径、演示条数（P0/P1）、建议时长、未覆盖的待确认项。

**禁止**：写入 Legacy 扁平目录；用 `*-new.html` 旁路；把完整用例步骤表塞进演示页。

## 演示规则（写入 HTML 页头「审核规则」）

| 项 | 约定 |
|----|------|
| 演示方 | 开发主操；QA 不代操作 |
| 审核方 | QA 主测 + 产品；结论由 QA 记录 |
| 判定 | 每条独立：`P` 通过 / `F` 不通过 / `B` 阻塞 |
| 准入 | 本 feature **全部 P0 演示项通过** 才准入 |
| P0 失败 | 整体打回；修复后可只补演未通过项 |
| P1 失败 | 记已知问题，不阻塞准入 |
| 无法演示 | 记 `B`，准入前须补齐数据/环境 |

## 用户指令

| 用户说法 | 行为 |
|----------|------|
| 提测演示 HTML / demo handoff / 演示引导 | 对指定 feature 生成/覆盖 `reports/demo-handoff.html` |
| 某 sprint 全部 feature | 对该 sprint 下各 feature 各生成一份（不合并成一页，除非用户要求汇总） |
| 只要 P0 | 演示项仅含 P0 |
| 更新演示页 | 重读最新 acceptance.md 后覆盖同路径 |

## 与其他 Skill

```text
story-acceptance-design → acceptance.md
demo-handoff-html       → reports/demo-handoff.html   ← 本 Skill
functional-testcase-md  → testcases/（完整用例，不替代演示页）
```

## 附加资源

- 模板：[assets/demo-handoff.template.html](assets/demo-handoff.template.html)
- 挑选规则与 HTML 区块：[reference.md](reference.md)
- 样例说明：[examples.md](examples.md)
