---
name: functional-testcase-md
description: >-
  将测试点（XMind / tree JSON / 测试点表）展开为可执行功能测试用例 Markdown 表格。
  跟随 acceptance 变更类型（UI/UX | Logic | Hybrid）调整用例比例；
  UI 与 Functional 用例区分步骤颗粒度与校验点；一条用例一个用户场景，步骤 ≤ 10。
  必含备注列标明来源（AC 写「来源 AC-0x: {AC 原文}」）。
  Use when 用户提到功能测试用例、用例 md、测试用例落地、从 xmind/测试点生成用例，
  或要把测试点展开为 import_ms_excel 可导入格式。
---

# Functional Testcase MD

将**粗颗粒度测试点（TP-ID）**展开为**可执行功能测试用例**，输出 Markdown 表格，对齐 `docs/templates/import_ms_excel_case.xlsx`。

完整字段规则见 [reference.md](reference.md)，黄金样例见 [examples.md](examples.md)。

## 工作流

1. **确认 Sprint / feature-slug 与输入来源**（优先级从高到低）
   - `docs/sprints/{sprint}/features/{feature-slug}/acceptance.md` → 读取测试点表（含 TP-ID、优先级）与文档头 **变更类型**
   - 用户指定 XMind / tree JSON（同 feature 包 `xmind/`）→ 读取叶子 `title`、`source`、`priority`（**不含 TP-ID**）
   - 对话中已有测试点表 → 直接使用
   - 仅有 Story AC → 先按 `story-acceptance-design` 补全 `acceptance.md`，再展开用例
2. **读取变更类型并定展开偏置**（见 [reference.md](reference.md)「变更类型与展开偏置」；acceptance 未声明则按 TP/AC 语义自判并写入用例 MD 头）
   - **UI/UX**：`【UI】` 为主；步骤细到控件态与文案；少造深逻辑矩阵用例
   - **Logic**：`【Functional】/【E2E】` 为主；步骤以业务操作为主，预期落业务结果与副作用；UI 断言只保留证明规则生效的最小反馈
   - **Hybrid**：比例跟主类型；次类型分条覆盖，不混进无关场景
3. **收集产品 baseline**（缺失则标注待确认，勿臆造）
   - 路径：`docs/sprints/{sprint}/features/{feature-slug}/baseline/`（见 feature `META.md`）
   - 页面入口路径（页 → 区域 → 按钮 → 弹窗）
   - 字段差异规则（如 Key 无系统默认 Tag、Cert 有）
   - **MeterSphere 模块映射**：全局 `docs/modules/metersphere-modules.json`；本 feature 可有 `testcases/module-mapping.json`
   - **Story / 飞书 AC 原文**（供备注列引用，勿改写）
4. **按用户场景设计用例**（见「用例设计原则」+「UI vs Functional 步骤与校验」）：先识别独立用户场景，**一条用例 = 一个场景**；场景内合并可连续校验的 TP；**按用例类型选用不同步骤颗粒度与校验点**；**每条用例步骤 ≤ 10**
5. **对齐上游强制清单**：若测试点含「仅 1 次 / 首次 / 仅发给 XX / 失败重试」等，展开时核对 [story-acceptance-design reference](../story-acceptance-design/reference.md) 类型 A/B——缺 TP 先回补测试点，再写用例；用例标题或「场景与 TP 覆盖」表须能直读：二次成功、失败恢复、操作者换人（禁止只埋在步骤末尾）
6. **填写备注列（必填）**：标明来源；来自需求 AC 时写 `来源 AC-0x: {飞书/Story AC 原文}`（见「备注」）
7. **分配用例等级** P0 / P1 / P2 / P3（规则见 reference.md）
8. **写入固定目录**（见下节）
9. **文档头 blockquote** 写：来源、需求名、**变更类型**、用例数统计、入口/产品规则（若有）、命名格式说明、备注来源约定、场景与 TP 覆盖说明
10. **告知用户**：文件路径、变更类型偏置、用例数、等级分布、`【UI】/【Functional】/【E2E】` 比例、TP 覆盖情况、待确认项
11. **（可选）导出 MeterSphere Excel**：见「MeterSphere 导出」

## MeterSphere 导出

依赖：`pip install openpyxl`

```bash
python .cursor/skills/functional-testcase-md/scripts/md_to_metersphere_excel.py \
  --feature-slug {feature-slug}
# 未注册时加：--sprint {sprint-id}
```

| 输入 | 输出 |
|------|------|
| `…/features/{slug}/testcases/{slug}.md` | `…/features/{slug}/testcases/{slug}-metersphere.xlsx` |

模板：`docs/templates/import_ms_excel_case.xlsx`（列映射见 [reference.md](reference.md)）

## 固定产出目录（强制）

根路径：`docs/sprints/{sprint-id}/features/{feature-slug}/`

| 类型 | 固定路径 |
|------|----------|
| 功能测试用例 MD | `testcases/{feature-slug}.md` |
| MeterSphere 导入 Excel | `testcases/{feature-slug}-metersphere.xlsx` |

- `{feature-slug}`：小写英文连字符；sprint 由 `docs/sprints/features-registry.json` 反查（或 `--sprint`）
- 目录不存在时自动创建；同路径**覆盖**更新，**禁止** `*-new.md`

## 表格列（顺序固定）

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |

## 核心范式（必遵守）

### 用例名称

```text
【{页面模块}】【{类型}】{子功能} - {一句话描述}
```

- `{类型}` 取以下三者之一（**禁止**写笼统的 `【功能】`）：

| 类型 tag | 适用场景 |
|----------|----------|
| `UI` | 控件可见性/隐藏、置灰态、文案展示、弹窗布局与按钮组合 |
| `Functional` | 单点业务规则：字段校验、配额计数、边界值、提交阻断 |
| `E2E` | 从入口到结果的完整用户旅程（含多步向导或跨页主路径） |

- 分配原则：优先按**测试意图**选类型；一条用例只标一种；UI 与 Functional 边界不清时，侧重业务规则归 `Functional`，侧重展示归 `UI`
- Story 级变更类型影响**比例**：UI/UX Story 多数为 `UI`；Logic Story 多数为 `Functional`/`E2E`；禁止整包用例类型与变更类型明显错位
- **TP-ID / AC 编号不进用例名称，也不进「标签」列**（追溯写在备注列与文档头「场景与 TP 覆盖」）
- 模块 slug 由**所属模块路径**推导：`/Cloud/Product/{子模块}` → `【Product-{子模块}】【{类型}】…`（如 Overview → `Product-Overview`）
- **禁止**双层模块前缀（如 `【Product】【Version】【UI】`）

### UI vs Functional：步骤颗粒度与校验点（必遵守）

| 维度 | `【UI】` 用例 | `【Functional】` / `【E2E】` 用例 |
|------|---------------|----------------------------------|
| 步骤颗粒度 | **细**：进入区域 → 聚焦控件 → 触发交互（展开/悬停/输入/切换）→ 必要时再操作 | **中**：按业务动作编排（打开 → 填关键项 → 提交/触发）；准备动作下沉前置条件 |
| 预期/校验点 | **界面可观察**：可见/隐藏、置灰、文案、布局/按钮组合、空态/加载态、焦点与即时反馈 | **业务可观察**：成功/阻断、计数变化、列表/详情数据、触达/不触达、权限结果；Toast/跳转仅作规则成立的最小证据 |
| 一步多断言 | 同步可并列多个**态/文案**断言 | 同步可并列多个**业务结果**；勿塞一长串无关 UI 巡检 |
| 禁止 | 用 UI 用例承担完整规则矩阵（去重/配额/多角色） | 用 Functional 用例逐步「逛界面」却不验证业务结果 |
| 混合出现时 | 拆条：展示态一条 `UI`，规则一条 `Functional`；仅当同属一场景且步骤仍 ≤ 10 时可同条，名称按主意图选型 | 同左 |

细则与正反例见 [reference.md](reference.md)「UI vs Functional 步骤与校验」。

### 所属模块

层级路径，以 `/` 开头；Product 子页面挂在 `/Cloud/Product/` 下：

```text
/Cloud/Product/Assets
/Cloud/Product/Version
/Cloud/Product/Overview
```

### 标签

**只填可读业务标签**（Feature / Story 短名或业务主题），供 MeterSphere 按功能筛选。

```text
{Feature 或 Story 短名}
```

示例：`创建Module与AddAssetType权限`、`Transactional Email`、`Product Asset Tag`

| 允许 | 禁止 |
|------|------|
| 可读功能名、业务主题（中英文均可） | `TP-MOD-POS-01`、`TP-PA-KEY-01` 等 TP-ID |
| 确需多主题时用分号分隔可读名 | `AC-01`、`AC-05` 等 AC 序号 |
| | 纯序号、编码类、不可阅读的技术 ID |

- **禁止**把 TP-ID、AC-0x 或其它序号类编码写入标签列（追溯放在「备注」与文档头覆盖表）
- 不写用例等级（等级单独列）

### 步骤 / 预期

- 单元格内用 `[1]…<br>[2]…` 编号
- **步骤编号与预期编号一一对应**
- 步骤写完整导航（例：Product Asset 页 **Keys** 区域 → **Assign Key**）
- **单条用例最长步骤不超过 10 步**（`[1]`～`[10]`）；超出则拆条或把准备动作下沉到前置条件
- **文案写给人看的原文，禁止代号**：用例名称、前置条件、步骤、预期结果中**禁止**写 `COPY-01`、`文案符合 COPY-xx`、`符合文案表编号` 等；须写界面可见原文（如「SE Profile 已锁定」）。中英文都要验时，预期内直接写出中/英原文。需求侧的 COPY-NN 仅可出现在**备注**所引 AC 原文中，不得作为执行人查找表的替代

### 用例等级

单独列，取值 `P0` | `P1` | `P2` | `P3`，按实际场景分配，禁止全部标 P0。

### 备注（来源，必填）

用例新增「备注」列，**表明来源**。每条用例必须填写，禁止留空。

若是来源于需求 AC，则标为：

```text
来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次
```

即：`来源 AC-0x: ` + **飞书 / Story 验收标准原文**（勿自行改写）。

| 来源类型 | 写法 |
|----------|------|
| 需求 AC | `来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次` |
| 需求正文未列入 AC | `来源 需求描述: {一句话}` |
| QA 补充 | `来源 QA扩展: {一句话}` |

- 命中多条 AC 时逐条列出，用 `<br>` 换行
- 导出 MeterSphere 时写入 Excel「备注」列

## 用例设计原则（必遵守）

用例每个用例其实都是几条用户场景，尽量保证用一条用例覆盖一个场景，但可以校验更多的测试点。测试用例步骤需要依旧保持步骤的清晰和逻辑性。

同时：单用例最长步骤不超过 10 步。

| 原则 | 说明 |
|------|------|
| **一场景一条** | 一条用例对应**一个**用户场景（如「自注册后收 Welcome」）；勿把多个独立场景（Welcome + 首次 DAC + 首次烧录）硬塞进一条 |
| **场景内多校验** | 同一场景内尽量覆盖触发、收件人、内容、去重等可连续观察的 TP，避免一点一案 |
| **步骤清晰逻辑** | 按真实操作顺序写：进入 → 操作 → 观察；步骤之间因果连贯，不跳步、不堆砌无关动作 |
| **一步多断言** | 单步操作后若有多个可观察结果，写在同一编号预期内（分号并列），不为此拆步 |
| **步骤上限** | 每条用例步骤数 **≤ 10**；准备数据、登录、造数优先写入**前置条件** |
| **必须拆分** | 互斥前置、独立负向、不同角色/Tenant 类型、不同业务时刻的独立场景 → 分条 |
| **覆盖完整** | 每条 TP-ID 至少被 1 条用例覆盖；文档头或回复中说明场景与 TP 对应关系 |

### 场景切分口诀

| 应拆成多条用例 | 可留在同一条用例 |
|----------------|------------------|
| 不同业务时刻（注册 vs 首次签发 vs 首次烧录） | 同一操作后的多项断言（发件人 + 主题 + 正文变量） |
| 互斥前置（Demo vs 真实、运营开通 vs 自注册） | 同场景内紧随的去重验证（首次发信后立刻再操作一次确认不重发；标题或场景表须点明「二次成功不重发」） |
| 独立失败路径（**投递/通道**失败重试 vs **业务**签发/烧录失败） | 同页/同弹窗内连续可见的 UI + 规则校验 |
| **业务失败后再成功**（恢复仍触发且仅 1 次） | — |
| **非创建者/非约定角色操作**，验收件人仍为创建者 | 创建者本人操作时顺带断言「其他成员未收到」 |

## 展开原则

| 测试点类型 | 展开方式 |
|------------|----------|
| 控件/交互 | 优先 `【UI】`：打开入口 → 交互 → 断言可见/可选/态/文案 |
| 必填/校验 | 优先 `【Functional】`：同表单负向 + 正向；阻断原因以业务结果为主，控件置灰可同预期点一句 |
| 列表展示 | Logic 场景：提交后断言列值；纯展示改版：独立 `【UI】` 断言列/空态 |
| 跨页一致 | 仅当同属一个用户目标场景时同条；否则分条 |
| 历史数据 | 独立场景单独成条；前置注明历史数据条件，等级通常 P1 |

## 与其他 Skill 的关系

```text
story-acceptance-design → …/features/{slug}/acceptance.md（含 AC 追溯）
test-points-xmind       → …/features/{slug}/xmind/
functional-testcase-md  → …/features/{slug}/testcases/（本 skill）
```

## 用户指令映射

| 用户说法 | 行为 |
|----------|------|
| 把 xmind 落地成测试用例 md | 读 tree JSON 或 XMind，输出 `{feature-slug}.md` |
| 补充入口 / 产品规则 | 更新 MD 头 blockquote + 相关用例步骤 |
| 调整用例名称格式 | 按 reference 命名范式批量改名称列 |
| UI/UX Story 出用例 | 变更类型 UI/UX；细步骤、界面校验为主 |
| 功能/逻辑 Story 出用例 | 变更类型 Logic；业务步骤与结果校验为主 |
| 只有测试点没有用例 | 完整工作流，缺 baseline 列待确认 |

## 附加资源

- 字段与等级细则：[reference.md](reference.md)
- 黄金样例：[examples.md](examples.md) → `docs/sprints/_examples/features/product-asset-tag/testcases/product-asset-tag.md`
- Sprint 索引：[docs/sprints/INDEX.md](../../../docs/sprints/INDEX.md)
- Excel 导入模板：`docs/templates/import_ms_excel_case.xlsx`
- 上游：`test-points-xmind`、`story-acceptance-design`
