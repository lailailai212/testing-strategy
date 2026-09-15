---
name: feishu-bug-verify
description: >-
  从飞书缺陷链接拉取 Bug 信息，评估 Agent 理解分；大于 80 分则用浏览器复现并
  记录步骤、合成 GIF、输出验证结果。低于阈值则返回缺项清单不执行。
  Use when 用户提供飞书 Bug/缺陷/issue 链接，或要求验证 bug、复现缺陷。
---

# Feishu Bug Verify

用户给出飞书缺陷链接后：拉取信息 → 打理解分 → 过线则复现并出 GIF 与结论。
**本 Skill 不写回归用例、不改 POM、默认不回写飞书评论。**

完整打分、字段映射、登录与模板见 [reference.md](reference.md)，示例见 [examples.md](examples.md)。

## 前置

- 飞书 MCP（`FeishuProjectMcp`）已配置且可用
- Playwright MCP（`user-playwright`）可用
- 登录与环境只读 `config/env.local.yaml`，禁止把账号/OTP 写入任何产出 MD
- GIF 合成：`pip install Pillow`

## 输入（优先级）

1. **完整 URL**（首选）→ `get_workitem_brief({ url, fields: ["_all"] })`
   - 兼容 `.../issue/detail/{id}`、`.../bug/detail/{id}`
2. **`project_key` + `work_item_id`** → `get_workitem_brief({ project_key, work_item_id, fields: ["_all"] })`
3. **仅 `work_item_id`** → 提示用户补充 `project_key`

`fields: ["_all"]` 不可省略。接着调 `list_workitem_comments`。描述/评论中的飞书图必须下载并 **读取图片** 后再打分。

## 工作流

复制并勾选：

```
- [ ] 1. 解析链接并拉取全量字段 + 评论
- [ ] 2. 下载并识读截图
- [ ] 3. 写 brief.md（脱敏）
- [ ] 4. 按六维打分，写 score.md
- [ ] 5. 闸门：>80 且无硬否决 → 执行；否则停止并列出缺项
- [ ] 6. 登录目标环境，逐步复现；每步截图到 frames/
- [ ] 7. 合成 repro.gif，写 steps.md + result.md
```

**≤ 80 或存在硬否决时，禁止打开业务页验证。** 用户补信息后重新从步骤 3 打分。

## 拉数与脱敏

字段按显示名 `name` 匹配，不要死记 key。匹配失败再调 `list_workitem_field_config`（`work_item_type` 用 `issue` / `缺陷`）。

可选：`list_related_workitem` 拉关联 Story，帮助定位菜单入口。

导出 MD **不得包含**：姓名、邮箱、`@提及`、mention 块、用户 key/id、`create_by` / `updated_by` / `owners` 中的个人信息。

**保留**：标题、编号、状态、优先级、环境、复现步骤、预期/实际、截图。

图片下载同 `feishu-story-to-md`：`get_download_url` → `curl -L -o ... -H "X-Meego-File-Sign: {sign}"`。保存到 `{outdir}/images/ref-01.png`（扩展名按 Content-Type）。识读后把可见 UI/报错文案补进 brief，再打分。

## 理解分闸门

六维合计 100 分（入口 20 + 前置 15 + 步骤 25 + 结果 20 + 环境 10 + 证据 10）。必须写出每维得分与依据，禁止只给一个整数。

**过线：** 总分 **> 80** 且无硬否决 → **直接执行**，不再询问「要不要跑」。
**不过线：** 返回 `score.md` + 缺项勾选清单后停止。80 分整视为不过线。

硬否决（有一条就不执行）：真机/蓝牙/硬件；生产或不可逆破坏；真人滑块/真短信且配置无法覆盖；纯后端且页面无观察点；环境 URL 映射不上。

细则见 [reference.md](reference.md)。

## 执行（仅过线）

1. 从 `config/env.local.yaml` 取 `default_env` 的 `base_url` 与登录方式；角色按缺陷要求选账号，未写则用默认高权限账号
2. Playwright MCP：`browser_navigate` → 登录 → 按 brief 步骤操作
3. Locator：优先 `data-testid` / `aria-label` / `get_by_role` + 精确 `name`；禁止无依据的 `nth`、通用占位符、大段 `get_by_text`
4. 每步固定节奏：操作 → `browser_take_screenshot` 存 `frames/{nn}.png` → 记入 `steps.md`（动作 / 观察 / 是否符合预期）
5. 同一失败动作只换证据（新 snapshot / 截图）重试一次；累计 4 次无进展 → 结论 **Blocked**，停止蛮力点击
6. 合成 GIF：

```bash
python .cursor/skills/feishu-bug-verify/scripts/frames_to_gif.py \
  --frames-dir bug-verify/{basename}/frames \
  --output bug-verify/{basename}/repro.gif
```

无帧则不造空 GIF，在 `result.md` 写「无录屏」。

## 产出目录

`bug-verify/{project_key}-{work_item_id}-{slug}/`

```
bug-verify/{basename}/
  brief.md
  score.md
  steps.md          # 仅过线执行后
  images/           # 缺陷原图
  frames/           # 验证截图序列
  repro.gif
  result.md         # 仅过线执行后；不过线可省略，以 score.md 为准
```

`slug`：标题转小写（英文）、空格改 `-`、保留中文、去掉 URL 不安全字符、合并连续 `-`。已存在则覆盖前告知用户。

`bug-verify/` 已在 `.gitignore` 中，截图与 GIF 不入库。

## 结论（四选一）

| 结论 | 何时 |
|------|------|
| **Reproduced** | 实际与缺陷描述一致，bug 仍在 |
| **Not reproduced** | 按步骤做完，实际符合预期，现象未出现 |
| **Blocked** | 环境/权限/数据/登录拦住，没走到断言 |
| **Inconclusive** | 走到了，但无法判断是否就是该 bug |

向用户汇报：结论（或不过线原因）、理解分、GIF/目录路径、还缺什么（若有）。

## 用户指令

| 用户说法 | 行为 |
|----------|------|
| 飞书缺陷链接 / 验证这个 bug / 复现缺陷 | 全流程；过线直接执行 |
| 只评估能不能跑 / 先打分 | 停在 `score.md` |
| 我补充了步骤/截图/环境 | 合并进 brief 后重新打分，过线再执行 |
| 把结果写回飞书 | 才允许 `add_comment`（脱敏、不贴账号） |

## 附加资源

- 打分细则、字段名、登录、模板：[reference.md](reference.md)
- 过线 / 不过线示例：[examples.md](examples.md)
