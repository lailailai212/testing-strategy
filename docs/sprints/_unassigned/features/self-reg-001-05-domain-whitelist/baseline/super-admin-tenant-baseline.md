# Super Admin — Tenant 域名白名单配置 Baseline

> **MeterSphere 模块**：`/Super Admin Platform/OBIS Biz/Tenant`  
> **Story**：【自注册】001-05 — 企业域名白名单审批管理  
> **关联 TP**：TP-WL-CFG-01、TP-WL-CFG-02、TP-EDGE-WL-01、TP-REG-APP-05/06  
> **截图（Self-Registration OFF）**：[`screenshots/super-admin-tenant-security.png`](screenshots/super-admin-tenant-security.png)  
> **截图（Default Roles 下拉）**：[`screenshots/super-admin-default-roles-dropdown.png`](screenshots/super-admin-default-roles-dropdown.png)

## 入口

```text
Super Admin Platform 左侧边栏 → Tenant（OBIS Biz 下）
→ 选择目标租户 → Tenant Detail Page
面包屑：Home / Tenant Detail Page
```

示例租户：**Future Secure(Future Security)**  
示例 URL：`/system/tenant/{tenantId}`

## Tenant Detail 页 Tab

| Tab | 本 Story 关联 |
|-----|---------------|
| **Basic** | 租户基础信息（本 Story 白名单**不在**此 Tab） |
| **Security** | **Self-Registration**、域名白名单、默认角色、SSO |

页内返回：**`< Future Secure(Future Security)`** 返回租户列表。

> **说明**：域名白名单与默认角色配置在 **Security** Tab（开启 Self-Registration 后展示），非 Basic Tab。

## Security Tab — Self-Registration Settings

### Self-Registration 关闭（OFF）

仅展示 **Self-Registration** 开关（灰色 OFF）。无 Email Domain / Default Roles 字段。  
用户注册侧不展示加入提示（TP-REG-APP-06）。

### Self-Registration 开启（ON）

| 字段 | 控件 | 必填 | 说明 |
|------|------|------|------|
| **Self-Registration** | Toggle | — | ON 后展示下列配置项 |
| **Default Roles** | 下拉 `Please Select` | ✅（红星） | 审批通过后申请人默认成员角色（TP-WL-CFG-01/02） |
| **Registration Method** | 多选标签 | ✅ | 示例已选 **Email** |
| **Email Domain** | 输入框，前缀 `@`，占位 `Please Enter` | ✅ | 域名白名单条目（如 `partner.com`） |

### Default Roles 下拉可选项（TP-WL-CFG-01）

| 选项 |
|------|
| **System Manager** |
| **Product Manager** |
| **Resource Manager** |
| **Factory Manager** |
| **Normal User** |

底部操作：**Cancel**、**Save**

### SSO Settings（同 Tab 下方）

| 字段 | 控件 | 截图状态 |
|------|------|----------|
| Sign In with SSO | Toggle | OFF（灰色） |

## 与本 Story 相关规则

| 规则 | 说明 |
|------|------|
| TP-WL-CFG-01 | 超管在 **Default Roles** 配置/修改审批通过后的默认成员角色 |
| TP-WL-CFG-02 | Approve 时按**审批时刻**白名单中的 Default Roles 分配给申请人 |
| TP-REG-APP-06 | Self-Registration OFF → 注册侧无加入提示 |
| TP-EDGE-WL-01 | Pending 期间修改/删除白名单配置，已落库申请及 Approve/Reject 不变；仅影响新申请 |
| TP-REG-APP-05 | 租户非有效状态不展示提示（状态枚举待确认） |

## 待确认

- [ ] **Email Domain** 是否支持多条域名、编辑/删除已有域名交互
- [ ] Save 后配置生效时延（即时 / 需刷新）
