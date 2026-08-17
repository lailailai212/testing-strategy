# Story: 【体验优化P2】细节补充

**来源**: [飞书项目 User Story #7051514356](https://project.feishu.cn/obis/userstory/detail/7051514356)  
**空间**: OBIS (`obis`)  
**编号**: 792 | **优先级**: Must | **Epic**: UI及体验优化  
**Sprint**: OBIS-20260727-20260807  
**模式**: Large（跨 +n hover、Toast、勾选主题色、多列表列宽、KMS/PKI 样式、本人编辑、Product Version、Role 权限 Tab，需独立测试点与抽样覆盖）

> Story 导出：`story/obis-7051514356-体验优化p2-细节补充/obis-7051514356-体验优化p2-细节补充.md`

---

## Story AC

1.（AC-01）用户在 Account 列表 User Role、Account 详情 Role、Group Linked Product Role，以及其它已出现 `+n` 的页面，hover `+n` 时应弹出小窗展示被折叠的全部数据。

2.（AC-02）用户触发无特殊约定的成功操作后，成功 Toast 文案应为中文「操作成功」/ 英文「Operation Successful」，样式为成功态绿色图标 + 浅绿底提示条。

3.（AC-03）用户在 Filter、表单等处勾选 Checkbox 时，勾选态颜色应为主题色（对照 Figma），旁侧标签文案不变。

4.（AC-04）用户打开 Product / KMS / PKI / Factory / U-safe / Device History / DAC Report / Account / Group 等大列表时：第一列（通常 Name）固定 280px、Status 固定 160px、Operation 固定 64px；大屏（宽度足以展示全部列）下中间非固定列按比例均分剩余宽度；小屏（宽度不足以展示全部列）下固定三列保持宽度不被挤占，并出现横向滚动以查看其余列。

5.（AC-05）用户查看 KMS 列表 Usage Count、PKI 列表 Issued Count 时，应为普通文字样式，无额外图标与边框。

6.（AC-06）用户编辑本人账号（列表 Edit 或详情/Profile Edit）时，Edit 可用，编辑表单隐藏 User Role 与 Notes，其余可编辑字段逻辑不变。

7.（AC-07）用户查看 Product 列表 Version 列时，应显示该产品 **Prod 环境**下最新的一个版本（不取 Test），且不随 Module 切换联动变化。

8.（AC-08）系统 Role 可配置 Vulnerability Tab、OTA Tab 权限；无权限用户看不到对应 Tab。会上线该功能的租户：雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 需配置上述权限；不上线的租户（如宜家及其关联租户）所有 Role 均不配置。

---

## 测试点

> **来源**：`AC-0x` = 覆盖 Story AC；`需求描述` = 正文有述未单列；`QA扩展` = 边界/负向。  
> **优先级**：P0 = 明确页面主路径；P1 = 抽样/边界；P2 = 中英文与边缘。

### +n hover

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PLUS-01 | AC-01 | P0 | Account 列表 User Role 出现 `+n` 时，hover 小窗展示被折叠的全部 Role |
| TP-PLUS-02 | AC-01 | P0 | Account 详情页 Role 出现 `+n` 时，hover 小窗展示全部 Role |
| TP-PLUS-03 | AC-01 | P0 | Group 详情 Linked Product — Role 列（如 `Member +2`）hover `+n` 展示其余角色全文 |
| TP-PLUS-04 | AC-01, 需求描述 | P1 | Product 列表 Module 列：首 Tag + `+n`；hover 浮层标题 Module :，Tag 列出全部溢出项，过多可滚动 |
| TP-PLUS-05 | AC-01, QA扩展 | P1 | 仅 1 个值无 `+n` 时不出现 hover 溢出窗；恰好溢出边界时 `+n` 与小窗内容正确 |
| TP-PLUS-06 | QA扩展 | P2 | 中英文环境下 `+n` hover 小窗均可打开且内容完整 |

### 成功 Toast

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-TOAST-01 | AC-02 | P0 | 中文环境任选一成功操作：Toast 文案为「操作成功」，绿勾 + 浅绿底 |
| TP-TOAST-02 | AC-02 | P0 | 英文环境同一类成功操作：Toast 文案为「Operation Successful」（非 Operation success） |
| TP-TOAST-03 | AC-02, QA扩展 | P1 | 至少再抽测 2 个不同模块成功操作，Toast 文案与样式一致 |
| TP-TOAST-04 | QA扩展 | P2 | 需求约定有特殊文案的成功提示不受本 AC 强制覆盖（按各 Story 例外） |

### 勾选框主题色

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-CHK-01 | AC-03 | P0 | Filter 内 Checkbox 勾选态为主题色（对照 Figma node 15959-188662） |
| TP-CHK-02 | AC-03 | P0 | 表单 / 下拉相关 Checkbox 勾选态为主题色，标签文案不变 |
| TP-CHK-03 | AC-03, QA扩展 | P1 | 至少再抽测 1 处非 Filter 勾选（如 Role 权限树），勾选态为主题色 |
| TP-CHK-04 | QA扩展 | P2 | 未勾选态与禁用态不误用勾选主题色（待确认是否含 Radio/Switch） |

### 大列表列宽

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-COL-01 | AC-04 | P0 | Product List：固定三列约 280/160/64；大屏中间列按比例均分剩余宽度 |
| TP-COL-02 | AC-04 | P0 | Account List、Group List：同上固定三列 + 大屏中间列均分剩余宽度 |
| TP-COL-03 | AC-04 | P0 | KMS List、PKI List：同上固定三列 + 大屏中间列均分剩余宽度 |
| TP-COL-04 | AC-04 | P1 | Factory / U-safe / Device History / DAC Report：同上（抽样） |
| TP-COL-05 | AC-04 | P1 | 小屏：固定三列保持宽度不被挤占，出现横向滚动可查看中间列（以 Product List 为主路径验收） |

### KMS / PKI Count 样式

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-CNT-01 | AC-05 | P0 | KMS 列表 Usage Count 为普通文字，无图标与边框 |
| TP-CNT-02 | AC-05 | P0 | PKI 列表 Issued Count（含树展开至有值节点）为普通文字，无图标与边框 |

### 本人编辑

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SELF-01 | AC-06 | P0 | Account 列表操作本人行：Edit 可用；打开抽屉后无 User Role、Notes |
| TP-SELF-02 | AC-06 | P0 | Account（SNB）列表操作本人行：Edit 可用；抽屉隐藏 User Role、Notes |
| TP-SELF-03 | AC-06 | P0 | 本人 Account 详情：Edit icon 可用；弹窗隐藏 User Role、Notes；Email 等其余字段逻辑不变 |
| TP-SELF-04 | AC-06 | P0 | 本人 Profile：Edit icon 可用；弹窗隐藏 User Role、Notes |
| TP-SELF-05 | QA扩展 | P1 | 本人编辑可保存成功后列表/详情展示更新（非 Role/Notes 字段） |
| TP-SELF-06 | QA扩展 | P1 | 非本人行：仅具备 System Admin role 的管理员可 Edit，其余人 Edit 置灰；管理员编辑他人时表单仍可见 User Role、Notes |

### Product Version

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-VER-01 | AC-07 | P0 | Product 列表 Version 列展示 **Prod** 环境下最新一个版本文案（有 Prod Version 时） |
| TP-VER-02 | AC-07 | P0 | 仅存在 Test Version、或 Test 比 Prod 更新时，列表仍只展示 Prod 最新 Version（不取 Test） |
| TP-VER-03 | AC-07 | P0 | 切换/筛选 Module 相关展示时，Version 列不随 Module 联动改变 |
| TP-VER-04 | QA扩展 | P1 | 无 Prod Version 时，Version 列展示 `-` |

### OTA / Vulnerability 权限

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PERM-01 | AC-08 | P0 | Role 权限树出现节点 **Vulnerability Tab Page / 漏洞 Tab 页面**、**OTA Tab Page / OTA Tab 页面**，可勾选配置 |
| TP-PERM-02 | AC-08 | P0 | 用户无 Vulnerability Tab Page 权限时，Product 详情不展示 Vulnerability Tab |
| TP-PERM-03 | AC-08 | P0 | 用户无 OTA Tab Page 权限时，Product 详情不展示 OTA Tab |
| TP-PERM-04 | AC-08 | P0 | 用户同时拥有两权限时，两 Tab 均可见且可进入 |
| TP-PERM-05 | AC-08 | P0 | **会上线**租户：雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 默认/交付后具备上述两权限 |
| TP-PERM-06 | AC-08 | P0 | **不上线**租户（如宜家及其关联租户）：所有 Role 均不配置上述两权限；对应用户看不到两 Tab |
| TP-PERM-07 | QA扩展 | P1 | 权限变更后重新登录/刷新，Tab 显隐与权限一致 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 +n hover | TP-PLUS-01～06 | ✅ |
| AC-02 成功 Toast | TP-TOAST-01～04 | ✅ |
| AC-03 勾选主题色 | TP-CHK-01～04 | ✅ |
| AC-04 列宽 | TP-COL-01～05 | ✅ |
| AC-05 Count 样式 | TP-CNT-01～02 | ✅ |
| AC-06 本人编辑 | TP-SELF-01～06 | ✅ |
| AC-07 Product Version | TP-VER-01～04 | ✅ |
| AC-08 OTA/Vulnerability | TP-PERM-01～07 | ✅ |

**AC-01～AC-08 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| +n hover | 3 | 2 | 1 | 6 |
| Toast | 2 | 1 | 1 | 4 |
| 勾选框 | 2 | 1 | 1 | 4 |
| 列宽 | 3 | 2 | 0 | 5 |
| Count 样式 | 2 | 0 | 0 | 2 |
| 本人编辑 | 4 | 2 | 0 | 6 |
| Version | 3 | 1 | 0 | 4 |
| 权限 Tab | 6 | 1 | 0 | 7 |
| **合计** | **25** | **10** | **3** | **38** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 35 |
| 需求描述 | 1 |
| QA 扩展 | 3 |

---

## 设计自检

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（未命中）

### 多角色可见 / 触达（类型 C）

- [x] 已覆盖有权/无权 × OTA、Vulnerability Tab 显隐（TP-PERM-02～04）
- [x] 已覆盖租户是否上线 × 指定 Role 默认配置 / 不上线租户全不配（TP-PERM-05～06）
- [x] 「他人不收/不可见」类与本 Story 无关，未互相替代

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）

---

## 待确认

- [ ] 勾选框「所有」是否含 Radio、Switch、树半选；主题色 token/hex 是否仅以 Figma 为准
- [ ] 第一列是否一律 Name；Operation 64px 是否仅放 ⋮
- [ ] 本人编辑：抽屉 vs 弹窗字段集是否完全一致
- [ ] 同为 Prod 时「最新」排序口径

## Out of Scope

- （原「窄屏 / 横向滚动不验收」已撤销；按 AC-04 验收小屏横向滚动与大屏比例均分）
