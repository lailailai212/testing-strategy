# docs/execution — 用例执行与数据准备

`docs/sprints/` 存放**设计期**产物（AC、测试点、用例）；本目录存放**执行期**产物（数据准备、数据台账、执行编排、执行记录）。两者按同一 Sprint ID 对应。

## 目录布局

```text
docs/execution/
├── README.md
└── {sprint-id}/
    ├── data-prep.md              # 数据准备清单：需要哪些账号 / 资源 / 日志 / 环境
    ├── data-ledger.md            # 数据台账：实际造出来的真实标识与当前状态
    ├── demo-review-checklist.md  # 提测演示审核清单：开发演示时逐条判定准入
    ├── execution-plan.md         # 执行编排：批次、顺序、不可逆用例的安全边界
    ├── batch-case-mapping.md     # 批次 ↔ 用例全名 + actor/resources（Agent 必读）
    └── run-log.md                # 执行记录：每轮执行的结果与数据变更
```

## 各份文档的分工

| 文档 | 回答的问题 | 何时写 |
|---|---|---|
| `data-prep.md` | 需要准备什么 | 用例评审后、造数前 |
| `data-ledger.md` | 实际造出来的是什么、现在什么状态 | 造数过程中持续更新 |
| `batch-case-mapping.md` | 每批具体跑哪几条用例全名、绑哪些代号 | plan 定稿后、Agent 开跑前 |
| `demo-review-checklist.md` | 开发演示要看哪些点、达到什么程度才准入测试 | 提测演示前 |
| `execution-plan.md` | 按什么顺序执行才不会互相污染 | 造数完成、开始执行前 |
| `run-log.md` | 执行了什么、结果如何、数据被改成了什么 | 每轮执行中与执行后 |

`data-ledger.md` 是执行期的单一事实来源。用例文档里写的是代号（`A3`、`KEY-1`、`t1`），代号对应的真实邮箱、资源 ID、直达 URL 都查台账；涉及凭证的部分查 [`config/env.local.yaml`](../../config/env.local.yaml)。

浏览器 Agent 按批次执行时，使用项目 Skill [`testcase-agent-run`](../../.cursor/skills/testcase-agent-run/SKILL.md)：先门禁 → 小批次执行 → 写 `run-log.md` → 🟡/🔴 回填台账。

## 约定

- 代号体系（`A` / `D` / `R` / `P` 账号，`t1` / `t2` / `t3` 租户）与命名前缀见 [`config/conventions.md`](../../config/conventions.md)。
- 台账与执行记录中**不得**出现明文密码或验证码。
- 不可逆操作（Transfer Admin、删除账号）执行后必须立即回填台账，标注执行时间与身份变化。

## 当前 Sprint

| Sprint | 数据准备 | 台账 | 演示审核 | 编排 | 记录 |
|---|---|---|---|---|---|
| `OBIS-20260727-20260807` | [data-prep](OBIS-20260727-20260807/data-prep.md) | [ledger](OBIS-20260727-20260807/data-ledger.md) | [demo-review](OBIS-20260727-20260807/demo-review-checklist.md) | [plan](OBIS-20260727-20260807/execution-plan.md) | [log](OBIS-20260727-20260807/run-log.md) |
