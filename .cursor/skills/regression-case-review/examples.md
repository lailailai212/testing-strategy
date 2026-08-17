# Examples — Regression Case Review

## 示例 A：对照 SIT 的上线回归 Product-Asset 包

**输入**

- Excel：`Downloads/上线回归-Product-Asset.xlsx`（约 44 条）
- 对照：`target_env=sit` · `https://iot-admin-sit.snowballtech.com/` Product → Assets
- 约束：不要参考仓库用例；SBOM/OTA 本轮不上线

**流程摘要**

1. 锁定 sit → 解析 44 条 → 登录 SIT → 建区块基线（Chip Config / Keys / … / Module 标签栏）
2. Canvas 分类：过时（文案与列名）、错误、重复（合并 −7）、遗漏
3. 用户纠偏：条件列、Module 内联新建、未设计删除、Remove Confirm、SBOM/OTA 移出
4. 产出：`上线回归-Product-Asset-评审修订.xlsx`；头标注 `对照环境: sit`

**去重键示例**

| 用例名（简） | 去重键 | 处理 |
|--------------|--------|------|
| 两处「添加 Key 成功」写法不同 | Assets×Keys×Add 成功 | 留一条 |
| 「删除 Chip」vs「删除自定义行」 | 主断言不同 | 不合并；改写无入口的那条 |

**遗漏扫描示例**

| 区块 | 原包 | 建议 |
|------|------|------|
| General File | 0 | 增 Add / 列表 / Tag / 上限等 |
| Module | 仅创建 | 补重命名；**不**补未设计的删除 |
| 权限 | 几乎无负向 | 补无权限角色看不到关键按钮 |

**错误示范 → 纠正**

| 错误做法 | 纠正 |
|----------|------|
| 因当前芯片无 Secure Boot 列，删相关用例 | 保留；前置改为「已选支持该能力的 Vendor/Series/Part」 |
| 未见 Module 关闭图标，仍写「删除功能正确」 | 产品说未设计 → 整类不做 |
| 直接改原 xlsx | 写 `*-评审修订.xlsx` |
| 用 SIT 结论直接改「UAT 回归包」且不声明 | 先锁定 uat 再测；或分两轮 |

---

## 示例 B：对照 UAT 整理回归包

**输入**

- Excel：`Downloads/UAT回归-Product-Asset.xlsx`
- 用户说：「按 UAT 整理这份回归用例」
- 解析：`target_env=uat`，`base_url` 取自 `config/env.local.yaml` → `environments.uat.base_url`（或用户给的 UAT URL）

**要点**

1. Canvas 文件名带环境：`product-asset-uat-regression-review.canvas.tsx`
2. 基线标题写「UAT 基线」，备注写 `评审补漏 · uat {区块}`
3. 若用户追问「和 SIT 是否一致」→ 列入未验证，或另开 sit 轮；**不把 sit 观察写进 uat findings**
4. 修订文件建议：`UAT回归-Product-Asset-uat-评审修订.xlsx`（避免与 sit 修订混名）

---

## 对话触发语（可复用）

```text
# SIT
评审 {xlsx路径}：重复/错误/过时/遗漏。对照 {SIT URL}。不要参考仓库用例。

# UAT
按 UAT 整理 {xlsx路径} 的回归用例，对照 {UAT URL}（或读 env.local.yaml 的 uat）。

# 两环境
同一份包先按 UAT 评一轮；SIT 差异另开一轮，不要混在一张表里。
```
