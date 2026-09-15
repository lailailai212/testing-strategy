# Reference — Feishu Bug Verify

## 六维打分（合计 100）

必须逐维给分并引用缺陷原文一句作为依据。禁止只给总分。

| 维度 | 分值 | 满分 | 约一半 | 0 |
|------|------|------|--------|---|
| 入口与页面 | 20 | 模块 + 页面 + 进入路径明确，或截图能对上导航 | 只有模块名或只有一张无法定位的图 | 不知道去哪个产品/菜单 |
| 前置条件 | 15 | 角色 / 租户 / 数据可执行，或能从 `env.local.yaml` 推断 | 缺一类，可用默认高权限账号试 | 关键前置未知（特定证书、设备、脏数据） |
| 复现步骤 | 25 | 编号步骤，每步是点击 / 填写 / 选择 | 有步骤但含糊（「设置一下」「保存后异常」） | 只有现象，无操作序列 |
| 可观察结果 | 20 | 预期与实际都有，能断言通过/失败 | 只写了其中一侧 | 「不对」「有问题」，无法断言 |
| 环境 | 10 | 写明 SIT/UAT，或可映射 `default_env` | 未写但项目有默认环境 | 必须特定构建号且未知 |
| 证据 | 10 | 有截图且能对应 UI / 报错文案 | 纯文字描述 | 无图无日志无字段值 |

**过线：** 总分 **> 80** 且无硬否决。80 分整视为不过线。

**扣分写法：** 每维写「得分 / 满分 — 依据 — 若未满分则缺什么」。

### 硬否决（有一条即禁止执行）

- 必须真机 / 蓝牙 / 硬件外设
- 必须生产环境，或不可逆破坏（删库、批量清数据且无法在 SIT 用前缀造数替代）
- 必须真人滑块 / 真短信，且 `env.local.yaml` 的登录方式无法覆盖
- 纯后端 / DB，页面上没有任何可观察结果
- 没有环境 URL，且 `environments` 映射不上

硬否决时：`score.md` 顶部写 **硬否决：…**，即使其他维很高也不打开业务页。

### 不过线时对用户只返回

1. 总分与是否过线
2. 六维表
3. 缺项勾选清单（写成「请补充：…」，不要写「信息不够」）

---

## 飞书字段映射

自定义字段按显示名 `name` 匹配（同一空间 key 可能不同）。任一别名命中即可。

| 显示名（任一命中） | 写入 brief |
|--------------------|------------|
| Description / 描述 / 缺陷描述 | 现象 |
| Reproduction Steps / 复现步骤 / Steps to Reproduce | 操作序列 |
| Expected Result / 预期结果 | 断言期望 |
| Actual Result / 实际结果 | 对照实际 |
| Environment / 环境 | 映射 `config/env.local.yaml` |
| Severity / 严重程度 / Priority / 优先级 | 元信息 |
| 附件 / Attachment / 截图 | 证据图（下载到 `images/`） |

固定信息（`work_item_attribute`）→ 元信息区：`work_item_name`、`work_item_id`、`owned_project`、`work_item_status`、`create_time` / `update_time`（只写日期）。

匹配失败：`list_workitem_field_config({ project_key, work_item_type: "issue" 或 "缺陷", page_num: 1 })`。

可选：`list_related_workitem` 拉关联 Story，补入口路径。

---

## 图片下载与识读

与 `feishu-story-to-md` 相同：

1. 从描述/评论提取 `https://project.feishu.cn/...` 图片 URL
2. `get_download_url({ project_key, work_item_id, file_url })`
3. `curl -L -o ... -H "X-Meego-File-Sign: {sign}" "{url}"`
4. `is_multipart` 为 true 时按 `part_index` / `start_byte` / `end_byte` 分片后合并
5. 保存到 `{outdir}/images/ref-01.png`（扩展名按 Content-Type，未知默认 `.png`）
6. **读取**每张图，把可见导航、控件、报错文案补进 brief 对应小节后再打分

单张失败写 `<!-- 参考图 N 下载失败 -->`，不中断。无图时证据维按「纯文字」或「无」给分。

---

## 登录与环境

只读 `config/env.local.yaml`，禁止把 email / OTP / 密码写入 `brief.md` / `score.md` / `steps.md` / `result.md`。

1. `default_env` → `environments.{env}.base_url`、`login_method`
2. 缺陷写了 UAT/SIT 则覆盖默认 env
3. 角色：缺陷指定则选对应 `accounts.*`；未写则用默认高权限账号
4. Playwright：`browser_navigate(base_url)` → 按 `login_method` 登录（当前仓库为邮箱 + 通用 OTP）→ 再走复现步骤

登录失败 → 结论 **Blocked**，不要改用生产地址重试。

---

## 执行约定

- 工具：Playwright MCP（`user-playwright`）。不要用 `browser_run_code_unsafe` 录屏。
- Locator：`data-testid` / `aria-label` / `get_by_role` + 精确 `name`。禁止无依据的 `nth`、通用占位符、大段 `get_by_text`。
- 每步：操作 → `browser_take_screenshot` 存 `frames/{nn}.png`（`01.png` 起）→ 记入 `steps.md`。
- 同一失败动作：换 snapshot / 截图后只再试一次。累计 4 次无进展 → **Blocked**。
- 不写 `src/locators` / `src/pages` / 回归用例。

### GIF

```bash
python .cursor/skills/feishu-bug-verify/scripts/frames_to_gif.py \
  --frames-dir bug-verify/{basename}/frames \
  --output bug-verify/{basename}/repro.gif
```

依赖：`pip install Pillow`。无 `frames/*.png` 则不调用脚本，在 `result.md` 写「无录屏」。

---

## 产出模板

`basename` = `{project_key}-{work_item_id}-{slug}`，slug 规则同 `feishu-story-to-md`。

### brief.md

```markdown
# Bug: [标题]

**来源**: [飞书项目 缺陷 #{id}]({url})
**空间**: [名称] (`{project_key}`)
**状态**: [状态]
**优先级**: [值]
**环境（缺陷原文）**: [原文或「未写，将用 default_env」]
**创建**: [日期]
**更新**: [日期]

---

## 现象

- ...

## 复现步骤

1. ...

## 预期结果

- ...

## 实际结果

- ...

## 前置（推断）

- 角色 / 租户 / 数据：...

## 参考图

![参考图 1 — 简要说明](./images/ref-01.png)

## 评论补充

- [日期]：[与复现相关的文字，已去 @提及]
```

### score.md

```markdown
# Bug 理解分：{n} / 100（过线，将执行 | 不过线，未执行 | 硬否决，未执行）

| 维度 | 得分 | 依据 |
|------|------|------|
| 入口与页面 | x/20 | … |
| 前置条件 | x/15 | … |
| 复现步骤 | x/25 | … |
| 可观察结果 | x/20 | … |
| 环境 | x/10 | … |
| 证据 | x/10 | … |

## 硬否决

无 | [原因]

## 请补充

- [ ] …（不过线或硬否决时必填；过线可省略本节）
```

### steps.md

```markdown
# 验证步骤

**环境**: SIT（不写账号）
**开始**: [时间]

| # | 动作 | 观察 | 符合预期 | 帧 |
|---|------|------|----------|----|
| 1 | 打开登录页 | 出现邮箱输入 | 是 | frames/01.png |
| 2 | … | … | 是/否 | frames/02.png |
```

### result.md

```markdown
# 验证结果：Reproduced | Not reproduced | Blocked | Inconclusive

**Bug**: [{id} {标题}]({url})
**理解分**: {n} / 100（已执行）
**环境**: SIT / UAT（不写账号）
**时间**: YYYY-MM-DD

## 结论

[一段话：做了什么、看到什么、与缺陷是否一致]

## 证据

- 步骤：./steps.md
- 录屏：./repro.gif（或「无录屏」）
- 关键帧：./frames/{nn}.png

## 与缺陷对照

- 预期：…
- 实际：…
- 偏差：一致 / 不一致 / 无法判断
```

默认不调用 `add_comment`。用户明确要求写回时：评论只含结论、理解分、关键观察；不贴账号、OTP、本地路径中的用户名。
