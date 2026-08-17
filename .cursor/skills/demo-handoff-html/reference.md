# Reference — Demo Handoff HTML

## 产出路径

| 文件 | 路径 |
|------|------|
| 演示 HTML | `docs/sprints/{sprint}/features/{slug}/reports/demo-handoff.html` |
| META 标注 | 同 feature `META.md` → Layout 增加 `reports/demo-handoff.html` |

同路径覆盖更新。

## 演示项挑选

1. **必演**：每条 Story AC 至少对应 1 条 P0 演示项（可合并覆盖多 AC）。
2. **来源**：优先 P0 测试点；同页面连续操作合并为 1 条「演示内容」。
3. **颗粒度**：一条演示 = 一次可观察结果（打开页 → 操作 → 判据），不是完整用例 10 步表。
4. **P1**：仅保留影响准入理解或易漏的关键项，标「建议 / 不阻塞」。
5. **不演**：Out of Scope；纯实现层 DB/outbox（无 UI 可观察）除非用户要求。
6. **不可逆**：删除、归档、移交等放演示末段，前置写清数据准备。
7. **编号**：`D-{短码}-NN`，短码取 feature 缩写（如 `ARCH`、`LOCK`、`NAV`、`BED`）。

## HTML 必含区块

1. **页眉**：Story 标题、飞书链接、sprint、feature-slug、acceptance 相对路径、生成日期
2. **审核规则**：与 SKILL 表一致（P/F/B、P0 准入）
3. **演示前置**：账号、环境、中英文、种子数据；可勾选
4. **演示顺序说明**：1～2 句（先只读后写、不可逆置后）
5. **演示项表**：列固定为  
   `# | 演示内容（开发操作） | 审核判据 | 依据 | 级别 | 结论`  
   结论为三个可点按钮或 radio：`P` / `F` / `B`
6. **现场待确认**：来自 acceptance「待确认」，checkbox
7. **不在本次演示范围**：Out of Scope 摘要
8. **本 Feature 结论**：准入 / 打回 / 有条件准入 + 备注
9. **进度条**：P0 通过数 / P0 总数；localStorage 按 `feature-slug` 持久化勾选

## 演示内容写法

- **演示内容**：祈使句，指向具体页面与控件（「打开 Locked SE Profile 详情 → 点 Archive」）
- **审核判据**：可当场判定的可见结果（文案 COPY、状态、跳转、有无按钮）
- **依据**：`AC-0x` / `TP-xxx`（可多条，用顿号）
- 避免写「体验更好」「正常」等不可验收词

## 模板使用

1. 以 [assets/demo-handoff.template.html](assets/demo-handoff.template.html) 为骨架
2. 替换所有 `{{PLACEHOLDER}}`（见模板注释）
3. 演示项用 `<tbody id="demo-rows">` 内多行 `<tr data-level="P0|P1">`
4. 保留模板内 `<script>`（进度、localStorage、打印）；勿删 `data-storage-key`
5. 单文件自包含：不外链 CSS/JS（除可选系统字体）

## 时长建议（写入页脚即可）

| 演示项规模 | 建议 |
|------------|------|
| ≤ 10 条 | 15～20 分钟 |
| 11～20 条 | 25～35 分钟 |
| > 20 条 | 拆两轮或只演 P0，P1 进测试期 |

## META.md 增补示例

```text
features/{slug}/
├── META.md
├── acceptance.md
├── xmind/
├── testcases/
├── baseline/
└── reports/
    └── demo-handoff.html   # 提测演示引导与确认项
```
