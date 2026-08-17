# Story: 【自注册】006-01 — 免费版事务邮件触达

**来源**: [飞书项目 User Story #7007422975](https://project.feishu.cn/obis/userstory/detail/7007422975)  
**空间**: OBIS (`obis`)  
**编号**: 588 | **优先级**: Must | **Epic**: OBIS自注册  
**模式**: Large（Welcome / 首次 DAC / 首次烧录三类触发 + 排除规则 + 双语变量 + 失败重试 + 升级企业 / 自建产品混用 Demo，跨模块且规则 > 10）  
**同步**: 2026-07-14 评论 — 告警暂不做；升级企业后不发 DAC/烧录邮件；自建产品混用 Demo 资产首次烧录仍发邮件

---

## Story AC

1.（AC-01）自注册 Tenant 创建成功后，系统向 Tenant 创建者发送 Welcome 邮件，且同一 Tenant 仅发送 1 次。

2.（AC-02）首条真实终端实体 DAC 证书签发成功后（非 Demo），系统发送首次 DAC 签发邮件，且同一 Tenant 仅发送 1 次。

3.（AC-03）首条真实 Production Record 生成后，系统发送首次产品烧录邮件，且同一 Tenant 仅发送 1 次。

4.（AC-04）三类事务邮件均为 HTML 中英文双语模板，发件人/主题符合规格，变量替换正确。

5.（AC-05）Demo 资源相关的签发 / 烧录不触发任何事务邮件（自建产品混用 Demo 资产的首次烧录除外，见需求描述澄清）。

6.（AC-06）邮件发送失败时后台重试 3 次（间隔 5 分钟），且不阻塞业务流程；本迭代不做 Operator 告警。

7.（AC-07）运营后台开通的 Tenant 不触发任何事务邮件（Welcome / DAC / 烧录均不发）。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### Welcome 邮件 — 触发与去重

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-WEL-01 | AC-01 | P0 | 自注册流程中 Account 创建完毕且 Tenant 创建成功后，系统向 Tenant 创建者邮箱发送 Welcome 邮件 |
| TP-MAIL-WEL-02 | AC-01 | P0 | 同一自注册 Tenant 仅发送 1 封 Welcome 邮件；重复触发创建成功事件不重复发送 |
| TP-MAIL-WEL-03 | 需求描述 | P0 | Welcome 邮件仅发送给 Tenant 创建者邮箱，不发送给同 Tenant 下其他成员 |
| TP-MAIL-WEL-04 | AC-01, QA扩展 | P0 | 注册邮箱**命中企业域名白名单**时，用户仍创建个人 trial/免费版 Tenant（Apply to Join 或 Skip&Enter System 均可）；Tenant 创建成功后仍向该创建者发送 Welcome（与是否同时提交企业加入申请无关；001-05 企业 Admin 申请通知不在本点范围） |

### 首次 DAC 签发邮件 — 触发与去重

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-DAC-01 | AC-02 | P0 | 自注册 Tenant 下首条真实终端实体 DAC 证书经 Vault 签发成功后，系统发送首次 DAC 签发邮件 |
| TP-MAIL-DAC-02 | AC-02 | P0 | 同一 Tenant 仅发送 1 封首次 DAC 签发邮件；后续再次签发真实 DAC 不重复发送 |
| TP-MAIL-DAC-03 | 需求描述 | P0 | 首次 DAC 签发邮件仅发送给 Tenant 创建者邮箱 |
| TP-MAIL-DAC-04 | AC-02, QA扩展 | P0 | 真实 DAC 签发**业务失败**不占用「首次成功」额度；失败后再次签发成功时仍发送首次 DAC 邮件，且同一 Tenant 仅 1 次 |
| TP-MAIL-DAC-05 | 需求描述, AC-02 | P0 | 非 Tenant 创建者（如 Manager / Member）完成首条真实 DAC 签发时，仍仅向 **Tenant 创建者**发送首次 DAC 邮件；操作者本人不收到 |

### 首次产品烧录邮件 — 触发与去重

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-FLASH-01 | AC-03 | P0 | 自注册 Tenant 下首条真实 Production Record 生成后，系统发送首次产品烧录邮件 |
| TP-MAIL-FLASH-02 | AC-03 | P0 | 同一 Tenant 仅发送 1 封首次烧录邮件；后续再次生成真实 Production Record 不重复发送 |
| TP-MAIL-FLASH-03 | 需求描述 | P0 | 首次烧录邮件仅发送给 Tenant 创建者邮箱 |
| TP-MAIL-FLASH-04 | AC-03, QA扩展 | P0 | 真实烧录 / Production Record 生成**业务失败**不占用「首次成功」额度；失败后再次烧录成功时仍发送首次烧录邮件，且同一 Tenant 仅 1 次 |
| TP-MAIL-FLASH-05 | 需求描述, AC-03 | P0 | 非 Tenant 创建者（如 Manager / Member）完成首条真实烧录时，仍仅向 **Tenant 创建者**发送首次烧录邮件；操作者本人不收到 |

### 触发排除规则

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-EXCL-01 | AC-05 | P0 | Demo 资源相关的 DAC 签发成功时，不发送首次 DAC 签发邮件，也不发送其他事务邮件 |
| TP-MAIL-EXCL-02 | AC-05 | P0 | Demo 预设产品 / 纯 Demo 烧录路径下 Production Record 生成时，不发送首次烧录邮件，也不发送其他事务邮件 |
| TP-MAIL-EXCL-03 | AC-05, AC-02 | P0 | 同一 Tenant 先发生 Demo 签发/烧录，再首次发生真实 DAC 签发时，仍应发送首次 DAC 签发邮件（Demo 不占用「首次」额度） |
| TP-MAIL-EXCL-04 | AC-05, AC-03 | P0 | 同一 Tenant 先发生 Demo 烧录，再首次生成真实 Production Record 时，仍应发送首次烧录邮件 |
| TP-MAIL-EXCL-05 | AC-07 | P0 | 运营后台开通的 Tenant 创建成功后，不发送 Welcome 邮件 |
| TP-MAIL-EXCL-06 | AC-07 | P0 | 运营后台开通的 Tenant 发生真实 DAC 签发 / 真实 Production Record 时，不发送首次 DAC / 首次烧录邮件 |
| TP-MAIL-EXCL-07 | 需求描述 | P0 | 自注册账户升级为企业后，再签发 DAC 不发送首次 DAC 签发邮件 |
| TP-MAIL-EXCL-08 | 需求描述 | P0 | 自注册账户升级为企业后，再完成首次烧录不发送首次烧录邮件 |
| TP-MAIL-EXCL-09 | 需求描述, AC-03, AC-05 | P0 | 用户第一个自建产品内使用了 demo key / demo cert / demo factory 数据时，完成第一次烧录仍发送首次烧录邮件 |
| TP-MAIL-EXCL-10 | AC-01, QA扩展 | P0 | **邀请加入自注册 Tenant**：被邀请人接受邀请成为成员时，不向被邀请人发送 Welcome；其亦非 DAC/烧录事务邮件收件人（收件人仍为该 Tenant 创建者） |
| TP-MAIL-EXCL-11 | AC-07, QA扩展 | P0 | **邀请加入非自注册 Tenant**（运营开通/企业等）：被邀请人接受邀请不触发 Welcome；在该 Tenant 上下文下真实 DAC 签发 / 真实烧录均不发送 006-01 事务邮件 |
| TP-MAIL-EXCL-12 | 需求描述, AC-03, QA扩展 | P0 | 自注册账户经**超管页面切回免费版**后，在免费版状态下完成**首次**真实烧录应发送首次烧录邮件（企业版期间的烧录不发信，不占用切回后免费版「首次」额度） |

### 邮件内容 — 公共规格

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-FMT-01 | AC-04 | P0 | 三类邮件发件人名称均为 `Snowball OBIS`，发件人地址均为 `noreply@snowballtech.com` |
| TP-MAIL-FMT-02 | AC-04 | P0 | 三类邮件均为 HTML 格式，正文含 OBIS Logo 与品牌色 |
| TP-MAIL-FMT-03 | AC-04 | P0 | 三类邮件正文同时包含英文与中文内容（双语模板） |
| TP-MAIL-FMT-04 | AC-04, 需求描述 | P0 | 三类邮件中的链接（`welcome_url` / `cert_url` / `record_url`）均为可访问的 OBIS 登录相关链接 |
| TP-MAIL-FMT-05 | AC-04 | P0 | `{name}` 变量替换为用户注册姓名，中英文称呼处均正确 |

### 邮件内容 — Welcome

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-WEL-CNT-01 | AC-04 | P0 | Welcome 邮件主题为：`Welcome to OBIS! Let's Get Started` |
| TP-MAIL-WEL-CNT-02 | AC-04 | P0 | Welcome 英文正文含评价租户就绪说明，以及 Complete first DAC signing / Try secure factory flash / Explore the docs 三项引导，含 Get Started 链接 |
| TP-MAIL-WEL-CNT-03 | AC-04 | P0 | Welcome 中文正文含免费版企业就绪说明，以及完成首次 DAC 签发 / 体验安全烧录 / 查阅操作文档三项引导，含「立即开始」链接 |

### 邮件内容 — 首次 DAC 签发

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-DAC-CNT-01 | AC-04 | P0 | 首次 DAC 邮件主题为：`Great Work! Your First DAC Certificate Has Been Issued` |
| TP-MAIL-DAC-CNT-02 | AC-04 | P0 | 首次 DAC 邮件证书信息变量正确：`{cert_type}` 为 DAC、`{issue_time}` 为 ISO 8601 UTC、`{serial_number}` 为十六进制序列号 |
| TP-MAIL-DAC-CNT-03 | AC-04 | P0 | 首次 DAC 邮件含「View Certificate / 查看证书」链接，指向证书相关 OBIS 入口 |

### 邮件内容 — 首次产品烧录

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-FLASH-CNT-01 | AC-04 | P0 | 首次烧录邮件主题为：`Production Milestone! Your First Device Has Been Flashed` |
| TP-MAIL-FLASH-CNT-02 | AC-04 | P0 | 首次烧录邮件生产信息变量正确：`{product_name}`、`{batch_name}`、`{flash_time}`（ISO 8601 UTC）与实际 Production Record 一致 |
| TP-MAIL-FLASH-CNT-03 | AC-04 | P0 | 首次烧录邮件含「View Production Records / 查看生产记录」链接，指向生产记录相关 OBIS 入口 |

### 并发与组合场景

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-COMBO-01 | 需求描述 | P0 | Matter module 场景下，首次烧录同时意味着首次 DAC 签发成功时，用户在烧录成功那一刻收到两封邮件（首次 DAC + 首次烧录），此为期望行为 |
| TP-MAIL-COMBO-02 | QA扩展 | P1 | 同一 Tenant 按顺序完成 Welcome → 首次真实 DAC → 首次真实烧录，三类邮件均各收到 1 封，互不影响去重计数 |
| TP-MAIL-COMBO-03 | QA扩展 | P1 | 自注册 Tenant 已发送 Welcome 后，运营侧对该 Tenant 的其他操作不导致 Welcome 再次发送 |

### 发送失败 — 重试（告警本迭代不做）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-RETRY-01 | AC-06 | P0 | 任一事务邮件首次发送失败后，系统后台按间隔 5 分钟重试，最多共重试 3 次 |
| TP-MAIL-RETRY-02 | AC-06 | P0 | 重试过程中某次发送成功，则停止后续重试 |
| TP-MAIL-RETRY-03 | AC-06 | P0 | 3 次重试均失败后，停止重试；本迭代**不要求**向 Operator 告警（可记录日志，以实现对齐） |
| TP-MAIL-RETRY-04 | AC-06 | P0 | 邮件发送失败（含重试中 / 最终失败）不阻塞 Tenant 创建、DAC 签发、Production Record 生成等业务流程 |

### 边界与负向（QA 扩展）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MAIL-NEG-01 | QA扩展 | P1 | Tenant 创建者邮箱无效 / 不可达时，仍按重试策略处理，最终失败不阻塞业务主流程（本迭代不验 Operator 告警） |
| TP-MAIL-NEG-02 | QA扩展 | P1 | 真实 DAC 签发失败时，不发送首次 DAC 签发邮件（失败后再次成功见 TP-MAIL-DAC-04） |
| TP-MAIL-NEG-03 | QA扩展 | P1 | Production Record 生成失败时，不发送首次烧录邮件（失败后再次成功见 TP-MAIL-FLASH-04） |
| TP-MAIL-NEG-04 | QA扩展 | P2 | 邮件正文时间戳时区展示为 UTC（ISO 8601），与系统记录一致 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Welcome 按 Tenant 仅 1 次 | TP-MAIL-WEL-01；TP-MAIL-WEL-02；TP-MAIL-WEL-04；TP-MAIL-EXCL-10 | ✅ |
| AC-02 首次真实 DAC 签发邮件 | TP-MAIL-DAC-01；TP-MAIL-DAC-02；TP-MAIL-DAC-04；TP-MAIL-DAC-05；TP-MAIL-EXCL-03 | ✅ |
| AC-03 首次真实烧录邮件 | TP-MAIL-FLASH-01；TP-MAIL-FLASH-02；TP-MAIL-FLASH-04；TP-MAIL-FLASH-05；TP-MAIL-EXCL-04；TP-MAIL-EXCL-09；TP-MAIL-EXCL-12 | ✅ |
| AC-04 双语模板与变量替换 | TP-MAIL-FMT-01～05；TP-MAIL-WEL-CNT-01～03；TP-MAIL-DAC-CNT-01～03；TP-MAIL-FLASH-CNT-01～03 | ✅ |
| AC-05 Demo 不触发 | TP-MAIL-EXCL-01；TP-MAIL-EXCL-02；TP-MAIL-EXCL-03；TP-MAIL-EXCL-04；TP-MAIL-EXCL-09（澄清边界） | ✅ |
| AC-06 失败重试 3 次 / 不阻塞（告警暂不做） | TP-MAIL-RETRY-01～04 | ✅ |
| AC-07 运营开通 Tenant 不触发 | TP-MAIL-EXCL-05；TP-MAIL-EXCL-06；TP-MAIL-EXCL-11 | ✅ |

**AC-01～AC-07 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| Welcome 触发与去重 | 4 | 0 | 0 | 4 |
| 首次 DAC 触发与去重 | 5 | 0 | 0 | 5 |
| 首次烧录触发与去重 | 5 | 0 | 0 | 5 |
| 触发排除规则 | 12 | 0 | 0 | 12 |
| 邮件内容公共规格 | 5 | 0 | 0 | 5 |
| Welcome 内容 | 3 | 0 | 0 | 3 |
| DAC 内容 | 3 | 0 | 0 | 3 |
| 烧录内容 | 3 | 0 | 0 | 3 |
| 并发与组合 | 1 | 2 | 0 | 3 |
| 发送失败重试 | 4 | 0 | 0 | 4 |
| 边界与负向 | 0 | 3 | 1 | 4 |
| **合计** | **45** | **5** | **1** | **51** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 40 |
| 需求描述 | 7 |
| QA 扩展 | 4 |

---

## 待确认

- [x] Operator 告警 — **本迭代不做**（评论 2026-07-14）；后续统一规划后再补测
- [x] 升级企业后 DAC / 烧录不发邮件 — 已确认（评论 2026-07-14）
- [x] 自建产品混用 demo key/cert/factory 首次烧录仍发邮件 — 已确认（评论 2026-07-14）
- [ ] 「所有的链接均为 OBIS 登录链接」与各邮件 CTA 落地页是否统一为登录页，还是登录后深链——建议联调确认
- [x] Demo 资源判定口径 — 已对齐 [002-02 三路 Demo 预设](https://project.feishu.cn/obis/userstory/detail/7006975243)：系统标签 `demo`；列表展示 `Demo-` /「Demo Data / 测试数据」；Vault/PKI 环境为 Test/TEST；Product 为 Testing；典型资源 TestKey / Test PAA·PAI·DAC（Matter）/ Demo-Product / TestCloudFactory；不计入配额
- [x] **企业版切回免费版**：路径在**超管页面**；切回后免费版首次真实烧录应发（企业版期间烧录不占额度）（2026-07-16 确认路径；发信规则见 EXCL-12）
- [ ] 命中白名单时 Apply / Skip 两条路径是否均完成个人 trial Tenant 创建并触发 Welcome（与 001-05 对齐，本 Story 只验 Welcome）

## Out of Scope

- 付费版 / 非自注册路径的营销类邮件
- 邮件模板可视化编辑后台
- 非 Tenant 创建者角色的订阅偏好设置
- 邮件打开率 / 点击率等运营统计
- **本迭代**：邮件发送最终失败后的 Operator 告警
