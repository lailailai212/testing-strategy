# Story: 【自注册】001-05 — 企业域名白名单审批管理

**来源**: [飞书项目 User Story #7007102862](https://project.feishu.cn/obis/story/detail/7007102862)  
**空间**: OBIS (`obis`)  
**编号**: 572 | **优先级**: Must | **Epic**: OBIS自注册  
**模式**: Large（用户侧申请 + 邮件通知 + Admin 审批 + 成员限额 + 审计，跨模块且 AC > 8）

---

## Story AC

1.（AC-01）Account 管理页「待审核申请 / Applications」Tab 角标仅统计 Pending 数量。

2.（AC-02）无待处理 Pending 时角标隐藏。

3.（AC-03）Tenant Admin 可查看申请列表（姓名 / 邮箱 / 时间 / 状态 / 操作），可通过 / 拒绝 Pending 申请。

4.（AC-04）审批通过后，申请人自动成为 Active 成员并出现在 Members Tab；不向申请人发送邮件；该条申请从 Applications 列表消失。

5.（AC-05）审批拒绝后，申请状态变更为 Rejected，记录保留在 Applications 列表。

6.（AC-06）拒绝后申请人仍可正常使用免费版 Tenant，再次登录不再提示该企业白名单申请。

7.（AC-07）Pending 待审批申请不计入成员限额；审批通过后占用名额；成员已达上限时无法通过。

8.（AC-08）审批通过操作记录审计日志。

9.（AC-09）审批通过 / 拒绝均不向申请人发送邮件通知。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### 用户侧 — 白名单申请提示

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-REG-APP-01 | 需求描述 | P0 | 前提：目标租户为有效状态、超管已在 Tenant Security Tab 开启 Self-Registration 并配置 Email Domain；用户无有效 OBIS 账号且注册邮箱命中白名单域名，首次进入流程时展示加入提示：标题 **Your email belongs to {企业名}**；按钮 **Apply to Join** / **Skip&Enter System** |
| TP-REG-APP-02 | 需求描述 | P0 | 点击 **Apply to Join** 提交后展示成功页 **Application Submitted!**；正文含申请已发送至企业管理员审核、通过后企业出现在头像下拉、可先使用 trial OBIS；按钮 **Enter Trail** |
| TP-REG-APP-03 | 需求描述 | P0 | 用户选择「跳过」后，再次登录不再展示该企业的白名单加入提示 |
| TP-REG-APP-04 | QA扩展 | P1 | 用户已有有效账号时，不展示白名单加入申请提示（即使邮箱命中企业域名） |
| TP-REG-APP-05 | QA扩展 | P0 | 目标租户状态为非有效状态时，不展示白名单加入提示 |
| TP-REG-APP-06 | 需求描述 | P0 | 目标租户未开启域名白名单时，不展示白名单加入提示 |

### 用户侧 — 域名匹配规则

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-REG-DOM-01 | 需求描述 | P1 | 子域名邮箱（如 user@sub.example.com）不匹配白名单域名 example.com |
| TP-REG-DOM-02 | QA扩展 | P1 | 邮箱域名大小写不影响白名单匹配（如 user@Example.COM 与 user@example.com 视为相同） |

### 邮件通知 — 申请提交

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-01 | 需求描述 | P0 | 用户首次提交企业域名白名单申请后，系统立即向该企业 Tenant Admin 发送通知邮件 |
| TP-MAIL-02 | 需求描述 | P0 | 同一用户重复提交申请时，不重复发送通知邮件（每个用户仅首次申请触发） |
| TP-MAIL-03 | 需求描述 | P0 | 通知邮件主题为英文：`OBIS New Join Request Pending Review` |
| TP-MAIL-04 | 需求描述 | P0 | 通知邮件正文英文在上、中文在下；不根据 Tenant Admin 系统语言切换单语版本 |
| TP-MAIL-05 | QA扩展 | P1 | 邮件正文包含申请人姓名、邮箱、申请时间、企业名称及 OBIS Portal 快速登录链接 |
| TP-MAIL-06 | AC-09 | P0 | 用户提交加入申请时，系统不向申请人发送任何邮件（仅通知 Tenant Admin） |
| TP-MAIL-07 | QA扩展 | P0 | 存量租户企业的 Tenant Admin 能正常收到申请通知邮件 |
| TP-MAIL-08 | QA扩展 | P0 | 新增企业的 Tenant Admin 能正常收到申请通知邮件 |
| TP-MAIL-09 | QA扩展 | P0 | 同一企业租户下多名 Tenant Admin 均收到申请通知邮件 |

### 邮件通知 — 异常与补偿

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-10 | QA扩展 | P1 / 待确认 | 申请通知邮件发送失败时的补偿机制（重试 / 告警 / 人工补发等，**TBD**） |

### 域名白名单配置 — 默认角色

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-WL-CFG-01 | 需求描述 | P0 | 超管在 Super Admin → Tenant → **Security** Tab 开启 Self-Registration，配置 **Default Roles**（可选：System Manager / Product Manager / Resource Manager / Factory Manager / Normal User）、**Email Domain** 等默认成员角色与白名单域名 |
| TP-WL-CFG-02 | AC-04 | P0 | Approve 通过后，申请人实际分配角色与审批时刻白名单配置中的默认角色一致 |

### Account 管理 — Applications Tab 与列表

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACCT-TAB-01 | QA扩展 | P0 | Account 管理页顶部展示三个 Tab：Members、Invitations、Applications；切换 Tab 互不影响各自内容展示 |
| TP-ACCT-APP-01 | AC-01 | P0 | Applications Tab 右侧角标展示 Pending 状态申请数量 |
| TP-ACCT-APP-02 | AC-02 | P0 | Pending 数量为 0 时，Applications Tab 角标隐藏 |
| TP-ACCT-APP-03 | AC-03 | P0 | Applications 列表展示字段：Name、Email、Applied At、Status、Actions |
| TP-ACCT-APP-04 | QA扩展 | P0 | 列表默认排序：Pending 排在 Rejected 之前；同一状态内按申请时间降序（最新在前） |
| TP-ACCT-APP-05 | AC-03 | P0 | 仅 Status 为 Pending 的记录展示 Approve、Reject 操作按钮；Rejected 记录不展示操作按钮 |

### Account 管理 — 审批操作

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACCT-ACT-01 | AC-01, AC-04 | P0 | Tenant Admin 点击 Approve 后，申请人自动成为企业 Tenant 的 Active 成员；该条申请从 Applications 列表消失；Pending 角标减 1 |
| TP-ACCT-ACT-02 | AC-04 | P0 | Approve 通过后，申请人出现在 Members Tab 成员列表中 |
| TP-ACCT-ACT-03 | 需求描述 | P1 | Approve 通过后，申请人登录时头像下拉菜单中自动出现该企业 Tenant，可切换进入 |
| TP-ACCT-ACT-04 | AC-01, AC-05 | P0 | Tenant Admin 点击 Reject 后，申请 Status 变更为 Rejected；记录保留在 Applications 列表；Pending 角标减 1 |
| TP-ACCT-ACT-05 | AC-04, AC-09 | P0 | 审批 Approve / Reject 操作均不向申请人发送邮件通知 |
| TP-ACCT-ACT-06 | AC-07 | P0 | 成员已达上限（免费版默认 10 人）时 Admin 点击 Approve 无法通过申请，弹出统一配额触达弹窗（标题 **Product Limit Reached**；按钮 **Contact Sales for Enterprise** / **Maybe later**） |
| TP-ACCT-ACT-07 | AC-07 | P1 | 成员已达上限时，Reject 操作应仍可正常执行，不受成员限额影响 |

### 边界场景 — 申请期间配置变更与跨企业

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-EDGE-WL-01 | AC-04, AC-05 | P1 | Pending 期间超管修改或删除 Tenant Security 白名单配置后，已落库的申请数据及 Approve / Reject 行为不变；变更仅对新申请生效 |
| TP-EDGE-REG-01 | AC-06 | P1 | 申请被拒绝后，用户无再次发起加入申请的入口；仅 Tenant Admin 可通过 Invitations 再次邀请 |
| TP-EDGE-REG-02 | 需求描述 | P1 | 用户已是其他企业 Active 成员时，无入口再次申请加入本企业域名白名单（白名单加入提示仅在用户注册账号时出现） |

### 审批后 — 申请人侧行为

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-REG-POST-01 | AC-06 | P0 | 申请被拒绝后，申请人仍可正常使用自己的免费版 Tenant |
| TP-REG-POST-02 | AC-06 | P0 | 申请被拒绝后，申请人再次登录不再提示该企业的白名单加入申请 |

### 权限

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PERM-01 | AC-03 | P0 | Tenant Admin 可进入 Applications Tab，查看列表并执行 Approve / Reject |
| TP-PERM-02 | 需求描述 | P0 | Tenant Manager 不可查看待审核申请列表（无入口或无权限） |
| TP-PERM-03 | QA扩展 | P1 | Tenant Manager 不可执行 Approve / Reject 操作 |

### 成员限额与业务规则

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-BIZ-01 | AC-07 | P0 | Pending 状态的待审批申请不计入企业成员限额 |
| TP-BIZ-02 | AC-07 | P0 | Approve 通过后，新成员占用 1 个成员名额；Members 列表人数相应增加 |

### 审计日志

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUDIT-01 | AC-08 | P0 | Approve 操作在 Account 审计日志中记录，包含操作时间、操作人邮箱、申请人邮箱、操作类型 |

> **已确认**：当前版本审计日志**仅记录 Approve 操作**；不记录 Reject，也不单独记录「申请人创建」日志。

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 角标仅统计 Pending | TP-ACCT-APP-01；TP-ACCT-ACT-01；TP-ACCT-ACT-04 | ✅ |
| AC-02 无 Pending 时角标隐藏 | TP-ACCT-APP-02 | ✅ |
| AC-03 Admin 查看列表并通过 / 拒绝 | TP-ACCT-APP-03、TP-ACCT-APP-05、TP-PERM-01、TP-ACCT-ACT-01、TP-ACCT-ACT-04 | ✅ |
| AC-04 通过后成为成员、无邮件、记录消失 | TP-ACCT-ACT-01、TP-ACCT-ACT-02、TP-WL-CFG-02、TP-ACCT-ACT-05、TP-MAIL-06 | ✅ |
| AC-05 拒绝后 Rejected 且保留列表 | TP-ACCT-ACT-04；TP-EDGE-WL-01 | ✅ |
| AC-06 拒绝后免费用、不再提示 | TP-REG-POST-01、TP-REG-POST-02、TP-EDGE-REG-01 | ✅ |
| AC-07 限额规则与达上限无法通过 | TP-BIZ-01、TP-BIZ-02、TP-ACCT-ACT-06、TP-ACCT-ACT-07 | ✅ |
| AC-08 审批通过记录审计日志 | TP-AUDIT-01 | ✅ |
| AC-09 通过 / 拒绝均不发邮件给申请人 | TP-ACCT-ACT-05、TP-MAIL-06 | ✅ |

**AC-01～AC-09 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | 合计 |
|------|----|----|------|
| 用户侧申请提示 | 5 | 1 | 6 |
| 域名匹配规则 | 0 | 2 | 2 |
| 邮件通知（申请提交） | 8 | 1 | 9 |
| 邮件通知（异常与补偿） | 0 | 1 | 1 |
| 域名白名单配置 | 2 | 0 | 2 |
| Applications Tab / 列表 | 6 | 0 | 6 |
| 审批操作 | 6 | 1 | 7 |
| 边界场景 | 0 | 3 | 3 |
| 审批后申请人行为 | 2 | 0 | 2 |
| 权限 | 2 | 1 | 3 |
| 成员限额 | 2 | 0 | 2 |
| 审计日志 | 1 | 0 | 1 |
| **合计** | **34** | **10** | **44** |

| 来源 | 条数 |
|------|------|
| Story AC（AC-01～AC-09） | 20 |
| 需求描述 | 14 |
| QA扩展 | 10 |

评论已纳入：邮件主题仅英文、正文英上中下、取消按 Admin 语言切换。

---

## 评审修订记录（2026-06-15）

| 修订项 | 处理 |
|--------|------|
| 默认角色配置缺失 | 新增 TP-WL-CFG-01/02；ACT-02 聚焦 Members 列表展示 |
| Pending 期间白名单变更 | 新增 TP-EDGE-WL-01 |
| 被拒后重新申请 | 新增 TP-EDGE-REG-01 |
| 达上限时 Reject | 新增 TP-ACCT-ACT-07 |
| 域名匹配规则 | 新增 TP-REG-DOM-01/02 |
| 跨企业申请 | 新增 TP-EDGE-REG-02 |
| ACT-06 交互未明 | 标注 **TBD**，保留 P0 / 待确认 |
| AUDIT-02 与 AC-08 不符 | 删除 TP-AUDIT-02；确认仅 Approve log |
| 邮件模块缺 AC-09 | 新增 TP-MAIL-06 |

## 评审修订记录（2026-06-16，XMind 评审）

| 修订项 | 处理 |
|--------|------|
| 申请提示前提条件 | TP-REG-APP-01 补充租户有效 / 白名单开启 / 域名已配置；新增 TP-REG-APP-05/06 |
| 子域名匹配 | TP-REG-DOM-01 确认：子域名不匹配 |
| 大小写规则 | TP-REG-DOM-02 确认：不区分大小写 |
| 存量 / 新增租户邮件 | 新增 TP-MAIL-07/08 |
| 多 Tenant Admin 收信 | 新增 TP-MAIL-09 |
| 邮件失败补偿 | 新增 TP-MAIL-10（机制 **TBD**） |
| 白名单配置角色 | TP-WL-CFG-01 修正为超管配置 |
| 达上限 Approve 交互 | TP-ACCT-ACT-06 确认为统一配额触达弹窗 |
| Pending 期间白名单变更 | TP-EDGE-WL-01 确认：已落库申请不受影响 |
| 被拒后重新申请 | TP-EDGE-REG-01 确认：无用户侧入口，仅 Admin 邀请 |
| 跨企业申请 | TP-EDGE-REG-02 确认：仅注册时出现提示，无二次入口 |

---

## 评审修订记录（2026-06-16，Baseline 对齐）

| 修订项 | 处理 |
|--------|------|
| 加入提示 UI 文案 | TP-REG-APP-01 对齐 **Your email belongs to {企业名}** 弹窗 |
| 提交成功页文案 | TP-REG-APP-02 对齐 **Application Submitted!** 成功页 |
| Default Roles 可选值 | TP-WL-CFG-01 补充五类角色与 Security Tab 入口 |
| 配额触达弹窗 | TP-ACCT-ACT-06 补充 **Product Limit Reached** 文案 |
| 白名单配置变更主体 | TP-EDGE-WL-01 修正为超管（非 Tenant Admin） |

---

## 待确认

- [ ] 申请通知邮件发送失败时的补偿机制细节（TP-MAIL-10）
- [ ] 「无有效账号」的精确定义：仅从未注册，还是含已注册未激活等状态
- [ ] 租户「非有效状态」的具体枚举（Suspended / Expired 等，TP-REG-APP-05 测试数据）
- [ ] Approve 审计日志中操作人/申请人邮箱字段落点（TP-AUDIT-01）

## Out of Scope

- 付费版 / 升级套餐后的成员上限变化（本 Story 仅引用免费版默认 10 人作为上限场景）
- 审批通过后向申请人发送通知邮件
- Reject 操作写入审计日志（当前版本不记录）
