# Examples — Story Acceptance Design

## 示例 A：Small 模式 + UI/UX 变更类型

**输入**：单入口 Story（Tab 改名 + 过滤默认文案）

**判定**：Small；**变更类型**：UI/UX（AC 以展示与文案为主）

**输出形态**（AC = 测试点，可不写独立测试点表）：

```markdown
**模式**: Small（单入口、预估 ≤ 8 条）  
**变更类型**: UI/UX（Tab 文案与过滤展示，无新业务规则）

## Story AC

1. 用户进入 XX 页时，Tab 应显示为「YY」。

2. 用户在 ZZ 区域应看到过滤下拉，默认文案为「ALL」。

3.（P1 / 待确认）边界场景行为应符合产品最终定义。
```

说明：P0 落在可见文案与默认展示；不展开配额/去重类矩阵。

---

## 示例 A2：Logic 变更类型（对照）

**输入**：配额不计 Demo；操作者换人时用量记在 Tenant 创建者

**判定**：可为 Small 或 Large；**变更类型**：Logic

**测试点侧重（节选）**：计入/不计入、换人归属、排除路径各至少 1 条 P0；UI 仅保留入口提示（若需求有写）。须跑规则类型 **D**。

---

## 示例 B：Large 模式 + 测试点 MD

**输入**：跨模块 Story（如企业域名白名单审批），飞书含 AC-01～AC-09

**判定**：Large；**变更类型**：Hybrid（主 Logic：审批与可见性；次 UI/UX：角标展示）

**产出路径**：`docs/sprints/_unassigned/features/self-reg-001-05-domain-whitelist/acceptance.md`

**输出形态**（节选）：

```markdown
**模式**: Large（跨模块、多 AC）  
**变更类型**: Hybrid（主 Logic，次 UI/UX：角标）

## Story AC

1.（AC-01）Applications Tab 角标仅统计 Pending 数量。

2.（AC-02）无 Pending 时角标隐藏。

## 测试点

### Account 管理 — Applications Tab

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ACCT-APP-01 | AC-01 | P0 | Applications Tab 角标展示 Pending 数量 |
| TP-ACCT-APP-02 | AC-02 | P0 | Pending 为 0 时角标隐藏 |

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 角标统计 Pending | TP-ACCT-APP-01 | ✅ |
| AC-02 无 Pending 隐藏角标 | TP-ACCT-APP-02 | ✅ |
```

完整样例见仓库：`docs/sprints/_unassigned/features/self-reg-001-05-domain-whitelist/acceptance.md`

---

## 示例 C：用户指令

| 用户说法 | 行为 |
|----------|------|
| 小需求 | Small，细粒度编号段落 |
| 大需求 / 设计测试点 | Large，AC + 测试点表 + 追溯矩阵 |
| UI 改版 / 交互 / 文案 | 变更类型 UI/UX，测试点偏展示与交互 |
| 功能逻辑 / 规则 / 权限配额 | 变更类型 Logic，测试点偏规则与回归 |
| 测试点 md / 放到 sprint feature 包 | 写入 `docs/sprints/{sprint}/features/{feature-slug}/acceptance.md` |
| 段落形式 / 不要表格 | Story AC 用编号段落；测试点仍用表格 |

---

## 示例 D：里程碑邮件 — 强制清单（易漏场景）

**输入信号**：按 Tenant 仅 1 次；首次 DAC / 首次烧录；仅发给创建者；发送失败重试 3 次。

**变更类型**：Logic（主；异步触达与去重规则）  
**规则类型**：A（里程碑）+ B（异步通知）均命中 → 必须跑强制清单。

| 做法 | 结果 |
|------|------|
| ❌ 只写：成功发信、失败不发、通道重试、Demo 不发 | 漏：失败占不占额度、失败后再成功、非创建者操作仍发给创建者、二次成功不重发（仅埋在步骤里） |
| ✅ 在主路径外独立落 TP | A2 再次成功不重发；A3+A4 业务失败不占额度且恢复后仍发；B2 非创建者操作仍仅触达创建者；B3 业务失败与投递失败分条 |

**测试点形态（节选，完整见 `docs/sprints/OBIS-20260706-20260717/features/self-reg-006-01-transactional-email/acceptance.md`）**：

```markdown
| TP-MAIL-DAC-02 | AC-02 | P0 | 同一 Tenant 仅 1 封；后续再次签发真实 DAC 不重复发送 |
| TP-MAIL-DAC-04 | AC-02, QA扩展 | P0 | 业务签发失败不占「首次」额度；失败后再成功仍发且仅 1 次 |
| TP-MAIL-DAC-05 | 需求描述, AC-02 | P0 | 非创建者完成首条真实 DAC 时，仍仅向 Tenant 创建者发送；操作者不收 |
```

**设计自检（须勾选）**：A1～A5、B1～B3 已覆盖；业务失败 ≠ 投递失败。
