#!/usr/bin/env python3
"""Generate self-reg-001-05-domain-whitelist testcases MD."""

from __future__ import annotations

OUTPUT = "docs/generate_doc/testcases/self-reg-001-05-domain-whitelist.md"

MODULE_SLUG = {
    "/Cloud/Login & Profile/Login": "Login-Profile-Login",
    "/Cloud/Login & Profile/My Profile": "Login-Profile-My-Profile",
    "/Super Admin Platform/OBIS Biz/Tenant": "OBIS-Biz-Tenant",
    "/Cloud/Admin/Account": "Admin-Account",
}

TAG = "企业域名白名单"

CASES: list[dict] = [
    # Login - 白名单申请提示
    {
        "tp": "TP-REG-APP-01", "mod": "/Cloud/Login & Profile/Login", "type": "UI", "branch": "白名单申请提示",
        "name": "首次注册命中域名展示弹窗", "level": "P0", "ac": "",
        "pre": "1. 超管已在 Super Admin → Tenant → Security Tab 开启 **Self-Registration** 并配置 **Email Domain**（如 partner.com）及 **Default Roles**<br>2. 目标企业租户为有效状态<br>3. 准备未注册 OBIS 账号的邮箱 user@partner.com",
        "steps": "[1] 使用 user@partner.com 完成注册/登录流程至首次进入系统前<br>[2] 查看是否出现企业加入提示弹窗",
        "exp": "[1] 注册流程正常进行<br>[2] 展示弹窗：标题 **Your email belongs to {企业名}**；正文含 *Would you like to join this enterprise?*；按钮 **Skip&Enter System**、**Apply to Join**",
    },
    {
        "tp": "TP-REG-APP-02", "mod": "/Cloud/Login & Profile/Login", "type": "UI", "branch": "白名单申请提示",
        "name": "Apply to Join 提交成功", "level": "P0", "ac": "",
        "pre": "1. 同 TP-REG-APP-01 前置<br>2. 已展示白名单加入提示弹窗",
        "steps": "[1] 点击 **Apply to Join**<br>[2] 查看提交后成功页文案与按钮",
        "exp": "[1] 申请提交成功<br>[2] 展示成功页：标题 **Application Submitted!**；正文 *Your application has been sent to the {企业名} enterprise administrator for review. Once approved, the enterprise will appear in your avatar dropdown menu. You don't need to wait — you can start using the trial OBIS now.*（示例企业名 Snow Tech）；底部按钮 **Enter Trail**",
    },
    {
        "tp": "TP-REG-APP-03", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "白名单申请提示",
        "name": "Skip 后再次登录不重复展示", "level": "P0", "ac": "",
        "pre": "1. 同 TP-REG-APP-01 前置<br>2. 首次已展示加入提示弹窗",
        "steps": "[1] 点击 **Skip&Enter System** 进入个人 trial workspace<br>[2] 退出登录后使用同一邮箱再次登录",
        "exp": "[1] 进入个人免费版/trial OBIS workspace，未提交加入申请<br>[2] 不再展示该企业的白名单加入提示弹窗",
    },
    {
        "tp": "TP-REG-APP-04", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "白名单申请提示",
        "name": "已有有效账号不展示", "level": "P1", "ac": "",
        "pre": "1. 目标企业已配置域名白名单且 Self-Registration 开启<br>2. 邮箱 user@partner.com 已存在有效 OBIS 账号",
        "steps": "[1] 使用 user@partner.com 登录 OBIS Portal",
        "exp": "[1] 登录成功；**不展示**白名单加入提示弹窗",
    },
    {
        "tp": "TP-REG-APP-05", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "白名单申请提示",
        "name": "租户非有效状态不展示", "level": "P0", "ac": "",
        "pre": "1. 目标企业租户处于非有效状态（待确认：Suspended/Expired 等）<br>2. 该租户曾配置 Email Domain 白名单<br>3. 准备未注册邮箱命中该域名",
        "steps": "[1] 使用命中域名的未注册邮箱完成注册/登录流程",
        "exp": "[1] **不展示**白名单加入提示弹窗",
    },
    {
        "tp": "TP-REG-APP-06", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "白名单申请提示",
        "name": "未开启 Self-Registration 不展示", "level": "P0", "ac": "",
        "pre": "1. 超管在 Tenant Detail **Security** Tab 将 **Self-Registration** 设为 **OFF**<br>2. 准备未注册邮箱，域名曾配置但未启用自注册",
        "steps": "[1] 使用该邮箱完成注册/登录流程",
        "exp": "[1] **不展示**白名单加入提示弹窗",
    },
    # 域名匹配
    {
        "tp": "TP-REG-DOM-01", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "域名匹配规则",
        "name": "子域名邮箱不匹配根域名白名单", "level": "P1", "ac": "",
        "pre": "1. 企业白名单仅配置 example.com<br>2. 准备未注册邮箱 user@sub.example.com",
        "steps": "[1] 使用 user@sub.example.com 完成注册/登录流程",
        "exp": "[1] **不展示**白名单加入提示弹窗（子域名不匹配）",
    },
    {
        "tp": "TP-REG-DOM-02", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "域名匹配规则",
        "name": "邮箱域名大小写不敏感", "level": "P1", "ac": "",
        "pre": "1. 企业白名单配置 example.com 且 Self-Registration 开启<br>2. 分别准备未注册邮箱 user@example.com 与 user@Example.COM",
        "steps": "[1] 使用 user@example.com 完成注册至加入提示弹窗<br>[2] 换账号使用 user@Example.COM 重复流程",
        "exp": "[1] 展示加入提示弹窗<br>[2] 同样展示加入提示弹窗（大小写视为相同域名）",
    },
    # 审批后申请人
    {
        "tp": "TP-REG-POST-01", "mod": "/Cloud/Login & Profile/Login", "type": "E2E", "branch": "审批后申请人行为",
        "name": "申请人仍可使用免费版 Tenant", "level": "P0", "ac": "AC-06",
        "pre": "1. 申请人已提交加入申请并被 Tenant Admin **Reject**<br>2. 申请人有个人免费版/trial workspace",
        "steps": "[1] 申请人登录 OBIS Portal<br>[2] 进入个人 workspace 执行基础操作（如查看 Welcome）",
        "exp": "[1] 登录成功<br>[2] 个人免费版 Tenant 可正常使用，未被禁用",
    },
    {
        "tp": "TP-REG-POST-02", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "审批后申请人行为",
        "name": "再次登录不重复展示加入提示", "level": "P0", "ac": "AC-06",
        "pre": "1. 申请人加入申请已被 **Reject**<br>2. 申请人曾展示过该企业加入提示",
        "steps": "[1] 申请人退出后再次使用同一邮箱登录",
        "exp": "[1] 登录成功；**不再展示**该企业的白名单加入提示弹窗",
    },
    # 边界 - 用户侧
    {
        "tp": "TP-EDGE-REG-01", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "边界场景",
        "name": "用户侧无再次申请入口", "level": "P1", "ac": "AC-06",
        "pre": "1. 申请人加入申请已被 Reject<br>2. 申请人已登录个人 workspace",
        "steps": "[1] 在注册/登录及登录后全流程查找「申请加入」或 **Apply to Join** 入口<br>[2] Tenant Admin 在 **ADMIN → Account → Invitations** Tab 发起邀请",
        "exp": "[1] 用户侧**无**再次发起域名白名单加入申请的入口<br>[2] Admin 可通过 **Invitations** 再次邀请该用户",
    },
    {
        "tp": "TP-EDGE-REG-02", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "边界场景",
        "name": "已是其他企业成员无二次申请入口", "level": "P1", "ac": "",
        "pre": "1. 用户已是企业 A 的 Active 成员<br>2. 企业 B 配置了包含该用户邮箱域名的白名单",
        "steps": "[1] 用户登录 OBIS Portal<br>[2] 尝试查找加入企业 B 的入口或重新注册",
        "exp": "[1] 登录成功<br>[2] **无**申请加入企业 B 的白名单提示或入口（提示仅在注册账号时出现）",
    },
    {
        "tp": "TP-MAIL-06", "mod": "/Cloud/Login & Profile/Login", "type": "Functional", "branch": "邮件通知",
        "name": "不向申请人发送邮件", "level": "P0", "ac": "AC-09",
        "pre": "1. 申请人邮箱可收信<br>2. 已展示加入提示弹窗",
        "steps": "[1] 点击 **Apply to Join** 提交申请<br>[2] 检查申请人邮箱收件箱（含垃圾邮件）",
        "exp": "[1] 申请提交成功<br>[2] 申请人邮箱**未收到**任何 OBIS 加入申请相关通知邮件",
    },
    # My Profile
    {
        "tp": "TP-ACCT-ACT-03", "mod": "/Cloud/Login & Profile/My Profile", "type": "UI", "branch": "审批操作",
        "name": "Approve 后头像下拉出现企业 Tenant", "level": "P1", "ac": "",
        "pre": "1. 申请人加入申请已被 Tenant Admin **Approve**<br>2. 申请人已登录 OBIS Portal",
        "steps": "[1] 点击右上角头像展开下拉菜单<br>[2] 查看 Tenant 列表<br>[3] 点击目标企业 Tenant 切换",
        "exp": "[1] 下拉展示用户姓名、邮箱<br>[2] Tenant 列表中出现目标企业（示例形态：**Enterprise · {企业名}**）<br>[3] 可成功切换进入该企业 Tenant",
    },
    # Super Admin
    {
        "tp": "TP-WL-CFG-01", "mod": "/Super Admin Platform/OBIS Biz/Tenant", "type": "Functional", "branch": "域名白名单配置",
        "name": "设置 Self-Registration 与 Default Roles", "level": "P0", "ac": "",
        "pre": "1. 使用超管账号登录 Super Admin Platform<br>2. 进入目标租户 Tenant Detail 页",
        "steps": "[1] 切换至 **Security** Tab<br>[2] 将 **Self-Registration** 设为 ON<br>[3] 展开 **Default Roles** 下拉，查看可选项并选择 **Normal User**（或任一目标角色）<br>[4] **Registration Method** 选择 **Email**<br>[5] **Email Domain** 输入白名单域名（如 partner.com）<br>[6] 点击 **Save**",
        "exp": "[1] Security Tab 正常展示<br>[2] 展开 Default Roles、Registration Method、Email Domain 字段<br>[3] 下拉包含 **System Manager**、**Product Manager**、**Resource Manager**、**Factory Manager**、**Normal User**；可成功选择目标角色<br>[4] Email 方式选中<br>[5] 域名输入成功<br>[6] 配置保存成功",
    },
    {
        "tp": "TP-WL-CFG-02", "mod": "/Super Admin Platform/OBIS Biz/Tenant", "type": "E2E", "branch": "域名白名单配置",
        "name": "Approve 后成员角色与白名单配置一致", "level": "P0", "ac": "AC-04",
        "pre": "1. 超管已将 **Default Roles** 设为 **Product Manager**<br>2. 申请人已提交加入申请且 Status 为 Pending<br>3. Tenant Admin 账号可审批",
        "steps": "[1] Tenant Admin 在 **ADMIN → Account → Applications** 点击该申请 **Approve**<br>[2] 切换至 **Members** Tab 查看新成员<br>[3] 或进入该成员 **User Detail** 查看 Role",
        "exp": "[1] Approve 成功，申请从 Applications 消失<br>[2] 新成员 Status 为 **Active**<br>[3] 成员 **Role** 为 **Product Manager**，与审批时刻 **Default Roles** 配置一致",
    },
    {
        "tp": "TP-EDGE-WL-01", "mod": "/Super Admin Platform/OBIS Biz/Tenant", "type": "Functional", "branch": "边界场景",
        "name": "修改白名单不影响已落库申请", "level": "P1", "ac": "AC-04;AC-05",
        "pre": "1. 已有 Pending 状态的加入申请<br>2. 超管可修改 Tenant Security 配置",
        "steps": "[1] 超管修改或删除对应 **Email Domain** / **Default Roles** 并 **Save**<br>[2] Tenant Admin 对原 Pending 申请执行 **Approve**<br>[3] 使用新邮箱（命中新配置域名）再次注册申请",
        "exp": "[1] 配置变更保存成功<br>[2] 原申请仍可 Approve/Reject；Approve 后角色等按**申请落库时**规则或审批时刻配置（与 Story 一致：已落库申请行为不变）<br>[3] 新申请受变更后配置约束",
    },
    # Mail
    {
        "tp": "TP-MAIL-01", "mod": "/Cloud/Admin/Account", "type": "E2E", "branch": "邮件通知",
        "name": "首次提交立即通知 Tenant Admin", "level": "P0", "ac": "",
        "pre": "1. 企业 Tenant Admin 邮箱可收信<br>2. 申请人首次点击 **Apply to Join** 提交申请",
        "steps": "[1] 申请人提交加入申请<br>[2] 检查该企业 Tenant Admin 邮箱",
        "exp": "[1] 申请在 Applications 列表为 Pending<br>[2] Tenant Admin **立即收到**申请通知邮件",
    },
    {
        "tp": "TP-MAIL-02", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "邮件通知",
        "name": "重复申请不重复发信", "level": "P0", "ac": "",
        "pre": "1. 同一用户已首次提交申请并触发过通知邮件<br>2. 记录 Tenant Admin 当前邮件数量",
        "steps": "[1] 同一用户再次尝试提交加入申请（若入口存在）或重复触发申请场景<br>[2] 检查 Tenant Admin 邮箱",
        "exp": "[1] 系统不视为新的首次申请<br>[2] **未重复发送**申请通知邮件",
    },
    {
        "tp": "TP-MAIL-03", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "邮件通知",
        "name": "主题为英文固定文案", "level": "P0", "ac": "",
        "pre": "1. 已触发首次申请通知邮件",
        "steps": "[1] 打开 Tenant Admin 收到的申请通知邮件<br>[2] 查看邮件主题",
        "exp": "[1] 邮件正常打开<br>[2] 主题为 **OBIS New Join Request Pending Review**（仅英文，不随 Admin 语言切换）",
    },
    {
        "tp": "TP-MAIL-04", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "邮件通知",
        "name": "正文英文在上中文在下", "level": "P0", "ac": "",
        "pre": "1. Tenant Admin 系统语言分别为英文与中文各测一次<br>2. 均已收到申请通知邮件",
        "steps": "[1] 分别打开两封通知邮件查看正文结构",
        "exp": "[1] 两封邮件正文均为**英文在上、中文在下**的双语结构；**不**根据 Admin 系统语言切换为单语版本",
    },
    {
        "tp": "TP-MAIL-05", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "邮件通知",
        "name": "正文包含申请关键信息", "level": "P1", "ac": "",
        "pre": "1. 申请人姓名、邮箱、申请时间、企业名称已知<br>2. Tenant Admin 已收到通知邮件",
        "steps": "[1] 打开申请通知邮件查看正文",
        "exp": "[1] 正文包含：申请人姓名、申请人邮箱、申请时间、企业名称及 OBIS Portal 快速登录链接",
    },
    {
        "tp": "TP-MAIL-07", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "邮件通知",
        "name": "存量租户 Admin 可收信", "level": "P0", "ac": "",
        "pre": "1. 使用**存量**企业租户（非新注册企业）<br>2. 已配置白名单且 Tenant Admin 邮箱有效",
        "steps": "[1] 新用户命中域名提交 **Apply to Join**<br>[2] 检查存量租户 Tenant Admin 邮箱",
        "exp": "[1] 申请提交成功<br>[2] 存量租户 Tenant Admin 正常收到通知邮件",
    },
    {
        "tp": "TP-MAIL-08", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "邮件通知",
        "name": "新增企业 Admin 可收信", "level": "P0", "ac": "",
        "pre": "1. 使用**新注册**企业租户并完成白名单配置<br>2. Tenant Admin 邮箱有效",
        "steps": "[1] 新用户命中域名提交 **Apply to Join**<br>[2] 检查新企业 Tenant Admin 邮箱",
        "exp": "[1] 申请提交成功<br>[2] 新企业 Tenant Admin 正常收到通知邮件",
    },
    {
        "tp": "TP-MAIL-09", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "邮件通知",
        "name": "多名 Tenant Admin 均收信", "level": "P0", "ac": "",
        "pre": "1. 同一企业租户下配置多名 Tenant Admin，邮箱均可收信<br>2. 准备新加入申请",
        "steps": "[1] 申请人提交 **Apply to Join**<br>[2] 分别检查各 Tenant Admin 邮箱",
        "exp": "[1] 申请提交成功<br>[2] **每名** Tenant Admin 均收到申请通知邮件",
    },
    {
        "tp": "TP-MAIL-10", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "邮件通知",
        "name": "发送失败补偿机制", "level": "P2", "ac": "",
        "pre": "1. 模拟或等待邮件发送失败场景（待确认：触发方式）",
        "steps": "[1] 触发申请通知邮件发送失败<br>[2] 观察系统补偿行为（重试/告警/人工补发等）",
        "exp": "[1] 发送失败可被观测<br>[2] （待确认：TBD）按产品定义的补偿机制执行",
    },
    # Account Tab / List
    {
        "tp": "TP-ACCT-TAB-01", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "Applications Tab",
        "name": "Members/Invitations/Applications 三 Tab 切换", "level": "P0", "ac": "",
        "pre": "1. Tenant Admin 已登录<br>2. 侧边栏 **ADMIN → Account** 进入 Account 页",
        "steps": "[1] 查看页顶 Tab 栏<br>[2] 依次点击 **Members**、**Invitations**、**Applications**<br>[3] 切换后返回前一 Tab",
        "exp": "[1] 展示 **Members**、**Invitations**、**Applications** 三个 Tab<br>[2] 各 Tab 展示对应列表内容<br>[3] 切换 Tab 互不影响各自数据展示",
    },
    {
        "tp": "TP-ACCT-APP-01", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "Applications 列表",
        "name": "展示 Pending 数量角标", "level": "P0", "ac": "AC-01",
        "pre": "1. Tenant Admin 已进入 Account 页<br>2. 当前存在 N 条 Status 为 **Pending** 的申请（不含 Rejected）",
        "steps": "[1] 查看 **Applications** Tab 右侧角标",
        "exp": "[1] 角标展示数字 **N**，且仅统计 **Pending** 状态申请",
    },
    {
        "tp": "TP-ACCT-APP-02", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "Applications 列表",
        "name": "无 Pending 时角标隐藏", "level": "P0", "ac": "AC-02",
        "pre": "1. Tenant Admin 已进入 Account 页<br>2. 当前 **无** Pending 申请（可为 0 条或仅 Rejected）",
        "steps": "[1] 查看 **Applications** Tab 角标",
        "exp": "[1] **Applications** Tab **不展示**数字角标",
    },
    {
        "tp": "TP-ACCT-APP-03", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "Applications 列表",
        "name": "展示 Name/Email/Applied At/Status/Actions 列", "level": "P0", "ac": "AC-03",
        "pre": "1. Tenant Admin 已进入 **Applications** Tab<br>2. 列表存在至少一条申请记录",
        "steps": "[1] 查看 Applications 列表表头与数据行",
        "exp": "[1] 列表展示列：**Name**、**Email**、**Applied At**、**Status**、**Actions**",
    },
    {
        "tp": "TP-ACCT-APP-04", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "Applications 列表",
        "name": "Pending 优先且同状态按时间降序", "level": "P0", "ac": "",
        "pre": "1. Applications 列表同时存在 Pending 与 Rejected 记录<br>2. 同状态内申请时间不同",
        "steps": "[1] 进入 **Applications** Tab 查看默认排序",
        "exp": "[1] **Pending** 排在 **Rejected** 之前；同一 Status 内按 **Applied At** 降序（最新在前）",
    },
    {
        "tp": "TP-ACCT-APP-05", "mod": "/Cloud/Admin/Account", "type": "UI", "branch": "Applications 列表",
        "name": "仅 Pending 展示 Approve/Reject", "level": "P0", "ac": "AC-03",
        "pre": "1. Applications 列表存在 Pending 与 Rejected 记录",
        "steps": "[1] 查看 Pending 行 **Actions** 列<br>[2] 查看 Rejected 行 **Actions** 列",
        "exp": "[1] Pending 行展示绿色 **Approve**、红色 **Reject**<br>[2] Rejected 行**不展示** Approve/Reject 按钮",
    },
    # 审批操作
    {
        "tp": "TP-ACCT-ACT-01", "mod": "/Cloud/Admin/Account", "type": "E2E", "branch": "审批操作",
        "name": "通过后成为成员且申请消失角标减 1", "level": "P0", "ac": "AC-01;AC-04",
        "pre": "1. Tenant Admin 在 **Applications** Tab<br>2. 存在 Pending 申请，角标为 N（N≥1）<br>3. 成员未达上限",
        "steps": "[1] 记录当前 Applications 角标数字<br>[2] 对目标 Pending 申请点击 **Approve**<br>[3] 刷新 Applications 列表并查看角标",
        "exp": "[1] 角标为 N<br>[2] Approve 成功<br>[3] 该条申请从 Applications **消失**；角标变为 **N-1**；申请人成为企业 **Active** 成员",
    },
    {
        "tp": "TP-ACCT-ACT-02", "mod": "/Cloud/Admin/Account", "type": "E2E", "branch": "审批操作",
        "name": "通过后出现在 Members 列表", "level": "P0", "ac": "AC-04",
        "pre": "1. 已对某 Pending 申请执行 **Approve** 成功",
        "steps": "[1] 在 Account 页切换至 **Members** Tab<br>[2] 按申请人邮箱查找该用户",
        "exp": "[1] Members 列表正常展示<br>[2] 申请人出现在列表中，**Status** 为 **Active**",
    },
    {
        "tp": "TP-ACCT-ACT-04", "mod": "/Cloud/Admin/Account", "type": "E2E", "branch": "审批操作",
        "name": "Reject 后 Rejected 保留列表角标减 1", "level": "P0", "ac": "AC-01;AC-05",
        "pre": "1. Applications 存在 Pending 申请，角标为 N（N≥1）",
        "steps": "[1] 对目标 Pending 申请点击 **Reject**<br>[2] 查看该行 Status 与列表<br>[3] 查看 Applications Tab 角标",
        "exp": "[1] Reject 成功<br>[2] 该条 **Status** 变更为 **Rejected**，记录**保留**在 Applications 列表<br>[3] 角标变为 **N-1**",
    },
    {
        "tp": "TP-ACCT-ACT-05", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "审批操作",
        "name": "审批不向申请人发送邮件", "level": "P0", "ac": "AC-04;AC-09",
        "pre": "1. 申请人邮箱可收信<br>2. 存在 Pending 申请",
        "steps": "[1] Tenant Admin 点击 **Approve** 通过申请<br>[2] 检查申请人邮箱<br>[3] 对另一条申请点击 **Reject**<br>[4] 再次检查申请人邮箱",
        "exp": "[1] Approve 成功<br>[2] 申请人**未收到**邮件<br>[3] Reject 成功<br>[4] 申请人**仍未收到**邮件",
    },
    {
        "tp": "TP-ACCT-ACT-06", "mod": "/Cloud/Admin/Account", "type": "E2E", "branch": "审批操作",
        "name": "达上限 Approve 弹出配额弹窗阻断", "level": "P0", "ac": "AC-07",
        "pre": "1. 免费版企业租户 Members 已达 **10** 人上限<br>2. Applications 存在 Pending 申请",
        "steps": "[1] 在 **Applications** Tab 点击该申请 **Approve**<br>[2] 查看弹窗内容与 Members 人数",
        "exp": "[1] 弹出统一配额触达弹窗：标题 **Product Limit Reached**；副标题 *Upgrade to Enterprise for higher limits.*；按钮 **Contact Sales for Enterprise**、**Maybe later**<br>[2] Approve **未生效**；申请仍为 Pending；Members 人数仍为 10",
    },
    {
        "tp": "TP-ACCT-ACT-07", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "审批操作",
        "name": "达上限 Reject 仍可执行", "level": "P1", "ac": "AC-07",
        "pre": "1. 免费版企业租户 Members 已达 **10** 人上限<br>2. Applications 存在 Pending 申请",
        "steps": "[1] 点击 **Approve** 触发配额弹窗后点击 **Maybe later** 关闭<br>[2] 对同一申请点击 **Reject**",
        "exp": "[1] 弹窗关闭，申请仍为 Pending<br>[2] **Reject** 成功；Status 变为 **Rejected**；不受成员限额影响",
    },
    # 权限
    {
        "tp": "TP-PERM-01", "mod": "/Cloud/Admin/Account", "type": "E2E", "branch": "权限",
        "name": "Tenant Admin 可查看并审批", "level": "P0", "ac": "AC-03",
        "pre": "1. 使用 **Tenant Admin** 角色账号登录",
        "steps": "[1] 进入 **ADMIN → Account → Applications** Tab<br>[2] 对 Pending 申请执行 **Approve** 或 **Reject**",
        "exp": "[1] 可查看申请列表及 **Approve**/**Reject** 按钮<br>[2] 审批操作执行成功",
    },
    {
        "tp": "TP-PERM-02", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "权限",
        "name": "Tenant Manager 不可查看待审核列表", "level": "P0", "ac": "",
        "pre": "1. 使用 **Tenant Manager** 角色账号登录",
        "steps": "[1] 进入 **ADMIN → Account** 页<br>[2] 查找 **Applications** Tab 或待审核申请入口",
        "exp": "[1] Account 页可访问（或按权限受限）<br>[2] **无** Applications 待审核列表入口，或访问被拒绝/不可见",
    },
    {
        "tp": "TP-PERM-03", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "权限",
        "name": "Tenant Manager 不可 Approve/Reject", "level": "P1", "ac": "",
        "pre": "1. Tenant Manager 账号可间接到达申请数据场景（如 API/越权测试）",
        "steps": "[1] 尝试对 Pending 申请执行 **Approve** 或 **Reject**",
        "exp": "[1] 操作被拒绝或无权限；申请状态不变",
    },
    # 成员限额
    {
        "tp": "TP-BIZ-01", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "成员限额",
        "name": "Pending 申请不计入成员名额", "level": "P0", "ac": "AC-07",
        "pre": "1. 当前 Active 成员 9 人<br>2. Applications 存在 2 条 Pending 申请<br>3. 免费版上限 10 人",
        "steps": "[1] 对其中 1 条 Pending 点击 **Approve**",
        "exp": "[1] Approve **成功**（9+1=10，Pending 本身不计入限额）；未因 Pending 数量误阻断",
    },
    {
        "tp": "TP-BIZ-02", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "成员限额",
        "name": "Approve 通过后占用 1 个名额", "level": "P0", "ac": "AC-07",
        "pre": "1. 记录 Approve 前 **Members** Tab 成员人数 M<br>2. 存在 Pending 申请且未达上限",
        "steps": "[1] 执行 **Approve** 通过<br>[2] 查看 **Members** Tab 人数",
        "exp": "[1] Approve 成功<br>[2] Members 人数变为 **M+1**",
    },
    # 审计
    {
        "tp": "TP-AUDIT-01", "mod": "/Cloud/Admin/Account", "type": "Functional", "branch": "审计日志",
        "name": "Approve 操作有审计记录", "level": "P0", "ac": "AC-08",
        "pre": "1. Tenant Admin 已对某申请执行 **Approve**<br>2. 已知操作人邮箱、申请人邮箱、操作时间",
        "steps": "[1] **ADMIN → Account → Members** → 进入相关成员 **User Detail**<br>[2] 滚动至页底 **Audit** 表格<br>[3] 查找 Approve 相关记录",
        "exp": "[1] User Detail 页正常打开<br>[2] Audit 表展示列：**Operation**、**Operation Type**、**Operation Time**、**Operation Name**<br>[3] 存在 Approve 操作记录，包含操作时间、操作类型；操作人邮箱、申请人邮箱（待确认：字段落点）",
    },
]


def row(c: dict) -> str:
    slug = MODULE_SLUG[c["mod"]]
    ac = f";{c['ac']}" if c.get("ac") else ""
    name = f"【{slug}】【{c['type']}】{c['branch']} - {c['name']}"
    tag = f"{TAG};{c['tp']}{ac}"
    return f"| {name} | {c['mod']} | {tag} | {c['level']} | {c['pre']} | {c['steps']} | {c['exp']} |"


def main() -> None:
    levels = {}
    types = {}
    for c in CASES:
        levels[c["level"]] = levels.get(c["level"], 0) + 1
        types[c["type"]] = types.get(c["type"], 0) + 1

    lvl_str = "，".join(f"{k} × {v}" for k, v in sorted(levels.items()))
    typ_str = "，".join(f"{k} × {v}" for k, v in sorted(types.items()))

    header = f"""# 【自注册】001-05 — 企业域名白名单审批管理 功能测试用例

> 来源：`docs/generate_doc/test-points/self-reg-001-05-domain-whitelist.md`（含 TP-ID）；脑图：`docs/generate_doc/test-points-xmind/self-reg-001-05-domain-whitelist-test-points.xmind`  
> 需求：【自注册】001-05 — 企业域名白名单审批管理  
> 用例数：{len(CASES)}（{lvl_str}；{typ_str}）  
> 入口规则：用户侧加入提示 → 注册/登录流程展示 **Your email belongs to {{企业名}}** 弹窗（**Skip&Enter System** / **Apply to Join**）；Tenant Admin 审批 → 侧边栏 **ADMIN → Account** → **Applications** Tab → **Approve**/**Reject**；超管白名单 → **Super Admin Platform → Tenant → Security** Tab（**Self-Registration**、**Default Roles**、**Email Domain**）；成员/审计 → **Members** Tab / **User Detail → Audit**；Tenant 切换 → 右上角头像下拉。  
> 产品规则：Applications 角标仅统计 Pending；Pending 不计入免费版 10 人成员限额；Approve/Reject 不向申请人发邮件；通知邮件主题 `OBIS New Join Request Pending Review`，正文英上中下；达上限 Approve 弹出 **Product Limit Reached** 统一配额弹窗；审计仅记录 Approve。  
> Baseline：`docs/baseline/self-reg-001-05/*-baseline.md`  
> 模块映射：`docs/generate_doc/testcases/modules/self-reg-001-05-domain-whitelist-module-mapping.json`  
> 用例名称格式：`【{{模块 slug}}】【UI|Functional|E2E】{{子功能}} - {{描述}}`（如 `/Cloud/Admin/Account` → `Admin-Account`）

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 |
| --- | --- | --- | --- | --- | --- | --- |
"""
    body = "\n".join(row(c) for c in CASES)
    content = header + body + "\n"

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Wrote {len(CASES)} cases to {OUTPUT}")
    print("Levels:", levels)
    print("Types:", types)


if __name__ == "__main__":
    main()
