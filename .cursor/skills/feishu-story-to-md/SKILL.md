---
name: feishu-story-to-md
description: >-
  从飞书项目拉取 User Story 并导出为脱敏 Markdown，本地化参考图到 story/ 目录，并读取图片补充需求规格。
  Use when 用户提供飞书 Story 链接/ID、要求 story 转 md、拉取飞书需求、导出 Story 文档。
---

# Feishu Story to Markdown

将飞书 User Story 转为结构化、脱敏、可离线阅读的 Markdown，供后续 `story-acceptance-design` 生成 AC。**本 Skill 只导出 MD，不生成 AC。**

## 前置条件

- 飞书 MCP（`FeishuProjectMcp`）已配置且可用
- 输出目录：项目根 `story/`

## 输入（优先级）

1. **`project_key` + `work_item_id`**（首选）→ `get_workitem_brief({ project_key, work_item_id, fields: ["_all"] })`
   - 示例：`obis 6993175767`、`project: obis, id: 6993175767`
2. **完整 URL**（备选，可从中解析 project 与 id）→ `get_workitem_brief({ url, fields: ["_all"] })`
3. **仅 `work_item_id`** → 提示用户补充 `project_key`

`fields: ["_all"]` 不可省略。可选调 `list_workitem_comments` 提取待确认项。

## 工作流

1. 解析输入，确定 `project_key` 与 `work_item_id`
2. 拉取全量字段
3. 脱敏清洗
4. 结构化 Product Doc（及 Description 等正文字段；Product Doc 为空时用其他字段）
5. 下载参考图到 `story/{basename}/images/`
6. **读取本地参考图**，将图中可见的 UI 规格、交互、标注补充进对应需求小节（见「参考图识读」）
7. 写入 `story/{basename}/{basename}.md`
8. 告知文件路径与待确认摘要

## 脱敏

导出 MD **不得包含**：姓名、邮箱、`@提及`、mention 块、用户 key/id、`create_by`/`updated_by`/`owners`/`members` 中的个人信息。

**保留**：Story 标题、编号、状态、优先级、Sprint、Epic、需求正文。

- 创建/更新：只写日期，不写人名
- 评论：去掉 `@提及` 和 mention 块，只保留与需求相关的文字
- **不导出** `role_members`、`work_item_current_node`（对 AC / 用例生成无帮助）

Skill 文档本身也不得写入真实姓名、邮箱等敏感信息；说明脱敏规则时用抽象描述，勿写「原文 vs 导出」对照表。

## 飞书返回数据怎么用

MCP 返回的 Story 数据分两块，导出时按下面规则填入 MD：

**固定信息**（响应里的 `work_item_attribute`）→ 填元信息区：

| 飞书字段 | 填入 MD |
|----------|---------|
| `work_item_name` | 标题 |
| `work_item_id` | 来源链接中的 id |
| `owned_project` | 空间名称与 `project_key` |
| `work_item_status` | 状态 |
| `create_time` / `update_time` | 创建 / 更新日期 |

**自定义字段**（响应里的 `work_item_fields`）→ 各空间字段名相同、内部 key 可能不同，**按字段显示名 `name` 匹配**，不要死记 key：

| 字段显示名 `name` | 填入 MD |
|-------------------|---------|
| Auto Number | 编号 |
| Priority | 优先级（取 `label`） |
| Sprint | Sprint |
| Epic | Epic（含 id） |
| Story Point (QC/DEV) | Story Point |
| Product Doc | **需求正文**（含图片，最重要） |
| Description | Product Doc 为空或「暂无」时作需求正文 |
| Tech Doc | 有内容则单独一节 |

匹配不到时调 `list_workitem_field_config` 查该空间的字段列表。

## Product Doc 解析

- 空行分段，独立需求句转为列表项
- `~~删除线~~` → 记入 **Out of Scope**（仅在有内容时输出该节，见输出模板）
- `<!-- ... -->` → 删除
- `![](飞书URL)` → 下载后改为相对路径，并触发「参考图识读」
- 合并同主题内容为 `### N. [主题]`；无法归纳时用 `需求点 N`

## 图片本地化

Product Doc 中的飞书图片**禁止**以 CDN 外链留在 MD 中。

1. 正则提取 `![](https://project.feishu.cn/...)` URL
2. `get_download_url({ project_key, work_item_id, file_url })`
3. `curl -L -o ... -H "X-Meego-File-Sign: {sign}" "{url}"` 下载
4. 保存到 `story/{basename}/images/ref-01.png`（扩展名按 Content-Type，未知默认 `.png`）
5. 评论附件中的原型/截图同理本地化，按实际类型命名（如 `.html`、`.png`）

`is_multipart` 为 true 时按返回的 `part_index`、`start_byte`、`end_byte` 分片下载后合并。单张失败写 `<!-- 参考图 N 下载失败 -->`，不中断导出。

## 参考图识读

下载完成后，**读取** `story/{basename}/images/` 下的每张图片，将可见信息补充进需求正文：

- **识读内容**：UI 布局、控件位置、标注数值（字号/行高/颜色）、交互状态（展开/收起、选中态）、树形/列表结构、Tab 名称等
- **写入方式**：补充到对应 `###` 小节内，用列表或表格；图片引用挂在该小节下，**不要**在文末单独堆「参考图」章节
- **优先级**：图中标注 > Product Doc 文字 > 推断；推断项写入「评论 / 待确认」
- **多张图**：按内容关联到不同小节；同一张图可跨节引用
- **已取消需求**：原文删除线或明确 Out of Scope 的，图仅作说明，不写入需求描述

## 文件命名

每个 Story 独占一个目录，`basename` = `{project_key}-{work_item_id}-{slug}`：

```
story/{basename}/
  {basename}.md
  images/ref-01.png
```

`slug`：标题转小写（英文）、空格改 `-`、保留中文、去掉 URL 不安全字符、合并连续 `-`。已存在则覆盖前告知用户。

## 输出模板

```markdown
# Story: [标题]

**来源**: [飞书项目 User Story #{id}]({url})
**空间**: [名称] (`{project_key}`)
**类型**: User Story
**编号**: [Auto Number]
**状态**: [状态]
**优先级**: [Priority]
**Sprint**: [Sprint]
**Epic**: [Epic] (#{id})
**Story Point**: [值]
**创建**: [日期]
**更新**: [日期]

---

## 需求描述（Product Doc）

### 1. [主题]
- ...
- **设计规格（来自参考图 ref-01）**：...

![参考图 1 — 简要说明](./images/ref-01.png)

---

## Tech Doc

- [有内容才写此节]

## 评论 / 待确认

- [日期]：[需求相关内容]

## Out of Scope

[仅当存在删除线、明确排除项或已取消需求时输出此节；无则整节省略]
```

## 用户指令

| 用户说法 | 行为 |
|----------|------|
| `{project} {id}` / 拉取 / 转 md | **首选** project_key + work_item_id |
| Story 链接 | 从 URL 解析 project 与 id，或直接用 `url` 参数 |
| 仅 id | 追问 project_key |
| 顺便生成 AC | 仅导出 MD，AC 交 `story-acceptance-design` |

## 完成后

告知：MD 路径、图片目录（若有）、待确认摘要；下一步可用 `story-acceptance-design` 生成 AC。
