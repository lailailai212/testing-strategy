# Story: 【自注册】002-02 — 三路 Demo 预设

**来源**: [飞书项目 User Story #7006975243](https://project.feishu.cn/obis/userstory/detail/7006975243)  
**空间**: OBIS (`obis`)  
**编号**: 576 | **优先级**: Must | **Epic**: OBIS自注册  
**模式**: Large（FM / Vault / PM 三路资源规格 + 标签/配额 + 编辑删除 + 租户隔离 + 真实可用，字段与规则多）

---

## Story AC

1.（AC-01）Factory 预设应创建 1 个 Cloud Factory + 1 个 Programming Station，状态均为 Active。

2.（AC-02）Vault 预设应创建 1 个 KMS 密钥（AES128、TEST 环境）+ 三层 PKI 证书链（PAA/PAI/DAC，Matter 规范，有效期 2 年）。

3.（AC-03）Product 预设应创建 1 个 Demo Product（Testing 环境、Matter 规范），含固件 / Chip Config（Silicon Labs EFR32MG24）/ Key 引用 / 证书引用 / Matter Config，以及默认 Module 与 Version（**Version 默认 Approved**，以评论为准）。

4.（AC-04）Demo 资源在列表展示 Demo 标签，不展示环境标签，且不计入配额和用量统计。

5.（AC-05）创建失败时按规则回滚已创建的资源。

6.（AC-06）用户可删除 Demo 资源，删除后系统不重建。

7.（AC-07）用户可编辑 Demo 产品的非核心字段。

8.（AC-08）Demo 数据按租户独立创建，各租户互不共享。

9.（AC-09）Demo 数据可被真实使用（如用预设密钥签发证书、用预设工厂创建批次），功能不做限制。

10.（AC-10）Demo 数据编辑/删除后的效果与用户自创建资源一致。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号；否则填 `需求描述` 或 `QA扩展`。  
> **优先级口径**：P0 = 冒烟/阻断主路径（每条 AC 至少 1 条）；P1 = 重要字段与回归；P2 = 细项规格与边缘。  
> **评论已合并**：Description 字段去掉；Demo 标签仅列表页；固件为真实可烧录文件；Allowed Range Max=30、Default Duration=30；Version=Approved。

### Factory Demo 预设

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-FM-01 | AC-01 | P0 | 自注册 Tenant 预设成功后，存在 1 个 Cloud Factory（名称 `TestCloudFactory`），状态 Active |
| TP-FM-02 | AC-01 | P0 | 该 Factory 下存在 1 个 Programming Station（名称 `TestStation`），状态 Active，登录方式为密码 |
| TP-FM-03 | 需求描述 | P1 | Factory 类型为云工厂（cloud）；管理员为租户 Admin 账号；API 密钥由系统自动生成 |
| TP-FM-04 | 需求描述 | P2 | Factory / Station 创建时间、同步时间为预设完成时刻（年月日时分秒） |

### Vault Demo 预设 — KMS

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-VAULT-KMS-01 | AC-02 | P0 | 预设成功后存在 1 个 KMS 密钥：名称 `TestKey`，环境 Test，对称密钥，规范 AES128 |
| TP-VAULT-KMS-02 | 需求描述 | P1 | 密钥用途包含加密解密、生成并验证 MAC；有效期 2 年；生成方式为系统生成 |
| TP-VAULT-KMS-03 | 需求描述 | P1 | Tenant Admin 对该 Demo 密钥拥有所有权限 |

### Vault Demo 预设 — PKI 证书链

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-VAULT-PKI-01 | AC-02 | P0 | 预设成功后存在三层证书链：PAA（`Test PAA`）+ PAI（`Test PAI`）+ DAC 模板（`Test DAC`），均为 Matter 规范、状态 Active |
| TP-VAULT-PKI-02 | AC-02 | P1 | PAA / PAI / DAC 有效期均为 2 Years；算法 ECC-P256；签名算法 ecdsa-with-SHA256 |
| TP-VAULT-PKI-03 | 需求描述 | P1 | PAA 类型为 Test PAA（非认证 PAA）；DAC 的 PID 为 8001 |
| TP-VAULT-PKI-04 | 需求描述 | P2 | Tenant Admin 对 Demo PAA / PAI / DAC 拥有所有权限 |
| TP-VAULT-PKI-05 | QA扩展 | P2 | Demo PAA 为租户自签名测试 PAA，不可当作 SNOWBALL 官方认证 PAA 用于生产环境（能力/标识层面可区分） |

### Product Demo 预设

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PM-PROD-01 | AC-03 | P0 | 预设成功后存在 1 个产品 `Demo-Product`：Specification=Matter，状态 Released，环境 Testing |
| TP-PM-PROD-02 | AC-03 | P0 | 产品含默认 Module（Module1）与 Version（`Demo-Version-v1.0`），Version 状态为 **Approved** |
| TP-PM-PROD-03 | AC-03 | P1 | 产品资源包含：固件 `Demo-Firmware-v1.0`（Type: Application）、Chip Config `Demo-Chip-Config-v1`（Silicon Labs / EFR32MG24 / EFR32MG24B210F1536IM48）、Key 引用 Demo KMS、证书引用 Demo DAC、Matter Config、PS Software |
| TP-PM-PROD-04 | 需求描述 | P1 | Max Production Volume=Limited 500；Allowed Range Min=1、Max=30；Default Duration=30；Vendor=SNB |
| TP-PM-PROD-05 | 需求描述 | P1 | 用户从列表进入产品详情默认进入 Test 环境，且可切换环境 |
| TP-PM-PROD-06 | 需求描述 | P2 | Matter Config：PID=8001，DAC Template=Demo DAC，Spike2Iteration=1000，Commissioning Flow=Standard，设备发现模式=BLE |
| TP-PM-PROD-07 | 需求描述 | P2 | 固件为真实可烧录文件（非占位空文件） |
| TP-PM-PROD-08 | 需求描述 | P2 | 创建产品流程无 Description 字段/填写入口 |

### Demo 标签、环境标签与配额

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-DEMO-TAG-01 | AC-04 | P0 | Factory / Vault / Product 等相关**列表页**对 Demo 资源展示「Demo Data / 测试数据」或 `Demo-` 标识 |
| TP-DEMO-TAG-02 | AC-04 | P1 | Demo 资源列表不展示环境标签（Test / 正式等），仅标识为 Demo 数据 |
| TP-DEMO-TAG-03 | 需求描述 | P1 | 产品/资源**详情页**不展示「Demo Data / 测试数据」标签（以评论修订为准） |
| TP-DEMO-TAG-04 | AC-04 | P0 | Demo 资源不计入配额和用量统计（与用量可视化等模块交叉验证） |

### 失败回滚

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-ROLL-01 | AC-05 | P0 | Cloud Factory 创建成功但 Station 创建失败时，回滚已创建的 Factory，该路记为失败 |
| TP-ROLL-02 | AC-05 | P1 | KMS 密钥创建成功但 PKI 链创建失败时，回滚已创建的 KMS 密钥，该路记为失败 |
| TP-ROLL-03 | AC-05 | P1 | PKI 链创建中途失败时，回滚已创建的 CA 证书，该路记为失败 |
| TP-ROLL-04 | AC-05 | P1 | Product 创建成功但资源包失败，或资源包成功但 Version 失败时，回滚已创建的 Product（及资源包），该路记为失败 |
| TP-ROLL-05 | 需求描述 | P2 | 单路重试 3 次均失败后，记录该路失败结果（编排层行为与 002-01 对齐） |

### 编辑、删除与真实使用

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-DEMO-ACT-01 | AC-06 | P0 | 用户可删除 Demo 产品内单个资源；删除后系统不重建 |
| TP-DEMO-ACT-02 | AC-06 | P1 | 用户可删除整个 Demo 产品；删除后系统不重建 |
| TP-DEMO-ACT-03 | AC-07 | P0 | 用户可编辑 Demo 产品的非核心字段，保存成功且详情展示更新后内容 |
| TP-DEMO-ACT-04 | AC-10 | P0 | 对 Demo 资源的编辑/删除效果与用户自创建资源一致（权限、校验、列表刷新等） |
| TP-DEMO-ACT-05 | AC-09 | P0 | 可使用预设 Demo KMS 密钥完成真实签发类操作（功能不做额外限制） |
| TP-DEMO-ACT-06 | AC-09 | P1 | 可使用预设 Demo Factory / Station 创建批次等真实业务流程 |
| TP-DEMO-ACT-07 | QA扩展 | P2 / 待确认 | 「非核心字段」可编辑范围清单（Description 已去掉后）与产品确认一致 |

### 租户隔离

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-DEMO-ISO-01 | AC-08 | P0 | 租户 A 仅能看到本租户 Demo 数据，不能看到租户 B 的 Demo Factory / Key / PKI / Product |
| TP-DEMO-ISO-02 | AC-08 | P1 | 两个自注册 Tenant 各自拥有独立的 Demo PAA/PAI/DAC 与密钥，互不共享同一证书链 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点（含 P0） | 覆盖状态 |
|----------|---------------------|----------|
| AC-01 Factory + Station Active | TP-FM-01（P0）；TP-FM-02（P0） | ✅ |
| AC-02 KMS + 三层 PKI | TP-VAULT-KMS-01（P0）；TP-VAULT-PKI-01（P0） | ✅ |
| AC-03 Demo Product + 资源 + Approved Version | TP-PM-PROD-01（P0）；TP-PM-PROD-02（P0） | ✅ |
| AC-04 列表 Demo 标签、无环境标签、不计配额 | TP-DEMO-TAG-01（P0）；TP-DEMO-TAG-04（P0） | ✅ |
| AC-05 失败按规则回滚 | TP-ROLL-01（P0） | ✅ |
| AC-06 可删除且不重建 | TP-DEMO-ACT-01（P0） | ✅ |
| AC-07 可编辑非核心字段 | TP-DEMO-ACT-03（P0） | ✅ |
| AC-08 租户独立不共享 | TP-DEMO-ISO-01（P0） | ✅ |
| AC-09 可被真实使用 | TP-DEMO-ACT-05（P0） | ✅ |
| AC-10 编辑删除效果与自建一致 | TP-DEMO-ACT-04（P0） | ✅ |

**AC-01～AC-10 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| Factory Demo 预设 | 2 | 1 | 1 | 4 |
| Vault Demo 预设 — KMS | 1 | 2 | 0 | 3 |
| Vault Demo 预设 — PKI 证书链 | 1 | 2 | 2 | 5 |
| Product Demo 预设 | 2 | 3 | 3 | 8 |
| Demo 标签、环境标签与配额 | 2 | 2 | 0 | 4 |
| 失败回滚 | 1 | 3 | 1 | 5 |
| 编辑、删除与真实使用 | 3 | 2 | 1 | 6 |
| 租户隔离 | 1 | 1 | 0 | 2 |
| **合计** | **13** | **16** | **8** | **37** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 24 |
| 需求描述 | 11 |
| QA 扩展 | 2 |

---

## 待确认

- [ ] AC-03 原文「Draft Version」与评论「Approved」冲突，测试点已按评论 **Approved** 执行；需产品同步正式 AC 文案。
- [ ] Description 去掉后，「非核心字段」具体可编辑清单未完整定义。
- [ ] 评论附图（创建产品无 Description 入口）因飞书附件下载未启用未能本地化，不影响测试点结论。

## Out of Scope

- Demo 预设编排触发、重试次数与运营开通排除（归属 002-01）
- 联系销售 / 升级付费流程
- 配额触达拦截弹窗本身（仅交叉验证 Demo 不计配额）
