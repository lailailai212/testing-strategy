# Sprint `OBIS-20260810-20260821` 执行记录

> 每轮执行的结果与数据变更。本轮无 execution-plan / data-ledger；用户指定账号与用例 MD 直跑。
> **禁止**在本文写明文密码或验证码。

## 轮次总览

| 轮次 | 环境 | 版本 / 部署时间 | 执行人 | 起止时间 | 通过 | 失败 | 阻塞 | 备注 |
|---|---|---|---|---|---|---|---|---|
| R1 | sit | 2026-08-13 现网 | Agent | 2026-08-13 | 2 | 4 | 10 | 角色权限矩阵回归 16 条；单账号门禁大量 Blocked |

HTML 报告：[`docs/sprints/OBIS-20260810-20260821/features/role-permission-matrix-regression/reports/report.html`](../../sprints/OBIS-20260810-20260821/features/role-permission-matrix-regression/reports/report.html)

## 批次进度

| 批次 | 用例数 | 已执行 | 通过 | 失败 | 阻塞 | 状态 |
|---|---|---|---|---|---|---|
| 角色权限矩阵回归（整包） | 16 | 16 | 2 | 4 | 10 | ✅ |

状态图例：⬜ 未开始 · 🟡 进行中 · ✅ 完成 · 🔴 阻塞

## 失败与阻塞明细

| 日期 | 批次 | 用例名称 | 结果 | 现象 | 缺陷链接 | 是否影响后续批次 |
|---|---|---|---|---|---|---|
| 2026-08-13 | RPM | 【Product-Member】【E2E】编辑产品内角色 - ⋮ 改为 Version Manager 后权限生效 | Fail | Assign Role 缺 Owner；步骤 3–4 无目标用户会话未保存 | 本地 BUG-RPM-01 | 否 |
| 2026-08-13 | RPM | 【Product-Member】【UI】无 Member 管理权限 - 不显示 Add 与 ⋮ | Blocked | 当前账号为该产品 Product Owner | - | 否 |
| 2026-08-13 | RPM | 【Factory】【E2E】Add User - 可分别赋予 Admin 与 Manager | Fail | Add 弹窗为 Add Factory Manager，无 Admin 选项 | 本地 BUG-RPM-02 | 否 |
| 2026-08-13 | RPM | 【Factory】【E2E】Edit User - Admin 与 Manager 切换 | Fail | 无 Edit User；Admin 行仅 Transfer，Manager 行仅 Remove | 本地 BUG-RPM-02 | 否 |
| 2026-08-13 | RPM | 【Factory】【UI】无工厂 Member 管理权限 - 不显示 Add/Edit | Blocked | Manager 现网仍有 Add；缺无管理权账号 | - | 否 |
| 2026-08-13 | RPM | 【Product-Overview】【UI】仅 Member - 不显示各写入口 | Blocked | 当前为 Owner | - | 否 |
| 2026-08-13 | RPM | 【Product-Version】【E2E】仅 Version Manager | Blocked | 无仅 VM 会话 | - | 否 |
| 2026-08-13 | RPM | 【Product-Batch】【E2E】仅 Batch Manager | Blocked | 无仅 BM 会话 | - | 否 |
| 2026-08-13 | RPM | 【Product-Assets】【E2E】仅 Resource Manager | Blocked | 无仅 RM 会话 | - | 否 |
| 2026-08-13 | RPM | 【Product-Overview】【UI】仅 Product Manager | Blocked | 无仅 PM 会话 | - | 否 |
| 2026-08-13 | RPM | 【Factory】【UI】Factory Manager - 不显示 Transfer Admin | Fail | Admin 行仍显示 Transfer Admin（disabled） | 本地 BUG-RPM-03 | 否 |
| 2026-08-13 | RPM | 【Product-Version】【Functional】无权限绕过 Version/Batch/Member | Blocked | 无仅 Member 会话，未打接口 | - | 否 |
| 2026-08-13 | RPM | 【Factory】【Functional】无权限绕过 Factory Add User | Blocked | 无无管理权会话，未打接口 | - | 否 |
| 2026-08-13 | RPM | 【Product-Member】【Functional】多角色叠加写入口并集 | Blocked | 仅观察到 test_user2 多角色标签，无法以其登录 | - | 否 |

### 【Product-Member】【E2E】编辑产品内角色 - ⋮ 改为 Version Manager 后权限生效

| 字段 | 值 |
|------|-----|
| 轮次 | R1 |
| 批次 | RPM |
| 结果 | Fail |
| 环境 | sit |
| actor / resources | future.wei@snowballtech.com / Test Product Negative `2087023093035761665` |
| 失败步骤 | [2] 缺 Owner；[3][4] Blocked |
| 现象 | Assign Role：PM / VM / BM / Member(锁) / RM |
| 证据 | `evidence/role-permission-matrix-regression/` 与 `reports/gifs/tc01-edit-role.gif` |
| 缺陷 | BUG-RPM-01 |
| 台账回填 | 无台账 |
| 复位 | 未保存角色，无需复位 |

### 【Factory】【UI】Factory Admin - 可见 Transfer Admin

| 字段 | 值 |
|------|-----|
| 轮次 | R1 |
| 批次 | RPM |
| 结果 | Pass |
| 环境 | sit |
| actor / resources | Cloud Factory 02 `6116540249038875` |
| 失败步骤 | - |
| 现象 | Transfer Admin 弹窗已开并 Cancel |
| 证据 | `reports/gifs/tc12-factory-admin-transfer.gif` |
| 缺陷 | - |
| 台账回填 | 无 |
| 复位 | 未 Confirm |

## 数据变更同步

| 日期 | 批次 | 变更内容 | 台账已回填 |
|---|---|---|---|
| 2026-08-13 | RPM | 无。Edit Role / Add Factory Manager / Transfer Admin / Chip Config Edit / Settings 均 Cancel | 无台账 |

## 复位确认

| 批次 | 需复位项 | 复位时间 | 确认人 |
|---|---|---|---|
| RPM | 无落库变更 | 2026-08-13 | Agent |

## 遗留与结论

- 未执行完整 E2E 的原因：单账号无法覆盖仅 Member / 仅 VM / 仅 BM / 仅 RM / 仅 PM；目标用户无法另开会话。
- 需下轮回归：TC01（补 Owner 选项或回写 AC）、TC03/04（Add/Edit 赋 Admin）、TC13（Manager 隐藏 Transfer）、TC02/06/08–11/14–16（补账号）。
- 另：Factory Cloud 01 头栏 Admin 与 Member 列表不一致（BUG-RPM-04）。
- 浏览器已关闭。
