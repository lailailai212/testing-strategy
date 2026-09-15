---
name: testcase-agent-run
description: >-
  用浏览器 Agent 按批次执行功能测试用例：读 execution-plan / data-ledger / baseline，
  绑定账号与直达 URL，逐步操作并对照预期，写入 run-log（含截图与台账回填）。
  Use when 用户提到执行用例、跑测试、agent 执行、按批次测、run-log、浏览器验收，
  或要对某 feature / sprint 的 testcases md 做手工自动化执行。
---

# Testcase Agent Run

将**已落地的功能测试用例 MD**交给浏览器 Agent **小批次执行**，产出写入 `docs/execution/{sprint}/run-log.md`。

本 Skill **只执行、不设计用例**。缺用例先走 `functional-testcase-md`；缺造数先补 `data-ledger.md`。

细则见 [reference.md](reference.md)，样例见 [examples.md](examples.md)。

## 输入（用户需提供或可推断）

| 项 | 说明 |
|----|------|
| `sprint-id` | 如 `OBIS-20260727-20260807` |
| 范围 | 批次号（`B1`…）或 feature-slug + 用例名称子集；**禁止一次整包 25+ 条** |
| 环境 | 默认 `config/env.local.yaml` 的 `default_env`（sit/uat） |

可选：`layer=L0|L1|L2`（见「分层」）；`dry-run=true` 只做门禁不点浏览器。

## 必读文件（按序，只读相关切片）

1. `docs/execution/{sprint}/batch-case-mapping.md` → **本批用例全名**、actor/resources（有则优先于 plan 摘要）  
2. `docs/execution/{sprint}/execution-plan.md` → 破坏级别、复位要求、B0 门禁  
3. `docs/execution/{sprint}/data-ledger.md` → **仅本批用到的账号/资源行**（代号 → 邮箱/URL/当前状态）  
4. `config/env.local.yaml` → `base_url`、登录方式、OTP；**勿把凭证写入 run-log / 对话摘要**  
5. `docs/sprints/{sprint}/features/{slug}/testcases/{slug}.md` → **仅本批用例行**  
6. 同 feature 的 `baseline/`（`entry-urls.md` / `*-baseline.md` / a11y snapshot）→ 直达 URL 与 locator  
7. `config/conventions.md` → 代号含义（若前置条件含 `A3`/`t1` 等）

## 工作流

```text
门禁 → 登录复用 → 逐条执行 → 写 run-log →（🟡/🔴）复位与台账回填 → 下一条
```

### 1. 门禁（不通过则标 Blocked，禁止探索补洞）

对本批每条用例检查：

- [ ] 前置中的代号在台账存在，且状态非 ⬜/🔴  
- [ ] 有直达 URL（台账资源 URL 或 baseline `fullUrl`）；否则 Blocked  
- [ ] 用例/acceptance「待确认」不阻塞本条关键控件文案  
- [ ] 破坏级别已知：🟢 可任意；🟡 批末复位；🔴 须有 plan 中的复位手法且资源未耗尽  
- [ ] 环境已部署目标功能（plan B0 或用户确认）

任一项失败 → 该条 `Blocked`，写清原因，**不要**在产品里瞎点找入口。

### 2. 登录与会话

- 凭证只读 `env.local.yaml`；台账只提供邮箱代号映射  
- **同账号同租户**：登录一次，串跑本批多条  
- **换账号 / 换租户**：重新登录；Transfer/删除后按台账「当前状态」决定用谁登  
- 登录后优先 `navigate` 直达 URL，少点左侧菜单

### 3. 单条执行协议

对每条用例：

1. **解析绑定**：`actor`（账号代号）、`resources`、`entry_url`、`locale`（中/英）  
2. **打开入口**：直达 URL → 若需 Tab/区域，用 baseline 文案定位  
3. **逐步操作**：步骤 `[n]` 与预期 `[n]` 一一对应；做完一步立刻核对该步预期  
4. **取证**：失败或关键断言处截图，落到 `docs/execution/{sprint}/evidence/{round}/{case-slug}.png`（目录可建）  
5. **判定**：全部预期满足 → `Pass`；任一步不符 → `Fail`（记录步骤号与实际现象）；无法继续 → `Blocked`  
6. **副作用**：🟡/🔴 成功改数据后，立即回填 `data-ledger.md`（身份/状态），并在 run-log「数据变更同步」记一行  
7. **复位**：按 `execution-plan` 要求；🔴 一般**每条后复位**再跑下一条；🟡 可批末统一复位

### 4. 浏览器操作约定

优先 **Chrome DevTools MCP**（`take_snapshot` → `click`/`fill`/`hover`）；Playwright MCP 亦可。

Locator 优先级（与项目规则一致）：

1. `data-testid` / `aria-label` / `get_by_role` + 精确 `name`  
2. baseline `stableLocator`（`elements-baseline.json`）  
3. 限定容器内的 role/文案  
4. **避免**：`nth(x)`、模糊大段 `get_by_text`、通用 placeholder（如 `Please Enter`）

操作前用最新 snapshot；失败先重新 snapshot，再换定位策略，**禁止**无依据盲点。

### 5. 写入 run-log

路径：`docs/execution/{sprint}/run-log.md`

- 更新「轮次总览」「批次进度」  
- 失败/阻塞写入「失败与阻塞明细」  
- 不可逆变更写入「数据变更同步」并回填台账  
- 单条结果格式见 [reference.md](reference.md)#run-log-条目格式  

**禁止**在 run-log 写明文密码或验证码。

### 6. 回复用户

简短汇总：批次、Pass/Fail/Blocked 数、失败用例名与步骤号、台账是否已回填、建议下一批。

## 分层（加速）

| 层 | 范围 | 何时用 |
|----|------|--------|
| **L0** | P0 + 🟢 只读 UI | 冒烟、验 locator/入口 |
| **L1** | P0 Functional/E2E（可逆） | 核心规则 |
| **L2** | 🔴 Transfer/删除 | 严格按 plan 顺序 |

用户未指定时：有 plan 则跟 plan 批次；否则默认 L0 → 再问是否继续 L1/L2。

## 硬性禁止

- 一次加载整份用例表 + 全量台账到上下文（只切本批）  
- 门禁未过仍「试着点点看」  
- 🔴 用例 Confirm 后不回填台账就跑下一条  
- 改非本 Sprint 命名前缀的数据（见 `conventions.md`）  
- 把 `env.local.yaml` 凭证提交 git 或写入文档  
- 自行发明按钮文案/配额数字（与 baseline/用例不一致时标 Fail 或 Blocked）

## 与其他 Skill 的关系

```text
functional-testcase-md  → …/testcases/{slug}.md（设计期）
docs/execution/*        → data-prep / ledger / plan / run-log（执行期）
testcase-agent-run      → 本 Skill：浏览器执行 + 记日志
```

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 跑 B1 / 执行 Audit 批次 | 读 plan B1，门禁后逐条执行 |
| 用 Agent 测 member-unify 的 P0 UI | L0：筛该 feature P0+🟢 |
| 只检查能不能跑、先别点 | `dry-run`：只出门禁报告 |
| 继续下一批 | 确认上批复位完成 → 下一批 |
| 重跑失败用例 | 读 run-log 失败行 + 台账当前状态后再跑 |

## 附加资源

- 门禁、绑定字段、run-log 模板：[reference.md](reference.md)
- 对话样例与切片清单：[examples.md](examples.md)
- 执行期约定：`docs/execution/README.md`
- 代号约定：`config/conventions.md`
