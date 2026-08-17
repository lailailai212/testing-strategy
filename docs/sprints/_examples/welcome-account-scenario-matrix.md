# Welcome 页测试账号场景矩阵

> 设计依据：仅 **003-02 场景引导** 与 **003-03 工具栏/页头** 存在用户/租户可见规则；**003-04 内容管理** 为配置级启用/禁用，不按角色区分，见 `welcome-content-management.md`  
> Story 链接：[003-02 #7007315100](https://project.feishu.cn/obis/userstory/detail/7007315100) · [003-03](story/obis-7007250530-【自注册】003-03-常驻工具栏与资源中心/) · [003-04 #7007109943](https://project.feishu.cn/obis/userstory/detail/7007109943)

图例：✅ 展示　❌ 不展示　— 恒为 ✅（Story 未写限制）

---

## 可见规则（矩阵设计依据）

| Story | 是否有角色/租户可见规则 | 核心可见规则摘要 |
| --- | --- | --- |
| **003-02 场景引导** | ✅ 有 | 仅自注册 Tenant Admin；邀请成员 / 运营开通 / 升级企业版 → 不展示 |
| **003-03 工具栏/页头** | 部分有 | 仅 Contact Us 按**账号下** Tenant 签约状态；四卡 / Docs / 全屏 / 语言**无可见限制** |

---

## 判定逻辑

**场景引导（003-02）— 四个条件同时满足才展示：**

```text
自注册创建当前 Tenant 的 Tenant Admin（注册者本人）
AND 当前 Tenant 未升级企业版
AND 非运营后台开通 Tenant 下的用户
→ 否则不展示
```

**Contact Us（003-03）— 仅看账号，不看当前 Tenant 上下文：**

```text
账号下全部 Tenant 均未签约 → 展示
账号关联 ≥1 已签约 Tenant → 任何 Tenant 上下文下均不展示
```

**底部四卡 / Docs / 全屏 / 语言（003-03）— 无额外可见规则：**

```text
能进入 Welcome 页 → 均展示（与角色、套餐、签约、升级无关）
```

---

## 主对照表

| 账号场景 | 创建方式 | 角色 | 当前 Tenant 已升级企业 | 账号有已签约 Tenant | 场景引导 | Contact Us | 四卡 / Docs / 全屏 / 语言 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 自注册 Admin，仅个人 Trial，未升级 | 用户自注册 | Tenant Admin（注册者） | 否 | 否 | ✅ | ✅ | — |
| 自注册 Admin，同一 Tenant 已升级企业 | 用户自注册 | Tenant Admin（注册者） | 是 | 是 | ❌ | ❌ | — |
| 自注册 Tenant 下被邀请 Manager | 用户自注册 | Manager | 否 | 否 | ❌ | ✅ | — |
| 自注册 Tenant 下被邀请 Member | 用户自注册 | Member | 否 | 否 | ❌ | ✅ | — |
| 运营后台开通 Tenant 的 Admin | 运营后台开通 | Tenant Admin | 视环境 | 视环境 | ❌ | 视「账号有已签约 Tenant」 | — |
| Mixed：自注册 Admin，上下文切到**个人 Trial**（未升级） | 自注册 + 加入企业 | Tenant Admin | 否 | 是 | ✅ | ❌ | — |
| Mixed：自注册 Admin，上下文切到**企业 Tenant**（已升级） | 自注册 + 加入企业 | Tenant Admin | 是 | 是 | ❌ | ❌ | — |
| 升级对比：同一自注册 Admin / 同一 Tenant（前 → 后） | 用户自注册 | Tenant Admin | 否 → 是 | 否 → 是 | ✅ → ❌ | ✅ → ❌ | — |

> 「四卡 / Docs / 全屏 / 语言」列恒为 **—**（表示 ✅ 且无分叉），Story 003-03 未规定按角色或签约隐藏；内容展示见 003-04 配置启用状态。

---

## 规则引用

### 场景引导列

| 主表行 | 003-02 依据 |
| --- | --- |
| 自注册 Admin，仅个人 Trial | Description「可见范围：仅对注册者本人（Tenant Admin）展示」 |
| 同一 Tenant 已升级企业 | Description「升级企业版后不再展示」；验收「升级企业版后场景引导不再展示」 |
| 被邀请 Manager / Member | Description「被邀请的 Manager / Member 不展示」 |
| 运营后台开通 Admin | Description「运营后台开通的 Tenant 用户不展示」 |
| Mixed · 个人 Trial 上下文 | 注册者 Admin + 当前 Tenant 未升级 → 满足可见条件 |
| Mixed · 企业 Tenant 上下文 | 企业 Tenant 已签约/已升级 → 不满足可见条件 |
| 升级前 → 后 | 上述两条组合验证 |

### Contact Us 列

| 主表行 | 003-03 依据 |
| --- | --- |
| 账号无已签约 Tenant | Description §6「仅当该用户所有租户均为未签约状态时展示」 |
| 账号有已签约 Tenant | Description §6「至少一个已签约租户时，在任何租户上下文下均不展示」；验收「Contact Us 仅在所有租户均未签约时展示」 |
| Mixed · 个人 Trial 上下文 | 虽当前 Tenant 未签约，账号已关联已签约 Tenant → **仍不展示** |
| 运营 Admin | 与创建方式无关，仅按账号签约状态判定 |

### 四卡 / Docs / 页头列

| 说明 | 003-03 依据 |
| --- | --- |
| 无角色/签约/升级限制 | 底部四卡「Welcome 页面底部常驻展示」；页头 Docs / 全屏 / 语言仅描述展示与交互，无隐藏规则 |

---

## 冒烟最小账号集（4 个）

| 账号 | 必须覆盖的规则分叉 |
| --- | --- |
| 自注册 Admin，仅个人 Trial，未升级 | 003-02 ✅ + Contact Us ✅ + 四卡/Docs 主路径 |
| 自注册 Admin，Mixed，个人 Trial 上下文 | Contact Us 全局 ❌（003-03 关键边界）+ 003-02 仍 ✅ |
| 自注册 Admin，Tenant 已升级 | 003-02 ❌ + Contact Us ❌ |
| 被邀请 Manager **或** 运营 Admin | 003-02 ❌（角色 / 创建方式负向） |

---

## 环境与数据前置

| 项 | 说明 |
| --- | --- |
| 003-04 内容 | Quick Start / Manual / FAQ / Downloads 预置生效；分类禁用/空态单独测配置，不依赖账号矩阵 |
| 003-02 状态 | 未开始 / 进行中 / 已完成按领域数据构造（Demo 不计入） |
| 语言 | 四卡/Docs 无可见限制，但需中英文各测 URL/文案；语言入口为页头地球图标 |
| 待确认 | 升级生效时机；切换 Tenant 后默认落地页 |
