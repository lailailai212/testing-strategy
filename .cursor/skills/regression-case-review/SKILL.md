---
name: regression-case-review
description: >-
  对照指定环境（SIT / UAT / 用户给出的 URL）评审回归用例 Excel：去重、纠错、汰过时、查漏补缺，
  用 Canvas 呈现结论并协作确认范围，再生成修订版 Excel（不覆盖原文件）。
  Use when 用户提到回归用例评审、上线/UAT 回归 Excel、对照 SIT 或 UAT 改用例、去重查漏、
  回归包修订，或提供 Downloads 下的回归 xlsx 要求按现网核对。
---

# Regression Case Review

将**既有回归用例 Excel**对照**用户指定的目标环境**做评审与修订：去重、纠错、汰过时、查漏。

本 Skill **只评审与改包，不执行用例**。执行走 `testcase-agent-run`；从 Story 新写用例走 `functional-testcase-md`。

细则见 [reference.md](reference.md)，样例见 [examples.md](examples.md)。依赖见 reference「依赖清单」。

## 新用户快速上手

### 这是干什么的

拿一份**已有回归用例 Excel**，对照 **SIT 或 UAT 现网**，找出：重复、错误、过时、遗漏；确认范围后产出**修订版 Excel**（原文件不动）。

### 用前准备（约 5 分钟）

1. 本仓库已拉取；确认存在 `.cursor/skills/regression-case-review/`
2. `pip install openpyxl`
3. 复制配置：`Copy-Item config/env.example.yaml config/env.local.yaml`，填目标环境的 `base_url`、账号/OTP
4. Cursor 已启用浏览器 MCP（Chrome DevTools 或 Playwright）
5. 能打开目标环境网页

### 怎么发起（复制改路径即可）

```text
用 regression-case-review 评审：
- Excel：C:\Users\你\Downloads\上线回归-Product-Asset.xlsx
- 对照环境：SIT（或 UAT）
- URL：https://iot-admin-sit.snowballtech.com/
- 不要参考仓库里的用例文件，只以现网为准
- （可选）SBOM/OTA 本轮不上线；某某功能未设计不做
```

UAT 把「对照环境 / URL」换成 UAT 即可。

### Agent 会做什么

1. 读 Excel → 登录你指定的环境 → 扫页面建基线  
2. 标出过时 / 错误 / 重复 / 遗漏，用 **Canvas** 给你看  
3. 你在 Canvas 上纠偏（不上线、未设计、二次确认等）  
4. 生成 `{原名}-评审修订.xlsx`，告知路径与条数口径  

### 你需要配合什么

| 时机 | 你说什么 |
|------|----------|
| 开头 | Excel 路径 + SIT 还是 UAT（或直接给 URL） |
| 评审中 | 「XX 不上线」「YY 未设计暂不考虑」「Remove 有二次确认」等短句即可 |
| 结束后 | 打开修订 xlsx 抽查；未验证项若还有，再补一句确认 |

### 不要指望它做的事

- 不会在环境里**执行**整包回归（那是 `testcase-agent-run`）
- 不会从 Story **新写**用例（那是 `functional-testcase-md`）
- 不会默认混用 SIT 结论去改 UAT 包（两环境要评就说「分两轮」）

---

## 硬约束

1. **先锁定对照环境**（`target_env` + `base_url`），全文结论只对该环境负责；未指定时按下方「环境解析」推断，推断不出则**先问用户**，禁止默认当成 SIT。
2. **对照源 = 该环境现网 UI**；用户明确说「不要参考仓库用例」时，**禁止**用本仓 `testcases/` / acceptance 当对错依据。
3. **不覆盖原 Excel**；产出 `{原名}-评审修订.xlsx`（同目录或用户指定路径）。
4. **未实测确认的现象不得写成定论**；放「未验证项」，等用户确认后再改结论/Excel。
5. **用户声明不上线 / 未设计的功能**：整块移出范围，删相关 finding 与新增建议，并回写统计。
6. **条件展示字段**（选完前置才出现）：不得判为「已删除」；写清触发条件，必要时换数据复测。

## 环境解析（每轮必做）

按优先级确定 `target_env` ∈ `{sit, uat, …}` 与 `base_url`：

| 优先级 | 来源 |
|--------|------|
| 1 | 用户明示：「对照 UAT」「整理 SIT 回归」「这个包是 UAT 的」 |
| 2 | 用户给出的完整 URL（从 host 识别 sit/uat，或原样用作 `base_url`） |
| 3 | 文件名/包名含 `UAT` / `SIT` / `上线` 等（上线包通常对发布目标环境；仍须与用户确认若有歧义） |
| 4 | `config/env.local.yaml` 的 `default_env` + `environments.{env}.base_url` |

Canvas 头、基线表标题、新增用例备注、交付话术必须写清：`对照环境: {target_env} · {base_url}`。

**禁止**：用 SIT 基线改 UAT 包（或反过来）却不声明；两环境都要评时，**分两轮**或分两个 Canvas，勿混进同一张 findings 表。

## 输入

| 项 | 说明 |
|----|------|
| 回归 Excel | 路径必给；列通常对齐 MeterSphere 导入模板 |
| `target_env` / URL | 见「环境解析」；UAT 示例 `https://iot-admin-uat.snowballtech.com/`（以 `env.local.yaml` 为准） |
| 范围说明 | 可选：本轮上线模块、明确不上线/不做的功能、产品/芯片样本 |

凭证：读 `config/env.local.yaml` 中**对应 env** 的账号；勿把密码写进 Canvas / 修订说明。

## 工作流

```text
锁定 target_env → 读 Excel → 登录该环境建基线 → 逐条对照分类 → Canvas 评审
  → 用户确认未验证/范围 → 生成修订 Excel →（可选）按反馈再 patch
```

### 1. 解析 Excel

用 `openpyxl`（`data_only=True`）导出全量行到临时 JSON/内存表。至少保留：

`ID | 用例名称 | 前置条件 | 所属模块 | 步骤描述 | 预期结果 | 备注 | 用例等级 | Is Regression | …其余原列`

统计：总条数、模块分布、名称高度相似对（候选重复）。

### 2. 环境基线（先结构后细节）

浏览器优先 Chrome DevTools MCP / Playwright MCP。用**该 env** 登录后对目标页（如 Product → Assets）：

1. 自上而下列出**区块**（含父/子表、Tab、标签栏）
2. 每块记：**区块级操作**、**行内操作**、**列名**、**新增/编辑弹窗字段与按钮文案**
3. 页内环境切换（如 PROD/TEST 数据区）、权限账号差异若未测，记入未验证项
4. 截图或 a11y snapshot 仅作核对辅助；**结论以实测控件文案为准**

基线表字段见 [reference.md](reference.md)「环境基线表」。文案一律称「{target_env} 基线」，勿写死 SIT。

### 3. 对照分类（每条必归一类或「保留」）

| 类 | 含义 | 处置倾向 |
|----|------|----------|
| **过时** | 文案/入口/列/流程与**对照环境**不符 | 改步骤/预期或改标题；失效步骤删除 |
| **错误** | 笔误、自相矛盾、步骤与预期对不上 | 就地修正 |
| **重复** | 同意图 + 同主断言（见去重键） | 合并留 1；其余删除并在备注写「并入 {ID}」 |
| **遗漏** | 对照环境有能力但包内无覆盖 | 建议新增（用户确认后再写入修订包） |
| **移出范围** | 本轮不上线 / 未设计 | 删除或标不回归；不进遗漏 |

**去重键** = `页面/区块 + 子功能 + 主断言`（不要只用用例名）。  
相似名但主断言不同 → **不合并**，可交叉引用。

条件 UI、二次确认弹窗、权限差可见性：无实测证据时进**未验证项**，不要猜。

### 4. Canvas 呈现（协作评审）

用 Cursor Canvas 输出评审产物（路径建议：`canvases/{包名}-{target_env}-regression-review.canvas.tsx`）。必含：

1. **头统计**：对照环境 · 原条数、过时/错误/重复条数、建议新增、修订后预计总数
2. **Findings 表**：分类 · ID · 问题 · 建议改法
3. **{target_env} 基线表**
4. **遗漏建议**（按区块，条数可加总）
5. **未验证项**（明确「结论未依赖此项」；含「未与另一环境交叉验证」若相关）
6. **已执行/待执行处置清单**（合并 −N、移出 −N、文案替换、新增 +N…）

用户在 Canvas 上点选纠偏时：**先改 Canvas 结论与统计，再改 Excel**（或同轮一起改并声明一致）。

### 5. 生成修订 Excel

1. 复制原表结构与样式习惯；**原文件不动**
2. 应用：删除（重复/移出范围）、改写步骤与预期、批量替换过时文案、补前置条件
3. **新增用例**：`ID` 留空（MeterSphere 导入按新用例）；模块路径与原包一致；备注写清来源（如 `评审补漏 · {target_env} {区块}`）
4. 自检：全文检索已废弃文案；统计 `原 − 删 − 移出 + 新增 = 现有`；无「未设计功能」残留

脚本约定见 [reference.md](reference.md)「修订脚本」。

### 6. 交付话术

告知用户：

- **对照环境**（`target_env` + URL）
- 修订文件绝对路径与条数口径
- 原文件未改
- Canvas 路径（便于继续确认未验证项）
- 仍待确认的未验证项列表（若有）
- 若用户还要另一环境：说明需另开一轮，不可直接复用本轮基线

## 与相邻 Skill 边界

| Skill | 关系 |
|-------|------|
| `functional-testcase-md` | 新功能从测试点展开；本 Skill 改**存量回归包** |
| `testcase-agent-run` | 按已定稿用例执行；本 Skill 产出可再交给它跑（注意执行 env 与评审 env 对齐） |
| `story-acceptance-design` | 不替代；范围争议时可回查 Story，但默认仍以**对照环境现网**为准 |

## 完成检查

- [ ] 已声明 `target_env` + `base_url`，Canvas/备注/交付一致
- [ ] 基线覆盖目标页主要区块，条件列已标注触发条件
- [ ] 每条 finding 有该环境证据或标在未验证项
- [ ] 用户确认的范围变更已同步 Canvas + Excel + 统计
- [ ] 修订包未覆盖原文件；新增 ID 为空
- [ ] 废弃文案（旧按钮名/旧列名/已砍功能）无残留
- [ ] 未把另一环境的观察当成本轮定论
