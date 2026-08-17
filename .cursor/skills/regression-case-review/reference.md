# Reference — Regression Case Review

## 环境基线表

标题写作 `{target_env} 基线`（如 `UAT 基线` / `SIT 基线`），表头可加一行元信息：`base_url`、登录账号角色、样本产品/芯片。

对每个区块（或 Tab / 子表）记录：

| 字段 | 内容 |
|------|------|
| 区块 | 页面上可见标题（含子表名） |
| 区块级操作 | Add / ⋮ → Edit / Filter…；无则写「—」或「父区块无操作」 |
| 行内操作 | ⋮ 菜单项原文（Download / Deactivate / Remove…） |
| 列 | 表头原文；条件列注明触发条件 |
| 新增/编辑弹窗 | 字段、主按钮文案、有无二次确认 |

页级脚注（可选）：环境切换、Tab 列表、标签栏交互、已确认的全局交互（如 Remove 带 Confirm）。

### 基线常见陷阱

| 现象 | 错误结论 | 正确做法 |
|------|----------|----------|
| 某列当前不可见 | 「功能已下线」 | 查是否依赖 Vendor/Series/Part 等前置 |
| 标签无关闭图标 | 「应补删除用例」 | 问产品是否已设计；未设计则**不做** |
| 有 Add 无弹窗 | 「缺 Confirm 步骤」 | 实测是弹窗还是内联编辑 |
| 仅用高权限账号 | 「无权限用例可删」 | 未验证项 + 遗漏「角色负向」 |
| 父区块改名、子表保留旧名 | 全文替换子表名 | 分清父/子；步骤写清层级 |

## 四类 Finding 写法

每条 finding 建议固定四段：

1. **ID / 标题**（可截断）
2. **现网证据**（对照环境下的控件文案、列名、有无入口；一句；可缀 `[{target_env}]`）
3. **问题**（过时点 / 矛盾点 / 与谁重复 / 缺哪块）
4. **建议改法**（改哪几步、并入谁、新增什么）

### 过时 — 高频替换映射（按实测更新，勿写死）

评审时建立「旧文案 → 对照环境文案」表，批量替换前先全文搜确认无例外。本轮 Product-Asset 曾出现：

| 旧 | 对照环境文案（示例，以实测为准） |
|----|----------------|
| Delete（行删除） | Remove（且常有 Confirm） |
| Asign / Upload / Add Dataset | Add，或 ⋮ → Edit 后在编辑态新增行 |
| Factory Tooling / Programming Script（作父名） | Programming Station Software Package（子表仍可能叫 Programming Script） |
| Updated Time / Note | Update Time / Notes |

### 错误 — 检查清单

- 标题与步骤操作对象不一致
- 预期写「成功」但步骤走负向
- 步骤引用已不存在的列/下拉/按钮
- Chip/资源「删除」但对照环境仅自定义行可删、实体无删除入口
- Secure Boot 类断言未写前置「已选支持该能力的芯片」

### 重复 — 合并规则

1. 算去重键；键相同 → 候选对
2. 优先保留：步骤更完整、ID 更稳、Is Regression=Yes 的一条
3. 被删条：Excel 删除；Canvas 记 `A → B`；备注可写 `并入 {B}`
4. 三条以上同意图：收成一条主路径 + 必要时一条负向，避免矩阵重复

### 遗漏 — 优先补什么

按**对照环境区块覆盖率**扫，不按原 Excel 模块树脑补：

1. 完全无用例的区块（如曾缺 General File / Attachment File）
2. 有创建无改名/停用恢复/工具栏/下载等主操作
3. 限制类：大小上限、重名、引用中不可 deactivate
4. 权限负向（若本包宣称回归权限）
5. **不做**：用户确认未设计、本轮不上线（SBOM/OTA 等）

## 未验证项

写入条件：本轮没点到、账号不够、页内只看了 PROD 数据区、条件列未触发、**只测了 SIT 未测 UAT（或相反）** 等。

模板句：

> · {现象} —— 影响 {用例 ID} 的「{步骤摘要}」是否成立。

用户确认后：

- 成立 → 移出未验证；写入基线脚注；必要时改 Excel 步骤
- 不成立 → 改相关用例步骤/预期
- 不在范围 → 删遗漏建议与相关新增用例，更新统计

## Canvas 结构建议

```text
Header（对照环境 + Stat 原/过时/错误/重复/新增/修订后）
FindingsSection（按 过时|错误|重复 分表或带 tone 的总表）
GapsSection（遗漏，按 area + count）
BaselineSection（{target_env} 基线 Table + 脚注）
ScopeSection（未验证项 Card）
PlanSection（处置步骤表：−N / +N）
```

统计口径必须可复算：

```text
修订后总数 = 原条数 − 合并删除 − 移出范围 + 新增
```

（「改写」不改变条数；「撤回某条新增」同时 −1 新增与修订后总数。）

## 修订脚本

依赖：`pip install openpyxl`

推荐两段式，避免一次巨型脚本难回滚：

1. **build**：读原 xlsx → 应用删除/改写/新增 → 写 `*-评审修订.xlsx`
2. **patch**：对修订文件做小范围校准（列名、父区块改名、单条流程更正）

约定：

- 读写路径用原始字符串；控制台打印用 `python -X utf8`（Windows）
- 改步骤时保持原编号风格：`[1]…\n[2]…` 与预期一一对应
- 批量替换后**再搜旧词**，清预期列里的残留说明
- 删除行后重核「Module 删除」等已撤范围关键词为零命中

### 最小自检命令

```bash
python -X utf8 -c "
import openpyxl
p=r'{修订xlsx}'
ws=openpyxl.load_workbook(p).active
print('用例数', ws.max_row-1)
# 按需替换废弃词列表
stale=['Add Dataset','Factory Tooling','Updated Time']
for r in range(2, ws.max_row+1):
    for c in range(1, ws.max_column+1):
        v=ws.cell(r,c).value
        if not v: continue
        s=str(v)
        for w in stale:
            if w in s: print('残留', r, w, s[:60])
"
```

## 账号与环境

- 登录：`config/env.local.yaml` → `environments.{target_env}`（`base_url`、账号）；OTP 场景可复用**该环境**已登录 Chrome 标签页
- `sit` 与 `uat` 部署版本、数据、开关可能不同：评审结论标注环境；跨环境差异进未验证或另开一轮
- 选样本产品时记下芯片型号（影响 Secure Boot 等条件列）
- 高权限账号测不出的按钮隐藏 → 未验证 + 遗漏「无权限负向」，不要假装已覆盖

## 依赖清单（给协作者）

| 类型 | 项 | 必须？ | 说明 |
|------|-----|--------|------|
| 运行时 | Cursor Agent + 本仓库 skill 目录 | 是 | `.cursor/skills/regression-case-review/` |
| Python | `Python 3` + `pip install openpyxl` | 是 | 读/写回归 xlsx、自检残留文案 |
| 配置 | `config/env.local.yaml`（从 `env.example.yaml` 复制） | 强烈建议 | 填目标 env 的 `base_url`、登录方式、OTP/账号；也可用对话里直接给 URL+账号 |
| 浏览器 MCP | `user-chrome-devtools` 或 `user-playwright` 至少其一 | 是（要对照现网时） | 登录目标环境、snapshot/点选建基线 |
| Canvas | Cursor Canvas（可写 `.canvas.tsx`） | 强烈建议 | 协作确认 findings；关掉则改为 Markdown 报告，流程仍可用 |
| 输入 | 回归用例 `.xlsx` + 对照 URL/环境名 | 是 | 列对齐 MeterSphere 导入习惯即可 |
| 网络 | 能访问目标 SIT/UAT | 是 | 公司 VPN/白名单按环境要求 |

**非依赖**：不必先有本仓 feature 用例 MD、不必装 MeterSphere CLI、不必跑 `testcase-agent-run`。本 skill 不引入 npm/额外 Python 包（除 openpyxl）。

## SIT vs UAT 选用

| 场景 | 建议 `target_env` |
|------|-------------------|
| 开发联调 / Sprint 内回归包对齐最新功能 | 通常 `sit` |
| 预发 / 上线前回归包对齐发布候选 | 通常 `uat` |
| 用户给了明确 URL | 以 URL 为准，env 名与 yaml 对齐 |
| 同一份 Excel 要两套环境都过 | 两轮评审、两个修订后缀（如 `-sit-评审修订` / `-uat-评审修订`）或分文件 |
