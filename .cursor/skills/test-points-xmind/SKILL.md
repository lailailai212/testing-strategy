---
name: test-points-xmind
description: >-
  将测试点 MD 按产品页面/模块结构生成 XMind 脑图。叶子含来源与优先级，不含 TP-ID。
  Use when 用户提到测试点 xmind、脑图、测试点导图，或要把 story-acceptance-design 产出可视化为 XMind。
---

# Test Points XMind

将**粗颗粒度测试点**转为 XMind，层级与产品导航结构对齐（页面 → 子功能 → 测试点）。

规则与 JSON 格式见 [reference.md](reference.md)，示例见 [examples.md](examples.md)。
目录约定见 [docs/sprints/INDEX.md](../../../docs/sprints/INDEX.md)。

## 工作流

1. **确认测试点来源**（优先级从高到低）
   - `docs/sprints/{sprint}/features/{feature-slug}/acceptance.md` → 读取 `## 测试点` 各表
   - 对话中已有测试点表 → 直接使用
   - 仅有需求 → 先按 `story-acceptance-design` 写 `acceptance.md`，再生成 XMind
2. **按 UI 结构建树**（不要按控件拆叶子）
   - 中心主题：Story / 功能名（若 `acceptance.md` 已声明变更类型，可在中心主题或备注体现，如 `…（UI/UX）`）
   - 一级分支：页面或模块
   - 二级分支：子功能；**UI/UX** Story 二级宜对齐「区域 / 交互态」，**Logic** Story 二级宜对齐「规则场景 / 业务动作」
   - **叶子对象**（推荐）：

```json
{
  "title": "一句话测试点描述",
  "source": "AC-03",
  "priority": "P0"
}
```

   - `source` 与 MD「来源」列一致：`AC-0x` / `需求描述` / `QA扩展`
   - **不写 TP-ID**（XMind 展示为 `[P0][AC-03] 描述`）
3. **（可选）从 MD 自动生成 tree JSON**：

```bash
python .cursor/skills/test-points-xmind/scripts/md_to_tree.py \
  --feature-slug {feature-slug}
# 未注册时加：--sprint {sprint-id}
```

4. **执行生成脚本**（需 `pip install xmind`）：

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug {feature-slug}
```

5. **校验**：XMind 可打开；zip 含 `meta.xml` 与 `META-INF/manifest.xml`
6. **告知用户**：输出路径、层级摘要、叶子条数

## 与 story-acceptance-design 的字段映射

| 测试点 MD | tree JSON 叶子 | XMind 展示 |
|-----------|----------------|------------|
| 测试点 | `title` | 描述正文 |
| 来源 | `source` | `[AC-01]` 等 |
| 优先级 | `priority` | `[P0]` 等 |
| TP-ID | — | 不展示 |

## 颗粒度约束

- **一个叶子 = 一条测试点主题**，不是一条功能用例
- 同主题内多个检查项用分号写在同一 `title`，不拆叶子
- 历史数据、列表展示等放在对应模块展示分支
- 变更类型只影响分支命名侧重点，**不改变**叶子字段（仍无 TP-ID）；细则以上游 `acceptance.md` 为准

## 固定产出目录（强制）

| 类型 | 固定路径 |
|------|----------|
| 树 JSON | `docs/sprints/{sprint}/features/{slug}/xmind/{slug}.tree.json` |
| XMind | `docs/sprints/{sprint}/features/{slug}/xmind/{slug}-test-points.xmind` |

- `{feature-slug}` 经 `docs/sprints/features-registry.json` 反查 sprint（或显式 `--sprint`）
- 目录不存在时自动创建；同路径**覆盖**更新

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 生成测试点 xmind / 脑图 | 读 acceptance.md → 写 tree JSON → 跑脚本 |
| 更新 xmind | 改 tree JSON 后重新跑脚本 |
| 只有需求没有测试点 | 先 `story-acceptance-design` 产出 acceptance.md |

## 附加资源

- JSON 格式：[reference.md](reference.md)
- 命令与结构：[examples.md](examples.md)
- 参考 JSON：[examples/product-asset-tag.tree.json](examples/product-asset-tag.tree.json)
- 黄金样例包：`docs/sprints/_examples/features/product-asset-tag/`
- 上游：`story-acceptance-design`；下游：`functional-testcase-md`（以 acceptance.md 为准，非 XMind）
