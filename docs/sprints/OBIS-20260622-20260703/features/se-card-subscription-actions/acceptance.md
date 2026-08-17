# Story: 【SE卡片】订阅与动作

**来源**: [飞书项目 User Story #7018714820](https://project.feishu.cn/obis/userstory/detail/7018714820)  
**空间**: OBIS (`obis`)  
**编号**: 658 | **优先级**: Must | **Sprint**: OBIS-20260622-20260703  
**术语**: **PW** = **Product Workspace**  
**模式**: Large（订阅 SEMS 状态变更 + 创建 Version / Batch 时 SE 状态校验与失败提示，跨 PW / SEMS / Version / Batch 多模块，需独立测试点表与 AC 追溯）

---

## Story AC

1.（AC-05）**Product Workspace（PW）** 订阅被引用到 PW workspace 中的 **SEMS 资产内容**的**状态变更信息**（**仅状态**）。

2.（AC-07）用户**创建版本**或**创建批次**时，系统须对被引用到资产中的 **SE profile** **调用状态接口**查询其当前状态。

3.（AC-08）当状态接口查询到 SE profile 状态为**非 active**（SEMS 侧状态）时，**创建版本或批次失败**。

4.（AC-09）创建版本或批次失败时须给出提示：中文 **SE profile状态变更，请检查SE profile状态**；英文 **The status of the SE profile has changed. Please check the status of the SE profile.**

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### PW — SEMS 状态变更订阅

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SES-SUB-01 | AC-05 | P0 | PW 对已引用到 workspace 的 SEMS SE 资产建立**状态变更订阅**（非 PKI/KMS 旧订阅模式） |
| TP-SES-SUB-02 | AC-05 | P0 | SEMS 侧 SE profile 状态由 **active → 非 active** 变更后，PW / Assets 侧 SE 卡片 **active 状态展示同步更新**（无需用户手动刷新或重新导入） |
| TP-SES-SUB-03 | AC-05 | P0 | 订阅范围**仅状态**字段：SE profile **name** 等其他字段变更走 Story #653 既有同步，**不依赖**本 Story 订阅 |
| TP-SES-SUB-04 | 需求描述 | P1 / 待确认 | 具体订阅哪些状态枚举（active / deactive / 其他 SEMS 状态）及推送时机（实时 / 轮询） |
| TP-SES-SUB-05 | QA扩展 | P1 | 多 Product / 多 Module 引用同一 SEMS SE 时，状态变更对各 workspace **均生效** |
| TP-SES-SUB-06 | QA扩展 | P2 | SEMS 状态恢复为 **active** 后，Assets SE 卡片状态展示**同步恢复** |

### 创建 Version — SE 状态校验

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SES-VER-01 | AC-07 | P0 | Product 已导入 SE 且 SE profile 为 **active** 时，创建 **Product Version**（引用含 SE 的 Module）**可成功** |
| TP-SES-VER-02 | AC-07 | P0 | 创建 Version 流程中，系统对资产内被引用的 **SE profile 调用状态接口**查询当前 SEMS 状态 |
| TP-SES-VER-03 | AC-08 | P0 | SE profile 状态为**非 active** 时，创建 Version **失败**，不产生新版本 |
| TP-SES-VER-04 | AC-09 | P0 | Version 创建失败提示（中文）：**SE profile状态变更，请检查SE profile状态** |
| TP-SES-VER-05 | AC-09 | P0 | Version 创建失败提示（英文）：**The status of the SE profile has changed. Please check the status of the SE profile.** |
| TP-SES-VER-06 | 需求描述 | P1 / 待确认 | 失败提示展示形式：Toast / Dialog / 行内错误（Product Doc 未述） |
| TP-SES-VER-07 | QA扩展 | P1 | SE Module **数据不充分**（Story #601）本就不出现在 Version Module 列表；与 AC-08 **非 active** 拦截为不同路径，均须覆盖 |
| TP-SES-VER-08 | QA扩展 | P1 | Version 创建失败后，用户修正 SEMS 状态为 active 后**可重试成功** |
| TP-SES-VER-09 | QA扩展 | P2 | Product **无 SE 引用**或 Module 不含 SE 时，创建 Version **不受**本 Story SE 状态校验影响 |

### 创建 Batch — SE 状态校验

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SES-BAT-01 | AC-07 | P0 | Product 已导入 SE 且 SE profile 为 **active** 时，创建 **Batch**（Manufacturing，引用含 SE 的版本 / 资产）**可成功** |
| TP-SES-BAT-02 | AC-07 | P0 | 创建 Batch 流程中，系统对资产内被引用的 **SE profile 调用状态接口**查询当前 SEMS 状态 |
| TP-SES-BAT-03 | AC-08 | P0 | SE profile 状态为**非 active** 时，创建 Batch **失败**，不产生新批次 |
| TP-SES-BAT-04 | AC-09 | P0 | Batch 创建失败提示（中文）：**SE profile状态变更，请检查SE profile状态** |
| TP-SES-BAT-05 | AC-09 | P0 | Batch 创建失败提示（英文）：**The status of the SE profile has changed. Please check the status of the SE profile.** |
| TP-SES-BAT-06 | QA扩展 | P1 | Batch 创建失败后，SE 状态恢复 active 后**可重试成功** |
| TP-SES-BAT-07 | QA扩展 | P2 | 无 SE 引用的 Product 创建 Batch **不受**本 Story 校验影响 |

### 负向与边界 — 状态接口

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-SES-NEG-01 | QA扩展 | P1 | 创建 Version / Batch 时状态接口**超时或不可用**，创建**失败**并给出可识别错误（非静默成功） |
| TP-SES-NEG-02 | 需求描述 | P1 / 待确认 | 「非 active」具体 SEMS 枚举值（deactive / revoked / 其他）均触发 AC-08 拦截 |
| TP-SES-NEG-03 | 需求描述 | P1 / 待确认 | Product Doc 动作段落文案为「SE**芯片**状态变更」，AC-09 为「SE **profile**状态变更」— **以 AC-09 为准或待产品统一** |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-05 PW 订阅 SEMS 状态变更（仅状态） | TP-SES-SUB-01～03 | ✅ |
| AC-07 创建 Version / Batch 时调用状态接口 | TP-SES-VER-01～02；TP-SES-BAT-01～02 | ✅ |
| AC-08 非 active 时创建失败 | TP-SES-VER-03；TP-SES-BAT-03 | ✅ |
| AC-09 失败提示中英文文案 | TP-SES-VER-04～05；TP-SES-BAT-04～05 | ✅ |

**AC-05、AC-07～AC-09 均已至少 1 条 P0 测试点覆盖。**（Product Doc 无 AC-06，见待确认）

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| SEMS 状态订阅 | 3 | 2 | 1 | 6 |
| 创建 Version 校验 | 5 | 3 | 1 | 9 |
| 创建 Batch 校验 | 5 | 1 | 1 | 7 |
| 负向与边界 | 0 | 3 | 0 | 3 |
| **合计** | **13** | **9** | **3** | **25** |

| 命中类型 | 条数 |
|----------|------|
| 直接命中 AC | 13 |
| 需求描述 | 5 |
| QA 扩展 | 7 |

---

## 待确认

- [ ] Product Doc **AC-06 缺失**（仅有 AC-05、AC-07～AC-09），是否为遗漏或合并至其他 Story
- [ ] 失败提示文案：**动作段落**（SE**芯片**）vs **AC-09**（SE **profile**）中英文不一致，以哪套为准
- [ ] 订阅具体状态字段与推送机制（实时 Webhook / 消息队列 / 轮询）
- [ ] 创建 Version / Batch 时调用的 **SEMS 状态接口**规格（路径、参数、非 active 枚举）
- [ ] 失败提示 UI 形式（Toast / Dialog / 表单行内）
- [ ] Assets 侧用户手动 **deactive** SE 卡片（Story #653 AC-07）与 SEMS **非 active** 在 Version / Batch 校验上是否等价

## Out of Scope

- ~~通过 PKI/KMS 旧订阅模式同步 SEMS 信息~~
- ~~授权被消费时 OBIS 消费记录同步至 SEMS~~
- ~~AC-01～AC-04（bind / unbind、`display_fields` 等消费记录参数）~~ — Product Doc 已全部取消
- SE 卡片**导入**流程 — 见 Story #655
- SE 卡片**字段展示、Tag、删除** — 见 Story #653

---

## 关联 Story

| 编号 | Story | 关系 |
|:----:|-------|------|
| 655 | SE 卡片内容导入 | 导入 SE 后方可被引用与校验 |
| 653 | SE 卡片内容说明 | SE active 展示、本地 deactive 操作 |
| 601 | 选择 module 类型 | SE Module Version 可选与数据充分性 |
