# Story: 【体验优化P2】提高整体信息密度

**来源**: [飞书项目 User Story #7042572937](https://project.feishu.cn/obis/userstory/detail/7042572937)  
**空间**: OBIS (`obis`)  
**类型**: User Story  
**编号**: 781  
**状态**: 联调中  
**优先级**: Must  
**Sprint**: OBIS-20260706-20260724  
**Epic**: UI及体验优化 (#7018945691)  
**Online Version**: V3.3.0  
**创建**: 2026-07-08  
**更新**: 2026-07-22  

---

## 需求描述（Description）

> Product Doc 为空（`/`）；正文取自 Description。飞书参考图因 MCP 附件下载未开通未能本地化，行高/菜单高度具体像素以设计稿/飞书附表截图为准。

### 1. 背景

- 为提高页面整体信息密度，对页面样式做调整。

### 2. 菜单栏

- 菜单栏选项的高度调整（对照设计稿）。

### 3. 所有列表

- 所有列表的**表头**和**数据行高**调整，详见附表清单。
- 覆盖模块：Group、Account、DAC Report、Device History、U-safe、Factory、PKI、KMS、Product 及其详情内嵌列表。

### 4. 浮窗文字

- 所有**黑色浮窗**内的文字字号调整为 **12px**。

### 5. Product Assets 字号例外（需求标注）

- Product → **Assets 页面所有的列表**：字号更小，为 **13**。
- **查看 Version 的 Assets 所有列表**：字号 **13**。
- **创建 Version 的 Assets 所有列表**：字号 **13**。

### 6. 附表 — 列表清单

| 功能 | 列表名称 |
|------|----------|
| Group | Group List |
| Group | Group 详情 — member list |
| Group | Group 详情 — Linked Product list |
| Group | Group 详情 — Audit list |
| Account | Account List |
| Account | Account 详情 — Audit list |
| DAC Report | DAC report list |
| Device History | Device History List |
| U-safe | U-safe list |
| Factory | Factory list |
| Factory | HSM U-safe list / Identity U-safe list |
| Factory | Batch List |
| Factory | Station list |
| Factory | Member list |
| PKI | PKI list |
| PKI | Usage list / Used by Product / Used by User |
| PKI | Member list |
| PKI | Audit list |
| KMS | KMS List |
| KMS | Usage list / Used by Product / Used by User |
| KMS | Member list |
| KMS | Audit list |
| Product | Product list |
| Product | Overview 的 Version list、Batch List |
| Product | Member list |
| Product | audit list |
| Product | Assets 页面所有列表（字号 13） |
| Product | Version 列表 |
| Product | 查看 Version 的 Assets 所有列表（字号 13） |
| Product | 创建 Version 的 Assets 所有列表（字号 13） |
| Product | Batch list |
| Product | 创建 batch 的列表 |
| Product | 查看 batch 的列表 |

---

## 评论 / 待确认

- 无评论。
- 菜单栏选项高度、通用列表表头/行高的**精确像素值**以设计稿为准（正文未写死数值）。
- 「所有黑色浮窗」是否含 Tooltip / Popover / 气泡确认等全部深色浮层，需与设计对齐。

## Out of Scope

- 业务功能逻辑变更（本 Story 仅样式/信息密度）
- 非附表所列页面的布局重构（除非产品另行声明「全局列表组件」一并生效）
