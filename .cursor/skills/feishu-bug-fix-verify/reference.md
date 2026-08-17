# feishu-bug-fix-verify — 参考

配合 [SKILL.md](SKILL.md) 使用；执行时按需打开本节，勿整份塞进每轮上下文。

## 飞书字段怎么用

`get_workitem_brief` + `fields: ["_all"]` 后：

| 来源 | 用途 |
|------|------|
| `work_item_attribute.work_item_name` | 标题 |
| `work_item_attribute.work_item_status` | 状态（只读，默认不改） |
| `work_item_fields` 中 `Description` | 前置 / 步骤 / 预期 / 实际 / 测试数据 |
| 显示名 `Bug Environment` | sit / uat |
| 显示名 `Sprint` | 决定 `docs/execution/{sprint}/` |
| 显示名 `Priority` / `Severity` | 写入 log 元信息即可 |

字段 key 可能因空间而异，**按显示名 `name` 匹配**。

### Description 解析优先级

1. 显式小节：`【前置条件】` `【复现步骤】` `【预期结果】` `【实际结果】` `【测试数据】` `【通过标准】`
2. 英文等价：Preconditions / Steps / Expected / Actual
3. 入口 URL：优先「测试数据 / 资源数据」中的完整 https 链接；其次步骤中的路径 + `env.local.yaml` base_url
4. 账号：测试数据中的邮箱 > 台账代号映射 > `accounts.super_admin`（仅当 Description 未指定且资源在同租户可访问时）

丢弃并禁止落盘：`Authorization`、`Cookie`、Bearer Token、完整 HAR。

## 浏览器选型与关闭

| 工具 | 适用 | 关闭 |
|------|------|------|
| Playwright MCP | **本 Skill 优先**（交互 + 关浏览器） | 结束必调 `browser_close` |
| Chrome DevTools MCP | snapshot / 调试亦可 | `list_pages` → `close_page`（**不能关最后一页**）→ 最后一页 `about:blank`；有 Playwright 会话再 `browser_close` |

关闭检查清单：

- [ ] 截图已写入磁盘（或已判定无法截图且结论非 Fixed）
- [ ] bug-verify-log 条目已写
- [ ] `browser_close` 和/或 DevTools 清理已执行
- [ ] 用户回复含「浏览器已关闭」或失败原因

## 截图证据

| 结论 | 最少截图 | 拍摄时机 |
|------|----------|----------|
| `Fixed` | ≥ 1 | 断言满足、错误结果不再出现的画面 |
| `Still Repro` | ≥ 1 | 原 Bug「实际结果」仍可见时 |
| `Blocked` | 0～1 | 若页面已打开，拍卡点页；登录都失败可无图 |

路径约定：

```text
docs/execution/{sprint}/evidence/bug-verify/{bug-id}/{yyyyMMdd-HHmm}-{slug}.png
```

- `{slug}`：短横线英文或拼音，如 `operator-name-filter`
- 无 Sprint：`docs/execution/_unsorted/evidence/bug-verify/...`
- 截图工具写文件失败时：仍须在对话中保留可视截图，并在 log 注明「仅会话内附图、未落盘」；**未落盘则不得标 Fixed**（除非用户当场确认接受会话附图为唯一证据——默认不接受）

## Locator 与操作

与 `testcase-agent-run` 相同：

1. `data-testid` / `aria-label` / `get_by_role` + 精确 `name`
2. baseline `stableLocator`（若有）
3. 限定容器内的 role/文案
4. 避免：`nth(x)`、模糊大段 `get_by_text`、通用 placeholder（如 `Please Enter`）

操作前用最新 snapshot；失败先重新 snapshot，禁止无依据盲点。

## 判定细则

| 结论 | 条件 |
|------|------|
| `Fixed` | Description「预期」或「通过标准」全部可观察满足，且有落盘截图 |
| `Still Repro` | 仍满足原「实际结果」或与「预期」明确冲突，且有截图 |
| `Blocked` | 缺账号/URL/权限/数据/环境未部署等，无法完成关键步骤 |

部分步骤通过、关键断言失败 → `Still Repro`（或用户要求拆分时在摘要中列步骤号）。

## bug-verify-log 条目格式

文件：`docs/execution/{sprint}/bug-verify-log.md`

若文件不存在，创建时用：

```markdown
# Bug 修复验证日志 · `{sprint}`

> 由 feishu-bug-fix-verify 追加。禁止写入 OTP / Token / Cookie。
```

每条追加：

```markdown
### BUG-{id} · {yyyy-MM-dd HH:mm}

- 结论：`Fixed` | `Still Repro` | `Blocked`
- 标题：{work_item_name}
- 链接：https://project.feishu.cn/{simple_name}/bug/detail/{id}
- 环境：{sit|uat}
- 入口：{url}
- 账号：{email 或台账代号}（勿写 OTP）
- 证据：`evidence/bug-verify/{id}/{file}.png`
- 摘要：{1～3 句可观察现象}
- 飞书评论：未写 | 已写
- 浏览器：已关闭 | 关闭失败：{原因}
```

## 飞书评论（仅 comment=true）

`add_comment`：

- `project_key`：空间 simple_name 或 key（如 `obis`）
- `work_item_id`：Bug id
- `content`：markdown，建议：

```markdown
【Agent 修复验证】结论：Fixed

- 环境：SIT
- 摘要：…
- 本地证据：docs/execution/{sprint}/evidence/bug-verify/{id}/….png
```

禁止评论中出现 OTP、Bearer、Cookie。
