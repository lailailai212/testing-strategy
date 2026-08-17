# Login — 域名白名单加入提示弹窗 Baseline

> **MeterSphere 模块**：`/Cloud/Login & Profile/Login`  
> **Story**：【自注册】001-05 — 企业域名白名单审批管理  
> **关联 TP**：TP-REG-APP-01～06、TP-REG-DOM-01/02、TP-REG-POST-01/02、TP-EDGE-REG-01/02、TP-MAIL-06  
> **截图**：[`screenshots/login-whitelist-join-prompt.png`](screenshots/login-whitelist-join-prompt.png)

## 触发前提（TP-REG-APP-01）

- 目标租户为**有效状态**
- 超管已在 Tenant Detail **Security** Tab 开启 **Self-Registration** 并配置 **Email Domain** 白名单
- 用户**无有效 OBIS 账号**，注册邮箱域名命中白名单
- **首次**进入注册/登录完成流程时展示

不展示场景：已有有效账号（TP-REG-APP-04）、租户非有效（TP-REG-APP-05）、未开启白名单（TP-REG-APP-06）、子域名不匹配（TP-REG-DOM-01）等。

## 弹窗文案（英文，与 UI 一致）

| 元素 | 文案 | 说明 |
|------|------|------|
| 主标题 | **Your email belongs to {企业名}** | 示例：`Your email belongs to Snow Tech` |
| 说明正文 | Would you like to join this enterprise? Joining grants access to the enterprise's products and resources. You can also continue with your own trial OBIS workspace without joining. | 居中灰色正文 |
| 次按钮 | **Skip&Enter System** | 白底描边；对应「跳过」 |
| 主按钮 | **Apply to Join** | 深蓝底白字；对应「申请加入」 |

## 按钮行为

| 操作 | 预期（Story） |
|------|----------------|
| **Apply to Join** | 提交加入申请；展示已提交、可先使用免费版提示（TP-REG-APP-02）；通知 Tenant Admin 邮件（TP-MAIL-01）；不向申请人发邮件（TP-MAIL-06） |
| **Skip&Enter System** | 不提交申请；进入个人 trial OBIS workspace；再次登录不再展示该企业提示（TP-REG-APP-03） |

## Apply to Join 提交成功页（TP-REG-APP-02）

**截图**：[`screenshots/login-application-submitted.png`](screenshots/login-application-submitted.png)

| 元素 | 文案 | 说明 |
|------|------|------|
| 图标 | 绿色勾选 + 同心圆光环 | 成功态 |
| 主标题 | **Application Submitted!** | |
| 正文 | Your application has been sent to the {企业名} enterprise administrator for review. Once approved, the enterprise will appear in your avatar dropdown menu. You don't need to wait — you can start using the trial OBIS now. | 示例：`Snow Tech` |
| 主按钮 | **Enter Trail** | UI 原文（与正文 trial OBIS 对应） |

## 与测试点对照

| TP-ID | 验证点 |
|-------|--------|
| TP-REG-APP-02 | Apply to Join 后展示 **Application Submitted!** 成功页 |
| TP-REG-POST-01/02 | 被拒后仍可试用；再次登录不重复提示 |
| TP-REG-DOM-02 | `user@Example.COM` 与 `user@example.com` 均命中同一白名单域名 |

## 待确认

- [ ] 完整注册流程入口步骤（注册页 → 验证码 → 加入提示弹窗 → 成功页）
