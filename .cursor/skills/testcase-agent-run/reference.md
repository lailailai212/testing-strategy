# testcase-agent-run — 参考

配合 [SKILL.md](SKILL.md) 使用；执行时按需打开本节，勿整份塞进每轮上下文。

## 上下文切片规则

| 资产 | 允许读入的范围 |
|------|----------------|
| `execution-plan.md` | 当前批次小节 + 总览破坏级别表 |
| `data-ledger.md` | 本批账号表行 + 本批资源行 +（若 🔴）第 6 节变更记录最近几行 |
| 用例 MD | 文档头 blockquote（入口/产品规则）+ **本批用例表格行**；可跳过未选中的行与冗长「场景与 TP 覆盖」 |
| baseline | 本批涉及页面的 `*-baseline.md` 关键交互表 / `elements-baseline.json` 对应 `pages.*` |
| `env.local.yaml` | `default_env`、`environments.{env}`、本批账号邮箱对应凭证；勿朗读 OTP 到用户可见摘要以外的落盘文件 |

单轮建议：**≤ 8 条用例**；L2/🔴 建议 **1 条一确认**（或严格按 plan 表顺序且每条后复位）。

## 可执行绑定（解析用例时抽取）

从「前置条件 + 步骤 + plan/台账」抽取下列字段；缺失则门禁 Blocked 或向用户确认一次。

| 字段 | 来源优先级 | 示例 |
|------|------------|------|
| `case_name` | 用例名称列 | `【KMS-Key-Detail】【UI】Member 列表 - …` |
| `feature_slug` | 路径或用户指定 | `ux-p2-member-unify` |
| `priority` | 用例等级列 | `P0` |
| `type` | 名称中的 `【UI】/【Functional】/【E2E】` | `UI` |
| `actor` | 前置代号 > plan 指定账号 | `A3` |
| `resources` | 前置/plan | `KEY-1` |
| `entry_url` | 台账资源 URL > baseline `fullUrl` > `base_url` + path | `https://…/key/detail/…` |
| `locale` | 用例步骤或环境默认 | `zh` / `en` |
| `destructiveness` | plan 批次级别；单条有特殊说明则覆盖 | 🟢 / 🟡 / 🔴 |
| `reset` | plan 复位清单 | `A4 登录 → Transfer 回 A3` |
| `locators_ref` | baseline 文件锚点 | `baseline/key-detail-baseline.md#Member` |

### 前置条件改写（Agent 内心模型，不强制改 MD）

遇到散文前置时，先归一成代号再执行：

```text
原文：已登录可进入某 KMS Key Detail → Member
归一：actor=A3（plan/台账：KEY-1 的 Admin），entry=KEY-1.url + Member Tab
```

无法归一（台账无资源 / 无 Admin）→ Blocked，而不是任选一个 Key。

## 断言策略

| 用例类型 | 主断言 | 取证 |
|----------|--------|------|
| `【UI】` | 可见/隐藏、置灰、文案、列顺序、`+n` hover、弹窗按钮组合 | 失败步截图；必要时对比 baseline 截图 |
| `【Functional】` | 阻断/成功、计数、列表字段、权限后果 | 结果态截图；计数可前后各一张 |
| `【E2E】` | 旅程终态 + 关键中间站 | 终态必截；Transfer/删除后核对台账字段 |

预期中的中英文并列：`中文「…」 / 英文「…」` —— 只断言**当前 locale**对应一侧；若用例要求双语，切换语言后再断言另一侧。

一步多断言（分号并列）：任一子断言失败则该步 Fail。

## 破坏性与复位

| 级别 | 含义 | Agent 行为 |
|------|------|------------|
| 🟢 | 只读或打开后 Cancel | 可连续执行；打开破坏性弹窗后**必须 Cancel**，禁止 Confirm |
| 🟡 | 可改回 | 记录改前值（写入 run-log 或台账备注）；批末按 plan 复位清单恢复 |
| 🔴 | 不可逆或高成本 | 严格按 plan 顺序；Confirm 后立刻台账回填；按表复位后再下一条 |

plan 写明「只看不 Confirm」的用例：误点 Confirm → 立即停，回填台账，标 Fail（操作偏离）并报告用户。

## run-log 条目格式

在 `run-log.md`「失败与阻塞明细」或批次附节追加（Pass 可只更新批次计数；Fail/Blocked 必写明细）：

```markdown
### {case_name}

| 字段 | 值 |
|------|-----|
| 轮次 | R1 |
| 批次 | B4 |
| 结果 | Pass \| Fail \| Blocked |
| 环境 | sit |
| actor / resources | A3 / KEY-1 |
| 失败步骤 | [3]（Pass 则 `-`） |
| 现象 | 实际文案/状态；Blocked 写门禁原因 |
| 证据 | `evidence/R1/kms-member-admin-transfer.png` |
| 缺陷 | 链接或 `-` |
| 台账回填 | 无 \| 已更新 A3 当前状态 |
| 复位 | 未涉及 \| 已完成 \| 待做 |
```

批次进度表状态：⬜ → 🟡（开跑）→ ✅ / 🔴。

## 登录步骤（email_otp）

1. 打开 `{base_url}` 登录页（可带 redirect）  
2. 填台账映射的邮箱 → Send Code  
3. 填 `environments.{env}.otp_universal`（或账号专属 OTP）→ Sign In  
4. 确认落到目标租户（`tenants` 映射）；不对则切换租户后再进 `entry_url`

密码登录：仅当 `login_method: password` 时用对应字段；仍禁止写入 run-log。

## Locator 冲突处理

1. 用例文案与 baseline「与 Story/用例差异」表冲突 → **以 baseline 实测文案操作**，若预期写的是旧文案则 Fail 并注明「文案与 baseline 不一致」  
2. baseline 标注 `fragile: true` → 先尝试 role/name；失败则截图 + Blocked「fragile 控件无法稳定定位」，勿连点 nth  
3. 动态行数据 → 用台账中的 Name/Email/资源名 `filter` 行，再对该行操作

## dry-run 输出模板

```markdown
## 门禁报告 `{sprint}` / `{batch}`

| 用例 | actor | entry_url | 破坏性 | 门禁 | 原因 |
|------|-------|-----------|--------|------|------|
| … | A3 | https://… | 🟢 | OK | |
| … | D2 | - | 🔴 | Blocked | 台账 D2 邮箱为空 |

可执行：n / 总数：m
```

## 证据目录

```text
docs/execution/{sprint-id}/evidence/{round-id}/
  {short-case-slug}.png
```

`short-case-slug`：模块 + 意图缩写，如 `kms-member-transfer-dialog`；避免过长中文文件名。
