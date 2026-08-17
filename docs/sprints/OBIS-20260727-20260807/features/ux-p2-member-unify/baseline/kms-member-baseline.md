# KMS Key Detail → Member Baseline

> **URL**：`https://iot-admin-sit.snowballtech.com/key/2081648131348414465`  
> **资源**：Name=`test permission` · Key ID=`KID-SAdba2d91445` · Status=Active · Admin=张峰  
> **扫描**：2026-08-03 · 雪球租户 · `feng.zhang`  
> **台账代号候选**：暂记为 **KEY-CAND-1**（正式 KEY-1 需满足 A4 在 Member 等造数要求后再改名）

## 页结构

```text
面包屑：KMS / test permission
Tabs：Overview | Usage | Audit | Member
Member 工具栏：Filter | Columns | Refresh | [Add]
Member 表（默认可见列）：Name | Role | Permission | Status |（Operations）
```

## 关键交互元素

| 区域 | 元素 | 文案 | 推荐 Locator | 稳定度 |
|------|------|------|--------------|--------|
| Tab | Member | Member | `getByText('Member', { exact: true })` 或 role tab | 高 |
| 工具栏 | Filter / Columns / Refresh | 同左 | `getByText('Filter'/'Columns'/'Refresh', { exact: true })` | 中 |
| 工具栏 | Add | Add | `getByRole('button', { name: 'Add' })` | 高 |
| 表头 | Name/Role/Permission/Status | 同左 | `getByRole('columnheader', { name })` 或表头文案 | 高 |
| 行 | Admin 角色 | Admin | 行内 `getByText('Admin', { exact: true })` | 高 |
| 行 | 操作三点 | （图标按钮） | 行末 `getByRole('button')` · **fragile** | 低 |
| Columns | 可选列 | Role / Permission / Operator / Join Time | checkbox + name | 中 |
| Columns | 锁定列 | Name / Status / Operations | disabled checkbox | 高 |

## Columns 面板实测选项

| 列 | 默认 | 可关 |
|----|------|------|
| Name | ✅ | 否（disabled） |
| Role | ✅ | 是 |
| Permission | ✅ | 是 |
| Operator | 否 | 是 |
| Join Time | 否 | 是 |
| Status | ✅ | 否 |
| Operations | ✅ | 否 |

## 样本行（扫描时）

| Name | Role | Permission（展示） | Status |
|------|------|-------------------|--------|
| 张峰 | Admin | View, Edit, Create Authorization, Lock, Unlock, Add Member, Revoke, Delete（**全部展开，未见 `+n`**） | Active |

## 与用例 / 早前探查的差异（重要）

| 项 | 用例 / 2026-08-03 上午探查 | 本次下午实测（本 Key） |
|----|---------------------------|------------------------|
| 默认列含 Organization | Name、Role、Permission、**Organization**、Status | **无 Organization 列**；Columns 面板也无 Organization 选项 |
| Permission `+n` | 默认 1 个 Tag + `+n`（曾见 `View +7`） | Admin 行 **全部 Permission 平铺**，无 `+n` |
| 工具栏 Sort | 用例写 Filter/Columns/Refresh/Sort/+ Add | 仅 Filter / Columns / Refresh / Add，**无 Sort** |
| Tab 名 | 部分文档写 Operation Log | 详情 Tab 为 **Audit**（非 Operation Log） |

> Agent 执行：以**本次 baseline 实测**操作；若预期仍写 Organization / `+n` / Sort，结果记 **Fail** 并注明与 baseline 差异，或标 Blocked「需换有 `+n` 的 Key / 与开发确认规格」。

## Fragile

- Admin 行三点菜单：无文案，需行内 button  
- Permission 是否折叠与成员角色/数量有关，勿假设全局 `+n`  
- 勿用通用 placeholder 跨页定位
