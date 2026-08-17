# Login & Profile — 头像下拉 Tenant 切换 Baseline

> **MeterSphere 模块**：`/Cloud/Login & Profile/My Profile`  
> **Story**：【自注册】001-05 — 企业域名白名单审批管理  
> **关联 TP**：TP-ACCT-ACT-03  
> **截图**：[`screenshots/avatar-tenant-switch.png`](screenshots/avatar-tenant-switch.png)

## 入口

```text
任意 Cloud 页面右上角头像（示例 initials「ZM」）→ 点击展开下拉菜单
```

页头同排可见：**Docs**、**Contact Us**、全屏、语言切换、头像。

## 下拉菜单结构

### 用户信息区

| 字段 | 示例 |
|------|------|
| 姓名 | Zhang Ming |
| 邮箱 | zhangming@example.com |

### Tenant 切换列表

每条展示：`{套餐 Tier} · {Tenant 名称}` + 右侧状态标签（如有）。

| 示例 Tenant | Tier | 状态标签 |
|-------------|------|----------|
| Guomin | Free Tier | **Current**（当前选中） |
| Snow Tech | Enterprise | 无（可切换） |
| SnowBall | Plus | 无（可切换） |
| SnowWave | — | **Pending**（橙色） |
| AutoParts GmbH | — | **Locked**（红色锁图标） |

左侧为彩色圆形图标 + Tenant 首字母。

### 底部操作

| 菜单项 | 说明 |
|--------|------|
| **Profile** | 进入个人资料（人形图标） |
| **Sign Out** | 退出登录 |

## 与本 Story 相关规则（TP-ACCT-ACT-03）

- 域名白名单申请 **Approve 通过**后，申请人再次登录，头像下拉 Tenant 列表中应出现**目标企业 Tenant**（示例形态：`Enterprise · {企业名}`），可点击切换进入。
- Pending / Locked 等状态与套餐标签独立展示；本 Story 关注通过后新增可切换的企业 Tenant。

## 待确认

- Approve 通过后新 Tenant 在列表中的 Tier 展示规则（Enterprise / Free Tier 等）
- 切换 Tenant 后的默认落地页
