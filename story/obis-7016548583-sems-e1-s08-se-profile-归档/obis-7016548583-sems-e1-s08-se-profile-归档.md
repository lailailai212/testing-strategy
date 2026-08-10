# Story: [SEMS] E1-S08：SE Profile 归档（Archive）

**来源**: [飞书项目 User Story #7016548583](https://project.feishu.cn/obis/userstory/detail/7016548583)
**空间**: OBIS (`obis`)
**类型**: User Story
**编号**: 638
**状态**: 待测试
**优先级**: Must
**Sprint**: OBIS-20260810-20260821
**Epic**: [SEMS] E1：SE Profile 管理（SE-F01） (#7016459001)
**Story Point**: QC 1
**Labels**: SEMS
**创建**: 2026-06-11
**更新**: 2026-08-07

---

## 需求描述（Description）

> Product Doc 为 SEMS PRD 链接（见文末）；正文取自 Description，并合并评论中的产品口径更新（lock_sources 终态处理）。UI 设计为 Figma 链接；评论附件「S08~S11 生命周期接口测试说明」已落盘至 `./images/`。

### 1. 归档操作（Locked / Revoked → Archived）

- Locked 和 Revoked 状态下，详情页操作栏或列表页操作列显示 Archive 入口。（AC-01）
- 点击 Archive 弹出二次确认对话框（COPY-01），对话框提供 Confirm Archive 和 Cancel 两个按钮。（AC-02）
- 用户确认后：（AC-03）
  - SE Profile 状态切换为 Archived
  - 页面顶部显示成功 Toast（COPY-02）
  - 若从详情页触发，归档后跳回列表页
- Archived 状态为终态，不可从 Archived 回退到任何其他状态。（AC-04）
- Archived 后该 SE Profile 对用户不可见：列表、搜索均不展示，详情页直链访问返回不存在提示（COPY-04）；记录保留于数据库供审计溯源，不对用户界面开放。（AC-05）
- 归档接口调用失败时，页面顶部显示错误 Toast（COPY-03），SE Profile 状态不发生变更。（AC-06）

### 2. 审计日志

- 归档操作完成后写入审计日志，记录操作人、时间、SE Profile ID、Name、操作类型（archive）、from_status → to_status，以及转换前的 `lock_sources`（Locked → Archived 时记录转换前集合）。（AC-07，含 2026-07-28 产品口径补充）

### 3. 业务规则（BR）

| 编号 | 规则 |
|------|------|
| BR-01 | 内容保留：Archived SE Profile 的所有配置内容保留，仅不参与新业务（不可被新 Product Version 引用）；历史引用关系不受影响（→ SEMS PRD §3.2） |
| BR-02 | Locked → Archived 时，转换前 `lock_sources` 集合写入审计日志；归档后当前 `lock_sources` 清空（→ PDR-033 §3.5）。进入终态（Revoked / Archived）后当前 `lock_sources` 清空——状态切换后锁源信息失去意义；转换前集合保留于审计日志。（2026-07-28 产品口径） |

### 4. UI 设计

- Figma（归档二次确认对话框）：[OBIS-Planning 设计稿](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=10977-150107)
- URL for UI Review：[Figma node 21074-257115](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=21074-257115)
- 评论补充设计稿：[Figma node 21074-257577](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=21074-257577)

### 5. 测试要点（来自 Description）

1. **正常流程（Locked → Archived）**：Locked SE Profile 点击 Archive → 二次确认 → 状态变为 Archived。
2. **正常流程（Revoked → Archived）**：Revoked SE Profile 点击 Archive → 二次确认 → 状态变为 Archived。
3. **Archived 用户不可见**：归档后从列表和搜索中消失；详情页直链访问返回不存在提示。
4. **Archived 记录保留**：归档后数据库仍保留该记录（供后台审计），用户界面无法访问。
5. **归档不可逆**：Archived 状态下无任何可切换状态的按钮；无法通过 API 变更状态。
6. **前置状态限制**：Active 状态下不显示 Archive 按钮（须先 Lock 或 Revoke）。
7. **取消二次确认**：点击 Cancel → 状态不变。
8. **列表页归档**：Locked / Revoked SE Profile 在列表操作列点击 Archive → 行为与详情页一致，归档后该行从列表消失。
9. **归档失败**：归档接口异常 → 页面顶部显示错误 Toast，状态保持不变。
10. **lock_sources 终态**：Locked → Archived 后当前 `lock_sources` 清空；审计日志保留转换前集合。

### 6. 接口与数据口径（来自评论附件 ref-01）

- 仅允许 Locked(3) 或 Revoked(4) 归档；成功后 `status=5`，`lock_sources='[]'`。
- 写入生命周期审计（`action=archive`，`trigger_reason=manual_archived`）、请求幂等记录、状态 outbox（`se_profile.archived`）。
- 不写 `sems_profile_source_event`，不调用 KMS 或 GPCA。
- 接口支持裸 ID 与 `SEP_<id>`；Redis 10 秒防重复提交；`clientRequestId` 由前端生成。

![参考附件 — SEMS S08~S11 生命周期接口测试说明](./images/ref-01-sems-s08-s11-参考.md)

### 7. 文案 / UI Copy

**标签与按钮：**

| COPY-NN | English | 中文 |
| --- | --- | --- |
| — | Archive | 归档（操作按钮） |
| — | Confirm Archive | 确认归档（对话框标题 / 确认按钮） |
| — | Cancel | 取消 |
| — | Clone | 克隆 |
| — | Draft | 草稿（状态 Badge） |
| — | Active | 活跃（状态 Badge） |
| — | Locked | 已锁定（状态 Badge） |
| — | Revoked | 已吊销（状态 Badge） |
| — | Archived | 已归档（状态 Badge） |

**句子型文案：**

| COPY-NN | English | 中文 |
| --- | --- | --- |
| COPY-01 | Archiving is permanent. The SE Profile will be removed from the list and no longer viewable; its content is retained in the backend for audit only. This cannot be undone. Confirm archiving? | 归档为永久历史终态，归档后将从列表移除、不可再查看，内容仅保留于后台供审计，且不可恢复。确认归档？ |
| COPY-02 | SE Profile archived. | SE Profile 已归档 |
| COPY-03 | Archiving failed, please try again later. | 归档失败，请稍后重试 |
| COPY-04 | This SE Profile does not exist or you don't have access. | 该 SE Profile 不存在或无访问权限 |

### 8. Product Doc 链接

- [SEMS_PRD](http://192.168.40.171:8080/#/modules/sems/SEMS_PRD?ref=main)

---

## Tech Doc

- N/A

## 评论 / 待确认

- [2026-07-28]：产品确认进入终态（Revoked / Archived）后当前 `lock_sources` 清空；转换前集合保留于审计日志。PDR-033 已同步升级 v2.7。本导出已将 AC-07 / BR-02 按该口径合并进需求正文；飞书 Description 字段本身是否已回写需核对。
- [2026-07-30]：因 TI 芯片烧录流程关联 Story 临时加入，与产品沟通后移出当前 Story 至下个 Sprint（排期说明）。
- [2026-07-30]：补充 Figma 节点与「S08~S11 测试可参考」接口说明附件（已本地化）。
- Draft / Active 是否完全无 Archive 入口（含列表批量操作）需对照现网与设计稿确认。

## Out of Scope

- Active → Archived 直达（须先 Lock 或 Revoke）。
- Archived 回退或恢复为其他状态。
- 用户界面重新开放 Archived 记录（仅后台审计保留）。
- Lock / Unlock / Revoke / Destroy 等其他生命周期操作（由兄弟 Story 覆盖）。
- 级联归档或上游驱动归档（正文未声明）。
