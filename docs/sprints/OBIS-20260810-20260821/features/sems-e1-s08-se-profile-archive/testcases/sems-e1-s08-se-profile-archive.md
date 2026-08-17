# SEMS E1-S08 SE Profile 归档 — 功能测试用例

> 来源：`docs/sprints/OBIS-20260810-20260821/features/sems-e1-s08-se-profile-archive/acceptance.md`  
> 飞书 Story：[7016548583](https://project.feishu.cn/obis/userstory/detail/7016548583)  
> **变更类型**：Hybrid（主 Logic：Locked/Revoked→Archived、终态不可见、审计/lock_sources；次 UI/UX：入口、二次确认、Toast/文案）→ 用例以 `【Functional】/【E2E】` 为主，入口与对话框用 `【UI】`  
> 用例数：18（P0 × 6，P1 × 10，P2 × 2）；类型分布：E2E × 2，Functional × 11，UI × 5  
> 入口：SEMS → SE Profile **列表**操作列 / **详情**操作栏 → Archive  
> 产品规则：仅 Locked / Revoked 可归档；Archived 为终态且对用户不可见；详情归档后跳回列表；列表归档留在列表且行消失；失败态不变  
> 用例名称：`【{模块 slug}】【{UI|Functional|E2E}】{子功能} - {描述}`  
> 备注约定：来自 AC 写 `来源 AC-0x: {AC 原文}`；否则 `来源 需求描述:` / `来源 QA扩展:`  
> 标签：`SE Profile Archive`（禁止写入 TP/AC 编号）  
> 模块映射：见同目录 `module-mapping.json`  
> 文案约定：步骤/预期写界面可见原文，不写文案编号代号

### 场景与 TP 覆盖

| 用例场景 | 覆盖 TP |
|----------|---------|
| Locked 详情归档主路径 + 不可见 + 审计 lock_sources | TP-ARCH-DTL-01、03、04；TP-ARCH-INV-01～03；TP-ARCH-AUD-01、02；TP-ARCH-TERM-01 |
| Revoked 详情归档主路径 | TP-ARCH-DTL-02、04；TP-ARCH-AUD-03 |
| 详情 Cancel | TP-ARCH-DTL-05 |
| 列表 Locked / Revoked 归档 | TP-ARCH-LST-01～05 |
| 列表 Cancel | TP-ARCH-LST-06 |
| Active / Draft 无 Archive 入口 | TP-ARCH-PRE-01、02 |
| 不可新引用 + 历史引用保留 | TP-ARCH-INV-04 |
| 归档 5xx / 超时 / 403 | TP-ARCH-ERR-01～03 |
| 中英文 COPY 文案 | TP-ARCH-COPY-01 |
| API ID 形态 / 并发 / 防重 | TP-ARCH-API-01～03 |
| 实现层 trigger_reason（可跳过） | TP-ARCH-AUD-04 |

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【SEMS-SE-Profile-Detail】【E2E】Locked 详情 Archive - Toast 跳列表不可见与审计 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P0 | 1. 已登录且具备 SE Profile Archive 权限<br>2. 存在 **Locked** SE Profile（记 Name/ID，可进详情；若含 `lock_sources` 便于核对审计）<br>3. 可查看审计日志入口（或联调接口） | [1] 打开该 Profile **详情页**，观察操作栏是否有 Archive<br>[2] 点击 **Archive**，阅读确认框文案与按钮<br>[3] 点击 **Confirm Archive**，观察 Toast、是否跳转、列表是否仍见该行<br>[4] 在列表用 Name/ID **搜索**<br>[5] 用原详情 URL **直链**访问<br>[6] 打开审计，定位刚产生的 archive 记录；核对 `lock_sources`（若归档前为 Locked） | [1] 显示 **Archive**<br>[2] 弹出二次确认；文案为「归档为永久历史终态，归档后将从列表移除、不可再查看，内容仅保留于后台供审计，且不可恢复。确认归档？」；含 **Confirm Archive** / **Cancel**<br>[3] Toast 为「SE Profile 已归档」；**跳回列表页**；该行**不再出现**；界面无继续改状态入口可操作该 Profile<br>[4] 搜索**不命中**<br>[5] 提示「该 SE Profile 不存在或无访问权限」<br>[6] 审计 action=**archive**，含操作人、时间、Profile ID/Name、from→to（Locked→Archived）；Locked→Archived 时含转换前 **lock_sources**，归档后当前 `lock_sources` 为 `[]`（可接口回读） | 来源 AC-01: Locked 和 Revoked 状态下，详情页操作栏或列表页操作列应显示 Archive 入口。<br>来源 AC-02: 用户点击 Archive 后，应弹出二次确认对话框（COPY-01），并提供 Confirm Archive 与 Cancel 两个按钮。<br>来源 AC-03: 用户确认归档后，SE Profile 状态应切换为 Archived，页面顶部显示成功 Toast（COPY-02）；若从详情页触发，归档后应跳回列表页；若从列表页触发，应留在列表页且该行从列表消失。<br>来源 AC-04: Archived 应为终态，不可从 Archived 回退到任何其他状态。<br>来源 AC-05: 归档后该 SE Profile 对用户不可见：列表、搜索均不展示；详情页直链访问应返回不存在提示（COPY-04）；记录保留于数据库供审计溯源，不对用户界面开放。<br>来源 AC-07: 归档操作完成后应写入审计日志，记录操作人、时间、SE Profile ID、Name、操作类型（archive）、from_status → to_status，以及转换前的 lock_sources（Locked → Archived 时记录转换前集合）。 |
| 【SEMS-SE-Profile-Detail】【E2E】Revoked 详情 Archive - Toast 跳列表与审计 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P0 | 1. 存在 **Revoked** SE Profile（记 Name/ID）<br>2. 可查看审计 | [1] 打开详情，确认有 Archive<br>[2] Archive → Confirm Archive<br>[3] 观察 Toast、落地页、列表是否仍见该行<br>[4] 核对审计 from→to 与 `lock_sources` 清空口径 | [1] 显示 Archive<br>[2][3] Toast「SE Profile 已归档」；跳回列表；行消失；搜索/直链同 Locked 主路径不可见规则<br>[4] 审计 action=archive，from Revoked→Archived；当前 `lock_sources` 为 `[]`（按产品终态口径） | 来源 AC-01: Locked 和 Revoked 状态下，详情页操作栏或列表页操作列应显示 Archive 入口。<br>来源 AC-03: 用户确认归档后，SE Profile 状态应切换为 Archived，页面顶部显示成功 Toast（COPY-02）；若从详情页触发，归档后应跳回列表页…<br>来源 AC-07: …from_status → to_status…<br>来源 需求描述: Revoked→Archived 后 lock_sources 清空 |
| 【SEMS-SE-Profile-Detail】【UI】Archive 二次确认 - 点 Cancel 状态不变 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 已打开 Locked 或 Revoked 详情页 | [1] 点击 Archive 打开确认框<br>[2] 点击 Cancel<br>[3] 观察状态与当前页 | [1] 确认框打开<br>[2] 对话框关闭<br>[3] 状态仍为 Locked/Revoked；仍在详情页；Archive 仍可见 | 来源 AC-02: 用户点击 Archive 后，应弹出二次确认对话框（COPY-01），并提供 Confirm Archive 与 Cancel 两个按钮。<br>来源 QA扩展: 二次确认点 Cancel：对话框关闭，状态保持 Locked/Revoked 不变 |
| 【SEMS-SE-Profile-List】【Functional】列表 Locked Archive - 留列表行消失 | /Cloud/SEMS/SE-Profile-List | SE Profile Archive | P0 | 1. 列表可见一条 **Locked** SE Profile<br>2. 已在列表页 | [1] 在该行操作列确认有 Archive<br>[2] 点击 Archive，核对确认框<br>[3] Confirm Archive，观察 Toast、是否仍在列表页、该行是否消失 | [1] 显示 Archive<br>[2] 确认框文案与 Confirm Archive / Cancel 同详情<br>[3] Toast「SE Profile 已归档」；**留在列表页**；该行消失 | 来源 AC-01: Locked 和 Revoked 状态下，详情页操作栏或列表页操作列应显示 Archive 入口。<br>来源 AC-02: 用户点击 Archive 后，应弹出二次确认对话框（COPY-01）…<br>来源 AC-03: …若从列表页触发，应留在列表页且该行从列表消失。 |
| 【SEMS-SE-Profile-List】【Functional】列表 Revoked Archive - 留列表行消失 | /Cloud/SEMS/SE-Profile-List | SE Profile Archive | P0 | 1. 列表可见一条 **Revoked** SE Profile | [1] 行操作列点击 Archive → Confirm Archive<br>[2] 观察 Toast、页面、该行 | [1][2] Toast「SE Profile 已归档」；留在列表；该行消失 | 来源 AC-01: …列表页操作列应显示 Archive 入口。<br>来源 AC-03: …若从列表页触发，应留在列表页且该行从列表消失。 |
| 【SEMS-SE-Profile-List】【UI】列表 Archive - 点 Cancel 行仍在 | /Cloud/SEMS/SE-Profile-List | SE Profile Archive | P1 | 1. 列表有 Locked 或 Revoked 行 | [1] 行内 Archive → Cancel<br>[2] 观察行与状态 | [1] 对话框关闭<br>[2] 行仍在列表；状态仍为 Locked/Revoked | 来源 AC-02: …提供 Confirm Archive 与 Cancel 两个按钮。<br>来源 QA扩展: 列表页二次确认点 Cancel：对话框关闭；行仍在列表；状态保持 Locked/Revoked |
| 【SEMS-SE-Profile-Detail】【UI】Active - 详情与列表无 Archive 入口 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P0 | 1. 存在 **Active** SE Profile<br>2. 可进详情与列表定位该行 | [1] 打开详情观察操作栏<br>[2] 回列表观察该行操作列 | [1] **不显示 Archive**<br>[2] **不显示 Archive** | 来源 需求描述: Active 状态下不显示 Archive 按钮（须先 Lock 或 Revoke） |
| 【SEMS-SE-Profile-Detail】【UI】Draft - 无 Archive 入口 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 存在 **Draft** SE Profile（详情+列表） | [1] 详情操作栏是否有 Archive<br>[2] 列表行操作列是否有 Archive | [1][2] **不显示 Archive**（若现网有批量入口亦不应可归档 Draft） | 来源 QA扩展: Draft 状态不显示 Archive 入口（须对照现网/设计稿） |
| 【SEMS-SE-Profile-List】【Functional】归档后 - 不可被新 Version 引用且历史引用保留 | /Cloud/SEMS/SE-Profile-List | SE Profile Archive | P1 | 1. Profile A：可归档（Locked/Revoked），**尚未**被新 Version 引用<br>2. Profile B：某 Product Version **已引用**该 Profile，再将其归档<br>3. 已知 Create Version / 引用选择入口 | [1] 将 Profile A 归档成功<br>[2] 进入 Product → Create Version（或 Version 编辑中的 SE Profile 选择入口），搜索 A 的 Name/ID<br>[3] 打开已引用 Profile B 的 Version 详情/只读引用区 | [1] A 归档成功且列表不可见<br>[2] A **不可选中 / 不出现在可选列表**<br>[3] B 的历史引用关系仍可见可追溯 | 来源 AC-05: 归档后该 SE Profile 对用户不可见…<br>来源 需求描述: BR-01 内容保留：Archived SE Profile…不可被新 Product Version 引用；历史引用关系不受影响 |
| 【SEMS-SE-Profile-Detail】【Functional】Archive 接口 5xx - 状态不变可重试 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P0 | 1. Locked 或 Revoked 详情已打开<br>2. 可 Mock/注入归档接口返回 **5xx** | [1] Archive → Confirm，触发 5xx<br>[2] 观察 Toast、状态、是否跳转<br>[3] 恢复接口后再次 Archive → Confirm | [1] 请求失败<br>[2] Toast 为「归档失败，请稍后重试」；状态仍为原 Locked/Revoked；仍在详情；Archive 仍可点<br>[3] 可再次发起并成功归档 | 来源 AC-06: 归档接口调用失败时，页面顶部应显示错误 Toast（COPY-03），且 SE Profile 状态不发生变更。 |
| 【SEMS-SE-Profile-Detail】【Functional】Archive - 网络超时或断网可重试 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. Locked/Revoked 详情已打开<br>2. 可模拟超时/断网 | [1] Confirm Archive 时断网或超时<br>[2] 恢复网络后观察状态并重试 | [1] 状态不变；有错误反馈（「归档失败，请稍后重试」或现网统一网络错误文案）<br>[2] 可重试；不出现前后端状态不一致 | 来源 AC-06: 归档接口调用失败时，页面顶部应显示错误 Toast（COPY-03），且 SE Profile 状态不发生变更。<br>来源 QA扩展: 归档请求网络超时 / 断网… |
| 【SEMS-SE-Profile-Detail】【Functional】Archive - 403 无权限有反馈 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 无 Archive 权限账号 A；有权限账号 B<br>2. 同一 Locked/Revoked Profile | [1] 账号 A 尝试 Archive（UI 或接口）<br>[2] 账号 B 对同 Profile 执行合法归档 | [1] 状态不变；有 403/无权限类错误反馈（UI 无按钮亦视为阻断）<br>[2] 有权限账号可成功归档 | 来源 AC-06: …错误 Toast…状态不发生变更。<br>来源 QA扩展: 归档接口返回 403… |
| 【SEMS-SE-Profile-Detail】【UI】中英文 - 确认框 Toast 与直链提示文案 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 可切中/英文<br>2. 有可归档 Profile；另备一条已归档直链（或归档后立刻核对） | [1] 中文打开 Archive 确认框（可 Cancel）；走一次成功看 Toast；用直链看不存在提示<br>[2] 英文界面重复核对确认框、成功 Toast、直链提示 | [1] 确认框：「归档为永久历史终态，归档后将从列表移除、不可再查看，内容仅保留于后台供审计，且不可恢复。确认归档？」；成功 Toast：「SE Profile 已归档」；直链：「该 SE Profile 不存在或无访问权限」；失败场景（若测）Toast：「归档失败，请稍后重试」<br>[2] 英文确认框：「Archiving is permanent. The SE Profile will be removed from the list and no longer viewable; its content is retained in the backend for audit only. This cannot be undone. Confirm archiving?」；成功 Toast：「SE Profile archived.」；直链：「This SE Profile does not exist or you don't have access.」；失败：「Archiving failed, please try again later.」 | 来源 AC-02: …二次确认对话框（COPY-01）…<br>来源 AC-03: …成功 Toast（COPY-02）…<br>来源 AC-05: …不存在提示（COPY-04）…<br>来源 AC-06: …错误 Toast（COPY-03）… |
| 【SEMS-SE-Profile-Detail】【Functional】Archive API - 裸 ID 与 SEP_ 前缀 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 已知同一可归档 Profile 的裸 ID 与 `SEP_<id>`（准备两条或归档前各测一种形态后换数） | [1] 用裸 ID 调用归档成功<br>[2] 用 `SEP_<id>` 对另一条可归档 Profile 归档成功 | [1][2] 两种 ID 形态均接受且归档成功（列表不可见） | 来源 QA扩展: businessProfileId 支持裸 ID 与 SEP_<id> 两种格式归档成功 |
| 【SEMS-SE-Profile-Detail】【Functional】并发 Archive - 仅成功一次 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 同一 Locked/Revoked Profile<br>2. 两名有权限用户（或双会话）可几乎同时 Confirm | [1] 两侧几乎同时 Confirm Archive<br>[2] 刷新列表/审计 | [1] **仅成功一次**（状态 Archived）；另一侧失败（错误 Toast/业务冲突）<br>[2] 列表仅一份归档结果；无双成功/脏状态 | 来源 QA扩展: 并发归档：两名有权限用户几乎同时…最终仅成功一次… |
| 【SEMS-SE-Profile-Detail】【Functional】防重复提交 - 10 秒与 clientRequestId | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P2 | 1. 可观察归档请求 `clientRequestId`<br>2. Locked/Revoked Profile | [1] 短间隔连续两次 Confirm Archive<br>[2] 复用同一 `clientRequestId` 重放<br>[3] 已归档后用新 `clientRequestId` 再调归档 | [1] 防重复：仅一次成功副作用<br>[2] 重试不重复归档<br>[3] 应按已归档/不可见拒绝 | 来源 QA扩展: 同用户 10 秒内重复提交同一归档请求被防重；clientRequestId 网络重试复用原 UUID |
| 【SEMS-SE-Profile-Detail】【Functional】Archived - 状态变更 API 拒绝 | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P1 | 1. 已知已归档 Profile 的 ID（后台/联调可得）<br>2. 可调用状态变更类 API（Unlock/Lock/Revoke 等） | [1] 对 Archived ID 尝试变更至 Active/Locked 等<br>[2] 核对状态仍为 Archived（接口或后台） | [1] 请求失败/拒绝<br>[2] 状态保持 Archived | 来源 AC-04: Archived 应为终态，不可从 Archived 回退到任何其他状态。<br>来源 QA扩展: 对 Archived 调用状态变更 API 应失败/拒绝，状态保持 Archived |
| 【SEMS-SE-Profile-Detail】【Functional】生命周期审计 trigger_reason（可跳过） | /Cloud/SEMS/SE-Profile-Detail | SE Profile Archive | P2 | 1. 具备 DB/内部表或联调日志访问权限；否则本条跳过 | [1] 完成一次手动归档<br>[2] 查生命周期审计/`se_profile.archived` outbox | [1][2] 可见 `trigger_reason=manual_archived` 与状态 outbox（无权限则跳过，不阻断 AC-07） | 来源 需求描述: （实现层细节，非 AC）生命周期审计 trigger_reason=manual_archived… |

---

## 待确认（执行时）

- [ ] Draft / 批量操作是否完全无 Archive（对照设计稿与现网）
- [ ] 网络超时 / 403 错误文案是否统一为「归档失败，请稍后重试」
- [ ] Product Version 中 SE Profile 引用选择器的准确路径（落实「不可新引用」）
- [ ] 并发失败侧具体提示文案与业务码
- [ ] Revoked→Archived 审计中 `lock_sources` 字段是否必填空数组
