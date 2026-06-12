---
name: test-points-xmind
description: >-
  将测试点（验收条目表）按产品页面/模块结构生成 XMind 脑图。叶子节点为 TP-ID + 一句话描述；
  中间层对齐 UI 目录（如 Product Asset / Assign 弹窗）。Use when 用户提到测试点 xmind、脑图、
  测试点导图，或要把 story-acceptance-design 产出可视化为 XMind。
---

# Test Points XMind

将**粗颗粒度测试点**转为 XMind，层级与产品导航结构对齐（页面 → 子功能 → 测试点）。

规则与 JSON 格式见 [reference.md](reference.md)，示例见 [examples.md](examples.md)。

## 工作流

1. **确认测试点来源**
   - 对话中已有测试点表 → 直接使用
   - 仅有需求 → 先按 `story-acceptance-design` 写粗颗粒度测试点（约 8–16 条 P0），再生成 XMind
2. **按 UI 结构建树**（不要按控件拆叶子）
   - 中心主题：Story / 功能名
   - 一级分支：页面或模块（如 Product Asset、Version 详情页）
   - 二级分支：子功能（如 Assign Security Key、Asset 列表展示）
   - 叶子：`TP-ID | 一句话描述`
3. **写入树 JSON**（固定目录，见下节「固定产出目录」）
4. **执行生成脚本**（需 `pip install xmind`）：

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug {feature-slug}
```

或显式指定路径（须落在固定目录内）：

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --tree docs/generate_doc/test-points-xmind/trees/{feature-slug}.tree.json \
  --output docs/generate_doc/test-points-xmind/{feature-slug}-test-points.xmind
```

5. **校验**：用 XMind 打开；或检查 zip 含 `meta.xml` 与 `META-INF/manifest.xml`（见 reference.md）
6. **告知用户**：输出文件路径与脑图层级摘要

## 颗粒度约束

- **一个叶子 = 一条测试点主题**（可验收的一句话），不是一条功能用例
- 同主题内的多个检查项用分号写在同一叶子里，不拆成多个 TP
- 历史数据、列表展示等「读数据」场景，放在对应模块下的展示分支，不并入 Assign 流程分支

## 固定产出目录（强制）

**所有本 skill 生成的产物必须落在以下目录，不得写入其他位置**（如项目根、`scripts/`、`.cursor/skills/` 内除示例外）。

| 类型 | 固定路径 | 说明 |
|------|----------|------|
| 树 JSON | `docs/generate_doc/test-points-xmind/trees/{feature-slug}.tree.json` | 源数据，便于 diff 与再生成 |
| XMind 脑图 | `docs/generate_doc/test-points-xmind/{feature-slug}-test-points.xmind` | 最终交付物 |

目录结构：

```text
docs/generate_doc/test-points-xmind/
├── trees/                              # 所有 *.tree.json
│   └── {feature-slug}.tree.json
└── {feature-slug}-test-points.xmind    # 生成的脑图
```

**命名**：`feature-slug` 用小写英文连字符（如 `product-asset-tag`）。

**执行约定**：

- 目录不存在时自动创建（`trees/` 与父目录）
- 重新生成时**覆盖**同路径下的 `.tree.json` / `.xmind`，不另存副本
- 优先使用 `--feature-slug` 让脚本解析固定路径，避免手写出错
- `.cursor/skills/test-points-xmind/examples/` 仅放**只读参考** JSON，实际产出一律写入 `docs/generate_doc/test-points-xmind/`

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 生成测试点 xmind / 脑图 | 完整工作流 |
| 按 Product Asset 结构 | 一级分支对齐页面目录，Assign 等作为二级 |
| 更新 xmind | 改 tree JSON 后重新跑脚本 |
| 只有需求没有测试点 | 先产出粗颗粒度测试点表，确认后再生成 |

## 附加资源

- JSON 格式与 TP-ID 规则：[reference.md](reference.md)
- 命令与结构示例：[examples.md](examples.md)
- 参考树 JSON：[examples/product-asset-tag.tree.json](examples/product-asset-tag.tree.json)
- 上游产出：`story-acceptance-design` skill
