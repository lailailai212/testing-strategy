# QA 测试策略项目 — 会议纪要

**日期**：2026-06-09

---

## 背景

团队推进 qa-testing-strategy 项目，目标是在需求阶段建立统一的方法论与 Cursor Skills，覆盖：

Story AC / 验收条目 → 测试点 → 功能 / E2E 用例

已初步明确：AC 一句话、Small/Large 双模式、用例等级 P0–P3、用例结构兼顾人工可读与 AI 逐步执行等。本次会议对 Story AC 落位、Skills 分工、测试点 baseline 等落地细节进行对齐。

---

## 会议结论

1. Story AC：写在 Story Comment 里，产品确认并留痕。
2. 测试点 baseline：细节待 @魏来、@张蒙 对齐。
3. Skills 分工：
   - CICD 评审 → @陈彦任（雪球-测试）
   - 导入 MeterSphere → @梁贤丹（梁咸蛋）

---

## 待办

| 事项 | 负责人 | 时限 |
| --- | --- | --- |
| 发出今日参考文档和链接 | @魏来 | 今日 |
| 确认测试点 baseline 细节 | @魏来、@张蒙 | TBD |
| 建立 CICD 评审 Skills | @陈彦任 | TBD |
| 建立导入 MeterSphere Skills | @梁贤丹 | TBD |

---

## 落地细节

### 1. Story AC

| 项 | 约定 |
| --- | --- |
| 存放位置 | Story Comment（评论） |
| 谁确认 | 产品主确认，留痕 |
| 写法 | 一句话：谁 + 做了什么 + 可观察结果 |
| 用途 | 开发快速 review，对齐「什么叫完」 |
| Small 模式 | ≤8 条、单主路径：AC = 测试点 |
| Large 模式 | AC 短（3–8 条）+ 测试点另表 |

### 2. 测试点

| 项 | 约定 |
| --- | --- |
| Small | 验收条目表（AC = 测试点） |
| Large — Story AC | Story Comment，产品确认 |
| Large — 测试点 | **基于产品功能 baseline**，v1.0 规范暂不写死；@魏来、@张蒙 待确认 |

**用例等级速查**

| 等级 | 含义 | 执行时机 |
| --- | --- | --- |
| P0 | 主流程、阻断性规则 | 冒烟、提测、发版前必跑 |
| P1 | 边界、重要负向 | 全量 / 迭代回归 |
| P2 | 低频、待确认场景 | 专项、有余力再测 |
| P3 | 体验细节、极低频 | 大版本抽测、按需 |

### 3. 功能 / E2E 用例

| 项 | 约定 |
| --- | --- |
| 用例结构 | 标题 + 用例 ID + 优先级 + 类型 + 前置 + 测试数据 + 步骤与期望 |
| 标题 | 场景-关键期望（不含编号，如：产品创建-合法提交-进入详情Basic页） |
| 用例 ID | TC-{模块}-{序号}，如 TC-PROD-001 |
| 测试数据 | 飞书《测试数据手册》维护，步骤引用 [DATA: x.x] |
| 步骤 | 一步一动作、动词开头、操作对象明确、期望可观察 |
| 本阶段 | 不考虑自动化 / Playwright |

### 4. Skills 分工

| Skills | 负责人 | 状态 |
| --- | --- | --- |
| story-acceptance-design（需求 → AC / 测试点） | 仓库已建 | 已落地 |
| CICD 评审 | @陈彦任 | 待建 |
| 导入 MeterSphere | @梁贤丹 | 待建 |
| 功能用例展开 | — | baseline 定稿后 |

### 5. 参考文档（@魏来 今日发出）

- qa-testing-strategy 仓库 README
- 功能测试用例设计规范 v1.0
- Story AC 指南
- Small / Large 模板
- Cursor Skill：story-acceptance-design
- 飞书《测试数据手册》（待建 / 链接待补）

---

## 全流程

产品确认 AC（Comment）
→ QA 写测试点（Small 合并 / Large 分开，标 P0–P3）
→ 展开功能用例（引用测试数据手册）
→ [后续] 导入 MeterSphere / CICD 评审
