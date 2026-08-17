# Examples — Test Points XMind

## 示例 A：从测试点 MD 生成

**输入**：`docs/sprints/_unassigned/features/self-reg-001-05-domain-whitelist/acceptance.md`

**叶子 JSON**（节选）：

```json
{
  "title": "Applications Tab 右侧角标展示 Pending 状态申请数量",
  "source": "AC-01",
  "priority": "P0"
}
```

**XMind 展示**：`[P0][AC-01] Applications Tab 右侧角标展示 Pending 状态申请数量`

**命令**：

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug self-reg-001-05-domain-whitelist
```

---

## 示例 B：叶子格式对照

| 来源 | priority | title（节选） | XMind 叶子标题 |
|------|----------|---------------|----------------|
| AC-09 | P0 | 用户提交…不向申请人发邮件 | `[P0][AC-09] 用户提交…` |
| 需求描述 | P0 | 首次提交后通知 Admin | `[P0][需求描述] 首次提交后…` |
| QA扩展 | P1 | 子域名是否匹配白名单 | `[P1][QA扩展] 子域名是否…` |

---

## 示例 C：树结构（Product Asset Tag）

```text
Product Asset — Certificate/Key Tag 测试点
├── Product Asset
│   ├── Assign Security Key        → 2 叶子
│   ├── Assign Certificate         → 2 叶子
│   ├── Tag 新增与删除             → 4 叶子
│   └── Asset 列表展示             → 4 叶子
├── Version 详情页                 → 2 叶子
└── 产品详情页                     → 2 叶子
```

完整 JSON：[examples/product-asset-tag.tree.json](examples/product-asset-tag.tree.json)
