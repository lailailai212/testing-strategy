# 测试用例评审 — 【体验优化P2】Audit功能统一

> **用途**：用例评审会材料（需求范围 / 覆盖关系 / 用例详述 / 等级说明 / 待确认）  
> **Story**：[飞书 User Story #7029049092](https://project.feishu.cn/obis/userstory/detail/7029049092)  
> **Sprint**：`OBIS-20260727-20260807`  
> **Feature**：`ux-p2-audit-unify`  
> **文档日期**：2026-07-30（修订：补充用例细节；按「仅阻塞/重要主功能标 P0」重评等级）  
> **评审结论**：（会后填写）通过 / 修改后通过 / 不通过

---

## 1. 评审目标

请评审方重点确认：

1. **范围**：六处 Audit 是否覆盖完整；是否有遗漏或误测  
2. **基准策略**：Group 深测 + 其余模块冒烟对齐，是否可接受  
3. **用例等级**：P0 是否仅落在阻塞/重要主功能（见 §3）  
4. **步骤与预期**：下列详述是否可执行、断言是否准确  
5. **待确认项**：会中拍板或记下责任人

---

## 2. 需求摘要

| 项 | 内容 |
|----|------|
| 目标 | 统一各模块 Audit 列表展示、Filter、Columns、Refresh/Sort |
| 基准 | **Group Audit** |
| 对齐模块 | Account / Profile / PKI / Product（与 Group 完全一致） |
| 差异模块 | **KMS**：Filter 在 Organization 后额外 **Operation Type** |
| 关键点 | 新增 Organization；Operator hover 邮箱+复制；原「Operation」= **Operation Details**（默认隐藏） |

### Story AC

| AC | 内容 |
|----|------|
| AC-01 | 默认列 Operator / Organization / Operation Type / Operation Time；Details 默认隐藏；Operator hover 邮箱复制；溢出 hover |
| AC-02 | Filter：姓名/邮箱/组织 + 时间范围（起 00:00:00 / 止 23:59:59） |
| AC-03 | Columns：Operator、Type 锁定；Organization、Time 可配；Details 可开且在 Type 后 |
| AC-04 | Refresh；Sort 仅按 Operation Time，默认倒序 |
| AC-05 | Account / Profile / PKI / Product 与 Group 一致 |
| AC-06 | KMS Filter 额外 Operation Type（Organization 后） |

---

## 3. 用例等级说明（本 Story 约定）

| 等级 | 定义（本项目） | 本 Story 落点 |
|------|----------------|---------------|
| **P0** | 阻塞发布或**重要环节/重要功能**主路径失败即无法验收 | #1 列表默认展示（核心交付）；#4 Columns 锁定与 Details（列规则核心）；#10 KMS Filter Operation Type（唯一差异功能） |
| **P1** | 重要能力，失败影响体验或完整性，但不单独阻塞「能否上线」 | Filter 时间边界、Refresh/Sort、各模块对齐冒烟 |
| **P2** | 边界/空态/恢复类、一致性抽测 | Filter 匹配空态、Columns 恢复默认、Profile↔Account 一致性 |

**本轮重评后**：用例 **P0 × 3，P1 × 6，P2 × 3**（原 10 条 P0 已下调）。

> 说明：测试点表（`acceptance.md`）中的 P0/P1 表示**测试点设计优先级**，与**用例执行等级**可不同；MeterSphere / 用例 MD 以用例等级为准。

---

## 4. 覆盖总览

| 维度 | 数量 |
|------|------|
| Story AC | 6 |
| 测试点 | 22（设计优先级：P0 × 15，P1 × 7） |
| 功能用例 | 12（**执行等级：P0 × 3，P1 × 6，P2 × 3**） |
| 类型 | UI × 3，Functional × 4，E2E × 5 |

### AC → 用例

| AC | 对应用例 | 是否含 P0 |
|----|----------|-----------|
| AC-01 | #1、#4、#7～#12 | ✅ #1 #4 |
| AC-02 | #2、#3 | —（P1/P2） |
| AC-03 | #4、#5 | ✅ #4 |
| AC-04 | #6 | —（P1） |
| AC-05 | #7～#9、#11、#12 | —（P1） |
| AC-06 | #9、#10 | ✅ #10 |

**22 条 TP 均已被至少 1 条用例覆盖。**

---

## 5. 用例详述（评审主材料）

> 完整表格见 `testcases/ux-p2-audit-unify.md`。下列为评审可读版本。

### 5.1 P0 — 阻塞 / 重要主功能

#### TC-01｜P0｜UI｜Group Audit 默认列与 Operator / Organization / Time

| 项 | 内容 |
|----|------|
| **所属模块** | `/Cloud/Admin/Group` |
| **覆盖 TP** | TP-AUD-G01～G04 |
| **对应 AC** | AC-01 |
| **为何 P0** | 本 Story 核心交付：默认列集 + Operator 交互；失败则基准规格无法验收 |
| **前置** | 可进 Group 详情 Audit；有可识别操作人的日志；可备长文本验证溢出 |
| **关键步骤** | ① 打开 Audit 看默认列 ② Operator：头像+Name+邮箱 icon，hover 复制邮箱 ③ Organization=租户简称 ④ Operation Time=年月日时分秒；溢出 hover 全文 |
| **关键预期** | 默认仅 Operator / Organization / Operation Type / Operation Time；**无**默认 Details；复制成功；时间格式正确 |
| **评审问** | 默认列顺序是否需写死为 Operator→Organization→Type→(Details)→Time？ |

---

#### TC-04｜P0｜UI｜Group Columns 锁定与开启 Operation Details

| 项 | 内容 |
|----|------|
| **所属模块** | `/Cloud/Admin/Group` |
| **覆盖 TP** | TP-AUD-G08、G09 |
| **对应 AC** | AC-03、AC-01 |
| **为何 P0** | 列权限规则 + Details（原 Operation）默认隐藏/可开位置，属重要列行为；错了直接影响验收 |
| **前置** | 已在 Group Audit；存在原 Operation 长文案数据 |
| **关键步骤** | ① Columns 尝试隐藏/拖拽 Operator、Operation Type ② 开启 Operation Details，看位置与内容 ③ 确认默认关闭时不可见 |
| **关键预期** | Operator、Type **不可**隐藏、不可换序；Details 在 Type **后**；内容为原 Operation 长文案；默认隐藏 |
| **评审问** | 「不可拖拽换序」是否包含与其他列相对位置的全部锁定？ |

---

#### TC-10｜P0｜Functional｜KMS Filter — Organization 后 Operation Type

| 项 | 内容 |
|----|------|
| **所属模块** | `/Cloud/KMS/Key Detail/Operation Log` |
| **覆盖 TP** | TP-AUD-K02、K03 |
| **对应 AC** | AC-06 |
| **为何 P0** | 本 Story **唯一相对 Group 的差异功能**；失败则 AC-06 不通过 |
| **前置** | 可进 KMS Audit；存在多种 Operation Type 日志；控件形态待确认（以可筛为准） |
| **关键步骤** | ① 点 Filter，确认 Organization **后**有 Operation Type ② 选一类型筛选 ③ 核对列表仅匹配类型 |
| **关键预期** | 筛选项位置正确；筛选生效 |
| **评审问** | Operation Type 控件：单选/多选/输入？可选值来源？ |

---

### 5.2 P1 — 重要能力

#### TC-02｜P1｜Functional｜Group Filter 筛选项与时间起止边界

| 项 | 内容 |
|----|------|
| **覆盖 TP** | G05、G06｜**AC** AC-02 |
| **前置** | 跨多日日志；边界日附近有可验证记录 |
| **关键步骤** | ① Filter 核对 Name/Email/Organization 输入框与 Placeholder、时间范围 ② 选起止日筛选 ③ 核对是否按起日 00:00:00、止日 23:59:59 |
| **关键预期** | Placeholder=`Please Enter / 请输入`；时间边界生效 |
| **为何非 P0** | 重要筛选规则，但列表默认可先验收；边界属规则细节 |

---

#### TC-06｜P1｜Functional｜Group Refresh 与 Sort

| 项 | 内容 |
|----|------|
| **覆盖 TP** | G11、G12｜**AC** AC-04 |
| **前置** | 多条不同 Operation Time；可制造新操作验证 Refresh |
| **关键步骤** | ① 默认排序 ② Refresh ③ Sort 仅 Time，切正序 ④ 无其它 Sort 维度 |
| **关键预期** | 默认倒序；Refresh 刷新；正序升序；仅 Time |
| **为何非 P0** | 工具栏常规能力，非本 Story 最大变更点 |

---

#### TC-07｜P1｜E2E｜Account Audit 对齐 Group

| 项 | 内容 |
|----|------|
| **覆盖 TP** | A01｜**AC** AC-05｜**模块** `/Cloud/Admin/Account` |
| **前置** | 可进 Account 详情 Audit；建议 Group 基准已测过 |
| **关键步骤** | ① 打开 Audit ② 默认列 + Operator hover + Organization ③ 抽测 Filter/Columns/Sort/Refresh 与 Group 一致 |
| **关键预期** | 规格与 Group 一致（冒烟，不重复 Group 全量细则） |
| **为何非 P0** | 对齐冒烟；阻塞点已在 Group 深测 |

---

#### TC-09｜P1｜E2E｜KMS 列/工具栏同 Group + Details 默认隐藏

| 项 | 内容 |
|----|------|
| **覆盖 TP** | K01、K04｜**AC** AC-05/06/01｜**模块** Key Detail Operation Log |
| **关键步骤** | ① 默认列与 Columns/Sort/Refresh 同 Group ② Details 默认隐藏，开启后可见且在 Type 后 |
| **关键预期** | 与 Group 对齐；Details 规则正确 |
| **为何非 P0** | 对齐冒烟；KMS **差异**由 TC-10（P0）覆盖 |

---

#### TC-11｜P1｜E2E｜PKI Audit 对齐且无额外 Operation Type

| 项 | 内容 |
|----|------|
| **覆盖 TP** | P01｜**AC** AC-05｜**模块** Cert & Template Detail / Audit |
| **关键步骤** | ① 默认列/Columns/Sort 同 Group ② Filter **无** KMS 独有 Operation Type |
| **关键预期** | 与 Group 一致且无多余筛选项 |

---

#### TC-12｜P1｜E2E｜Product Audit 对齐且无 KMS 独有 Filter

| 项 | 内容 |
|----|------|
| **覆盖 TP** | P02、P03｜**AC** AC-05｜**模块** 暂 `/Cloud/Product` |
| **关键步骤** | ① 默认列（含 Organization）、Operator hover、Details 默认隐藏 ② Filter/Columns/Sort 同 Group ③ Filter 无 KMS 独有 OT |
| **关键预期** | 与基准一致；无多余 OT 筛选 |
| **评审问** | MeterSphere 最终模块路径？ |

---

### 5.3 P2 — 边界 / 一致性

#### TC-03｜P2｜Functional｜Group Filter 姓名/邮箱/组织匹配与空态

| 项 | 内容 |
|----|------|
| **覆盖 TP** | G07｜**AC** AC-02 |
| **关键步骤** | ① 分别按 Name/Email/Organization 匹配筛选 ② 无匹配关键词看空态 |
| **关键预期** | 匹配正确；空态合理无报错 |
| **为何 P2** | 正向匹配+空态，属 Filter 边界 |

---

#### TC-05｜P2｜UI｜Group Columns Organization/Time 可配置并恢复默认

| 项 | 内容 |
|----|------|
| **覆盖 TP** | G10｜**AC** AC-03 |
| **关键步骤** | ① 隐藏 Organization、Operation Time ② 再显示或恢复默认可见集 |
| **关键预期** | 可隐藏/显示；恢复后为默认四列，Details 仍默认隐藏 |
| **为何 P2** | 可配置恢复，非锁定规则主路径（锁定在 TC-04 P0） |

---

#### TC-08｜P2｜E2E｜Profile 对齐 + 与 Account 行为一致

| 项 | 内容 |
|----|------|
| **覆盖 TP** | A02、A03｜**AC** AC-05｜**模块** My Profile |
| **关键步骤** | ① Profile Audit 对齐 Group ② 对照 Account：列配置/筛选行为一致 |
| **关键预期** | 与 Group 一致；与 Account 结果一致（是否同组件待确认） |
| **为何 P2** | Account 已有对齐冒烟（TC-07）；本条偏一致性抽测 |

---

## 6. 一览表

| # | 等级 | 类型 | 用例 | 覆盖 TP | AC |
|---|------|------|------|---------|-----|
| 1 | **P0** | UI | Group 默认列与 Operator/Org/Time | G01～G04 | 01 |
| 2 | P1 | Functional | Group Filter 筛选项与时间边界 | G05, G06 | 02 |
| 3 | P2 | Functional | Group Filter 匹配与空态 | G07 | 02 |
| 4 | **P0** | UI | Group Columns 锁定与 Details | G08, G09 | 03, 01 |
| 5 | P2 | UI | Group Columns 可配置恢复 | G10 | 03 |
| 6 | P1 | Functional | Group Refresh 与 Sort | G11, G12 | 04 |
| 7 | P1 | E2E | Account 对齐 Group | A01 | 05 |
| 8 | P2 | E2E | Profile 对齐 + 与 Account 一致 | A02, A03 | 05 |
| 9 | P1 | E2E | KMS 列/工具栏 + Details | K01, K04 | 05, 06, 01 |
| 10 | **P0** | Functional | KMS Filter Operation Type | K02, K03 | 06 |
| 11 | P1 | E2E | PKI 对齐且无额外 OT | P01 | 05 |
| 12 | P1 | E2E | Product 对齐且无 KMS 独有 Filter | P02, P03 | 05 |

### 测试策略

- **深测 Group**（#1～#6）：列表 / Filter / Columns / Sort  
- **冒烟对齐**（#7～#9、#11～#12）：不重复 Group 全量细则  
- **KMS 差异**（#10）：P0 专测  

---

## 7. 产物入口

| 类型 | 路径 |
|------|------|
| AC + 测试点 | `features/ux-p2-audit-unify/acceptance.md` |
| 用例 MD（已同步等级） | `features/ux-p2-audit-unify/testcases/ux-p2-audit-unify.md` |
| MeterSphere Excel | `features/ux-p2-audit-unify/testcases/ux-p2-audit-unify-metersphere.xlsx` |
| 测试点 XMind | `features/ux-p2-audit-unify/xmind/ux-p2-audit-unify-test-points.xmind` |
| Story MD | `story/obis-7029049092-体验优化p2-audit功能统一/` |

根路径：`docs/sprints/OBIS-20260727-20260807/`

---

## 8. 待确认（会中优先）

| # | 问题 | 影响 | 结论栏 |
|---|------|------|--------|
| 1 | KMS Filter Operation Type：单选/多选/输入？可选值来源？ | TC-10 | |
| 2 | Organization Filter 是否模糊匹配？空组织展示与筛选？ | TC-02/03 | |
| 3 | 默认列顺序是否固定 Operator→Organization→Type→(Details)→Time？ | TC-01/04 | |
| 4 | Profile 与 Account Audit 是否同组件？ | TC-08 | |
| 5 | Product Audit 的 MeterSphere 最终路径？（现 `/Cloud/Product`） | TC-12 导入 | |
| 6 | **P0 三条是否认可**（#1 列表 / #4 Columns+Details / #10 KMS OT）？ | 等级 | |

---

## 9. 评审检查清单

| 检查项 | 通过 |
|--------|------|
| AC 可追溯，无孤立 AC | ☐ |
| Group 基准主路径覆盖充分 | ☐ |
| 五模块对齐冒烟策略可接受 | ☐ |
| KMS 差异有 P0 专测 | ☐ |
| **用例 P0 仅含阻塞/重要主功能** | ☐ |
| 步骤/预期可执行，待确认已登记 | ☐ |
| MeterSphere 路径可导入或已标待确认 | ☐ |

---

## 10. 评审记录（会后填写）

| 项 | 内容 |
|----|------|
| 评审时间 | |
| 参与人 | |
| 结论 | ☐ 通过　☐ 修改后通过　☐ 不通过 |
| 必改项 | |
| 可选优化 | |
| 待确认责任人 / 截止日期 | |

### 修改跟踪

| # | 问题描述 | 处理结果 | 状态 |
|---|----------|----------|------|
| | | | ☐ 打开 / ☐ 已关 |
