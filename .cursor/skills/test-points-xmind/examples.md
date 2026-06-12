# Examples — Test Points XMind

## 示例 A：从已有测试点表生成

**输入**：用户已确认 Product Asset Tag 测试点（16 条 P0）。

**步骤**：

1. 按页面模块整理树（见 `examples/product-asset-tag.tree.json`）
2. 写入 `docs/generate_doc/test-points-xmind/trees/product-asset-tag.tree.json`
3. 执行生成脚本

**命令**（推荐 `--feature-slug`，路径自动对齐固定目录）：

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug product-asset-tag
```

**固定产出**：

- 树 JSON：`docs/generate_doc/test-points-xmind/trees/product-asset-tag.tree.json`
- XMind：`docs/generate_doc/test-points-xmind/product-asset-tag-test-points.xmind`

---

## 示例 B：用户只说「帮我把测试点做成 xmind」

**行为**：

1. 从对话或 `story-acceptance-design` 产出中提取测试点
2. 若无条目表 → 先按模块输出粗颗粒度测试点（8–16 条），用户确认后再生成
3. **固定目录**写入 XMind：`docs/generate_doc/test-points-xmind/{feature-slug}-test-points.xmind`
4. **固定目录**写入树 JSON：`docs/generate_doc/test-points-xmind/trees/{feature-slug}.tree.json`（不得改路径）

---

## 示例 C：树结构对照（Product Asset）

```text
Product Asset — Certificate/Key Tag 测试点
├── Product Asset
│   ├── Assign Security Key        → 2 叶子
│   ├── Assign Certificate         → 2 叶子
│   ├── Tag 新增与删除             → 4 叶子
│   └── Asset 列表展示             → 4 叶子（含历史数据）
├── Version 详情页                 → 2 叶子
└── 产品详情页                     → 2 叶子
```

完整 JSON：[examples/product-asset-tag.tree.json](examples/product-asset-tag.tree.json)
