# testcase-agent-run — 样例

## 样例 1：执行 B4 Member 只读批次（L0/🟢）

**用户**：

```text
按 testcase-agent-run，跑 OBIS-20260727-20260807 的 B4，只做只读类，打开 Transfer 后一律 Cancel。
```

**Agent 读取切片**：

| 文件 | 切片 |
|------|------|
| `docs/execution/OBIS-20260727-20260807/execution-plan.md` | B4 整节 |
| `docs/execution/OBIS-20260727-20260807/data-ledger.md` | A3、KEY-1/2、CERT-1、FAC-1/2、GRP-1、D2（若涉及删除弹窗观察） |
| `…/ux-p2-member-unify/testcases/ux-p2-member-unify.md` | B4 对应 UI 行（Member 列表、Transfer 弹窗 Cancel 等） |
| feature `baseline/`（若有） | 相关页入口与按钮文案 |
| `config/env.local.yaml` | sit base_url + A3 邮箱凭证 |

**执行要点**：

1. 门禁：KEY-1 URL 与 A3 为 Admin 均 ✅  
2. A3 登录一次 → 直达 KEY-1 Member → 跑 KMS UI 条  
3. Transfer 弹窗用例：打开 → 断言文案 → **Cancel**，不 Confirm  
4. 全部 🟢 → 只更新 run-log 批次计数；无需台账身份变更  

**回复摘要示例**：

```text
B4 已执行 14 条：Pass 12 / Fail 1 / Blocked 1
Fail：【PKI…】Transfer Cancel — 步骤[3] 蒙层点击后弹窗关闭（预期不关闭）
Blocked：Factory Member Columns — 台账 FAC-1.url 为空
证据：docs/execution/OBIS-20260727-20260807/evidence/R1/
```

---

## 样例 2：dry-run 门禁

**用户**：

```text
先别点浏览器，检查 B5 Transfer E2E 能不能跑。
```

**Agent**：只读 plan B5 + 台账 A3/A4/A5/A8/A10/A11 + KEY/CERT/FAC 行，输出门禁表。

**合格输出片段**：

```markdown
| 用例 | actor | entry_url | 破坏性 | 门禁 | 原因 |
|------|-------|-----------|--------|------|------|
| KMS 目标已在 Member 成功移交 | A3→A4 | KEY-1.url | 🔴 | OK | |
| KMS 目标不在 Member | A3→A5 | KEY-2.url | 🔴 | Blocked | A5 邮箱未填 |
```

---

## 样例 3：单条 🔴 与复位

**用户**：

```text
执行 member-unify：KMS Transfer 目标已在 Member 成功移交（P0）。
```

**Agent 顺序**：

1. 绑定：actor=A3，target=A4，resource=KEY-1  
2. 记录移交前 A3 Permission 快照（截图或列表文本）  
3. Confirm 移交 → 断言 Toast / Role  
4. 台账：A3 当前状态 → Normal Member；A4 → Admin；第 6 节加变更行  
5. 复位：A4 登录 → Transfer 回 A3 → 再回填台账  
6. run-log 明细 + 复位确认  

---

## 样例 4：用例散文 → 绑定

**用例前置**：

```text
1. Admin 本人登录
2. 目标用户已在 Member 且非 Admin
```

**结合 plan B5 行 1 与台账后的绑定**：

```yaml
case_name: 【KMS-Key-Detail】【E2E】Transfer Admin - 目标已在 Member 成功移交
actor: A3
target: A4
resources: [KEY-1]
entry_url: <ledger KEY-1 直达 URL>
destructiveness: 🔴
reset: A4 登录 → Transfer 回 A3
```

若用户未指定 sprint/plan，而用例只写「Admin 本人」，Agent **必须**询问或查 plan，禁止随机选 Key。

---

## 样例 5：推荐启动句

```text
@testcase-agent-run 执行 {sprint} 批次 {Bn}，layer=L0
@testcase-agent-run dry-run {sprint} B5
@testcase-agent-run 重跑 run-log 里 R1 失败的那条，先核对台账状态
```
