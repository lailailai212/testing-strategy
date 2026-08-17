---
name: feishu-bug-fix-verify
description: >-
  从飞书项目拉取 Bug，按描述在目标环境（默认 SIT）复验修复是否生效；
  必须落盘验证截图证据，验证结束后关闭浏览器；结果写入 bug-verify-log，
  仅当用户显式 comment=true 时回写飞书评论。
  Use when 用户提供飞书 Bug 链接/ID、要求 Bug 复验、修复验证、verify fix、
  回归确认 Bug、Still Repro / Fixed 判定。
---

# Feishu Bug Fix Verify

对飞书 **Bug** 做修复后验证（也可用于首次复现确认）。**只验证、不改产品代码；默认不改飞书状态、不写评论。**

细则见 [reference.md](reference.md)，样例见 [examples.md](examples.md)。

## 硬性规则（不可违反）

1. **截图证据强制**：每条 Bug 至少 1 张关键断言截图写入证据目录；无截图不得输出 `Fixed`。
2. **浏览器必须关闭**：本轮若曾打开浏览器（Chrome DevTools / Playwright），在写出结论前必须以 `finally` 语义关闭；失败/阻塞同样关闭。
3. **凭证不落盘**：OTP/密码/Token 只读 `config/env.local.yaml`，禁止写入 bug-verify-log、飞书评论、对话落盘摘要。
4. **默认不回写飞书**：仅当用户显式 `comment=true` 时才 `add_comment`。

## 输入（优先级）

1. 飞书 Bug URL（如 `https://project.feishu.cn/obis/bug/detail/{id}`）
2. `project_key` + `work_item_id`（如 `obis` + `7068955890`）
3. 可选：`env=sit|uat`（默认 `env.local.yaml` → `default_env`）
4. 可选：`comment=true`（默认 **false**，不写飞书评论）

## 前置依赖

- 飞书 MCP：`get_workitem_brief({ url | project_key + work_item_id, fields: ["_all"] })`
- 可选：`list_workitem_comments`；仅 `comment=true` 时用 `add_comment`
- 浏览器：优先 **Playwright MCP**（便于 `browser_close`）；Chrome DevTools 亦可，关闭步骤见 reference
- `config/env.local.yaml`：`base_url`、登录方式、OTP、账号

## 工作流

```text
拉 Bug → 门禁 → 登录 → 按步骤验证 → 关键断言截图 → 判定 → 写 bug-verify-log
  →（仅 comment=true）飞书评论 → finally: 关闭浏览器 → 回复用户
```

### 1. 拉取与解析

- `get_workitem_brief`，`fields: ["_all"]` 不可省略
- 从 `Description`（及截图说明）抽取：环境、入口 URL、账号/租户、前置、步骤、预期、实际、通过标准
- Sprint 字段 → 证据与日志目录：`docs/execution/{sprint}/`；无 Sprint 时用 `docs/execution/_unsorted/`
- 脱敏：对话与落盘不写 Token/Cookie；飞书评论不写 OTP/Token

### 2. 门禁（不通过 → Blocked，禁止瞎点）

- [ ] 有环境（Bug 字段 Bug Environment 或 Description）
- [ ] 有直达入口 URL（或可唯一推断）
- [ ] 有可登录账号（Description / 台账代号 → `env.local.yaml`）
- [ ] 有可观察的预期（或「修复后通过标准」）
- [ ] 账号与资源租户可对齐（已知则检查；未知则登录后首次导航验证）

任一项失败 → `Blocked` + 原因；**若已开浏览器仍须关闭**。

### 3. 执行验证

1. 登录（同账号同租户复用会话）
2. `navigate` 直达 URL；Tab / Filter 用界面文案定位
3. 严格按 Bug 复现/回归步骤；每关键步对照预期
4. **取证（强制）**：在能证明 Fixed / Still Repro 的画面截图  
   路径：`docs/execution/{sprint}/evidence/bug-verify/{bug-id}/{yyyyMMdd-HHmm}-{slug}.png`  
   目录不存在则创建；截图失败则不得判 `Fixed`
5. 判定：
   - `Fixed`：预期全部满足 + **至少 1 张截图**
   - `Still Repro`：实际仍符合原 Bug「实际结果」+ 截图
   - `Blocked`：无法完成（权限/数据/环境）+ 原因；有部分截图则一并归档

Locator 优先级与项目规则一致：`data-testid` / `aria-label` / `get_by_role` → baseline → 避免 `nth` 与模糊大段文案。

### 4. 写 bug-verify-log

路径：`docs/execution/{sprint}/bug-verify-log.md`（无则创建；无 Sprint 用 `_unsorted`）

单条格式见 [reference.md](reference.md)#bug-verify-log-条目格式。禁止写 OTP/Token。

### 5. 飞书评论（默认跳过）

- 默认：**不调用** `add_comment`
- 仅 `comment=true`：简短结论 + 本地证据相对路径（不贴 Token）；用 markdown `content`

### 6. finally：关闭浏览器（强制）

无论 Pass / Fail / Blocked：

1. Playwright：调用 `browser_close`
2. Chrome DevTools：`list_pages` → 对可关闭页 `close_page`；最后一页导航 `about:blank`，并尝试 Playwright `browser_close` 清理
3. 在回复中明确：「浏览器已关闭」或关闭失败原因

先写完 log / 结论草稿，**再关浏览器**，再发最终回复。

## 输出给用户

- 结论：`Fixed` / `Still Repro` / `Blocked`
- Bug 链接与标题
- 证据截图路径（必给；无路径不得声称 Fixed）
- 与预期不符的步骤号（若有）
- 浏览器关闭状态
- 是否已写飞书评论（默认否）
