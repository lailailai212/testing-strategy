# Story: 【卡片编辑】选择module类型

**来源**: [飞书项目 User Story #7013300594](https://project.feishu.cn/obis/userstory/detail/7013300594)  
**空间**: OBIS (`obis`)  
**编号**: 601 | **优先级**: Must | **Sprint**: OBIS-20260622-20260703  
**模式**: Large（需求含 Add Module 弹框、Module 编辑、三种 Module Type 默认卡片 / 不可删除 / Version 必填等多套规则，需独立测试点表与 AC 追溯）

---

## Story AC

1.（AC-01）用户在 Assets Tab 点击 **Add Module** 时，弹框须含 **Module Type** 单选（Matter / Secure Element / Other）、**必填**、默认 **Matter**；并根据所选类型在 **Section** 区展示对应默认卡片预览（副文案 **Already visible**）。

2.（AC-02）用户可通过 Module **编辑**入口修改 Module **名称**并保存。

3.（AC-03）用户**创建新产品**时，系统默认添加 **Matter** 类型的 Module。

4.（AC-04）**Matter** 类型 Module 创建后，Assets 须默认展示 **8** 张内置卡片（Chip Config、Keys、Certificate、Firmware、Matter Config、Factory Data、General File、PS Software Package），且该 8 张卡片均为模板 **不可删除项**。

5.（AC-05）**Secure Element** 类型 Module 创建后，Assets 须默认展示 **SE**、**PS Software Package**、**General File** 三张卡片；其中 **SE** 为模板 **不可删除项**；SE 卡片数据不充分时，该 Module **不出现在** Product Version 可选 Module 列表中。

6.（AC-06）**Other** 类型 Module 创建后，Assets 须默认展示 **7** 张内置卡片（Matter 默认 8 张 **减去 Matter Config**）；模板 **无不可删除项**；创建 Version 时 **chip config** 必填——数据不充分则 Module 不可选；**matter**（Matter Config）**仅当用户已加回该卡片时**校验必填。

7.（AC-07）任意 Module Type 下，当卡片内 **密钥或证书被引用** 时，该卡片 **不可删除**（删除置灰），直至取消引用。

---

## 测试点

> **来源**：覆盖 Story AC 时填实际 AC 编号（如 `AC-01`；多条用逗号分隔）；否则填 `需求描述` 或 `QA扩展`。

### Assets — Add Module 弹框

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-ADD-01 | AC-01 | P0 | Assets Tab → Module 选择器旁 **Add**，弹出 **Add Module** 对话框（标题、副标题、Cancel / Confirm） |
| TP-MT-ADD-02 | AC-01 | P0 | 弹框含 **Name**（必填 `*`）与 **Module Type**（必填 `*`，Radio 单选） |
| TP-MT-ADD-03 | AC-01 | P0 | Module Type 枚举：**Matter** / **Secure Element** / **Other** |
| TP-MT-ADD-04 | AC-01 | P0 | 打开弹框时 **Matter** 默认选中 |
| TP-MT-ADD-05 | AC-01 | P0 | **Matter** 选中时 Section 展示 **8** 张卡片预览，均为 **Already visible**：Firmware、Certificates、Matter Config、Programming Station Script、Keys、Chip Config、Factory Data、General File |
| TP-MT-ADD-06 | AC-01 | P1 / 待确认 | 切换 **Secure Element** 后 Section 预览更新为 SE 类型默认卡片（预期含 SE、脚本、General File；具体 UI 待补截图） |
| TP-MT-ADD-07 | AC-01 | P1 / 待确认 | 切换 **Other** 后 Section 预览更新为 Other 默认 **7** 张卡片（**不含 Matter Config**；具体 UI 待补截图） |
| TP-MT-ADD-08 | 需求描述 | P0 | 填写 Name + 选择 Module Type 后 **Confirm**，Module 创建成功并在 Module 选择器中可选 |
| TP-MT-ADD-09 | QA扩展 | P1 | **Cancel** 或右上角 **X** 关闭弹框，不创建 Module |

### Module — 名称编辑

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-EDT-01 | AC-02 | P0 | Module 选择器 / 模块区域提供 **编辑**入口 |
| TP-MT-EDT-02 | AC-02 | P0 | 点击编辑后可修改 Module **名称**并保存；保存后名称展示更新 |

### 创建产品 — 默认 Module

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-PRD-01 | AC-03 | P0 | **新建 Product** 后，默认存在 **Matter** 类型 Module（Module Type = Matter） |

### Matter Module — 默认卡片与不可删除

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-MAT-01 | AC-04 | P0 | 新建 **Matter** Module 并进入 Assets，默认展示 **8** 张内置卡片 |
| TP-MT-MAT-02 | AC-04 | P0 | 8 张卡片自上而下顺序：Chip Config → Keys → Certificate → Firmware → Matter Config → Factory Data → General File → PS Software Package |
| TP-MT-MAT-03 | AC-04 | P0 | Matter Module 下上述 **8** 张卡片均为模板 **不可删除项**：删除操作 **置灰**或不可用（无引用 / 未进版本前提下仍不可删） |
| TP-MT-MAT-04 | 需求描述 | P1 | Add Module 弹框 Section 预览卡片与创建后 Assets 实际卡片 **一一对应**（弹框 **Certificates** ↔ Assets **Certificate**；**Programming Station Script** ↔ **PS Software Package**） |

### Secure Element Module — 默认卡片、不可删除与 Version 必填

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-SE-01 | AC-05 | P0 | 新建 **Secure Element** Module，Assets 默认展示：**SE**、**PS Software Package**、**General File**（共 3 张） |
| TP-MT-SE-02 | AC-05 | P0 | **SE** 卡片为模板 **不可删除项**：删除操作置灰或不可用 |
| TP-MT-SE-03 | AC-05 | P0 | SE Module 下 **PS Software Package**、**General File** **非**模板不可删除项（在无引用 / 未进版本等前提下 **可删除**，具体删除交互见 Story #602） |
| TP-MT-SE-04 | AC-05 | P0 | SE 卡片 **数据未填写 / 不充分** 时，创建 Product **Version** 该 Module **不出现在**可选 Module 列表中 |
| TP-MT-SE-05 | AC-05 | P0 | SE 卡片数据 **填写完整** 后，创建 Version 时该 Module **出现在**可选 Module 列表中 |

### Other Module — 默认卡片与 Version 校验

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-OTH-01 | AC-06 | P0 | 新建 **Other** Module，Assets 默认展示 **7** 张内置卡片，**不含 Matter Config** |
| TP-MT-OTH-02 | AC-06 | P0 | 7 张卡片为：Chip Config、Keys、Certificate、Firmware、Factory Data、General File、PS Software Package |
| TP-MT-OTH-03 | AC-06 | P0 | Other Module **无**模板不可删除项：各默认卡片在无引用 / 未进版本等前提下 **可删除**（删除流程见 Story #602） |
| TP-MT-OTH-04 | AC-06 | P0 | **chip config** 数据 **未填写 / 不充分** 时，创建 Version 该 Other Module **不出现在**可选 Module 列表中 |
| TP-MT-OTH-05 | AC-06 | P0 | **chip config** 填写完整、且 **未添加** Matter Config 卡片时，创建 Version 该 Module **可出现在**可选 Module 列表中 |
| TP-MT-OTH-06 | AC-06 | P0 | Other Module 通过 Story #602 **手动加回 Matter Config** 卡片后，若 matter 数据 **未填写 / 不充分**，创建 Version 该 Module **不出现在**可选 Module 列表中 |
| TP-MT-OTH-07 | AC-06 | P0 | 已加回 Matter Config 且 **chip config + matter 均填写完整** 时，创建 Version 该 Module **出现在**可选 Module 列表中 |

### 引用保护（跨 Module Type）

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-REF-01 | AC-07 | P0 | **Matter / SE / Other** 任一 Module 下，卡片内 **密钥或证书已被引用** 时，该卡片删除操作 **置灰**，无法删除 |
| TP-MT-REF-02 | AC-07 | P0 | 取消引用后，若该卡片 **非**模板不可删除项且未满足 Story #602 其他删除限制，删除操作 **恢复可用** |

### UI 设计对齐

| TP-ID | 来源 | 优先级 | 测试点 |
|-------|------|--------|--------|
| TP-MT-UI-01 | 需求描述 | P2 | Add Module 弹框、Module Type 控件布局与 [Figma node-id=11874-168328](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%AE%A1%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=11874-168328) 一致 |

---

## AC ↔ 测试点追溯矩阵

| Story AC | 覆盖测试点 | 覆盖状态 |
|----------|------------|----------|
| AC-01 Add Module + Module Type + Section 预览 | TP-MT-ADD-01～TP-MT-ADD-08 | ✅ |
| AC-02 Module 名称编辑 | TP-MT-EDT-01、TP-MT-EDT-02 | ✅ |
| AC-03 创建产品默认 Matter Module | TP-MT-PRD-01 | ✅ |
| AC-04 Matter 8 张默认卡 + 不可删除 | TP-MT-MAT-01～TP-MT-MAT-03 | ✅ |
| AC-05 SE 默认卡 + SE 不可删 + Version 必填 | TP-MT-SE-01～TP-MT-SE-05 | ✅ |
| AC-06 Other 7 张默认卡 + Version 校验 | TP-MT-OTH-01～TP-MT-OTH-07 | ✅ |
| AC-07 引用保护 | TP-MT-REF-01、TP-MT-REF-02 | ✅ |

**AC-01～AC-07 均已至少 1 条 P0 测试点覆盖。**

---

## 覆盖摘要

| 模块 | P0 | P1 | P2 | 合计 |
|------|----|----|-----|------|
| Add Module 弹框 | 6 | 3 | 0 | 9 |
| Module 名称编辑 | 2 | 0 | 0 | 2 |
| 创建产品默认 Module | 1 | 0 | 0 | 1 |
| Matter Module | 3 | 1 | 0 | 4 |
| Secure Element Module | 5 | 0 | 0 | 5 |
| Other Module | 7 | 0 | 0 | 7 |
| 引用保护 | 2 | 0 | 0 | 2 |
| UI 设计 | 0 | 0 | 1 | 1 |
| **合计** | **26** | **4** | **1** | **31** |

| 来源 | 条数 |
|------|------|
| Story AC（AC-01～AC-07） | 26 |
| 需求描述 | 2 |
| QA 扩展 | 1 |
| P1 / 待确认 | 2（含在 Add Module 模块 P1 计数内） |

---

## 待确认

- [ ] Add Module 弹框 **Secure Element / Other** 选中时 Section 预览卡片清单（Story MD 待补截图；TP-MT-ADD-06、TP-MT-ADD-07）
- [ ] **chip config / matter / SE**「数据充分」判定标准（必填字段清单或保存成功即算充分）
- [ ] Matter Module 8 张 **均不可删** 与 Story #602「非必填可删」交叉时，以 **601 模板不可删除** 为准（已在 TP-MT-MAT-03 按 601 编写，联调时与 #602 一并回归）

## Out of Scope

- 卡片增删隐藏、二次确认、固定位、内置/自定义卡片新增等通用流程（Story #602 / #603）
- SE 卡片内容导入、展示、订阅与 Version 拦截（Story #655 / #653 / #658）
- Module Type **创建后是否允许修改**（Product Doc 未述）

## 关联 Story

| 编号 | Story | 与本测试点关系 |
|:----:|-------|---------------|
| 602 | assets 卡片自定义 | 删除/新增/隐藏/固定位；Other 加回 Matter Config |
| 603 | 自定义卡片 | 自定义卡片不受本 Story Module Type 模板默认集约束 |
| 655/653/658 | SE 卡片系列 | SE Module 下 SE 卡片内容与管理 |
