# Story: PM-S-F01-01：创建 Product 表单 Batch Expiry Duration Max. Duration 默认值调整

**来源**: [飞书项目 User Story #7067202174](https://project.feishu.cn/obis/userstory/detail/7067202174)
**空间**: OBIS (`obis`)
**类型**: User Story
**编号**: 852
**状态**: 技术设计中
**优先级**: Must
**Sprint**: OBIS-20260810-20260821
**Epic**: （飞书字段为空）
**Story Point**: DEV 0.1 / QC 0.8
**Labels**: Product Management、批次有效期配置
**创建**: 2026-08-05
**更新**: 2026-08-07

---

## 需求描述（Description）

> Product Doc 字段为「无」；正文取自 Description。无参考图。

### 1. 用户故事

- 作为产品经理（Product Manager），希望创建 Product 时 Batch Expiry Duration 的 Max. Duration 默认值与常见批次周期匹配，以便多数场景下无需修改即可直接提交。

### 2. 默认值调整

- 改前：Create Product 页 Batch Expiry Duration 的 **Max. Duration** 默认值为 **30 天**。
- 改后：进入 Create Product 页面时，Max. Duration 字段默认值为 **90 天**。（AC-01）
- **BR-01**：Max. Duration 默认值为 90 天。
- **本期范围**：只改 Max. Duration 默认值；Min. Duration、校验范围、单位及其他 Batch Expiry 字段均不变。

---

## 评论 / 待确认

- 无飞书评论。
- [2026-08-10 已确认]：改前 Max. Duration 默认值为 30 天；本期只改 Max. Duration 默认值（30 → 90）。

## Out of Scope

- Min. Duration 及其他 Batch Expiry / Create Product 表单字段的默认值、校验规则与提交流程。
- 已创建 Product 的存量 Batch Expiry Duration 配置回填或迁移（正文未声明）。
