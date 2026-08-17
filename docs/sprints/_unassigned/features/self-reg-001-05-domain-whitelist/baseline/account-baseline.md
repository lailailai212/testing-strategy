# Account 管理页 UI Baseline — 【自注册】001-05

> **MeterSphere 模块**：`/Cloud/Admin/Account`  
> **Story**：企业域名白名单审批管理  
> **截图来源**：用户提供（2026-06-16）

## 页面入口

```text
左侧边栏 ADMIN → Account
面包屑：Home / Account
```

页头：

- 标题：**Account**
- 副标题：**Manage team members and their access.**
- 右上角：**Limit** 开关、**+ Create** 按钮

## Tab 结构

| Tab | 角标 | 用途（本 Story） |
|-----|------|------------------|
| **Members** | 无 | 审批通过后申请人出现在此列表 |
| **Invitations** | 红点数字（示例 `1`） | 被拒后 Admin 再次邀请入口（TP-EDGE-REG-01） |
| **Applications** | 红点数字，**仅统计 Pending**（示例 `2`） | 域名白名单加入申请列表与 Approve/Reject |

切换 Tab 互不影响各自内容（TP-ACCT-TAB-01）。

## Applications Tab

**截图**：[`screenshots/account-applications.png`](screenshots/account-applications.png)

### 列表列

| 列名 | 说明 |
|------|------|
| Name | 申请人姓名 |
| Email | 申请人邮箱 |
| Applied At | 申请时间（示例 `2026-05-24 14:30`） |
| Status | 状态徽章（Pending 为黄色） |
| Actions | 操作按钮 |

### 操作按钮

- **Pending** 行：绿色 **Approve**、红色 **Reject**
- **Rejected** 行：不展示 Approve/Reject（TP-ACCT-APP-05）

### 示例数据

| Name | Email | Applied At | Status |
|------|-------|------------|--------|
| Alice Wang | alice@partner.com | 2026-05-24 14:30 | Pending |
| Bob Liu | bob@partner.com | 2026-05-25 09:15 | Pending |

## Members Tab

**截图**：[`screenshots/account-members.png`](screenshots/account-members.png)

### 列表列

| 列名 | 说明 |
|------|------|
| Email | 成员邮箱 |
| Username | 成员姓名 |
| Phone | 手机号（脱敏，如 `+86 138****1234`） |
| Role | 成员角色 |
| Status | Active（绿）/ Locked（灰）等 |
| Created | 创建时间 |
| Actions | 行内 **…** 菜单 |

### 示例 Role 值

System Admin、Tenant Manager、Key Member、Factory Manager、Product Member

Approve 通过后，申请人应以 **Active** 状态出现在此列表（TP-ACCT-ACT-02）。

## Invitations Tab

**截图**：[`screenshots/account-invitations.png`](screenshots/account-invitations.png)

### 列表列

| 列名 | 说明 |
|------|------|
| Email | 被邀请人邮箱 |
| Username | 被邀请人姓名 |
| Role | 邀请角色 |
| Status | Pending / Expired 等 |
| Created | 创建时间 |
| Actions | 行内 **…** 菜单 |

### Status 展示

- **Pending**：黄色徽章 + 副文案 `Invitation sent, awaiting activation.`
- **Expired**：红色徽章 + 副文案 `Invitation expired.`

## 与本 Story 相关的 UI 规则

| 规则 | 说明 |
|------|------|
| Applications 角标 | 仅统计 **Pending** 数量；为 0 时隐藏（AC-01/02） |
| Approve 成功 | 该条从 Applications 消失；Members 新增 Active 成员；角标减 1 |
| Reject | Status 变为 Rejected；记录保留在 Applications；角标减 1 |
| 达上限 Approve | 弹出**统一配额触达弹窗**，阻断通过（TP-ACCT-ACT-06；见下节） |
| 达上限 Reject | 仍可正常 Reject（TP-ACCT-ACT-07） |
| 审计日志 | Approve 操作记录审计（见下节，TP-AUDIT-01） |

## 配额触达弹窗（TP-ACCT-ACT-06）

**触发**：成员已达上限（免费版默认 10 人）时，在 Applications Tab 对 Pending 申请点击 **Approve**。

**截图**：[`screenshots/quota-limit-reached-dialog.png`](screenshots/quota-limit-reached-dialog.png)

### 弹窗文案（英文，与 UI 一致）

| 区域 | 文案 |
|------|------|
| 主标题 | **Product Limit Reached** |
| 副标题 | Upgrade to Enterprise for higher limits. |
| 利益点 1 标题 | No product cap |
| 利益点 1 描述 | Unlimited products across all regions |
| 利益点 2 标题 | Higher quotas |
| 利益点 2 描述 | More keys, certs, batches, and volume |
| 利益点 3 标题 | Multi-factory |
| 利益点 3 描述 | Connect all your ODM/OEM lines |
| 利益点 4 标题 | Priority support |
| 利益点 4 描述 | Dedicated engineer & enterprise SLA |
| 底部说明 | Let your security provisioning move from evaluation to mass production. |
| 主按钮 | **Contact Sales for Enterprise** |
| 次按钮 | **Maybe later** |

### 行为规则

- 弹窗出现后 **Approve 不生效**，申请保持 Pending，Members 人数不变。
- 点击 **Maybe later** 关闭弹窗，可继续执行 **Reject**（TP-ACCT-ACT-07）。
- 本弹窗为平台**统一配额触达**样式；成员上限场景复用同一弹窗（标题为 Product Limit Reached，非单独「成员已满」文案）。

## User Detail 与审计日志（TP-AUDIT-01）

**截图**：[`screenshots/user-detail-audit.png`](screenshots/user-detail-audit.png)

### 入口

```text
ADMIN → Account → Members Tab → 点击目标成员行（或 Actions）
→ User Detail 页（页顶 **Back to Account**）
```

### User Detail 子 Tab

| Tab | 说明 |
|-----|------|
| **Self-Service** | 默认展示（截图当前 Tab） |
| **Whitelist** | 用户级白名单相关（与超管 Tenant 配置区分） |
| **Invite** | 邀请相关 |

### 用户信息卡片（摘要）

- 头像、姓名、邮箱、Role 标签（如 **System Admin**）
- **Tenant**：关联租户名（示例 `Zhang Ming's example.com`）
- **Phone**：脱敏手机号
- **Access Keys**：Access Key ID / Secret Access Key（Copy）
- **Account Info**：Register Channel（Self-Service）、Created、Creator、Last Login

### Audit 区域（页底表格）

| 列名 | 说明 | 示例 |
|------|------|------|
| **Operation** | 操作标识 | signup |
| **Operation Type** | 操作类型分类 | Authentication |
| **Operation Time** | 操作时间（UTC） | 2026-05-01 10:00 UTC |
| **Operation Name** | 操作名称 | Account Registration |

### 与 TP-AUDIT-01 的字段对照

Story 要求 Approve 记录包含：**操作时间、操作人邮箱、申请人邮箱、操作类型**。

当前 UI 列名为 Operation / Operation Type / Operation Time / Operation Name，**未直接展示操作人邮箱、申请人邮箱列**。

**待确认**：

- [ ] Approve 审计是写在**申请人** User Detail 还是**审批人** User Detail
- [ ] 操作人邮箱、申请人邮箱是否在 Operation Name 等字段内展示，或需展开/导出查看
- [ ] Approve 对应的 Operation / Operation Name 精确文案

> 本版本**仅记录 Approve**，不记录 Reject（见测试点 MD）。

## 关联 Baseline

| 主题 | 文档 |
|------|------|
| Login 白名单加入提示弹窗 | [`login-baseline.md`](login-baseline.md) |
| 头像下拉 Tenant 切换 | [`login-profile-baseline.md`](login-profile-baseline.md) |
| 超管 Tenant 白名单配置 | [`super-admin-tenant-baseline.md`](super-admin-tenant-baseline.md) |

## 仍待补充的 Baseline

- Approve 审计日志精确字段与落库位置确认
