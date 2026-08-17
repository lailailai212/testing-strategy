# QA Testing Strategy

维护需求分析 → 验收条目的方法论与 Cursor Skills。

## 核心流程

```text
飞书 Story（可选）→ feishu-story-to-md → story/（暂存）
       ↓
需求文档 / 口述 / Story MD
       ↓
story-acceptance-design（Small 或 Large）
       ↓
docs/sprints/{sprint}/features/{feature-slug}/acceptance.md
       ↓
test-points-xmind（可选）→ …/xmind/
       ↓
functional-testcase-md → …/testcases/
       ↑
所属模块对齐 docs/modules/metersphere-modules.json
```

索引：[`docs/sprints/INDEX.md`](docs/sprints/INDEX.md) · [`features-registry.json`](docs/sprints/features-registry.json)

## 两种模式

| 模式 | 何时用 | 产出 |
|------|--------|------|
| **Small** | 单 Story、≤8 条、单主路径 | Story AC（AC = 测试点，可选写入 `acceptance.md`） |
| **Large** | 跨模块、多角色、>8 条或复杂规则 | Story AC + 测试点表 + **AC ↔ TP 追溯矩阵** → `acceptance.md` |

判定规则见 `story-acceptance-design` skill 内 [reference.md](.cursor/skills/story-acceptance-design/reference.md)。

## 目录结构

```text
qa-testing-strategy/
├── README.md
├── config/                            # ★ 环境 · 凭证 · 造数约定
│   ├── env.example.yaml               # 模板（提交）
│   ├── env.local.yaml                 # 真实凭证（gitignore，禁止提交）
│   ├── conventions.md                 # 租户 / 账号代号、命名前缀、清理纪律
│   └── README.md
├── docs/
│   ├── templates/                     # AC / 用例 / MS 导入模板
│   ├── modules/
│   │   └── metersphere-modules.json   # 全局合法模块路径
│   ├── sprints/                       # ★ 设计期产出（按 Sprint → Feature 打包）
│   │   ├── INDEX.md
│   │   ├── features-registry.json     # slug → sprint 索引
│   │   └── {sprint-id}/
│   │       ├── README.md
│   │       ├── reports/               # Sprint 级报告（如 bug 统计）
│   │       └── features/{feature-slug}/
│   │           ├── META.md
│   │           ├── acceptance.md      # AC + 测试点
│   │           ├── xmind/
│   │           ├── testcases/
│   │           ├── baseline/
│   │           └── reports/
│   ├── execution/                     # ★ 执行期产出（按 Sprint）
│   │   └── {sprint-id}/
│   │       ├── data-prep.md
│   │       ├── data-ledger.md
│   │       ├── execution-plan.md
│   │       └── run-log.md
│   └── guides/                        # 操作指南（飞书 Agent 等）
├── scripts/
│   ├── feature_paths.py
│   └── archive/                       # 历史脚本（含 migrate_to_sprints）
├── story/                             # feishu-story-to-md 暂存
└── .cursor/skills/
    ├── feishu-story-to-md/
    ├── feishu-bug-fix-verify/
    ├── story-acceptance-design/
    ├── test-points-xmind/
    ├── functional-testcase-md/
    ├── testcase-agent-run/
    ├── demo-handoff-html/
    ├── weekly-report/
    └── regression-case-review/
```

Feature 包内布局：

```text
features/{feature-slug}/
├── META.md
├── acceptance.md
├── xmind/{slug}.tree.json
├── xmind/{slug}-test-points.xmind
├── testcases/{slug}.md
├── testcases/{slug}-metersphere.xlsx
├── testcases/module-mapping.json   # 可选
├── baseline/
└── reports/                        # 可选
```

整理记录见 [`docs/REPO-CLEANUP.md`](docs/REPO-CLEANUP.md)（`docs/generate_doc/`、`docs/baseline/` 已清理）。

## 执行期与环境配置

用例产出后进入执行期，产物落在 [`docs/execution/{sprint-id}/`](docs/execution/)：数据准备清单 → 数据台账 → 执行编排 → 执行记录，分工见 [`docs/execution/README.md`](docs/execution/README.md)。

环境地址、账号、验证码、租户映射统一放 `config/env.local.yaml`（**已 gitignore**），首次使用从 [`config/env.example.yaml`](config/env.example.yaml) 复制。租户与账号代号、造数命名前缀见 [`config/conventions.md`](config/conventions.md)。

> 文档、用例、baseline 中**不得**出现明文账号或验证码，需要时写「见 `config/env.local.yaml`」。

## 如何使用 Skills

在 Cursor 中 @ 引用 skill，或用自然语言触发：

- 「飞书 Story 转 md / 拉取需求」→ `feishu-story-to-md`
- 「根据这份需求写验收条目 / 测试点 md」→ `story-acceptance-design`
- 「小需求，AC 和测试点合并」→ Small 模式
- 「大需求，先 AC 再拆测试点」→ Large 模式（产出含 AC 追溯矩阵）
- 「把测试点生成 xmind / 脑图」→ `test-points-xmind`
- 「把测试点落地成用例 md / 功能测试用例」→ `functional-testcase-md`
- 「执行用例 / Agent 跑批次 / 写 run-log」→ `testcase-agent-run`
- 「提测演示 / demo handoff HTML」→ `demo-handoff-html`
- 「周报 / weekly report」→ `weekly-report`
- 「回归用例评审」→ `regression-case-review`
- 「飞书 Bug 复验 / 修复验证 / Fixed·Still Repro」→ `feishu-bug-fix-verify`（强制截图落盘，结束后关浏览器；默认不写飞书评论）

落盘前确认 **Sprint** 与 **feature-slug**，并更新 `docs/sprints/features-registry.json`。**禁止** `*-new.md` 旁路副本。

### XMind 生成（test-points-xmind）

依赖：`pip install xmind`（或按 skill 说明）

```bash
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug product-asset-tag
```

产出：`docs/sprints/{sprint}/features/{slug}/xmind/`。

### 功能用例 → MeterSphere Excel

```bash
python .cursor/skills/functional-testcase-md/scripts/md_to_metersphere_excel.py \
  --feature-slug {feature-slug}
```

黄金样例：`docs/sprints/_examples/features/product-asset-tag/testcases/product-asset-tag.md`。
