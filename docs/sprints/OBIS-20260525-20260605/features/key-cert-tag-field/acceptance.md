# Story: key和cert增加tag字段与数据迁移（评论补测）

**来源**: [飞书项目 User Story #6996267987](https://project.feishu.cn/obis/userstory/detail/6996267987)  
**空间**: OBIS (`obis`)  
**编号**: 548 | **优先级**: Must | **Epic**: —  
**Sprint**: OBIS-20260525-20260605  
**模式**: Large（判定依据：主路径已有样例用例；本次按产品评论补空格 / 长度 / 删除三类独立规则）  
**变更类型**: Hybrid（主 Logic：空格忽略/拦截、1024 边界、禁止删除；次 UI/UX：无删除入口的可观察点）

---

## 已确认规则（飞书评论 / Bug 关闭结论）

| 项 | 结论 | 出处 |
|----|------|------|
| 空格 | **Tag 不支持空格**。开发关闭 Bug #7024397639（无需修复 / 无效问题）：不允许输入空格。现网曾表现为输入空格被 ignore（如 `Tag Test` → `TagTest`） | 2026-06-22 Bug；2026-08-11 产品评论 |
| 长度 | **只有长度限制 1024** | 2026-06-11 开发评论 |
| 删除 | **目前不支持** Tag 删除 | 2026-06-11 产品评论 |
| 自定义 Tag 范围 | 产品级，Key / Cert / General File 共用；系统默认 `google certificate config` / `matter config` 不能作为自定义添加 | 2026-06-02 / 06-09 评论 |
| Cert Tag | 必填；系统默认项仅 Assign Certificate | Product Doc |
| Key Tag | 非必填；下拉无系统默认项 | Product Doc |

## 本次补测范围（评论指示）

1. Assign Key / Assign Certificate 输入**含空格** Tag，确认忽略空格或拦截（与「不支持空格」一致）。
2. 输入 **1025+** 字符，确认截断 / 报错 / 拦截。
3. Assign 弹窗与 Asset 列表均**无 Tag 删除入口**。

**不在本包展开**：pixiu #104904 Step 1 ERROR 核实（执行记录，非新用例）；主路径 Assign/列表/跨页一致性仍以 `_examples/product-asset-tag` 为准。

---

## Story AC

1.（AC-01）用户在 Product Assets 的 **Assign Key** 或 **Assign Certificate** 弹窗新增 Tag 时，Tag **不支持空格**：输入含空格的名称（如 `Tag Test`）时，空格被忽略或无法键入，**不得**创建名称中含空格的 Tag。

2.（AC-02）用户新增自定义 Tag 时，名称长度上限为 **1024**：长度为 1024 的名称可以添加；超过 1024（如 1025）时被截断、报错或拦截，**不得**以超长名称落库。

3.（AC-03）产品已明确 Tag **目前不支持删除**：Assign Key / Assign Certificate 弹窗与 Assets 列表（Keys / Certificates）均不展示 Tag 删除操作入口。

---

## 测试点

> **命中 AC 列**：`AC-0x` = 直接覆盖 Story AC；`需求描述` = 需求正文有述但未列入本次补测 AC；`QA扩展` = QA 补充边界。

### Product Assets — Tag 新增

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-TAG-SPC-01 | AC-01 | P0 | Assign Key：Enter Value 输入含中间空格的名称（如 Tag Test），Add 后 Tag 名称不含空格（忽略或拦截） |
| TP-TAG-SPC-02 | AC-01 | P0 | Assign Certificate：同上，含空格输入不得创建带空格 Tag |
| TP-TAG-LEN-01 | AC-02 | P0 | 输入恰好 1024 个字符可 Add 成功 |
| TP-TAG-LEN-02 | AC-02 | P0 | 输入 1025 个及以上字符被截断、报错或 Add 不可用，列表/下拉不出现超长 Tag |
| TP-TAG-DEL-01 | AC-03 | P0 | Assign Key、Assign Certificate 弹窗 Tag 下拉/选项无删除按钮、无删除图标 |
| TP-TAG-DEL-02 | AC-03 | P0 | Assets Keys / Certificates 列表 Tag 列无删除操作入口 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Tag 不支持空格 | TP-TAG-SPC-01、TP-TAG-SPC-02 | ✅ |
| AC-02 长度限制 1024 | TP-TAG-LEN-01、TP-TAG-LEN-02 | ✅ |
| AC-03 不支持删除 | TP-TAG-DEL-01、TP-TAG-DEL-02 | ✅ |

**AC-01～AC-03 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | 合计 |
|------|----|----|------|
| Tag 空格 | 2 | 0 | 2 |
| Tag 长度 | 2 | 0 | 2 |
| Tag 无删除 | 2 | 0 | 2 |
| **合计** | **6** | **0** | **6** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 6 |
| 需求描述 | 0 |
| QA 扩展 | 0 |

---

## 设计自检

### 变更类型

- [x] 已声明 Hybrid（主 Logic / 次 UI）
- [x] P0 全部落在空格、长度、无删除入口
- [x] 未把「删除成功」写成正向用例（与产品结论相反）

### 里程碑 / 去重 / 通知 / 配额

- [x] N/A（未命中类型 A–D）

---

## 待确认 / 执行备注

- 空格：以「最终 Tag 名称不含空格」为通过标准；执行时记录是忽略还是无法键入。
- 超长：以「不以 1025+ 字符落库」为通过标准；执行时记录截断 / 报错 / 置灰。
- pixiu 用例 #104904 Step 1 ERROR：评论要求核实是否为重复样式 Bug #7024377896 遗留记录，不在本包出新用例。
