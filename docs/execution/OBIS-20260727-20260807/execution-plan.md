# Sprint `OBIS-20260727-20260807` 执行编排

> 64 条用例的执行批次与顺序。核心目标：**把不可逆操作尽量后置**，让破坏性用例不污染前序场景。
> 数据要求见 [`data-prep.md`](data-prep.md)；真实标识查 [`data-ledger.md`](data-ledger.md)。
> **批次 → 用例名称全文**见 [`batch-case-mapping.md`](batch-case-mapping.md)（Agent 执行以映射表为准；本节保留顺序与复位说明）。
> **批次 ↔ 用例全名**：[`batch-case-mapping.md`](batch-case-mapping.md)（Agent 执行以映射表为准；下文为摘要清单）。

## 破坏性分级

| 级别 | 含义 | 处理方式 |
|---|---|---|
| 🟢 只读 | 不改变任何数据 | 可任意顺序、可重复执行 |
| 🟡 可逆 | 改了数据但能改回来（编辑字段、改 Role 权限） | 批次结束后复位 |
| 🔴 不可逆 | Admin 降级、账号销毁 | 需独立资源或复位手法，一次性用完 |

## 批次总览

| 批次 | 内容 | 用例数 | 级别 | 前置依赖 |
|---|---|---|---|---|
| B0 | 造数自检 | — | — | 台账全部 ✅ |
| B1 | Audit 全量 | 12 | 🟢 | 六处 Audit 日志就位 |
| B2 | 细节补充：展示类 | 18 | 🟢 | R1–R3、PROD-1–4、各大列表 |
| B3 | 细节补充：编辑与权限类 | 9 | 🟡 | P1–P4、A1、A2 |
| B4 | Member：只读类 | 14 | 🟢 | KEY-1/2、CERT-1、FAC-1/2、GRP-1 |
| B5 | Transfer E2E | 6 | 🔴 | A3 及各目标账号 |
| B6 | Account 删除类 | 5 | 🔴 | D1–D5、S-* 状态资源 |

---

## B0 造数自检

开跑前逐项确认，任一不满足则相应批次不启动。

- [ ] `data-ledger.md` 第 0 节总览无 ⬜ 与 🔴
- [ ] 第 7 节「待补关键信息」7 项均已闭环或明确不阻塞
- [ ] 用 A1 登录成功，确认可进入 Account 删除与 Role 权限树
- [ ] 用 A3 登录成功，确认在 KEY-1 / KEY-2 / CERT-1 / FAC-1 / FAC-2 均为 Admin
- [ ] 确认本 Sprint 功能已部署到目标环境（Transfer 入口与 Confirm Action 可见）

## B1 Audit 全量（12 条，🟢）

`ux-p2-audit-unify` 全部用例。纯展示与筛选，不改数据，最先跑。

执行顺序建议：Group 基准 6 条 → Account → Profile → KMS 2 条 → PKI → Product。基准先过，后面的一致性对照才有参照。

- [ ] Group：默认列与 Operator/Organization/Time（P0）
- [ ] Group：Filter 筛选项与时间起止边界（P1）
- [ ] Group：Filter 姓名邮箱组织匹配与空态（P2）
- [ ] Group：Columns 锁定列与开启 Operation Details（P0）
- [ ] Group：Columns Organization/Time 可配置并恢复默认（P2）
- [ ] Group：Refresh 与 Sort 默认倒序及升序切换（P1）
- [ ] Account Audit 与 Group 基准一致（P1）
- [ ] Profile Audit 与 Group 一致且与 Account 行为一致（P2）
- [ ] KMS Audit 列/工具栏同 Group 且 Details 默认隐藏（P1）
- [ ] KMS Filter Organization 后 Operation Type 可筛（P0）
- [ ] PKI Audit 与 Group 一致且无额外 Operation Type（P1）
- [ ] Product Audit 对齐基准且无 KMS 独有 Filter（P1）

> 验证 Refresh 需现场制造一条新操作，会新增一条日志，无害。

## B2 细节补充 · 展示类（18 条，🟢）

`+n` hover、Toast、勾选框、列宽、Version，均为观察类。

- [ ] `+n`：Account 列表 User Role（P0）／Account 详情 Role（P1）／Group Linked Product（P1）／Product Module 浮层与滚动（P1）
- [ ] `+n`：单值无溢出与边界正确（P2）／中英文环境（P2）
- [ ] Toast：中文「操作成功」（P0）／英文 Operation Successful（P1）／两模块一致（P2）／特殊文案例外（P2）
- [ ] 勾选框：Filter 勾选态主题色（P1）／表单或下拉（P2）／未勾选与禁用态（P2）
- [ ] 列宽：Product 列表固定列宽及 Prod 最新版（P0）／Account 与 Group（P1）／KMS·PKI 与 Count 样式（P1）／Factory 等抽样（P2）
- [ ] Version：无 Prod Version 展示 `-`（P2）
- [ ] 列宽：小屏固定三列不被挤占且横向滚动（P1）

> Toast 类用例需要触发一次成功操作，建议复用 B3 的本人编辑保存，避免额外改数据。
> 列宽用例需开发者工具量 280 / 160 / 64 px。

## B3 细节补充 · 编辑与权限类（9 条，🟡）

涉及字段修改与 Role 权限变更，**批次结束统一复位**。

- [ ] 本人编辑：Account 列表 Edit 隐藏 Role/Notes 并可保存（P0，会改字段）
- [ ] 本人编辑：Account（SNB）列表（P1）／Account 详情弹窗（P1）／Profile（P1）
- [ ] 非本人编辑：仅 System Admin 可 Edit 且可见 Role/Notes（P1，需 A1 与 A2 切换登录）
- [ ] Role 树：勾选主题色及 OTA/Vulnerability 节点可配（P0，会改权限）
- [ ] OTA/Vulnerability Tab：无权限隐藏、有权限可见及变更刷新（P0，需 P1/P2/P3 切换 + 重登）
- [ ] 租户默认配置：会上线与不上线租户 Role 权限（P0，需 t1 与 t2 对照）

**复位清单**：把本人编辑改过的 Name / Phone 改回原值（原值记在台账）；把为验证而调整过的 Role 权限恢复到初始配置。

## B4 Member · 只读类（14 条，🟢）

Member 列表展示、Transfer 弹窗 UI、Cancel 与蒙层、Group 规则。**打开 Transfer 弹窗后一律 Cancel，不点 Confirm。**

- [ ] KMS：Member 默认列 Permission `+n` 与 Organization（P0）／工具栏入口（P1）／Admin 行本人与他人（P0）
- [ ] KMS：Transfer 弹窗标题 Placeholder 下拉与必填报错（P0）／Cancel 关闭与蒙层（P1）
- [ ] PKI：Member 默认列与 Admin Transfer 权限（P0）／Transfer 弹窗文案与必填报错（P0）／Cancel 与蒙层（P2）
- [ ] Factory：Member 默认列 Columns 与 Admin 菜单（P0）／Transfer 弹窗文案与必填报错（P0）／Cancel 蒙层与下拉仅 Active（P2）
- [ ] Group：Admin 行隐藏三点菜单且无 Transfer（P0）
- [ ] Account：删除批量转移 Confirm Action 弹窗文案与资源卡片（P0，**只看不 Confirm**）
- [ ] Account：批量转移 Cancel 关闭与蒙层（P2）

> 最后两条依赖 D2 已具备 Admin 身份，但只观察弹窗不确认，D2 不会被消耗。

## B5 Transfer E2E（6 条，🔴）

**每条执行后按下表复位，再跑下一条。** 复位方式：用新 Admin 登录，把 Admin 再 Transfer 回 A3。

| 顺序 | 用例 | 资源 | 目标 | 执行后 A3 变为 | 复位操作 |
|---|---|---|---|---|---|
| 1 | KMS 目标已在 Member 成功移交（P0） | KEY-1 | A4 | Normal Member | A4 登录 → Transfer 回 A3 |
| 2 | KMS 目标不在 Member 新增为 Admin（P1） | KEY-2 | A5 | Normal Member | A5 登录 → Transfer 回 A3 |
| 3 | KMS 中英文标题报错与 Toast（P2） | KEY-1 或 KEY-2 | — | — | **见下方合并建议** |
| 4 | PKI 成功移交（P0） | CERT-1 | A8 | Normal Member | A8 登录 → Transfer 回 A3 |
| 5 | Factory 目标已在列表（P0） | FAC-1 | A10 | **Factory Manager** | A10 登录 → Transfer 回 A3 |
| 6 | Factory 目标不在列表（P1） | FAC-2 | A11 | Factory Manager | A11 登录 → Transfer 回 A3 |

**合并建议**：KMS 中英文用例的前置要求「触发必填报错与**一次成功 Toast**」，单独执行会额外消耗一次移交。建议把它并入顺序 1 或 2——在执行成功移交时，分别在中文与英文环境各完成一次（正好对应 KEY-1 与 KEY-2 两次移交），顺带核对标题、报错与 Toast 文案，可省下一个 Key。

每条执行后在台账第 6 节追加一行变更记录。

## B6 Account 删除类（5 条，🔴）

**账号销毁不可回收，放在最后。** 按对数据影响从小到大排序：

| 顺序 | 用例 | 消耗账号 | 说明 |
|---|---|---|---|
| 1 | 无 Admin 身份可直接删除（P1） | D4 | 影响面最小，先验证基础删除链路 |
| 2 | Product Member Account 删除后不可见（P0） | D1 | 需先在 PROD-5 确认删除前可见 |
| 3 | 归档锁定纳入、已删除已销毁不纳入（P1） | D3 | 🔴 依赖 S-* 状态资源；可先只观察弹窗卡片 |
| 4 | 选择 Target Admin 移交并删除（P0） | D2 | 会把 D2 的资源 Admin 移交给 A12 |
| 5 | Account（SNB）与 Account 一致（P1） | D5 | 对照顺序 4 的结果 |

执行要点：

- 顺序 3 可拆两步——先只打开 Confirm Action 观察资源卡片是否含归档/锁定资源（不消耗 D3），确认无误后再执行删除。
- 顺序 4 执行后 A12 会成为多个资源的 Admin，若还需回归 B5，须先把这些资源的 Admin 转回 A3。
- 每次删除后在台账 1.3 更新「删除时间」，并在第 6 节追加变更记录。

## 回归重跑须知

B5、B6 的数据均为一次性。若需重跑：

- B5：重新准备 KEY / CERT / FAC 资源，或确认上一轮复位已完成
- B6：**必须新建 D 类账号**，已删除的无法恢复；建议每类常备 1 个备用号（台账 D6 行）
