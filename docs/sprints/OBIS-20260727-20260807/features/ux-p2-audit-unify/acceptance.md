# Story: 【体验优化P2】Audit功能统一

**来源**: [飞书项目 User Story #7029049092](https://project.feishu.cn/obis/userstory/detail/7029049092)  
**空间**: OBIS (`obis`)  
**编号**: 745 | **优先级**: Must | **Epic**: UI及体验优化  
**Sprint**: OBIS-20260727-20260807  
**模式**: Large（跨 Group/Account/Profile/KMS/PKI/Product 六处 Audit 统一列、Filter、Columns、Sort；KMS 额外筛选项，需独立测试点与抽样）

> Story 导出：`story/obis-7029049092-体验优化p2-audit功能统一/obis-7029049092-体验优化p2-audit功能统一.md`

---

## Story AC

1.（AC-01）用户打开任意目标模块 Audit 列表时，默认可见 Operator（头像+Name+邮箱 icon，hover 完整邮箱+复制）、Organization（租户简称）、Operation Type、Operation Time（年月日时分秒）；溢出内容 hover 展示全文；Operation Details 默认隐藏且位于 Operation Type 后。

2.（AC-02）用户打开 Audit Filter 时，可按 Operator Name、Operator Email、Organization（输入框，Placeholder「Please Enter / 请输入」）及 Operation Time 范围筛选；Start date 取当日 00:00:00，End date 取当日 23:59:59。

3.（AC-03）用户配置 Columns 时：Operator、Operation Type 不可隐藏且不可换顺序；Organization、Operation Time 可配置；Operation Details 默认可开启且位置在 Operation Type 后。

4.（AC-04）用户使用 Refresh 可刷新列表；Sort 仅按 Operation Time，默认倒序。

5.（AC-05）Group / Account / Profile / PKI / Product 的 Audit 规格与 Group 基准完全一致。

6.（AC-06）KMS Audit 在 Filter 按钮展开面板中，于 Organization 后额外提供 Operation Type 筛选项；其余规格与 Group 一致。

---

## 测试点

> **来源**：`AC-0x` / `需求描述` / `QA扩展`。  
> **优先级**：P0 = Group 基准 + 各模块冒烟；P1 = Columns/Filter 细节与抽样。  
> **说明**：现状「Operation」列 = Operation Details（默认隐藏）。

### 基准 — Group Audit

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUD-G01 | AC-01 | P0 | Group Audit 默认列：Operator、Organization、Operation Type、Operation Time；无默认展示 Operation Details |
| TP-AUD-G02 | AC-01 | P0 | Operator 展示头像+Name+邮箱 icon；hover 出完整邮箱与复制，复制成功 |
| TP-AUD-G03 | AC-01 | P0 | Organization 展示操作人所属租户简称 |
| TP-AUD-G04 | AC-01 | P0 | Operation Time 为年月日时分秒；单元格溢出时可 hover 见全文 |
| TP-AUD-G05 | AC-02 | P0 | Filter 含 Operator Name / Email / Organization 输入框（Placeholder 正确）与 Operation Time 范围 |
| TP-AUD-G06 | AC-02 | P0 | 按时间范围筛选：起日按 00:00:00、止日按 23:59:59 生效 |
| TP-AUD-G07 | AC-02 | P1 | 按姓名/邮箱/组织输入可筛出匹配行；无匹配时空态合理 |
| TP-AUD-G08 | AC-03 | P0 | Columns：Operator、Operation Type 不可隐藏、不可拖拽换序 |
| TP-AUD-G09 | AC-03 | P0 | 开启 Operation Details 后出现在 Operation Type 后；内容为原 Operation 长文案格式 |
| TP-AUD-G10 | AC-03 | P1 | 可隐藏/显示 Organization、Operation Time；关闭后恢复默认可见集 |
| TP-AUD-G11 | AC-04 | P0 | Refresh 刷新列表数据；默认 Sort 按 Operation Time 倒序 |
| TP-AUD-G12 | AC-04 | P1 | 切换为正序后列表按时间升序；无其它 Sort 维度可选 |

### Account / Profile Audit

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUD-A01 | AC-05 | P0 | Account 详情 Audit：默认列、Operator hover、Organization、Filter/Columns/Sort 与 Group 一致 |
| TP-AUD-A02 | AC-05 | P0 | Profile Audit：同上与 Group 一致 |
| TP-AUD-A03 | QA扩展 | P1 | Account 与 Profile 列配置/筛选行为一致（是否同组件待确认，验收结果一致即可） |

### KMS Audit

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUD-K01 | AC-05, AC-06 | P0 | KMS Audit 默认列与 Columns/Sort/Refresh 同 Group |
| TP-AUD-K02 | AC-06 | P0 | 点击列表上方 Filter：面板在 Organization 后有 Operation Type 筛选项 |
| TP-AUD-K03 | AC-06 | P0 | 使用 Operation Type 筛选后列表仅保留匹配类型（控件细节待确认，以可筛为准） |
| TP-AUD-K04 | AC-01 | P1 | 开启 Operation Details 可见且默认隐藏 |

### PKI / Product Audit

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-AUD-P01 | AC-05 | P0 | PKI Audit：默认列、Filter（无额外 Operation Type）、Columns、Sort 同 Group |
| TP-AUD-P02 | AC-05 | P0 | Product Audit：同上；Organization 列与基准一致（含 Operator hover、Details 默认隐藏） |
| TP-AUD-P03 | QA扩展 | P1 | Product 不额外出现仅 KMS 才有的 Filter Operation Type |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 列表字段 | TP-AUD-G01～04；K04；各模块冒烟 | ✅ |
| AC-02 Filter | TP-AUD-G05～07 | ✅ |
| AC-03 Columns | TP-AUD-G08～10 | ✅ |
| AC-04 Refresh/Sort | TP-AUD-G11～12 | ✅ |
| AC-05 五模块对齐 | TP-AUD-A01～02；P01～02；K01 | ✅ |
| AC-06 KMS Filter Operation Type | TP-AUD-K02～03 | ✅ |

**AC-01～AC-06 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| Group 基准 | 8 | 4 | 0 | 12 |
| Account/Profile | 2 | 1 | 0 | 3 |
| KMS | 3 | 1 | 0 | 4 |
| PKI/Product | 2 | 1 | 0 | 3 |
| **合计** | **15** | **7** | **0** | **22** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 20 |
| 需求描述 | 0 |
| QA 扩展 | 2 |

---

## 设计自检

### 里程碑 / 去重（类型 A）

- [x] N/A（未命中）

### 异步通知（类型 B）

- [x] N/A（未命中）

### 多角色可见 / 触达（类型 C）

- [x] N/A（未命中；本 Story 为列表展示统一，无角色分叉交付）

### 配额 / 用量归属（类型 D）

- [x] N/A（未命中）

---

## 待确认

- [ ] KMS Filter 内 Operation Type：单选 / 多选 / 输入及可选值来源
- [ ] Organization Filter 是否模糊匹配；空组织展示与筛选
- [ ] 默认列顺序是否固定为 Operator → Organization → Operation Type →（Details）→ Operation Time
- [ ] Profile 与 Account Audit 是否共用同一组件

## Out of Scope

- （原文无明确排除项）
