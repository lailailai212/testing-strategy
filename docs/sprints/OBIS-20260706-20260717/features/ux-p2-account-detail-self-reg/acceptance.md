# Story: 【体验优化P2】Account 详情（自注册版本）

**来源**: [飞书项目 User Story #7024469848](https://project.feishu.cn/obis/userstory/detail/7024469848)  
**空间**: OBIS (`obis`)  
**编号**: 735 | **优先级**: Must | **Epic**: UI及体验优化  
**模式**: Large（Create/Edit 抽屉 + 多类确认弹窗 + 详情/Profile/切换租户 + 权限矩阵，跨模块且规则多；飞书无 AC 编号，自拟粗粒度 AC）

---

## Story AC

1.（AC-01）有权限用户在 Account 列表点击 Create 后，应打开全宽「创建用户」抽屉；校验通过创建成功后关闭抽屉，Toast 提示已发送邀请邮件，并自动切换到 Invitation Tab，新记录在第一行且状态为 Pending。

2.（AC-02）从 Member 列表 Edit、用户详情编辑 icon、Invitation 列表 Edit 三个入口打开的「编辑用户」抽屉样式与功能一致；Email 不可改，其余字段可改；保存成功后 Toast 提示，详情/再次编辑可见更新。

3.（AC-03）Member 锁定/删除、Invitation 重新邀请/删除、Application 通过/拒绝的确认弹窗标题均为「确认操作」，文案符合规格；Confirm 执行操作，Cancel/关闭 icon 不执行，点击蒙层不可关闭。

4.（AC-04）用户详情页展示基本信息与右侧其他信息（含注册渠道、套餐标签、Notes 展开）；免费版套餐标签可打开版本对比弹窗，企业版不可点；返回列表保持原页码/筛选/排序/列显示。

5.（AC-05）头像下拉展示切换账户列表（正常/Locked/Pending 样式与当前 ✅）；免费版展示「升级套餐」并打开版本对比，企业版不展示；可进入 Profile、可退出登录。

6.（AC-06）Profile 页功能与 Account 详情一致；返回上一页；进入时左侧菜单保持进入前选中项。

7.（AC-07）Account 权限：Create 按钮按【Create Button】显隐；Member/Invitation/Application 的 Operation 三点始终可点，无对应权限时菜单项置灰。

8.（AC-08）用户详情 Audit Tab 名称为「Audit / 日志」，日志列表按 UI 样式更新（日志业务规则另 Story）。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号；否则填 `需求描述` 或 `QA扩展`。  
> **优先级口径**：P0 = 冒烟/阻断主路径（每条 AC 至少 1 条）；P1 = 重要交互与权限回归；P2 = 文案细节、样式与边缘。

### 邀请用户 — Create Account 抽屉

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACCT-CRT-01 | AC-01 | P0 | 有 Create 权限用户在 Account 列表点击右上角 Create，打开全宽「Create Account / 创建用户」抽屉 |
| TP-ACCT-CRT-02 | AC-01 | P0 | 必填 Email、Name、User Role 校验通过后点击 Create：关闭抽屉；Toast 为「操作成功。已发送邀请邮件…」中英文规格文案；自动切到 Invitation Tab，新记录在第一行且状态 Pending |
| TP-ACCT-CRT-03 | 需求描述 | P1 | 表单含 Phone、Notes（非必填）；Email/Name 占位 `Please Enter`/`请输入`，User Role 占位 `Please Select`/`请选择`；必填项带 `*` |
| TP-ACCT-CRT-04 | 需求描述 | P1 | 点击右上角关闭 icon 或 Cancel：关闭抽屉且不保存已填内容 |
| TP-ACCT-CRT-05 | 需求描述 | P1 | 点击抽屉外黑色蒙层，抽屉不关闭 |
| TP-ACCT-CRT-06 | QA扩展 | P1 | 必填项为空时点击 Create，不创建成功、不切 Tab、不发邀请（停留抽屉并提示校验） |
| TP-ACCT-CRT-07 | 需求描述 | P2 | 抽屉文字颜色/大小、输入框尺寸等样式与 UI 稿一致（对照 Figma） |

### 编辑用户 — Edit Account 抽屉

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACCT-EDT-01 | AC-02 | P0 | Member 列表 Operation → Edit，打开「Edit Account / 编辑用户」抽屉，自动带入已有数据 |
| TP-ACCT-EDT-02 | AC-02 | P0 | 修改 Name/Role/Phone/Notes 后点 Save：关闭抽屉，Toast 操作成功；再次打开 Edit 或进入用户详情可见更新；Email 始终不可修改 |
| TP-ACCT-EDT-03 | AC-02 | P0 | 用户详情页卡片右上角编辑 icon 打开的编辑抽屉与列表 Edit 样式、字段、行为一致 |
| TP-ACCT-EDT-04 | AC-02 | P1 | Invitation 列表 Operation → Edit 打开的编辑抽屉与 Member/详情入口完全一致 |
| TP-ACCT-EDT-05 | 需求描述 | P1 | 编辑抽屉关闭 icon / Cancel 不保存；点击蒙层不可关闭 |
| TP-ACCT-EDT-06 | QA扩展 | P2 | 未修改任何字段直接 Save，仍可成功关闭并提示成功（或按产品约定无变更提示） |

### 确认弹窗 — Member 锁定 / 删除

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACCT-LCK-01 | AC-03 | P0 | 触发 Member 锁定：弹窗标题「Confirm Action / 确认操作」；正文为锁定后禁用账号、无法操作系统的中英文规格文案；Confirm 执行锁定 |
| TP-ACCT-DEL-01 | AC-03 | P0 | 触发 Member 删除：标题「确认操作」；正文为删除后无法恢复的中英文规格文案；Confirm 执行删除 |
| TP-ACCT-DEL-02 | 需求描述 | P1 | Member 删除确认文案使用独立 i18n key，不与「删除租户」文案共用 |
| TP-ACCT-CFM-01 | AC-03 | P1 | Member 锁定/删除弹窗：Cancel 与关闭 icon 不执行操作；点击蒙层不可关闭 |

### 确认弹窗 — Invitation 重新邀请 / 删除

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-INV-REI-01 | AC-03 | P0 | 触发重新邀请：标题「确认操作」；正文为将生成全新激活链接并邮件通知受邀人的中英文规格文案；Confirm 执行 |
| TP-INV-DEL-01 | AC-03 | P0 | 触发 Invitation 删除：标题「确认操作」；正文为邀请链接立即失效且无法恢复的中英文规格文案；Confirm 执行 |
| TP-INV-CFM-01 | AC-03 | P1 | Invitation 重邀/删除弹窗：Cancel、关闭 icon 不执行；蒙层不可关闭 |

### 确认弹窗 — Application 通过 / 拒绝

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-APP-APV-01 | AC-03 | P0 | 触发 Approve：标题「确认操作」；正文为通过后将成为本组织成员的中英文规格文案；Confirm 执行通过 |
| TP-APP-REJ-01 | AC-03 | P0 | 触发 Reject：标题「确认操作」；正文为拒绝不可撤回、申请作废的中英文规格文案；Confirm 执行拒绝 |
| TP-APP-CFM-01 | AC-03 | P1 | Application 通过/拒绝弹窗：Cancel、关闭 icon 不执行；蒙层不可关闭 |

### 用户详情 — 基本信息与其他信息

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-DET-BAS-01 | AC-04 | P0 | 用户详情左侧展示 Name、Email、User Role、Tenant、Phone；右侧展示 Created Time（年月日时分秒）、Created By、Register Channel、Notes |
| TP-DET-BAS-02 | AC-04 | P0 | Register Channel 按用户来源展示：`Self Register` 自注册 / `Apply to Join` 申请加入 / `Invited Join` 邀请加入 |
| TP-DET-PLAN-01 | AC-04 | P0 | Tenant 旁套餐标签：免费版可点击并打开版本对比弹窗；企业版仅展示、点击不打开 |
| TP-DET-BACK-01 | AC-04 | P0 | 点击左上角返回：回到 Account List，且保持进入详情前的页码、筛选项、排序规则、列显示 |
| TP-DET-NOTE-01 | AC-04 | P1 | Notes 单行独占；最长展示三行，超出省略号 + 展开箭头；点击展开打开抽屉展示全文，关闭 icon 关闭抽屉 |
| TP-DET-STS-01 | 需求描述 | P1 | 头像状态小点：Active 为绿色，Locked 为黄色（尺寸对照 UI） |
| TP-DET-CRT-01 | 需求描述 | P1 | Created By 展示头像 + Name + 邮箱 icon；鼠标悬停展示邮箱与复制 icon，可复制邮箱 |
| TP-DET-EDT-01 | AC-02, AC-04 | P1 | 详情卡片右上角编辑按钮打开与列表一致的 Edit 抽屉 |
| TP-DET-KEY-01 | 需求描述 | P2 | Access Keys 仍在详情卡片内，现有功能与样式不变（不提前迁到 Tab） |
| TP-DET-UI-01 | 需求描述 | P2 | Role 标签、Tenant/Phone 图标等样式与列表/UI 稿一致 |

### 切换租户（头像下拉）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SW-01 | AC-05 | P0 | 点击系统右上角头像弹出切换弹窗：顶部头像+邮箱；列表标题「Switch Account / 切换账户」；当前账户有 ✅ |
| TP-SW-02 | AC-05 | P0 | 列表项展示：正常账户=头像+Name+套餐名；Locked/Pending 账户置灰并显示对应状态文案 |
| TP-SW-03 | AC-05 | P0 | 当前为免费版时展示「Upgrade Plan / 升级套餐」，点击打开版本对比弹窗；企业版不展示该入口 |
| TP-SW-04 | AC-05 | P1 | 点击 Profile 跳转 Profile 页；点击 Sign Out 退出登录并进入登录页 |
| TP-SW-05 | 需求描述 | P2 | 顶部邮箱过长显示省略号；租户头像由系统按首字母/首汉字生成 |

### Profile

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PROF-01 | AC-06 | P0 | Profile 页展示内容与交互与 Account 用户详情页一致（基本信息、其他信息、编辑等） |
| TP-PROF-02 | AC-06 | P0 | 从任意页进入 Profile 后，左侧菜单仍保持进入前选中的菜单项 |
| TP-PROF-03 | AC-06 | P1 | 点击左上角返回，回到进入 Profile 前的上一页面 |

### 权限控制

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PERM-CRT-01 | AC-07 | P0 | Role 配置【Create Button】时 Account 列表可见 Create；未配置时 Create 按钮不可见 |
| TP-PERM-MEM-01 | AC-07 | P0 | 无 Member Edit/Lock/Delete 对应权限时：Operation 三点仍可点开，对应菜单项置灰不可用；有权限时可正常操作 |
| TP-PERM-INV-01 | AC-07 | P0 | Invitation：无 Edit / Delete / Re-invite 权限时三点可开、对应项置灰；有权限可操作（Edit→【Edit Operation】；Delete→【Delete Operation】；Re-invite→【Re-invite Operation】） |
| TP-PERM-APP-01 | AC-07 | P0 | Application：无【Review Operation】时 Approve/Reject 置灰；有权限可操作；三点始终可点 |
| TP-PERM-MEM-02 | AC-07 | P1 / 待确认 | Member Edit 置灰/可用受【Create Button】控制（与 Create 同权限码，按需求原文验收；产品是否有意待确认） |

### Audit 日志 Tab

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUD-01 | AC-08 | P0 | 用户详情存在 Tab「Audit / 日志」，列表布局与样式按 UI 稿更新 |
| TP-AUD-02 | 需求描述 | P2 | 本 Story 不验收日志字段业务规则（属另 Story）；仅核对列表视觉与 Tab 名称 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点（含 P0） | 覆盖状态 |
|----------|---------------------|----------|
| AC-01 Create 邀请抽屉与成功后切 Invitation | TP-ACCT-CRT-01（P0）；TP-ACCT-CRT-02（P0） | ✅ |
| AC-02 三入口编辑抽屉一致、保存生效 | TP-ACCT-EDT-01～03（P0）；TP-ACCT-EDT-04（P1） | ✅ |
| AC-03 各类确认弹窗文案与 Confirm/Cancel/蒙层 | TP-ACCT-LCK-01、DEL-01、INV-REI-01、INV-DEL-01、APP-APV-01、APP-REJ-01（P0） | ✅ |
| AC-04 用户详情信息、套餐标签、返回保持列表状态 | TP-DET-BAS-01/02、PLAN-01、BACK-01（P0） | ✅ |
| AC-05 切换租户列表与升级套餐入口 | TP-SW-01～03（P0） | ✅ |
| AC-06 Profile 与详情一致、菜单保持、返回 | TP-PROF-01/02（P0） | ✅ |
| AC-07 Create 显隐与 Operation 置灰规则 | TP-PERM-CRT-01、MEM-01、INV-01、APP-01（P0） | ✅ |
| AC-08 Audit Tab 名称与列表 UI | TP-AUD-01（P0） | ✅ |

**AC-01～AC-08 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| 邀请用户 — Create Account 抽屉 | 2 | 4 | 1 | 7 |
| 编辑用户 — Edit Account 抽屉 | 3 | 2 | 1 | 6 |
| 确认弹窗 — Member 锁定/删除 | 2 | 2 | 0 | 4 |
| 确认弹窗 — Invitation 重邀/删除 | 2 | 1 | 0 | 3 |
| 确认弹窗 — Application 通过/拒绝 | 2 | 1 | 0 | 3 |
| 用户详情 — 基本信息与其他信息 | 4 | 4 | 2 | 10 |
| 切换租户（头像下拉） | 3 | 1 | 1 | 5 |
| Profile | 2 | 1 | 0 | 3 |
| 权限控制 | 4 | 1 | 0 | 5 |
| Audit 日志 Tab | 1 | 0 | 1 | 2 |
| **合计** | **25** | **17** | **6** | **48** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 36 |
| 需求描述 | 9 |
| QA 扩展 | 3 |

---

## 待确认

- [ ] Member-Edit 权限绑定【Create Button】是否为产品有意（与 Create 同码）；测试点暂按需求原文验收。
- [ ] 各确认弹窗中英文完整文案以 Story/UI 为准；实现若有标点/换行差异需产品确认。
- [ ] UI 样式类测试点需对照 Figma（详情 node `12399-170465`、切换租户 `12513-63575`、Audit `12399-170841`）；Story 内嵌参考图未本地化。

## Out of Scope

- Audit 日志业务规则与字段细节（另 Story）
- GPCA API Keys 从详情卡片迁移到 Tab（后续开发）
- 版本对比弹窗内容规格（引用如 005-01）
- Create/Edit 抽屉视觉像素级验收以外的纯 CSS 细节（以 UI 走查为准，测试点仅列关键项）
