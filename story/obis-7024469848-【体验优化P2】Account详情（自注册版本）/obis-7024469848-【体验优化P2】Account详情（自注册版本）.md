# Story: 【体验优化P2】Account详情（自注册版本）

**来源**: [飞书项目 User Story #7024469848](https://project.feishu.cn/obis/userstory/detail/7024469848)
**空间**: OBIS (`obis`)
**类型**: User Story
**编号**: 735
**状态**: 开发中
**优先级**: Must
**Sprint**: OBIS-20260706-20260717
**Epic**: UI及体验优化 (#7018945691)
**Online Version**: V3.3.0
**Story Point (QC)**: 1
**创建**: 2026-06-22
**更新**: 2026-07-13

---

## 需求描述（Product Doc）

> Product Doc 字段为「/」；以下内容整理自 Description 字段。  
> 参考图下载失败（飞书附件下载接口未启用），未本地化到 `images/`；文中保留 Figma 链接。

### 1. 邀请用户（Create Account）

**入口**

- 点击 Account 列表页右上角 Create 按钮，弹出创建用户抽屉

**抽屉样式**

- 占据整个页面宽度，参考 UI 校准
- 页面内文字颜色/大小、输入框尺寸等样式有调整，参考 UI 校准

**抽屉内容**

- 标题：`Create Account` / `创建用户`
- 表单：
  - **Email / 邮箱**：必填（右上角 `*`）；Placeholder：`Please Enter` / `请输入`
  - **Name / 姓名**：必填（`*`）；Placeholder：`Please Enter` / `请输入`
  - **User Role / 用户角色**：必填（`*`）；Placeholder：`Please Select` / `请选择`
  - **Phone / 联系电话**：非必填；Placeholder：`Please Enter` / `请输入`
  - **Notes / 备注**：非必填；Placeholder：`Please Enter` / `请输入`

**操作**

- **关闭**（右上角关闭 icon）：关闭抽屉，不保存当前编辑内容；点击抽屉外黑色蒙层**不可**关闭抽屉
- **Create / 创建**（右下角主按钮）：
  - 校验通过后执行创建
  - 关闭弹窗，Toast：`操作成功。已发送邀请邮件给对方，点击邮件内链接即可激活账号。` / `Operation successful. An invitation email has been sent to the invitee. Click the link in the email to activate the account.`
  - 自动切换到 Invitation Tab，页面刷新，新数据在第一行，状态为 Pending
- **Cancel / 取消**（右下角副按钮）：关闭抽屉，不保存

<!-- 参考图 1 — 邀请用户抽屉：下载失败 -->

### 2. Member / Invitation — 编辑（Edit Account）

**入口（3 个，打开同一编辑抽屉，样式与功能完全一致）**

1. Member 列表 Operation 列 **Edit**
2. 用户详情页第一个卡片右上角编辑 icon
3. Invitation 列表 Operation 列 **Edit**

**抽屉样式**

- 全页宽；文字/输入框样式参考 UI 校准

**抽屉内容**

- 标题：`Edit Account` / `编辑用户`
- 表单：
  - **Email**：自动带入，**不可修改**
  - **Name / User Role / Phone / Notes**：自动带入，**可修改**

**操作**

- 关闭 / Cancel：关闭且不保存；蒙层不可关闭
- **Save / 保存**：校验通过后保存；Toast 操作成功；再次 Edit / 进入详情可见更新

<!-- 参考图 2 — 编辑用户抽屉：下载失败 -->

### 3. Member — 锁定确认弹窗

- **标题**：`Confirm Action` / `确认操作`
- **内容**：`Locking the user will disable the account and prevent system operations. Click Confirm to proceed.` / `锁定用户后，账号将被禁用，无法执行任何系统操作，点击确认继续`
- **按钮**：Confirm 执行；Cancel / 关闭 icon 不执行；蒙层不可关闭

<!-- 参考图 3 — 锁定确认：下载失败 -->

### 4. Member — 删除确认弹窗

- **标题**：`Confirm Action` / `确认操作`
- **内容**：`Deleting the user cannot be restored. Click Confirm to proceed.` / `删除用户后将无法恢复，点击确认继续。`
- **备注**：国际化 code 目前与删除租户共用，**需要拆开**
- **按钮**：Confirm 执行；Cancel / 关闭 icon 不执行；蒙层不可关闭

<!-- 参考图 4 — 删除确认：下载失败 -->

### 5. Invitation — 重新邀请确认弹窗

- **标题**：`Confirm Action` / `确认操作`
- **内容**：`This operation will generate a brand-new activation link and send an email to the invitee. Click Confirm to proceed.` / `本次操作将生成全新激活链接并发送邮件给受邀人，点击确认继续`
- **按钮**：Confirm 执行；Cancel / 关闭 icon 不执行；蒙层不可关闭

<!-- 参考图 5 — 重新邀请确认：下载失败 -->

### 6. Invitation — 删除确认弹窗

- **标题**：`Confirm Action` / `确认操作`
- **内容**：`Delete this invitation? The link will be invalidated immediately and cannot be restored.` / `确认删除？该邀请链接将立即失效，无法恢复。`
- **按钮**：Confirm 执行；Cancel / 关闭 icon 不执行；蒙层不可关闭

<!-- 参考图 6 — Invitation 删除确认：下载失败 -->

### 7. Application — 通过确认弹窗

- **标题**：`Confirm Action` / `确认操作`
- **内容**：`Approved users will become members of your organization. Click Confirm to proceed.` / `审核通过的用户将成为本组织的成员，点击确认继续`
- **按钮**：Confirm 执行；Cancel / 关闭 icon 不执行；蒙层不可关闭

<!-- 参考图 7 — Application 通过确认：下载失败 -->

### 8. Application — 拒绝确认弹窗

- **标题**：`Confirm Action` / `确认操作`
- **内容**：`Confirm rejection? This action cannot be undone and the request will be voided. Click Confirm to proceed.` / `确认拒绝？此操作不可撤回，该申请将作废，点击确认继续`
- **按钮**：Confirm 执行；Cancel / 关闭 icon 不执行；蒙层不可关闭

<!-- 参考图 8 — Application 拒绝确认：下载失败 -->

### 9. 用户详情 — 基本信息

**Figma**：[OBIS Planning 设计稿（node 12399-170465）](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=12399-170465)

**左侧卡片 — 基本信息**

- **返回按钮**：返回 Account List；保持进入详情前的页码、筛选项、排序、列显示不变
- **头像**：无变化
- **头像状态小点**：尺寸按 UI；Active=绿色，Locked=黄色
- **Name / Email / User Role**：Role 标签样式与列表一致
- **Basic Information**
  - **Tenant / 组织**：图标等样式见 UI；右侧显示**套餐名称标签**
    - 免费版可点击 → 打开版本对比弹窗
    - 企业版仅展示、不可点击
  - **Phone / 联系电话**：图标等样式见 UI
- **Access Keys**：在 GPCA API Keys 功能实现前仍放在卡片内；现有功能与样式不变；后续 API Keys 开发时再移到下方 Tab
- **右上角编辑按钮**：打开与列表一致的编辑抽屉

**右侧卡片 — 其他信息**

- **Created Time / 创建时间**：年月日时分秒
- **Created By / 创建人**：头像 + Name + 邮箱 icon；鼠标浮入展示邮箱 + 复制 icon
- **Register Channel / 注册渠道**：`Self Register` 自注册 / `Apply to Join` 申请加入 / `Invited Join` 邀请加入
- **Notes / 备注**：
  - 单起一行，不与其他字段并行
  - 最长展示三行，超出省略号 + 展开箭头
  - 点击展开 → 抽屉展示完整内容；关闭 icon 关闭抽屉

<!-- 参考图 9 — 用户详情：下载失败 -->

### 10. 切换租户（头像下拉）

**Figma**：[OBIS Planning 设计稿（node 12513-63575）](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=12513-63575)

**入口**：系统右上角头像 → 弹出弹窗

**弹窗内容**

- **顶部**：头像 + 邮箱；显示不全用省略号
- **切换租户 list**
  - 标题：`Switch Account` / `切换账户`
  - 正常账户：租户头像 + 租户 Name + 套餐名称
  - 已锁定：置灰，状态 `Locked` / `已锁定`
  - 待激活：置灰，状态 `Pending` / `待激活`
  - 当前账户打 ✅
  - 租户头像：系统按租户首字母/首汉字生成
- **Profile / 个人信息**：跳转 Profile 页
- **Upgrade Plan / 升级套餐**：仅免费版展示，点击打开版本对比弹窗；企业版不展示
- **Sign Out / 退出登录**：退出并跳转登录页

<!-- 参考图 10 — 切换租户：下载失败 -->

### 11. Profile

- **左上角返回按钮**：返回上一页面
- **进入 Profile 时左侧菜单**：保持进入前选中菜单不变
- **页面其他功能与 Account 详情页一致**

<!-- 参考图 11 — Profile：下载失败 -->

### 12. 权限控制

**Account 管理权限**

1. **Create / 创建**
   - Role 配置了【Create Button】→ 可见 Create 按钮
   - 未配置 → 不可见

2. **Member Operation**
   - Operation 三点始终可点；无权限时点开看到**置灰**按钮
   - **Edit**：需【Create Button】权限，否则置灰
   - **Lock**：需【Lock / Unlock Operation】，否则置灰
   - **Delete**：需【Delete Operation】，否则置灰

3. **Invitation Operation**
   - 三点始终可点；无权限时置灰
   - **Edit**：需【Edit Operation】
   - **Delete**：需【Delete Operation】
   - **Re invite**：需【Re-invite Operation】

4. **Application Operation**
   - 三点始终可点；无权限时置灰
   - **Approve / Reject**：均需【Review Operation】

<!-- 参考图 12 — 权限：下载失败 -->

### 13. Audit（日志）

**Figma**：[OBIS Planning 设计稿（node 12399-170841）](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=12399-170841)

- Tab 名称：`Audit` / `日志`
- 日志相关能力另有单独 Story 澄清；本 Story 仅要求将日志 list **按 UI 样式更新**

<!-- 参考图 13 — Audit：下载失败 -->

---

## Tech Doc

- 无

## 评论 / 待确认

- 无评论
- [ ] Description 末尾残留字符 `S`，疑似笔误，不影响正文解读
- [ ] Member-Edit 权限绑定的是【Create Button】（与 Create 同权限码），是否为产品有意设计需确认
- [ ] 参考图共 13 张因飞书附件下载未启用未能本地化；实现/验收请对照 Figma 与飞书 Description 内嵌图

## Out of Scope

- Audit 日志业务规则与字段细节（另 Story）
- GPCA API Keys 从详情卡片迁移到 Tab（后续开发）
- 版本对比弹窗本身的内容规格（引用其他 Story，如 005-01）
