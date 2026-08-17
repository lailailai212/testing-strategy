# Story: [SEMS] E1-S10：SE Profile 锁定与解锁（Lock / Unlock）

**来源**: [飞书项目 User Story #7016535074](https://project.feishu.cn/obis/userstory/detail/7016535074)
**空间**: OBIS (`obis`)
**编号**: 640 | **优先级**: Must | **Epic**: [SEMS] E1：SE Profile 管理（SE-F01）
**Sprint**: OBIS-20260810-20260821
**模式**: Large（手动 Lock/Unlock + 级联场景按钮不可见 + 审计；飞书 AC 含 AC-01～06 与 AC-09，状态机规则多）
**变更类型**: Hybrid（主 Logic：lock_sources / 状态流转 / 级联不可手动解锁；次 UI/UX：按钮可见性、二次确认、Toast）

> Story 导出：`story/obis-7016535074-sems-e1-s10-se-profile-锁定与解锁/`  
> 接口口径参考：同目录 `images/ref-01-sems-s08-s11-参考.md`  
> 级联 Locked / 自动解锁事件消费归 **E4-S6**，本 Story 仅验 UI「无 Unlock」与审计字段可观察结果。

---

## Story AC

1.（AC-01）Active 状态下，详情页操作栏应显示「Lock」按钮；非 Active（含 Locked / Draft / Revoked 等）不显示「Lock」，不可重复锁定。

2.（AC-02）用户点击「Lock」后，应弹出二次确认对话框（COPY-01）。

3.（AC-03）用户确认锁定后，SE Profile 状态应切换为 Locked，页面顶部显示成功 Toast（COPY-02），并**留在详情页**（不跳转列表或其他页）。

4.（AC-04）Locked 且锁定原因为纯手动锁定（无级联来源）时，详情页操作栏应显示「Unlock」按钮。

5.（AC-05）级联 Locked（上游 GP CA 证书 Locked 或 Vault KMS Key Suspended）时，「Unlock」按钮不可见；不允许手动解锁。

6.（AC-06）用户点击「Unlock」后弹出二次确认对话框（COPY-03）；确认后状态恢复 Active，页面顶部显示成功 Toast（COPY-04），并**留在详情页**。

7.（AC-09）手动 Lock、手动 Unlock、上游级联 Locked、上游恢复自动解锁均应写入审计日志，记录操作人、时间、SE Profile ID、Name、操作类型（lock / unlock / cascade_lock / cascade_unlock）、lock_sources、from_status → to_status。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号；否则填 `需求描述` 或 `QA扩展`。  
> **入口范围**：飞书 AC 仅定义**详情页操作栏**；列表页无 Lock/Unlock 操作列（见 Out of Scope）。

### 详情页 — 手动锁定（Active → Locked）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-LOCK-01 | AC-01 | P0 | Active 详情页操作栏显示 Lock 按钮 |
| TP-LOCK-02 | AC-02 | P0 | 点击 Lock 弹出二次确认，文案符合 COPY-01，含 Confirm / Cancel |
| TP-LOCK-03 | AC-03 | P0 | 确认锁定：① 状态变为 Locked；② 顶部 Toast 为 COPY-02；③ **留在详情页**（URL/页签不跳转列表） |
| TP-LOCK-04 | AC-02, QA扩展 | P1 | Lock 对话框点 Cancel：状态保持 Active；仍留在详情页 |
| TP-LOCK-05 | AC-03, 需求描述 | P0 | 手动锁定成功后 `lock_sources` 含且仅含一个 `manual` 来源（可对照接口/审计） |
| TP-LOCK-06 | AC-01, 需求描述 | P0 | Draft 状态详情页无 Lock 入口 |
| TP-LOCK-07 | AC-01 | P0 | Locked 状态详情页 **不显示 Lock**（不可重复锁定；可显示 Unlock，见 TP-UNL-01） |
| TP-LOCK-08 | AC-01, QA扩展 | P0 | Revoked 状态详情页 **不显示 Lock、不显示 Unlock**（Revoked 走 Archive，见 S08；本 Story 仅验无 Lock/Unlock 入口） |

### 详情页 — 手动解锁（Locked → Active）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-UNL-01 | AC-04 | P0 | 纯手动 Locked（无级联来源）详情页显示 Unlock，且不显示 Lock |
| TP-UNL-02 | AC-06 | P0 | 点击 Unlock 弹出 COPY-03 确认框；确认后：① 状态恢复 Active；② Toast 为 COPY-04；③ **留在详情页** |
| TP-UNL-03 | AC-06, QA扩展 | P1 | Unlock 对话框点 Cancel：状态保持 Locked；仍留在详情页 |
| TP-UNL-04 | AC-06, 需求描述 | P0 | 手动解锁成功后 `lock_sources` 清空为 `[]` |
| TP-UNL-05 | AC-01, AC-06 | P1 | Unlock 成功回到 Active 后，操作栏重新显示 Lock、不显示 Unlock |

### 级联 Locked — Unlock 不可见

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-CAS-01 | AC-05 | P0 | 上游级联 Locked（GP CA Locked 或 KMS Key Suspended 任一）时，详情页不显示 Unlock，也不显示 Lock |
| TP-CAS-02 | AC-05, BR-02 | P0 | 手动锁定与级联锁定共存时，Unlock 不可见 |
| TP-CAS-03 | AC-05, QA扩展 | P1 | 级联 Locked 场景下直接调用手动 Unlock 接口应被拒绝，状态不变（前端无入口的后端兜底） |
| TP-CAS-04 | BR-01, 需求描述 | P1 | 仅当所有 lock_sources 解除后才可恢复 Active（本 Story 验「有级联则不可手动」；自动解锁细节归 E4-S6） |

### 失败与反馈

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ERR-01 | QA扩展 | P0 | Lock 接口返回 **5xx**：顶部显示错误 Toast（或与现网统一失败文案）；状态保持 Active；仍留在详情页且可再次发起 Lock |
| TP-ERR-02 | QA扩展 | P0 | Unlock 接口返回 **5xx**：顶部显示错误 Toast；状态保持 Locked；仍留在详情页且可再次发起 Unlock |
| TP-ERR-03 | QA扩展 | P1 | Lock/Unlock **网络超时 / 断网**：状态不变；有错误反馈；可重试 |
| TP-ERR-04 | QA扩展 | P1 | Lock/Unlock 返回 **403**：状态不变；有错误反馈；有权限账号仍可操作 |

### 审计日志

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUD-01 | AC-09 | P0 | 手动 Lock 写入审计：action=lock，含操作人、时间、Profile ID/Name、**lock_sources**、from→to |
| TP-AUD-02 | AC-09 | P0 | 手动 Unlock 写入审计：action=unlock，含操作人、时间、Profile ID/Name、**lock_sources**（解锁后集合或转换前集合按实现可观察口径）、from→to |
| TP-AUD-03 | AC-09 | P0 | 上游级联 Locked 写入审计：action=cascade_lock，且记录含 **lock_sources**（含级联来源）、from→to（需级联联调环境） |
| TP-AUD-04 | AC-09 | P0 | 上游恢复自动解锁写入审计：action=cascade_unlock，且记录含 **lock_sources**、from→to（联调/E4-S6 环境） |

### 文案与一致性

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-COPY-01 | AC-02, AC-03, AC-06 | P1 | 中英文 COPY-01～COPY-04 与需求文案表一致 |
| TP-COPY-02 | QA扩展 | P2 | Locked 后禁止建立新引用的业务结果可在引用入口观察到阻断（COPY-01 语义抽测） |

### 接口边界（QA 扩展）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-API-01 | QA扩展 | P1 | Lock/Unlock 支持裸 ID 与 `SEP_<id>` |
| TP-API-02 | QA扩展 | P2 | 同用户 10 秒防重复提交；`clientRequestId` 重试复用 |
| TP-API-03 | QA扩展 | P1 | 对 Locked 调用 Lock、对 Revoked 调用 Lock/Unlock：接口拒绝且状态不变（与 UI 无入口兜底一致） |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Lock 按钮可见（仅 Active） | TP-LOCK-01；TP-LOCK-06；TP-LOCK-07；TP-LOCK-08 | ✅ |
| AC-02 Lock 二次确认 | TP-LOCK-02 | ✅ |
| AC-03 锁定成功 + Toast + 留详情 | TP-LOCK-03；TP-LOCK-05 | ✅ |
| AC-04 纯手动 Unlock 可见 | TP-UNL-01 | ✅ |
| AC-05 级联无 Unlock | TP-CAS-01；TP-CAS-02 | ✅ |
| AC-06 Unlock 确认 + Active + Toast + 留详情 | TP-UNL-02；TP-UNL-04 | ✅ |
| AC-09 审计（四类操作均含 lock_sources） | TP-AUD-01～04 | ✅ |

**AC-01～AC-06、AC-09 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| 手动锁定 | 6 | 1 | 0 | 7 |
| 手动解锁 | 3 | 2 | 0 | 5 |
| 级联 Locked | 2 | 2 | 0 | 4 |
| 失败与反馈 | 2 | 2 | 0 | 4 |
| 审计 | 4 | 0 | 0 | 4 |
| 文案与一致性 | 0 | 1 | 1 | 2 |
| 接口边界 | 0 | 2 | 1 | 3 |
| **合计** | **17** | **10** | **2** | **29** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 18 |
| 需求描述 | 3 |
| QA 扩展 | 11 |

---

## 设计自检

### 变更类型

- [x] 已声明 Hybrid（主 Logic，次 UI/UX）
- [x] P0 侧重状态流转、lock_sources、级联不可解锁、审计
- [x] 未把 E4-S6 级联消费细节写成可独立完成的 P0（联调项已标注）
- [x] A–D：未命中里程碑/邮件/配额；角色矩阵未声明 → C 标 N/A

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（IF-05/E4-S5 推送细节 Out of Scope）

### 多角色可见 / 触达（类型 C）

- [x] N/A（正文未声明角色分支）

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）

---

## 待确认

- [ ] 飞书 AC 编号跳过 AC-07 / AC-08，是否缺号或已删改
- [ ] cascade_lock / cascade_unlock 审计在本 Sprint 是否具备联调数据；若无则与 E4-S6 联调排期对齐
- [ ] Lock/Unlock 失败 Toast 是否有专用 COPY，或沿用全局网络/服务错误文案（正文未定义 COPY-ERR）
- [ ] Unlock 审计中 `lock_sources` 记转换前集合还是清空后集合（实现口径）

## Out of Scope

- **列表页 Lock / Unlock 操作列**（飞书 AC 仅定义详情页操作栏；本期不验收列表入口）
- 上游级联 Locked / 自动解锁的事件消费与 lock_sources 级联填充规则（E4-S6）
- 状态变更通知推送细节（IF-05 / E4-S5）
- Archive / Revoke / Destroy 等其他生命周期操作（含 Revoked 的 Archive 入口，归 S08）
