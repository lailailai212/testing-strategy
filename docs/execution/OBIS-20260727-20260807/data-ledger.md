# Sprint `OBIS-20260727-20260807` 数据台账

> 执行期的**单一事实来源**：用例文档写代号，代号对应的真实标识查本表。
> 需求侧要求见 [`data-prep.md`](data-prep.md)；执行顺序见 [`execution-plan.md`](execution-plan.md)。
>
> **纪律**：造出即登记；不可逆操作执行后立即回填「当前状态」并在第 6 节记一行。
> **禁止**在本文件写明文密码或验证码，凭证一律查 `config/env.local.yaml`。

- 环境：**sit**，地址见 `config/env.local.yaml` → `environments.sit`
- 命名前缀：`qa0807-`
- 造数负责人：`<填写>`
- 最后更新：`2026-08-03`
- 批次映射：[`batch-case-mapping.md`](batch-case-mapping.md)
- 入口 baseline：`docs/sprints/OBIS-20260727-20260807/features/ux-p2-member-unify/baseline/entry-urls.md`

## 0. 准备状态总览

| 区块 | 应备 | 已备 | 状态 |
|---|---|---|---|
| 权限与角色账号（A1/A2/A3/A6） | 4 | 1 | 🟡 A1 已绑 super_admin；A2/A3/A6 待造 |
| Transfer 目标账号（A4/A5/A8/A10/A11/A12） | 6 | 0 | ⬜ 未开始 |
| 一次性可删账号（D1–D5） | 5 | 0 | ⬜ 未开始 |
| `+n` 档位账号（R1–R3） | 3 | 0 | ⬜ 未开始（A1 Profile 有 Role `+3` 可暂代部分） |
| 权限对照账号（P1–P4） | 4 | 0 | ⬜ 未开始 |
| KMS 资源（KEY-1/2/3） | 3 | 0 | 🟡 有候选 KEY-CAND-1，未满足 KEY-1 成员矩阵 |
| PKI 资源（CERT-1、List 数据） | 2 | 0 | ⬜ 列表入口已确认 |
| Factory 资源（FAC-1/2） | 2 | 0 | ⬜ 列表入口已确认 |
| Group 资源（GRP-1 三类数据） | 1 | 0 | ⬜ 列表入口已确认 |
| Product 资源（PROD-1–6） | 6 | 0 | 🟡 列表有 `+n`/Version `-` 候选行，未登记代号 |
| **特殊状态资源（S-ARCH/LOCK/DEL/DESTROY）** | 4 | 0 | 🔴 **阻塞项** |
| Audit 日志（六处） | 6 | 1 | 🟡 Profile Audit 已有数据；其余待绑 URL |
| 列表入口 URL 目录 | — | ✅ | 见 §2.8 |

状态图例：⬜ 未开始 · 🟡 进行中 · ✅ 已就位 · 🔴 阻塞

## 1. 账号

### 1.1 权限与角色类（可复用）

| 代号 | 真实邮箱 | 租户 | 要求 | 当前状态 | 造数时间 | 备注 |
|---|---|---|---|---|---|---|
| A1 | `feng.zhang@snowballtech.com` | t1 | System Admin：可删用户、可配 Role 权限树 | ✅ Active · System Admin +3 | 2026-08-03 | 绑 `env.local.yaml` → `accounts.super_admin`；凭证见该文件 |
| A2 | | t1 | 普通 Active，非 System Admin，非任何资源 Admin | ⬜ | | 验证置灰与无权限提示 |
| A3 | | t1 | 同时为 KEY-1/KEY-2 的 KMS Admin、CERT-1 的 PKI Admin、FAC-1/FAC-2 的 Factory Admin | ⬜ | | **Transfer 后身份会变，见第 6 节**；B4 只读可暂用 A1+KEY-CAND-1 |
| A6 | | t1 | **Locked** 状态用户 | ⬜ | | 验证 Transfer 下拉不含 Locked |

### 1.2 Transfer 目标类

| 代号 | 真实邮箱 | 租户 | 要求 | 当前状态 | 造数时间 | 备注 |
|---|---|---|---|---|---|---|
| A4 | | t1 | Active，**已在** KEY-1 Member 且非 Admin | | | |
| A5 | | t1 | Active，**不在** KEY-2 Member | | | |
| A8 | | t1 | Active，PKI Transfer 目标 | | | |
| A10 | | t1 | Active，**已在** FAC-1 Member 且非 Factory Admin | | | |
| A11 | | t1 | Active，**不在** FAC-2 Member | | | |
| A12 | | t1 | Active，Account 删除时的 Target Admin | | | 会接收 D2/D3 的资源 Admin |

### 1.3 一次性可删账号（销毁后不可复用）

| 代号 | 真实邮箱 | 要求 | 当前状态 | 删除时间 | 备注 |
|---|---|---|---|---|---|
| D1 | | 已加入 PROD-5 的 Member | | | 验证删除后 Product Member 不可见 |
| D2 | | 命中 ≥1 类 Product Owner / KMS / PKI / Factory Admin | | | 建议兼任两类，留一类为 0 作卡片对照 |
| D3 | | 对 S-ARCH、S-LOCK 为 Admin；另关联 S-DEL、S-DESTROY | | | 依赖特殊状态资源 |
| D4 | | **不是**任何 Owner / Admin | | | 验证可直接删除 |
| D5 | | SNB 侧命中 Admin 条件 | | | User(SNB) 一致性 |
| D6 备 | | 备用，供回归重跑 | | | 建议每类多备 1 个 |

### 1.4 `+n` 角色档位类

| 代号 | 真实邮箱 | 要求 | 实际角色数 | 是否出现 `+n` | 当前状态 |
|---|---|---|---|---|---|
| R1 | | 角色数足以触发 `+n`（建议 ≥ 3） | | | |
| R2 | | 仅 1 个角色 | | 否（对照） | |
| R3 | | 恰好落在溢出边界 | | | 边界值需实测确认 |

### 1.5 OTA / Vulnerability 权限类

| 代号 | 真实邮箱 | 租户 | 权限配置 | 预期 Tab 可见性 | 当前状态 |
|---|---|---|---|---|---|
| P1 | | t1 | 无 Vulnerability Tab Page | 不显示 Vulnerability | |
| P2 | | t1 | 无 OTA Tab Page | 不显示 OTA | |
| P3 | | t1 | 两项权限齐全 | 两 Tab 均可见 | |
| P4 | | t2 | 租户不上线，所有 Role 均不配 | 两 Tab 均不可见 | |

## 2. 资源实例

### 2.1 KMS

| 代号 | 资源名 | Key ID | 直达 URL | 当前 Admin | 数据要求满足情况 | 状态 |
|---|---|---|---|---|---|---|
| KEY-CAND-1 | test permission | KID-SAdba2d91445 | `https://iot-admin-sit.snowballtech.com/key/2081648131348414465` | 张峰（A1） | Member 仅 Admin 本人；Permission **全部平铺无 +n**；Columns **无 Organization** | 🟡 入口可用；**不满足** KEY-1 成员矩阵，见 baseline |
| KEY-1 | | | | A3 | Member 含 A4；≥1 名成员 Permission ≥ 2（需出现 `+n`） | ⬜ |
| KEY-2 | | | | A3 | A5 **不在** Member | ⬜ |
| KEY-3 | | | | | Audit Tab 含多种 Operation Type | ⬜ |
| Key List | — | — | `…/key/list` | — | 列表 Total: 396；Usage Count 列存在 | ✅ 入口 |

### 2.2 PKI

| 代号 | 资源名 | ID | 直达 URL | 当前 Admin | 数据要求满足情况 | 状态 |
|---|---|---|---|---|---|---|
| CERT-1 | | | | A3 | 同租户有其他 Active 用户；有审计日志 | ⬜ |
| PKI List | — | — | `…/pki/list` | — | 列表入口已确认 | ✅ 入口 |

### 2.3 Factory

| 代号 | 资源名 | ID | 直达 URL | 当前 Admin | 数据要求满足情况 | 状态 |
|---|---|---|---|---|---|---|
| FAC-1 | | | | A3 | A10 **已在** Member | ⬜ |
| FAC-2 | | | | A3 | A11 **不在** Member | ⬜ |
| Factory List | — | — | `…/factory/list` | — | 列表入口已确认 | ✅ 入口 |

### 2.4 Group

| 代号 | 资源名 | ID | 直达 URL | 数据要求满足情况 | 状态 |
|---|---|---|---|---|---|
| GRP-1 Member | | | | 同时含 Admin 行与非 Admin 行 | ⬜ 列表=`…/user/group/list` |
| GRP-1 Audit | | | | 跨多日 / 边界时间 / ≥2 个 Organization / 长文案 Details | ⬜ |
| GRP-1 Linked Product | | | | 某行 Role 形如 `Member +2` | ⬜ |

### 2.5 Product

| 代号 | 产品名 | ID | 直达 URL | 数据要求满足情况 | 状态 |
|---|---|---|---|---|---|
| PROD-1 | | | | 有多个 Prod 版本（验证「最新」） | ⬜ |
| PROD-2 | | | | 仅 Test，或 Test 比 Prod 更新 | ⬜ |
| PROD-3 候选 | 多行 Version=`-` | — | `…/product/list` | 无 Prod Version → `-` | 🟡 列表可见，未钉死单行 |
| PROD-4 候选 | product-rare | — | `…/product/list`（点进详情后补 URL） | Module_12 **+11**，可验浮层滚动 | 🟡 |
| PROD-4 候选2 | success.test | — | 同上 | Module `My +6` | 🟡 |
| PROD-5 | | | | Member 含 D1 | ⬜ |
| PROD-6 | | | | 含 OTA 与 Vulnerability Tab，有审计日志 | ⬜ |

### 2.6 特殊状态资源 🔴 阻塞项

| 代号 | 资源类型 | 资源名 / ID | 状态构造方式 | 支持人 | D3 是否为 Admin | 状态 |
|---|---|---|---|---|---|---|
| S-ARCH | | | 前台入口 / 后端支持 | | | |
| S-LOCK | | | | | | |
| S-DEL | | | | | | |
| S-DESTROY | | | | | | |

> 前台是否有归档 / 锁定入口需先探查；已删除与已销毁在环境中能否区分需与开发确认。**本区块未就位则 member-unify 的资源状态范围用例无法执行。**

### 2.7 其余大列表（列宽抽样，需 ≥ 2 类有数据）

| 列表 | 直达 URL | 有数据 | 状态 |
|---|---|---|---|
| Account 列表 | `https://iot-admin-sit.snowballtech.com/user/list` | ✅ | ✅ |
| Group 列表 | `https://iot-admin-sit.snowballtech.com/user/group/list` | 待点进确认 | ✅ 入口 |
| Role 列表 | `https://iot-admin-sit.snowballtech.com/system/role/list` | ✅ Total: 283 | ✅ |
| User (SNB) | `https://iot-admin-sit.snowballtech.com/system/user/list` | 待确认 | ✅ 入口 |
| U-safe List | | | ⬜ |
| Device History | | | ⬜ |
| DAC Report | | | ⬜ |

### 2.8 列表入口速查（Agent 直达）

完整说明：`docs/sprints/OBIS-20260727-20260807/features/ux-p2-member-unify/baseline/entry-urls.md`

| 模块 | Path |
|------|------|
| Product | `/product/list` |
| KMS | `/key/list` |
| PKI | `/pki/list` |
| Factory | `/factory/list` |
| Account | `/user/list` |
| Group | `/user/group/list` |
| Role | `/system/role/list` |
| User (SNB) | `/system/user/list` |
| KMS 样本详情 | `/key/2081648131348414465`（KEY-CAND-1） |

## 3. Audit 日志覆盖（六处均需有数据）

| 位置 | 直达 URL | 日志条数 | 跨多日 | 含边界时间 | ≥2 Organization | 含长文案 Details | 状态 |
|---|---|---|---|---|---|---|---|
| Group（基准） | | | | | | | ⬜ |
| Account 详情 | | | — | — | | | ⬜ |
| My Profile | 头像 → My Profile → Audit（A1） | 多条 | ✅ 06～07 | 待核 | 待核（操作人含多人） | 待核 | 🟡 上午探查可用 |
| KMS Key 详情 | KEY-CAND-1 → **Audit** Tab | 待核 | | | | | 🟡 入口已知；Tab 名是 Audit |
| PKI 资源详情 | | | — | — | | | ⬜ |
| Product 详情 | | | — | — | | | ⬜ |

## 4. 租户与环境

| 代号 | 真实租户名 | Organization 简称 | OTA/Vulnerability | 可访问 | 备注 |
|---|---|---|---|---|---|
| t1 | 雪球(上海雪球信息科技有限公司) | 雪球 | enabled | ✅ A1 | 映射见 `env.local.yaml` → `tenants.t1` |
| t2 | IKEA(IKEA) | 待确认 | disabled | ⬜ 无可登录用户 | 关联候选 IKEA-test1 / LEEDARSON |
| t3 | HW(HUAWEI) | HW | — | 🟡 future.wei | Audit/Member 仍为旧规格；跨 Org 日志可行性待确认 |

## 5. 工具与访问

| 项 | 就绪 | 备注 |
|---|---|---|
| 中英文切换 | 🟡 | 顶栏语言按钮可见，未系统验收 |
| 浏览器开发者工具（量列宽） | ✅ | 280 / 160 / 64 px |
| Figma node `15959-188662` | ⬜ | 需完整链接与 fileKey，见 `env.local.yaml` |
| 剪贴板权限（Audit 邮箱复制） | ⬜ | |
| Role 权限变更并重登生效 | ⬜ | 上午探查：点 Role 行无响应，需换入口 |
| 批次↔用例映射 | ✅ | [`batch-case-mapping.md`](batch-case-mapping.md) |
| Member/Audit baseline | 🟡 | feature `baseline/` 已建入口与 KMS Member |

## 6. 不可逆操作变更记录

每执行一次 Transfer 或删除，追加一行，并同步更新上文对应表格的「当前状态」。

| 时间 | 操作 | 对象 | 变更前 | 变更后 | 是否已复位 | 执行人 |
|---|---|---|---|---|---|---|
| | | | | | | |

## 7. 待补关键信息（阻塞造数）

| # | 待补项 | 影响范围 | 责任人 | 状态 |
|---|---|---|---|---|
| 1 | 万能验证码是否对任意邮箱生效 | 决定能否自助批量建 15–18 个账号 | | 🟡 对已注册账号已验证有效；新邮箱待验 |
| 2 | 高权限账号有效性与权限范围 | 全部造数动作的前提 | | ✅ 已验证，见 8.2 |
| 3 | t1 / t2 真实租户名与访问权限 | 跨租户对照与 OTA 上线范围用例 | | ✅ t1 已确认；t2 已定位，登录方式待补 |
| 4 | 本 Sprint 功能是否已部署到目标环境 | 造数前提 | | ✅ **已部署，见 8.1** |
| 5 | Figma 完整链接（缺 fileKey） | 勾选框主题色对照 | | ⬜ |
| 6 | 特殊状态资源构造方式 | member-unify 资源状态范围用例 | | ⬜ |
| 7 | 同为 Prod 时「最新」排序口径 | 决定 PROD-1 造几个版本、按什么顺序造 | | ⬜ |

## 8. SIT 环境探查记录

### 8.1 部署状态：已部署 ✅（2026-08-03 以 `feng.zhang` / 雪球租户复核）

| 检查点 | 期望（本 Sprint） | 雪球租户实际 | 结论 |
|---|---|---|---|
| KMS Member 默认列 | Name、Role、Permission、**Organization**、Status | Name、Role、Permission、**Organization**、Status | ✅ 一致，Organization 紧跟 Permission |
| KMS Member Permission 列 | 默认 1 个 Tag + `+n` 折叠 | `View +7` | ✅ 已折叠 |
| KMS Member Organization 列 | 租户简称 | 「雪球」 | ✅ |
| KMS Admin 行操作菜单 | **仅** Transfer Admin | **仅** Transfer Admin | ✅ 一致 |
| Profile Audit 默认列 | Operator、Organization、Operation Type、Operation Time | Operator、Organization、Operation Type、Operation Time | ✅ 一致 |
| Profile Audit Sort | 仅 Operation Time | `Sort ·1` | ✅ 单维度 |

> **重要更正**：2026-07-31 首次探查曾判定「三个 feature 均未部署」，该结论**错误**。根源是当时使用的是浏览器遗留会话 `future.wei@snowballtech.com`（**HW 租户**），该租户下 Member 与 Audit 均为旧规格。改用配置账号 `feng.zhang`（雪球租户）复核后，各检查点均符合本 Sprint 验收标准。
>
> **推论**：新功能疑似按租户灰度，HW 与雪球版本不一致。**执行用例必须固定在雪球租户**，跨租户对照时需注意版本差异可能造成误判。该差异本身也值得向开发确认是否为预期。

### 8.2 账号与租户（`feng.zhang@snowballtech.com` / 张峰）

| 项 | 实际 |
|---|---|
| 租户 | **雪球**（Profile → Basic Information → Tenant） |
| User Role | **System Admin** +3（首位即用例所需的 System Admin） |
| 登录方式 | 邮箱 + 验证码 `111111`，**无需点 Send Code** |
| Operation 模块 | ✅ 可见：Tenant、Role、User (SNB)、DAC Topup |
| System 模块 | ✅ 可见：Language Resources、Parameters |
| Tenant 列表 | 可见全部 **83** 个租户（跨租户视图） |
| Role 列表 | 跨租户可见，含 Tenant 列；类型为 Business Tenant |
| 数据量 | Product 30+、KMS Key 30+（Usage Count 有值），远优于 HW 租户 |

租户定位结果（Tenant 列表共 83 个，无筛选功能，需翻页查找）：

| 代号 | 租户 | 所在页 |
|---|---|---|
| t1 | `雪球(上海雪球信息科技有限公司)` | 第 3 页 |
| t2 | `IKEA(IKEA)` | 第 3 页；另有 `IKEA-test1(IKEA-TEST1)`（第 2 页）、`LEEDARSON(LEEDARSON)`（第 3 页）疑似关联租户 |
| t3 | `HW(HUAWEI)` | 第 2 页；已知用户 `future.wei` |

### 8.3 可直接利用的现成数据

| 数据 | 位置 | 可覆盖用例 |
|---|---|---|
| Member `View +7` | 雪球租户任一 KMS Key → Member | Permission `+n` hover（TP-KMS-L02） |
| Profile Role `+3` | `feng.zhang` My Profile | `+n` hover（TP-PLUS-02） |
| Audit 多条日志 | `feng.zhang` My Profile → Audit | Operator/Organization/Type/Time 齐全，Operator 含肖金栋与张峰两人，Operation Type 含 Join User Group / Join Product / Exit User Group / Edit User，时间跨 2026-06 至 2026-07 → 可覆盖 Profile Audit 与时间排序类用例 |
| `Module_C +2` | HW 租户 Product「A」 | 溢出项仅 2 个，**不足以验证浮层滚动**；雪球租户需另找或新建 |

### 8.4 剩余阻塞项（原 8~11 项已因复核失效，重新登记）

| # | 问题 | 影响 |
|---|---|---|
| 8 | t2（IKEA）尚无可登录用户 | detail-supplement「不上线租户所有 Role 均不配置」2 条 P0 无法执行 |
| 9 | 宜家关联租户范围未确认 | 影响 t2 对照覆盖面（IKEA / IKEA-test1 / LEEDARSON 是否都算） |
| 10 | Role 权限树未成功打开（点击行无响应，需换入口） | OTA / Vulnerability Tab Page 节点是否存在仍待验证 |
| 11 | 雪球租户账号总数与可用性未清点 | 决定 15–18 个测试账号中有多少需要新建 |
