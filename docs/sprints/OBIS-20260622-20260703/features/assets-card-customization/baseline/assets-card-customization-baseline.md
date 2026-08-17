# Assets 卡片自定义 / 自定义卡片 — UI Baseline

**Story**: 7013275155 Assets 卡片自定义、7013241436 自定义卡片、7013841136 Overview  
**更新**: 2026-06（对照 SIT/设计稿 UI 截图）

---

## 页面入口

| 场景 | 路径 | 截图 |
|------|------|------|
| Overview 卡片区 | Product → **Overview** Tab → Module 选择器（Module_A/B/C + **+ Add**）→ **Assets-{Module}** 区块 | `ref-overview-create-assets-type.png` |
| 新增卡片（Overview） | **Assets-{Module}** 区块右上角 **Create Assets Type** | 同上 |
| 新增卡片（Assets） | Product → **Assets** Tab → 右侧导航底部 **+ Create Assets T…** | `ref-assets-chip-config-menu.png` |
| 删除卡片 | Assets 主内容区卡片标题栏 **⋮** → **Edit** / **Delete**（Delete 为红色） | `ref-assets-chip-config-menu.png` |
| 创建 Version | Product → **Version** Tab → **Create Version** | `ref-overview-create-assets-type.png` |

## Confirm Create 弹框（新增卡片 / Version 创建共用样式）

**截图**: `ref-confirm-create-section.png`

| 元素 | UI 规格 |
|------|---------|
| 标题 | **Confirm Create**；右上角 **X** 关闭 |
| Section 区 | 2 列网格卡片；每张含图标、标题、副文案 |
| 已启用内置类型 | 副文案 **Already visible**（如 Firmware、Keys、Certificates、Chip Config、Matter Config、Factory Data、Programming Station Script、General File、Secure Element） |
| 自定义类型 | **Customize** 卡片；副文案 **Click to add**；选中时深色边框高亮 |
| Name | 必填 **Name \***；placeholder **Enter value**（**内置类型加回 / Version 等流程**；**Customize 路径不使用此字段**） |
| 底栏 | **Cancel** / **Confirm** |

### Customize 创建流程（产品确认 2026-06）

1. **Confirm Create** 中点击 **Customize**（Click to add）
2. **不**在 Confirm Create 填写 Name；**直接进入 Customize 卡片编辑器**
3. 编辑器为 **编辑态（edit mode）**：Asset Type Name \* 为空待填；行表可增删
4. **Asset Type Name \*** 为必填；Save 前须填写

## Customize 卡片编辑器

**截图**: `ref-customize-card-editor-edit-view.png`（编辑态 + 保存后查看态）

### 编辑态

| 元素 | UI 规格 |
|------|---------|
| 标题 | **Customize** |
| 副标题 | module-scoped production data templates written during manufacturing |
| 右上角 | **⋮** 溢出菜单 |
| 卡片名称 | **Asset Type Name \***；placeholder **Please enter** |
| 行表表头 | **Label** / **Type** / **Key** / **Value** |
| 行内 placeholder | Label、Key → **Please Enter**；Type、Value → **Please Select** |
| 删行 | 行末 **垃圾桶（Trash）** 图标 |
| 增行 | **+ Add New Content**（虚线边框按钮） |
| 底栏 | **Cancel** / **Save**（Save 为主按钮蓝色） |

### 查看态（Save 成功后）

| 元素 | UI 规格 |
|------|---------|
| 行表 | 四列只读文本展示（无输入框） |
| 样本行 | Start Address / Hex / startAddress / 0x003F8000；Device Serial Number / String / Batch Injection / 2003yioon |

> **Type 枚举（需求 AC）**：String / Number / Boolean / Key / Certificate / File；baseline 查看态样本含 Hex，验收以 Product Doc 下拉选项为准。

## Overview 上 Customize 卡片展示

**截图**: `ref-overview-se-customize-card.png`

| 元素 | UI 规格 |
|------|---------|
| 卡片标题 | **Customize** |
| 摘要 | **Data Key: {n}**（行数） |
| 底栏 | {编辑者头像} {用户名} - {相对时间}（如 John Smith - 2h ago） |

## Assets Tab 布局

**截图**: `ref-assets-chip-config-menu.png`

| 元素 | UI 规格 |
|------|---------|
| Module 选择器 | 顶部 Tab：Module_A / Module_B / Module_C / **+ Add** |
| 主内容 | 当前选中卡片详情（如 **Chip Config** 表格：Label / Type / Key / Value） |
| 右侧导航 | Chip config、Keys、Certificate、Frimware、Matter Config、Factory Data、Generate File、**+ Create Assets T…** |

## Version / 删除规则（产品确认）

见原 baseline：必填 Chip Config / Certificate / Matter Config / Firmware；已进 Version 不可删；隐藏卡不纳入 Version。

## 删除二次确认文案

- 英文：**Are you sure you want to delete this asset type?**
- 中文：**确定要删除该资产类型吗？**
