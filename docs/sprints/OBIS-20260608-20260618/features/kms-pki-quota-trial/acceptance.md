# Story: 【自注册】004-02 — KMS 与 PKI 配额限制（自注册免费版）

**来源**: [飞书项目 User Story #7007200385](https://project.feishu.cn/obis/story/detail/7007200385)  
**空间**: OBIS (`obis`)  
**编号**: 582 | **优先级**: Must | **Epic**: OBIS自注册  
**模式**: Large（KMS + PKI 双模块配额与有效期校验，AC = 8）

---

## Story AC

1.（AC-01）点击创建密钥时校验密钥数量 ≥ 5，超限弹出简单提示并阻断，不打开创建页面。

2.（AC-02）创建/编辑密钥时有效期 ≤ 2 年，支持按年限和按日期两种模式。

3.（AC-03）密钥有效期失焦校验，> 2 年时显示对应错误提示。

4.（AC-04）点击 Create Certificate 时校验每类模板 ≥ 2，超限弹出简单提示并阻断，不打开创建页面。

5.（AC-05）创建证书时有效期 ≤ 2 年，支持按年和按日期两种模式（本版本不支持编辑证书）。

6.（AC-06）证书有效期失焦校验，> 2 年时显示对应错误提示。

7.（AC-07）仅已销毁 / Deleted 状态的密钥和证书模板不计入配额统计；其余状态（含 Active、Revoked、Expired 等）均计入。

8.（AC-08）Demo 资源不计入配额统计（**自注册租户无 Demo/预设数据，本 Story 不测**）。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### KMS — 密钥数量配额

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-KMS-CNT-01 | 需求描述 | P0 | 新注册自注册租户 KMS 无预设 default key，列表初始为空；首次点击「+ Create Key」直接打开创建页，不弹提示 |
| TP-KMS-CNT-02 | QA扩展 | P0 | 自注册免费版租户已有 4 个计入配额密钥，点击「+ Create Key」打开创建页，不弹提示 |
| TP-KMS-CNT-03 | AC-01 | P0 | 自注册免费版租户已有 5 个计入配额密钥，点击「+ Create Key」弹出简单提示并阻断，不打开创建页 |
| TP-KMS-CNT-04 | AC-07 | P1 | 5 个密钥含 1 个 Deleted，点击创建应打开创建页（Deleted 不计入配额） |
| TP-KMS-CNT-05 | AC-07 | P1 | Active、Revoked、Expired 等状态均计入配额；合计达 5 时触发数量上限提示 |

### KMS — 密钥有效期

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-KMS-VAL-01 | 需求描述 | P0 | 创建密钥页，有效期类型 Unlimited / 无限制 不可见 |
| TP-KMS-VAL-02 | AC-02 | P0 | 按年限模式：输入 ≤ 2 年，失焦无错误，点击 Next 可进入下一步 |
| TP-KMS-VAL-03 | AC-03 | P0 | 按年限模式：输入 > 2 年，失焦显示 Trial max validity is 2 years / 免费版有效年限最长 2 年 |
| TP-KMS-VAL-04 | AC-02 | P0 | 按日期模式：选择 ≤ 当前+2 年，失焦无错误，点击 Next 可提交 |
| TP-KMS-VAL-05 | AC-03 | P0 | 按日期模式：选择 > 当前+2 年，失焦显示同上错误提示 |
| TP-KMS-VAL-06 | AC-02 | P0 | 失焦通过后提交前改为超限值，点击 Next 再次校验并阻止提交 |
| TP-KMS-VAL-07 | AC-02 | P1 | 编辑密钥时修改有效期超过 2 年，失焦与保存/下一步均校验并阻止 |
| TP-KMS-VAL-08 | QA扩展 | P1 | 按年限边界：恰好 2 年通过；2.1 年或 3 年报错 |

### PKI — 根证书数量配额（+ Create Root Cert）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PKI-CNT-01 | 需求描述 | P0 | 新注册自注册租户 PKI 无系统预设证书模板，根证书列表初始为空；首次点击「+ Create Root Cert」直接打开创建页 |
| TP-PKI-ROOT-01 | QA扩展 | P0 | 租户下计入配额的根证书合计 1 个（任意 Specification），点击「+ Create Root Cert」应打开创建页 |
| TP-PKI-ROOT-02 | AC-04 | P0 | 租户下计入配额的根证书合计达 2 个（不论 Specification 为 Matter / Google Cast / Custom），点击「+ Create Root Cert」弹出简单提示并阻断，不打开创建页 |
| TP-PKI-ROOT-03 | 需求描述 | P0 | 租户下已有 2 个根证书且分属不同 Specification（如 1 个 Matter + 1 个 Custom），点击「+ Create Root Cert」仍触发上限弹窗 |
| TP-PKI-CNT-03 | AC-07 | P1 | 租户下根证书含 1 个 Deleted 与 1 个 Active，合计按 1 个计入配额；未达 2 时点击「+ Create Root Cert」可打开创建页 |
| TP-PKI-ROOT-04 | AC-07 | P1 | 租户下根证书含 Active、Revoked、Expired 等非 Deleted 状态合计达 2，点击「+ Create Root Cert」触发上限阻断 |

### PKI — 中级/设备证书数量配额

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PKI-MID-01 | AC-04 | P0 | 租户下计入配额的中级证书合计达 2 个，创建中级证书时应弹提示并阻断 |
| TP-PKI-MID-02 | AC-07 | P1 | 中级证书含 1 个 Deleted 与 1 个 Active，合计按 1 计入配额；未达 2 时可打开创建页 |
| TP-PKI-MID-03 | AC-07 | P1 | 中级证书 Active、Revoked、Expired 等非 Deleted 状态合计达 2，创建中级证书触发上限阻断 |
| TP-PKI-DEV-01 | AC-04 | P0 | 租户下计入配额的设备证书模板合计达 2 个，创建设备证书模板时应弹提示并阻断 |
| TP-PKI-DEV-02 | AC-07 | P1 | 设备证书模板含 1 个 Deleted 与 1 个 Active，合计按 1 计入配额；未达 2 时可打开创建页 |
| TP-PKI-DEV-03 | AC-07 | P1 | 设备证书模板 Active、Revoked、Expired 等非 Deleted 状态合计达 2，创建设备证书模板触发上限阻断 |

### PKI — 证书有效期（仅创建；本版本不支持编辑）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-PKI-VAL-01 | 需求描述 | P0 | 可设置有效期的创建页，Unlimited / 无限制 不可见 |
| TP-PKI-VAL-02 | AC-05 | P0 | 按年模式：输入 ≤ 2，失焦无错误，点击 Create 可提交 |
| TP-PKI-VAL-03 | AC-06 | P0 | 按年模式：输入 > 2，失焦显示 Trial max validity is 2 years / 免费版有效年限最长 2 年 |
| TP-PKI-VAL-04 | AC-06 | P0 | 按日期模式：选择 > 当前+2 年，失焦显示同上错误提示 |
| TP-PKI-VAL-05 | AC-05 | P0 | 点击 Create 提交时再次校验有效期，超限阻止提交 |
| TP-PKI-VAL-06 | 需求描述 | P0 | 非根证书且上级不含私钥：不展示有效期字段，不受 2 年限制（按 CSR 签发） |
| TP-PKI-VAL-07 | 需求描述 | P0 | 根证书上传公钥方式（Import your own PAA）：有效期不可修改，不受 2 年限制 |
| TP-PKI-VAL-09 | QA扩展 | P1 | 按年边界：输入恰好 2 通过；输入 3 报错 |

### 公共 — 配额触达提示

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-COMMON-DLG-01 | AC-01, AC-04 | P0 | KMS 密钥数量或 PKI 任一类模板触达上限时，弹出简单提示并阻断后续操作，不打开创建页 |
| TP-COMMON-DLG-02 | QA扩展 | P1 | 本版本不要求升级引导/跳转按钮；完整引导文案与跳转逻辑 Out of Scope（下版本完善） |
| TP-COMMON-DEMO-01 | AC-08 | P3 | 自注册租户无 Demo/预设 KMS/PKI 资源；AC-08 Demo 不计入配额本 Story 不执行（Out of Scope 追溯） |

> **已确认**：自注册租户 KMS 无预设 default key、PKI 无系统预设数据；AC-08 Demo 不计入配额对本 Story 不适用。根证书配额按租户合计统计（跨 Specification），校验入口为「+ Create Root Cert」。

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 密钥数量 ≥ 5 阻断 | TP-KMS-CNT-03；TP-COMMON-DLG-01 | ✅ |
| AC-02 密钥有效期 ≤ 2 年（创建/编辑） | TP-KMS-VAL-02、TP-KMS-VAL-04、TP-KMS-VAL-06、TP-KMS-VAL-07 | ✅ |
| AC-03 密钥有效期失焦报错 | TP-KMS-VAL-03、TP-KMS-VAL-05 | ✅ |
| AC-04 每类证书模板 ≥ 2 阻断 | TP-PKI-ROOT-02、TP-PKI-ROOT-03、TP-PKI-MID-01、TP-PKI-DEV-01；TP-COMMON-DLG-01 | ✅ |
| AC-05 证书有效期 ≤ 2 年（创建） | TP-PKI-VAL-02、TP-PKI-VAL-05 | ✅ |
| AC-06 证书有效期失焦报错 | TP-PKI-VAL-03、TP-PKI-VAL-04 | ✅ |
| AC-07 Deleted 不计入；其余状态计入 | TP-KMS-CNT-04、TP-KMS-CNT-05；TP-PKI-CNT-03、TP-PKI-ROOT-04；TP-PKI-MID-02、TP-PKI-MID-03；TP-PKI-DEV-02、TP-PKI-DEV-03 | ✅ |
| AC-08 Demo 不计入配额 | TP-COMMON-DEMO-01 | ⏭️ 不执行（自注册无 Demo/预设数据；追溯用例） |

**AC-01～AC-07 均已至少 1 条 P0 测试点覆盖；AC-08 以 Out of Scope 追溯用例标记，不构造 Demo 场景。**

---

## 覆盖摘要

| 模块 | P0 | P1 | 合计 |
|------|----|----|------|
| KMS 密钥数量配额 | 3 | 2 | 5 |
| KMS 密钥有效期 | 6 | 2 | 8 |
| PKI 根证书数量配额 | 4 | 2 | 6 |
| PKI 中级/设备证书数量配额 | 2 | 4 | 6 |
| PKI 证书有效期 | 6 | 1 | 7 |
| 公共配额触达提示 | 1 | 1 | 2 |
| 公共 Demo/预设资源 | 0 | 0 | 1 |
| **合计** | **21** | **12** | **36** |

| 来源 | 条数 |
|------|------|
| Story AC（AC-01～AC-08） | 24 |
| 需求描述 | 7 |
| QA扩展 | 5 |

> **已确认（根证书）**：根证书配额按**租户下合计**统计，不按 Specification 分别计数；触达上限校验入口为「+ Create Root Cert」。


---

## 待确认

- [ ] 配额触达简单提示弹窗的具体文案（中英文）是否与设计稿一致
- [ ] 中级/设备证书的创建入口按钮文案及是否同样按租户合计统计
- [ ] KMS/PKI 列表页触达上限时，除阻断创建外是否禁用其他入口（若有）

## Out of Scope

- 付费版用户的配额行为
- 配额触达弹窗的完整引导文案、升级按钮与跳转逻辑（TP-COMMON-DLG-02）
- 编辑证书模板（本版本不支持）
- AC-08 Demo 资源不计入配额（自注册租户无预设数据）
