# Examples — Functional Testcase MD

## 示例 A：按用户场景生成用例

**输入**：`docs/sprints/{sprint}/features/{feature-slug}/acceptance.md`（多条 TP）

**触发**：「把 xxx 测试点落地成用例 md」

**产出**：`docs/sprints/{sprint}/features/{feature-slug}/testcases/{feature-slug}.md`

**要点**：

- 先读 acceptance **变更类型**，再定 `【UI】/【Functional】/【E2E】` 比例与步骤颗粒度
- **一条用例 = 一个用户场景**；勿把多个独立业务时刻硬塞进一条
- **场景内**合并可连续校验的 TP（触发 + 内容 + 收件人等）
- UI 细步骤验态/文案；Functional 验业务结果；单条步骤 ≤ 10；造数/登录写前置条件
- **备注列必填**：来自 AC 时写 `来源 AC-0x: {AC 原文}`；否则 `来源 需求描述:` / `来源 QA扩展:`
- **标签列**：只写可读业务名（如 `CreateModule与AddAssetType权限`）；**禁止** `TP-*`、`AC-0x` 等序号类标签
- 文档头含变更类型、入口规则、产品规则、场景与 TP 覆盖说明

---

## 示例 B：场景切分 vs 场景内合并

| 做法 | 示例 | 对错 |
|------|------|------|
| 一场景一条 | 「自注册收 Welcome」一条；「首次真实 DAC 发信」另条 | ✅ |
| 场景内多校验 | Welcome 场景内同时验发件人、主题、双语正文、仅创建者收信 | ✅ |
| 多场景硬塞 | 一条 10 步跑完 Welcome + DAC + 烧录全链路深校验 | ❌ |
| 一点一案 | Welcome 主题一条、发件人一条、双语一条 | ❌ |

---

## 示例 C：备注列（来源）

| 场景 | 备注 |
|------|------|
| Welcome 触发与内容 | `来源 AC-01: Welcome 邮件在自注册 Tenant 创建成功后发送，按 Tenant 仅 1 次<br>来源 AC-04: 邮件模板中英文双语，变量替换正确` |
| Demo 不触发 | `来源 AC-05: Demo 资源不触发邮件` |
| Matter 双发（需求正文） | `来源 需求描述: Matter module 首次烧录同时收到 DAC 与烧录两封邮件` |
| 签发失败不发信（QA） | `来源 QA扩展: 真实 DAC 签发失败时不发送首次 DAC 邮件` |

错误示例：只写 `AC-01`、只写 TP-ID、改写 AC 原文、备注留空。

---

## 示例 D：用例名称与类型

| 场景（可含多 TP） | 类型 | 用例名称 |
|-------------------|------|----------|
| Assign Key 选择 Tag 并提交 | Functional | 【Product-Assets】【Functional】Assign Security Key - Tag 选择与提交 |
| Tag 空值 Add 置灰 | UI | 【Product-Assets】【UI】Tag 新增 - 空值时 Add 置灰 |
| Version 页与 Asset Tag 一致 | E2E | 【Product-Version】【E2E】Certificate Tag 跨页一致 |

---

## 示例 D2：UI vs Functional — 步骤颗粒度与校验点

**变更类型 UI/UX** 时，同页交互应写成细步骤 + 界面预期：

```text
用例：【Product-Assets】【UI】Tag 新增 - 空值时 Add 置灰
步骤：[1] 打开 Tag 新增 [2] 清空名称 [3] 观察 Add
预期：[2] 名称为空或出现校验提示 [3] Add 置灰不可点
```

**变更类型 Logic** 时，规则场景应写成业务动作 + 业务结果（勿细逛 UI）：

```text
用例：【Account-Mail】【Functional】首次 DAC 邮件 - 二次成功不重发
前置：该 Tenant 已成功发送过首次 DAC 邮件
步骤：[1] 再次完成真实 DAC 签发成功 [2] 检查创建者收件箱
预期：[1] 签发成功 [2] 不产生第二封首次 DAC 邮件
```

| 错法 | 原因 |
|------|------|
| UI 用例里验「仅 1 次 / 记在谁头上」 | 规则矩阵应 Functional 分条 |
| Functional 用例逐步点 Tab、对文案，却不验业务结论 | 与用例类型不匹配 |
| UI/UX Story 整包几乎全是 Functional 深路径 | 与变更类型比例错位 |

---

## 示例 E：所属模块与等级

| 所属模块 | 用例等级 | 说明 |
|----------|----------|------|
| `/Cloud/Product/Assets` | P0 | 主流程 Assign（同场景多 TP） |
| `/Cloud/Product/Assets` | P1 | 历史 Certificate Tag（独立场景，单独成条） |
| `/Cloud/Product/Version` | P0 | 跨页展示一致（独立场景） |

---

## 示例 F：同场景多校验 — 步骤与预期（≤ 10 步）

**场景**：Assign Security Key 并确认列表 Tag

**备注**：`来源 AC-0x: {对应 Story AC 原文}`（按实际 AC 填写）

**前置条件**

```text
1. 已登录具备 Product Asset 权限的账号<br>2. 目标 Product 下已有可用 Security Key 与至少一个自定义 Tag
```

**步骤描述**

```text
[1] 进入 Product Asset 页，定位 **Keys** 区域，点击 **Assign Key**，打开 Assign Security Key 弹窗<br>[2] 查看 Tag 选择控件形态及下拉选项<br>[3] 展开 Tag 下拉，选择一个已有自定义 Tag，完成其余必填项并提交<br>[4] 返回 Keys 列表，定位刚 Assign 的记录
```

**预期结果**

```text
[1] Assign Security Key 弹窗正常打开<br>[2] 展示 Tag 下拉单选；不含系统默认 Tag 项（google certificate config、matter config 等）<br>[3] 可单选已有自定义 Tag；提交成功，弹窗关闭<br>[4] 列表对应行 Tag 列展示所选自定义 Tag
```

说明：4 步同属「Assign Key」一个场景；控件形态、提交成功、列表展示在同场景内连续校验。

---

## 示例 G：必须拆分（跨场景勿硬合并）

| 场景 A | 场景 B | 原因 |
|--------|--------|------|
| 自注册后收 Welcome | 首次真实 DAC 发信 | 不同业务时刻 |
| Demo 签发不发信 | 真实签发发信 | 互斥前置（可同条仅当构成「先 Demo 再真实」对照且仍属同一排除场景） |
| 运营开通 Tenant 不发信 | 自注册发 Welcome | 不同 Tenant 类型 |
| 邮件**通道**重试成功 | DAC **业务**签发失败不发信 | 独立失败轴（投递 vs 业务） |
| DAC 业务失败不发信 | 失败后再成功仍发且仅 1 次 | 负向 vs 恢复；禁止停在「失败不发」 |
| 创建者操作首次烧录（他人不收） | 非创建者操作首次烧录仍仅触达创建者 | 触发者 × 收件人；后者不可省略 |
| 首次烧录发信 | 二次成功烧录不重发 | 可同条紧随验证，但标题/场景表须点明「二次成功」 |

里程碑邮件完整样例：`docs/sprints/OBIS-20260706-20260717/features/self-reg-006-01-transactional-email/testcases/self-reg-006-01-transactional-email.md`

---

## 示例 H：文档头 blockquote

```markdown
> 来源：`docs/sprints/_examples/features/product-asset-tag/`（acceptance / xmind）  
> 需求：Product Asset — Certificate/Key Tag  
> 变更类型：Hybrid（主 Logic：Tag 赋值规则；次 UI/UX：下拉与置灰）  
> 用例数：8（P0 × 6，P1 × 2）；类型分布：UI × 2，Functional × 4，E2E × 2；覆盖 TP 16 条  
> 入口规则：**Assign Security Key** 弹窗 → Product Asset 页 **Keys** 区域 **Assign Key**。  
> 产品规则：系统默认 Tag 仅 Assign Certificate；Assign Security Key 无系统默认项。  
> 用例名称格式：`【{页面模块}】【UI|Functional|E2E】{子功能} - {描述}`  
> 设计原则：一条用例一个场景；UI 细步骤验态，Functional 验业务结果；步骤 ≤ 10  
> 备注列：标明来源；来自 AC 时写 `来源 AC-0x: {AC 原文}`
```
---

## 黄金样例（完整文件）

[`docs/sprints/_examples/features/product-asset-tag/testcases/product-asset-tag.md`](../../../docs/sprints/_examples/features/product-asset-tag/testcases/product-asset-tag.md)

> 注：历史黄金样例可能仍缺「备注」列或偏「一点一案」。**新生成**用例以本 skill 为准（含备注来源列、一场景一条）；结构、列顺序、命名与编号风格与该文件保持一致。
