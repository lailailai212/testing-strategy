# QA Testing Strategy

维护需求分析 → 验收条目的方法论与 Cursor Skills。

## 核心流程

```text
需求文档 / 口述
       ↓
story-acceptance-design（Small 或 Large 模式）
       ↓
验收条目 / Story AC + 测试点
       ↓
test-points-xmind（可选：按页面结构导出 XMind 脑图）
       ↓
（后续：功能测试用例展开）
```

## 两种模式

| 模式 | 何时用 | 产出 |
|------|--------|------|
| **Small** | 单 Story、≤8 条、单主路径 | 一张「验收条目表」（AC = 测试点） |
| **Large** | 跨模块、多角色、>8 条或复杂规则 | Story AC（短）；测试点待产品功能 baseline |

判定规则见 `story-acceptance-design` skill 内 [reference.md](.cursor/skills/story-acceptance-design/reference.md)。

## 目录结构

```text
qa-testing-strategy/
├── README.md
├── docs/
│   ├── templates/
│   │   ├── small-mode-template.md
│   │   └── large-mode-template.md
│   └── generate_doc/
│       └── test-points-xmind/         # XMind 产出
│           ├── trees/                 # 树 JSON 源数据
│           └── *.xmind                # 生成的脑图
└── .cursor/skills/
    ├── story-acceptance-design/   # 需求 → 验收条目
    └── test-points-xmind/        # 测试点 → XMind 脑图
```

## 如何使用 Skills

在 Cursor 中 @ 引用 skill，或用自然语言触发：

- 「根据这份需求写验收条目」→ `story-acceptance-design`
- 「小需求，AC 和测试点合并」→ Small 模式
- 「大需求，先 AC 再拆测试点」→ Large 模式
- 「把测试点生成 xmind / 脑图」→ `test-points-xmind`

### XMind 生成（test-points-xmind）

依赖：`pip install xmind`

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug product-asset-tag
```

产出固定落在 `docs/generate_doc/test-points-xmind/`（树 JSON 在 `trees/` 子目录）。
