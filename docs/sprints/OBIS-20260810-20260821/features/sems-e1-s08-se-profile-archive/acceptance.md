# Story: [SEMS] E1-S08：SE Profile 归档（Archive）

**来源**: [飞书项目 User Story #7016548583](https://project.feishu.cn/obis/userstory/detail/7016548583)
**空间**: OBIS (`obis`)
**编号**: 638 | **优先级**: Must | **Epic**: [SEMS] E1：SE Profile 管理（SE-F01）
**Sprint**: OBIS-20260810-20260821
**模式**: Large（状态机 Locked/Revoked→Archived、列表/详情双入口、终态不可见、审计与 lock_sources 终态口径；AC ≥ 7）
**变更类型**: Hybrid（主 Logic：状态流转/终态/审计/lock_sources；次 UI/UX：入口可见性、二次确认、Toast/文案）

> Story 导出：`story/obis-7016548583-sems-e1-s08-se-profile-归档/`  
> 接口口径参考：同目录 `images/ref-01-sems-s08-s11-参考.md`

---

## Story AC

1.（AC-01）Locked 和 Revoked 状态下，详情页操作栏或列表页操作列应显示 Archive 入口。

2.（AC-02）用户点击 Archive 后，应弹出二次确认对话框（COPY-01），并提供 Confirm Archive 与 Cancel 两个按钮。

3.（AC-03）用户确认归档后，SE Profile 状态应切换为 Archived，页面顶部显示成功 Toast（COPY-02）；若从详情页触发，归档后应跳回列表页；若从列表页触发，应留在列表页且该行从列表消失。

4.（AC-04）Archived 应为终态，不可从 Archived 回退到任何其他状态。

5.（AC-05）归档后该 SE Profile 对用户不可见：列表、搜索均不展示；详情页直链访问应返回不存在提示（COPY-04）；记录保留于数据库供审计溯源，不对用户界面开放。

6.（AC-06）归档接口调用失败时，页面顶部应显示错误 Toast（COPY-03），且 SE Profile 状态不发生变更。

7.（AC-07）归档操作完成后应写入审计日志，记录操作人、时间、SE Profile ID、Name、操作类型（archive）、from_status → to_status，以及转换前的 `lock_sources`（Locked → Archived 时记录转换前集合）。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号；否则填 `需求描述` 或 `QA扩展`。

### SE Profile 详情页 — Archive 入口与确认

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-DTL-01 | AC-01 | P0 | Locked 状态详情页操作栏显示 Archive 入口 |
| TP-ARCH-DTL-02 | AC-01 | P0 | Revoked 状态详情页操作栏显示 Archive 入口 |
| TP-ARCH-DTL-03 | AC-02 | P0 | 点击 Archive 弹出二次确认对话框，文案符合 COPY-01（中/英对照需求表），含 Confirm Archive 与 Cancel |
| TP-ARCH-DTL-04 | AC-03 | P0 | 详情页确认归档：状态变为 Archived；顶部 Toast 为 COPY-02；跳回列表页 |
| TP-ARCH-DTL-05 | AC-02, QA扩展 | P1 | 二次确认点 Cancel：对话框关闭，状态保持 Locked/Revoked 不变 |

### SE Profile 列表页 — Archive

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-LST-01 | AC-01 | P0 | Locked 行操作列显示 Archive 入口 |
| TP-ARCH-LST-02 | AC-01 | P0 | Revoked 行操作列显示 Archive 入口 |
| TP-ARCH-LST-03 | AC-02 | P0 | 列表页点击 Archive：弹出二次确认对话框，文案符合 COPY-01，含 Confirm Archive 与 Cancel（Locked / Revoked 各至少验 1 次） |
| TP-ARCH-LST-04 | AC-03 | P0 | 列表页对 Locked 确认归档：① 状态变为 Archived；② 顶部 Toast 为 COPY-02；③ **留在列表页**（不跳详情）；④ 该行从当前列表消失 |
| TP-ARCH-LST-05 | AC-03 | P0 | 列表页对 Revoked 确认归档：同上四项（Toast COPY-02、留在列表、行消失、状态 Archived） |
| TP-ARCH-LST-06 | AC-02, QA扩展 | P1 | 列表页二次确认点 Cancel：对话框关闭；行仍在列表；状态保持 Locked/Revoked |

### 前置状态限制

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-PRE-01 | 需求描述 | P0 | Active 状态详情页与列表操作列均不显示 Archive 入口 |
| TP-ARCH-PRE-02 | QA扩展 | P1 | Draft 状态不显示 Archive 入口（须对照现网/设计稿） |

### 终态与不可见

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-TERM-01 | AC-04 | P0 | Archived 后界面无任何可切换至其他状态的操作按钮 |
| TP-ARCH-TERM-02 | AC-04, QA扩展 | P1 | 对 Archived 调用状态变更 API 应失败/拒绝，状态保持 Archived |
| TP-ARCH-INV-01 | AC-05 | P0 | 归档后列表不展示该 SE Profile |
| TP-ARCH-INV-02 | AC-05 | P0 | 归档后搜索不命中该 SE Profile |
| TP-ARCH-INV-03 | AC-05 | P0 | 详情页直链访问返回 COPY-04（不存在或无访问权限） |
| TP-ARCH-INV-04 | AC-05, BR-01 | P1 | **不可被新引用**：前置造一 Active/Locked SE Profile 并归档 → 进入 Product → Create Version（或 Version 编辑中的 SE Profile 选择/引用入口）→ 搜索该 Profile Name/ID → **不可选中/不出现在可选列表**。**历史引用不受影响**：前置另造一 Version 已引用该 Profile → 归档后打开该 Version 详情/只读引用区 → 原引用关系仍可见且可追溯 |

### 失败与反馈

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-ERR-01 | AC-06 | P0 | 归档接口返回 **5xx**：顶部 Toast 为 COPY-03；SE Profile 状态保持原 Locked/Revoked；列表/详情仍可见且可再次发起 Archive |
| TP-ARCH-ERR-02 | AC-06, QA扩展 | P1 | 归档请求 **网络超时 / 断网**：Toast 为 COPY-03（或与现网统一网络错误文案，若非 COPY-03 则记入待确认）；状态不变 |
| TP-ARCH-ERR-03 | AC-06, QA扩展 | P1 | 归档接口返回 **403**（无权限）：顶部展示错误反馈（COPY-03 或权限类错误文案）；状态不变；有权限账号仍可归档 |
| TP-ARCH-COPY-01 | AC-02, AC-03 | P1 | 中英文界面下 COPY-01 / COPY-02 / COPY-03 / COPY-04 与需求文案表一致 |

### 审计与 lock_sources

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-AUD-01 | AC-07 | P0 | 归档成功写入审计：操作人、时间、SE Profile ID、Name、action=archive、from_status→to_status（优先经产品审计 UI / 可导出审计；无 UI 时用联调接口） |
| TP-ARCH-AUD-02 | AC-07, BR-02 | P0 | Locked→Archived：审计记录含转换前 `lock_sources` 集合；归档后当前 `lock_sources` 清空为 `[]`（清空可用详情/接口回读；审计集合同 AUD-01 验证通道） |
| TP-ARCH-AUD-03 | BR-02, 需求描述 | P1 | Revoked→Archived：当前 `lock_sources` 清空；审计含 from/to 状态（按产品终态口径） |
| TP-ARCH-AUD-04 | 需求描述 | P2 | （实现层细节，非 AC）生命周期审计 `trigger_reason=manual_archived` 与状态 outbox `se_profile.archived`：**验证方式**需 DB / 内部表或联调日志；无访问权限时本条跳过，不阻断 AC-07 验收 |

### 接口边界（QA 扩展）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ARCH-API-01 | QA扩展 | P1 | `businessProfileId` 支持裸 ID 与 `SEP_<id>` 两种格式归档成功 |
| TP-ARCH-API-02 | QA扩展 | P2 | **同用户** 10 秒内重复提交同一归档请求被防重；`clientRequestId` 网络重试复用原 UUID |
| TP-ARCH-API-03 | QA扩展 | P1 | **并发归档**：两名有权限用户几乎同时对同一 Locked/Revoked SE Profile 确认 Archive → 最终仅成功一次（状态为 Archived）；另一侧失败（错误 Toast / 业务冲突），且不出现双成功或脏状态；列表侧仅一份归档结果 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Archive 入口（Locked/Revoked） | TP-ARCH-DTL-01；TP-ARCH-DTL-02；TP-ARCH-LST-01；TP-ARCH-LST-02 | ✅ |
| AC-02 二次确认对话框 | TP-ARCH-DTL-03；TP-ARCH-LST-03 | ✅ |
| AC-03 确认后状态/Toast/跳转 | TP-ARCH-DTL-04；TP-ARCH-LST-04；TP-ARCH-LST-05 | ✅ |
| AC-04 终态不可回退 | TP-ARCH-TERM-01 | ✅ |
| AC-05 用户不可见 | TP-ARCH-INV-01；TP-ARCH-INV-02；TP-ARCH-INV-03 | ✅ |
| AC-06 失败 Toast 且状态不变 | TP-ARCH-ERR-01；TP-ARCH-ERR-02；TP-ARCH-ERR-03 | ✅ |
| AC-07 审计 + lock_sources | TP-ARCH-AUD-01；TP-ARCH-AUD-02 | ✅ |

**AC-01～AC-07 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| 详情页 Archive | 4 | 1 | 0 | 5 |
| 列表页 Archive | 5 | 1 | 0 | 6 |
| 前置状态限制 | 1 | 1 | 0 | 2 |
| 终态与不可见 | 4 | 2 | 0 | 6 |
| 失败与文案 | 1 | 3 | 0 | 4 |
| 审计与 lock_sources | 2 | 1 | 1 | 4 |
| 接口边界 | 0 | 2 | 1 | 3 |
| **合计** | **17** | **11** | **2** | **30** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 22 |
| 需求描述 | 3 |
| QA 扩展 | 8 |

---

## 设计自检

### 变更类型

- [x] 已声明 Hybrid（主 Logic，次 UI/UX）
- [x] P0 侧重状态流转、不可见、审计与失败不落库态
- [x] UI 侧重入口/对话框/Toast 已覆盖，未以纯样式为 P0
- [x] A–D：未命中里程碑/邮件/配额；多角色可见未声明差异 → C 标 N/A

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（未命中；状态推送细节不在本 Story）

### 多角色可见 / 触达（类型 C）

- [x] N/A（正文未声明角色分支；ARBAC 为通用前置）

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）

---

## 待确认

- [ ] Draft 是否完全无 Archive 入口（含列表批量操作）需对照现网与设计稿
- [ ] 飞书 Description 是否已回写 lock_sources 终态口径（导出 MD 已按评论合并）
- [ ] 网络超时 / 403 时错误文案是否统一为 COPY-03，或沿用全局网络/权限错误文案
- [ ] 并发归档失败侧的具体提示文案与 HTTP/业务码（乐观锁冲突 / 已归档）
- [ ] Product Version 中 SE Profile 引用入口的准确页面路径（Create Version 选择器 vs 其他）以落实 TP-ARCH-INV-04

## Out of Scope

- Active → Archived 直达
- Archived 回退或其他状态恢复
- 用户界面重新开放 Archived 记录
- Lock / Unlock / Revoke / Destroy（兄弟 Story）
- 级联归档或上游驱动归档
