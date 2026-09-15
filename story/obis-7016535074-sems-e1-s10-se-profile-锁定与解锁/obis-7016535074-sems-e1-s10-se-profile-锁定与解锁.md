# Story: [SEMS] E1-S10：SE Profile 锁定与解锁（Lock / Unlock）

**来源**: [飞书项目 User Story #7016535074](https://project.feishu.cn/obis/userstory/detail/7016535074)
**空间**: OBIS (`obis`)
**类型**: User Story
**编号**: 640
**状态**: 待测试
**优先级**: Must
**Sprint**: OBIS-20260810-20260821
**Epic**: [SEMS] E1：SE Profile 管理（SE-F01） (#7016459001)
**Story Point**: QC 1.5
**Labels**: SEMS
**创建**: 2026-06-11
**更新**: 2026-08-07

---

## 需求描述（Description）

> Product Doc 为 SEMS PRD 链接（见文末）；正文取自 Description。UI 设计为 Figma 链接，无飞书 CDN 参考图可本地化。评论附件「S08~S11 生命周期接口测试说明」已落盘至 `./images/`。

### 1. 手动锁定（Active → Locked）

- Active 状态下详情页操作栏显示「Lock」按钮。（AC-01）
- 点击「Lock」弹出二次确认对话框（COPY-01）。（AC-02）
- 确认后 SE Profile 状态切换为 Locked；页面顶部显示成功 Toast（COPY-02）。（AC-03）

### 2. 手动解锁（Locked → Active）

- Locked 状态下，若锁定原因为纯手动锁定（无级联来源），详情页操作栏显示「Unlock」按钮。（AC-04）
- 级联 Locked（上游 GP CA 证书 Locked 或 Vault KMS Key Suspended）时，「Unlock」按钮不可见；须等上游恢复后系统自动解锁，不允许手动解锁。（AC-05）
- 点击「Unlock」弹出二次确认对话框（COPY-03）；确认后状态恢复 Active；页面顶部显示成功 Toast（COPY-04）。（AC-06）

> **上游级联 Locked：** 上游密码学资产（GP CA 证书 Locked / KMS Key Suspended）触发 SE Profile 自动 Locked 的级联消费逻辑、状态恢复条件（上游全部恢复后自动解锁）和事件消费机制由 **E4-S6（上游状态订阅消费）** 统一定义，本 Story 不重复定义。`lock_sources` 在级联场景中的填充规则同样由 E4-S6 覆盖。

### 3. 业务规则（BR）

| 编号 | 规则 |
|------|------|
| BR-01 | `lock_sources` 追踪所有当前激活的锁定来源（手动锁定 + 各上游级联来源）；仅当所有来源全部解除时方可恢复 Active（→ PDR-033 §3） |
| BR-02 | 手动锁定与级联锁定共存时，Unlock 按钮不可见；须上游全部恢复后，系统再检查是否存在手动锁定来源（→ PDR-033 §3） |
| BR-03 | 手动锁定与解锁的状态变更通知由 IF-05（E4-S5）统一推送，本 Story 不定义推送细节 |

### 4. 审计日志

- 手动 Lock、手动 Unlock、上游级联 Locked、上游恢复自动解锁均写入审计日志，记录操作人、时间、SE Profile ID、Name、操作类型（lock / unlock / cascade_lock / cascade_unlock）、lock_sources、from_status → to_status。（AC-09）

### 5. UI 设计

- Figma（锁定 / 解锁二次确认对话框）：[OBIS-Planning 设计稿](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=10977-150162)
- URL for UI Review：[Figma node 21074-257433](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=21074-257433)

### 6. 测试要点（来自 Description）

1. **手动锁定正常流程**：Active SE Profile 点击 Lock → 二次确认 → 状态变为 Locked；顶部 Toast 显示。
2. **手动解锁正常流程**：手动 Locked SE Profile 点击 Unlock → 二次确认 → 状态恢复 Active；顶部 Toast 显示。
3. **级联 Locked - 无 Unlock 按钮**：上游级联 Locked 时详情页不显示 Unlock 按钮（级联锁定恢复由 E4-S6 定义）。
4. **取消二次确认**：Lock / Unlock 弹窗点击取消 → 状态不变。
5. **Draft 不可锁定**：Draft 状态下无 Lock 入口。

### 7. 接口与数据口径（来自评论附件 ref-01）

- 状态映射：Active=2，Locked=3；Lock 仅允许 Active；Unlock 仅当 `lock_sources` **严格只包含一个 `manual` 锁源**时允许。
- Lock 成功后 `lock_sources` 写入 `[{"type":"manual","source_id":null,"locked_at":"..."}]`；Unlock 成功后清空为 `[]`。
- 存在级联锁源时手动 Unlock 被拒绝；人工 Lock / Unlock 不调用 KMS、GPCA 或 ARBAC 变更接口，只做 ARBAC 权限校验。
- 写入审计 / 请求幂等 / 状态 outbox（`se_profile.locked` / `se_profile.unlocked`）；级联入口由 E4-S6 覆盖，前端不调用。
- 接口支持 `businessProfileId` 裸 ID 与 `SEP_<id>`；Redis 10 秒防重复提交；`clientRequestId` 由前端生成，网络重试须复用原 UUID。

![参考附件 — SEMS S08~S11 生命周期接口测试说明](./images/ref-01-sems-s08-s11-参考.md)

### 8. 文案规范（UI Copy）

**标签与按钮：**

| COPY-NN | English | 中文 |
| --- | --- | --- |
| — | Lock | 锁定（操作按钮） |
| — | Unlock | 解锁（操作按钮） |
| — | Confirm | 确认（对话框确认按钮） |
| — | Cancel | 取消 |

**句子型文案：**

| COPY-NN | English | 中文 |
| --- | --- | --- |
| COPY-01 | This SE Profile will be locked. New references are prohibited; existing references remain valid. You can unlock it at any time. Confirm lock? | 锁定后该 SE Profile 禁止建立新引用，已有引用继续有效。可随时解锁恢复。确认锁定？ |
| COPY-02 | SE Profile locked. | SE Profile 已锁定 |
| COPY-03 | Unlocking will restore this SE Profile to Active, allowing new references. Confirm unlock? | 解锁后该 SE Profile 恢复 Active，可再次建立新引用。确认解锁？ |
| COPY-04 | SE Profile unlocked. | SE Profile 已解锁 |

### 9. Product Doc 链接

- [SEMS_PRD](http://192.168.40.171:8080/#/modules/sems/SEMS_PRD?ref=main)

---

## Tech Doc

- N/A

## 评论 / 待确认

- [2026-07-30]：因 TI 芯片烧录流程关联 Story 临时加入，与产品沟通后移出当前 Story 至下个 Sprint（与本 Lock/Unlock 范围无关的排期说明）。
- AC 编号跳过 AC-07 / AC-08，直接到 AC-09，是否缺号或已删改需与产品确认。
- 级联 Locked / 自动解锁的端到端验收边界：本 Story UI 侧验「无 Unlock」；级联消费细节归 E4-S6。
- 评论附件为 S08~S11 共用测试说明，已本地化到 `./images/ref-01-sems-s08-s11-参考.md`。

## Out of Scope

- 上游级联 Locked / 自动解锁的事件消费与 `lock_sources` 级联填充规则（E4-S6）。
- 状态变更通知推送细节（IF-05 / E4-S5）。
- Draft / Revoked / Archived 等其他生命周期操作（Destroy、Archive、Revoke 等由兄弟 Story 覆盖）。
