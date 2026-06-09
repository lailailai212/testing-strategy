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
（后续：功能测试用例展开 — 见 functional-test-case-design-v1.md）
```

## 两种模式

| 模式 | 何时用 | 产出 |
|------|--------|------|
| **Small** | 单 Story、≤8 条、单主路径 | 一张「验收条目表」（AC = 测试点） |
| **Large** | 跨模块、多角色、>8 条或复杂规则 | Story AC（短）；测试点待产品功能 baseline |

判定规则见 [docs/story-ac-guide.md](docs/story-ac-guide.md)。  
完整飞书规范见 [docs/functional-test-case-design-v1.md](docs/functional-test-case-design-v1.md)（含 [落地细节](docs/functional-test-case-design-v1.md#附录-c落地细节)）。

## 目录结构

```text
qa-testing-strategy/
├── README.md
├── docs/
│   ├── story-ac-guide.md
│   └── templates/
│       ├── small-mode-template.md
│       └── large-mode-template.md
└── .cursor/skills/
    └── story-acceptance-design/   # 需求 → 验收条目
```

## 如何使用 Skills

在 Cursor 中 @ 引用 skill，或用自然语言触发：

- 「根据这份需求写验收条目」→ `story-acceptance-design`
- 「小需求，AC 和测试点合并」→ Small 模式
- 「大需求，先 AC 再拆测试点」→ Large 模式
