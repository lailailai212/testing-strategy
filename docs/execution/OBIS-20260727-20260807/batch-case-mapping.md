# Sprint `OBIS-20260727-20260807` 批次 ↔ 用例映射

> Agent 执行时以本表为准：批次 → **用例名称全文** → feature 文件 → 绑定代号。
> 配套：[`execution-plan.md`](execution-plan.md)（顺序与复位）· [`data-ledger.md`](data-ledger.md)（真实标识）· Skill `testcase-agent-run`。

| 批次 | 用例数 | Feature | 破坏性 |
|---|---|---|---|
| B1 | 12 | `ux-p2-audit-unify` | 🟢 |
| B2 | 19 | `ux-p2-detail-supplement`（展示类；plan 总览写 18，按用例全文计 19） | 🟢 |
| B3 | 8 | `ux-p2-detail-supplement`（编辑/权限；plan 总览写 9，按用例全文计 8） | 🟡 |
| B4 | 14 | `ux-p2-member-unify`（只读；Transfer 只 Cancel） | 🟢 |
| B5 | 6 | `ux-p2-member-unify`（Transfer E2E；含中英文合并条） | 🔴 |
| B6 | 5 | `ux-p2-member-unify`（Account 删除） | 🔴 |
| **合计** | **64** | | |

用例文件：

- `docs/sprints/OBIS-20260727-20260807/features/ux-p2-audit-unify/testcases/ux-p2-audit-unify.md`
- `docs/sprints/OBIS-20260727-20260807/features/ux-p2-detail-supplement/testcases/ux-p2-detail-supplement.md`
- `docs/sprints/OBIS-20260727-20260807/features/ux-p2-member-unify/testcases/ux-p2-member-unify.md`

## B1 Audit 全量（12 · 🟢）

| # | 用例名称 | feature | 等级 | actor | resources | 备注 |
|---|---|---|---|---|---|---|
| 1 | `【Admin-Group】【UI】Audit 列表 - 默认列与 Operator/Organization/Time` | `ux-p2-audit-unify` | P0 | A1 | GRP-1 Audit | Group 基准先跑 |
| 2 | `【Admin-Group】【Functional】Audit Filter - 筛选项与时间起止边界` | `ux-p2-audit-unify` | P1 | A1 | GRP-1 Audit |  |
| 3 | `【Admin-Group】【Functional】Audit Filter - 姓名邮箱组织匹配与空态` | `ux-p2-audit-unify` | P2 | A1 | GRP-1 Audit | 需 t3 或跨 Org 日志 |
| 4 | `【Admin-Group】【UI】Audit Columns - 锁定列与开启 Operation Details` | `ux-p2-audit-unify` | P0 | A1 | GRP-1 Audit |  |
| 5 | `【Admin-Group】【UI】Audit Columns - Organization/Time 可配置并恢复默认` | `ux-p2-audit-unify` | P2 | A1 | GRP-1 Audit |  |
| 6 | `【Admin-Group】【Functional】Audit Refresh 与 Sort - 默认倒序及升序切换` | `ux-p2-audit-unify` | P1 | A1 | GRP-1 Audit | Refresh 可现场造一条 |
| 7 | `【Admin-Account】【E2E】Account Audit - 与 Group 基准规格一致` | `ux-p2-audit-unify` | P1 | A1 | Account Audit URL |  |
| 8 | `【Login-&-Profile-My-Profile】【E2E】Profile Audit - 与 Group 一致且与 Account 行为一致` | `ux-p2-audit-unify` | P2 | A1 | My Profile Audit | 可用 super_admin=A1 |
| 9 | `【KMS-Key-Detail-Operation-Log】【E2E】KMS Audit - 列/工具栏同 Group 且 Details 默认隐藏` | `ux-p2-audit-unify` | P1 | A3 | KEY-3 或 KEY-1 Operation Log | 多种 Operation Type |
| 10 | `【KMS-Key-Detail-Operation-Log】【Functional】KMS Audit Filter - Organization 后 Operation Type 可筛` | `ux-p2-audit-unify` | P0 | A3 | KEY-3 或 KEY-1 | Filter Organization → Type |
| 11 | `【PKI-Cert-&-Template-Detail-Audit】【E2E】PKI Audit - 与 Group 一致且无额外 Operation Type 筛选` | `ux-p2-audit-unify` | P1 | A3 | CERT-1 Audit |  |
| 12 | `【Product】【E2E】Product Audit - 对齐基准且无 KMS 独有 Filter` | `ux-p2-audit-unify` | P1 | A1 | PROD-6 Audit |  |

## B2 细节补充 · 展示类（19 · 🟢）

> 含「窄屏不验收」一条（文档声明不验收，仍列入映射便于追溯）。Role 树勾选见 B3。

| # | 用例名称 | feature | 等级 | actor | resources | 备注 |
|---|---|---|---|---|---|---|
| 1 | `【Admin-Account】【UI】+n hover - Account 列表 User Role 展示全部` | `ux-p2-detail-supplement` | P0 | R1 | Account 列表 |  |
| 2 | `【Admin-Account】【UI】+n hover - Account 详情 Role 展示全部` | `ux-p2-detail-supplement` | P1 | R1 | Account 详情 |  |
| 3 | `【Admin-Group】【UI】+n hover - Group Linked Product Role 展示其余角色` | `ux-p2-detail-supplement` | P1 | A1 | GRP-1 Linked Product |  |
| 4 | `【Product-Product-List】【UI】+n hover - Product 列表 Module 浮层与滚动` | `ux-p2-detail-supplement` | P1 | A1 | PROD-4 | Module≥6 |
| 5 | `【Admin-Account】【Functional】+n hover - 单值无溢出与边界正确` | `ux-p2-detail-supplement` | P2 | R2 | Account 列表 | 单角色对照 |
| 6 | `【Admin-Account】【UI】+n hover - 中英文环境均可完整打开` | `ux-p2-detail-supplement` | P2 | R1 | Account 列表 | 切中英文 |
| 7 | `【Admin-Account】【UI】成功 Toast - 中文「操作成功」样式` | `ux-p2-detail-supplement` | P0 | A1 或本人 | Account/Profile | 可与 B3 编辑合并触发 |
| 8 | `【Admin-Account】【UI】成功 Toast - 英文 Operation Successful` | `ux-p2-detail-supplement` | P1 | A1 或本人 | Account/Profile | 英文环境 |
| 9 | `【Admin-Account】【UI】成功 Toast - 至少抽测两个模块一致` | `ux-p2-detail-supplement` | P2 | A1 | ≥2 模块 |  |
| 10 | `【Admin-Account】【Functional】成功 Toast - 特殊文案例外不强制覆盖` | `ux-p2-detail-supplement` | P2 | A1 | — | 例外清单 |
| 11 | `【Product-Product-List】【UI】勾选框 - Filter 勾选态为主题色` | `ux-p2-detail-supplement` | P1 | A1 | Product List Filter |  |
| 12 | `【Admin-Account】【UI】勾选框 - 表单或下拉相关勾选主题色` | `ux-p2-detail-supplement` | P2 | A1 | Account 表单/下拉 |  |
| 13 | `【Product-Product-List】【UI】勾选框 - 未勾选与禁用态不误用主题色` | `ux-p2-detail-supplement` | P2 | A1 | Product Filter | 未勾选/禁用 |
| 14 | `【Product-Product-List】【UI】列宽与 Version - Product 固定三列、大屏均分及 Prod 最新版` | `ux-p2-detail-supplement` | P0 | A1 | PROD-1 | 量 280/160/64；大屏中间列均分 |
| 15 | `【Product-Product-List】【UI】Version - 无 Prod Version 展示短横线` | `ux-p2-detail-supplement` | P2 | A1 | PROD-3 | 显示 `-` |
| 16 | `【Admin-Account】【UI】列宽 - Account 与 Group 固定三列及大屏中间列均分` | `ux-p2-detail-supplement` | P1 | A1 | Account + Group 列表 |  |
| 17 | `【KMS-Key-List】【UI】列宽与 Count - KMS/PKI 固定三列、大屏均分及普通文字 Count` | `ux-p2-detail-supplement` | P1 | A1 | KMS/PKI List | Usage/Issued Count |
| 18 | `【Ecosystem-Factory-Factory-List】【UI】列宽 - Factory 等大列表固定三列与大屏均分（抽样）` | `ux-p2-detail-supplement` | P2 | A1 | Factory List 等 |  |
| 19 | `【Product-Product-List】【UI】列宽 - 小屏固定三列不被挤占且横向滚动` | `ux-p2-detail-supplement` | P1 | A1 | PROD-1 窄视口 | 横向滚动 + 280/160/64 |

## B3 细节补充 · 编辑与权限类（8 · 🟡）

> 批末复位：本人编辑字段、Role 权限树。

| # | 用例名称 | feature | 等级 | actor | resources | 备注 |
|---|---|---|---|---|---|---|
| 1 | `【Operation-Role】【UI】勾选框与权限节点 - Role 树主题色及 OTA/Vulnerability 可配` | `ux-p2-detail-supplement` | P0 | A1 | Role 列表 | 会改权限，须复位 |
| 2 | `【Admin-Account】【E2E】本人编辑 - Account 列表可 Edit 且隐藏 Role/Notes 并可保存` | `ux-p2-detail-supplement` | P0 | 本人账号 | Account 列表 | 记录改前 Name/Phone |
| 3 | `【Operation-User(SNB)】【UI】本人编辑 - Account（SNB）列表隐藏 Role/Notes` | `ux-p2-detail-supplement` | P1 | 本人账号 | User(SNB) |  |
| 4 | `【Admin-Account】【UI】本人编辑 - Account 详情 Edit 弹窗隐藏 Role/Notes` | `ux-p2-detail-supplement` | P1 | 本人账号 | Account 详情 |  |
| 5 | `【Login-&-Profile-My-Profile】【UI】本人编辑 - Profile Edit 隐藏 Role/Notes` | `ux-p2-detail-supplement` | P1 | 本人账号 | My Profile |  |
| 6 | `【Admin-Account】【Functional】非本人编辑 - 仅 System Admin 可 Edit 且可见 Role/Notes` | `ux-p2-detail-supplement` | P1 | A1 + A2 | Account 列表 | 切换登录 |
| 7 | `【Product-OTA】【E2E】OTA/Vulnerability Tab - 无权限隐藏、有权限可见及变更刷新` | `ux-p2-detail-supplement` | P0 | P1/P2/P3 | PROD-6 | 改权限后重登 |
| 8 | `【Operation-Role】【Functional】租户默认配置 - 会上线与不上线租户 Role 权限` | `ux-p2-detail-supplement` | P0 | A1 | t1 + t2 Role | t2 可登录用户仍缺 |

## B4 Member · 只读类（14 · 🟢）

> **禁止 Confirm** Transfer / 删除批量转移；一律 Cancel。

| # | 用例名称 | feature | 等级 | actor | resources | 备注 |
|---|---|---|---|---|---|---|
| 1 | `【KMS-Key-Detail】【UI】Member 列表 - 默认列 Permission +n 与 Organization` | `ux-p2-member-unify` | P0 | A3 | KEY-1 | Permission≥2 成员 |
| 2 | `【KMS-Key-Detail】【UI】Member 列表 - 工具栏入口可达` | `ux-p2-member-unify` | P1 | A3 | KEY-1 |  |
| 3 | `【KMS-Key-Detail】【UI】Member 列表 - Admin 行 Transfer 本人与他人` | `ux-p2-member-unify` | P0 | A3 + A2 | KEY-1 | 他人账号验证置灰 |
| 4 | `【KMS-Key-Detail】【UI】Transfer Admin - 弹窗标题 Placeholder 下拉与必填报错` | `ux-p2-member-unify` | P0 | A3 | KEY-1 | 只看弹窗 |
| 5 | `【KMS-Key-Detail】【UI】Transfer Admin - Cancel 关闭与蒙层不可关` | `ux-p2-member-unify` | P1 | A3 | KEY-1 | Cancel/蒙层 |
| 6 | `【PKI-Cert-&-Template-Detail】【UI】Member 列表 - 默认列与 Admin Transfer 权限` | `ux-p2-member-unify` | P0 | A3 | CERT-1 |  |
| 7 | `【PKI-Cert-&-Template-Detail】【UI】Transfer Admin - 弹窗文案 Placeholder 与必填报错` | `ux-p2-member-unify` | P0 | A3 | CERT-1 |  |
| 8 | `【PKI-Cert-&-Template-Detail】【UI】Transfer Admin - Cancel 与蒙层` | `ux-p2-member-unify` | P2 | A3 | CERT-1 |  |
| 9 | `【Ecosystem-Factory-Factory-Info】【UI】Member 列表 - 默认列 Columns 与 Admin 菜单` | `ux-p2-member-unify` | P0 | A3 | FAC-1 |  |
| 10 | `【Ecosystem-Factory-Factory-Info】【UI】Transfer Admin - 弹窗文案 Placeholder 与必填报错` | `ux-p2-member-unify` | P0 | A3 | FAC-1 |  |
| 11 | `【Ecosystem-Factory-Factory-Info】【UI】Transfer Admin - Cancel 蒙层与下拉仅 Active` | `ux-p2-member-unify` | P2 | A3 | FAC-1 |  |
| 12 | `【Admin-Group】【UI】Member - Admin 行隐藏三点菜单且无 Transfer` | `ux-p2-member-unify` | P0 | A1 | GRP-1 Member |  |
| 13 | `【Admin-Account】【UI】删除批量转移 - Confirm Action 弹窗文案与资源卡片` | `ux-p2-member-unify` | P0 | A1 | D2 | 只打开 Confirm Action，不 Confirm |
| 14 | `【Admin-Account】【UI】删除批量转移 - Cancel 关闭与蒙层` | `ux-p2-member-unify` | P2 | A1 | D2 | Cancel/蒙层 |

## B5 Transfer E2E（6 · 🔴）

> 每条后按 plan 复位；建议将「中英文」并入顺序 1/2，避免额外消耗 Key。

| # | 用例名称 | feature | 等级 | actor | resources | 备注 |
|---|---|---|---|---|---|---|
| 1 | `【KMS-Key-Detail】【E2E】Transfer Admin - 目标已在 Member 成功移交` | `ux-p2-member-unify` | P0 | A3→A4 | KEY-1 | 复位：A4→Transfer 回 A3 |
| 2 | `【KMS-Key-Detail】【E2E】Transfer Admin - 目标不在 Member 新增为 Admin` | `ux-p2-member-unify` | P1 | A3→A5 | KEY-2 | 复位：A5→Transfer 回 A3 |
| 3 | `【KMS-Key-Detail】【UI】Transfer Admin - 中英文标题报错与 Toast` | `ux-p2-member-unify` | P2 | A3 | KEY-1 或 KEY-2 | 合并进 #1/#2 执行 |
| 4 | `【PKI-Cert-&-Template-Detail】【E2E】Transfer Admin - 成功移交` | `ux-p2-member-unify` | P0 | A3→A8 | CERT-1 | 复位：A8→Transfer 回 A3 |
| 5 | `【Ecosystem-Factory-Factory-Info】【E2E】Transfer Admin - 目标已在列表成功移交` | `ux-p2-member-unify` | P0 | A3→A10 | FAC-1 | 原 Admin→Factory Manager；复位回 A3 |
| 6 | `【Ecosystem-Factory-Factory-Info】【E2E】Transfer Admin - 目标不在列表新增为 Factory Admin` | `ux-p2-member-unify` | P1 | A3→A11 | FAC-2 | 复位：A11→Transfer 回 A3 |

## B6 Account 删除类（5 · 🔴）

| # | 用例名称 | feature | 等级 | actor | resources | 备注 |
|---|---|---|---|---|---|---|
| 1 | `【Admin-Account】【Functional】删除 - 无 Admin 身份可直接删除` | `ux-p2-member-unify` | P1 | A1 | D4 | 无 Admin，可直接删 |
| 2 | `【Product-Member】【E2E】Member 列表 - Account 删除后不可见该用户` | `ux-p2-member-unify` | P0 | A1 | D1 + PROD-5 | 删前确认 Member 可见 |
| 3 | `【Admin-Account】【Functional】删除批量转移 - 归档锁定纳入、已删除已销毁不纳入` | `ux-p2-member-unify` | P1 | A1 | D3 + S-* | 可先只观察弹窗 |
| 4 | `【Admin-Account】【E2E】删除批量转移 - 选择 Target Admin 移交并删除` | `ux-p2-member-unify` | P0 | A1 | D2→A12 | 消耗 D2 |
| 5 | `【Operation-User(SNB)】【E2E】删除批量转移 - Account（SNB）与 Account 一致` | `ux-p2-member-unify` | P1 | A1 | D5 | User(SNB) |

## Agent 读取切片速查

| 批次 | 必读用例文件 | 台账最小切片 | baseline |
|---|---|---|---|
| B1 | `ux-p2-audit-unify.md` 全表 | A1、GRP-1 Audit、KEY-3、CERT-1、PROD-6、Profile | `ux-p2-audit-unify/baseline/` |
| B2 | `ux-p2-detail-supplement.md` 展示行 | R1–R3、PROD-1–4、各大列表 URL | `ux-p2-detail-supplement/baseline/` |
| B3 | 同上 · 编辑/权限行 | A1、A2、P1–P4、改前字段快照 | 同上 + Role |
| B4 | `ux-p2-member-unify.md` 只读行 | A3、A2、KEY-1、CERT-1、FAC-1、GRP-1、D2 | `ux-p2-member-unify/baseline/` |
| B5 | 同上 · Transfer E2E 行 | A3–A5、A8、A10、A11、KEY-1/2、CERT-1、FAC-1/2 | 同上 |
| B6 | 同上 · 删除行 | A1、A12、D1–D5、PROD-5、S-* | Account 删除弹窗 |

