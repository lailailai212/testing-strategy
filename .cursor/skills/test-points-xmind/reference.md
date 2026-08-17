# Reference — Test Points XMind

## 固定产出目录

| 产物 | 路径模板 |
|------|----------|
| 树 JSON | `docs/sprints/{sprint}/features/{slug}/xmind/{slug}.tree.json` |
| XMind | `docs/sprints/{sprint}/features/{slug}/xmind/{slug}-test-points.xmind` |

- `{feature-slug}`：经 `docs/sprints/features-registry.json` 反查 sprint，或传 `--sprint`
- 禁止写入：项目根、任意 `scripts/`、skill 目录内（`examples/` 下的参考 JSON 除外）
- 正式产出仅 `docs/sprints/{sprint}/features/{slug}/xmind/`

## JSON 树结构

| 字段 | 必填 | 说明 |
|------|------|------|
| `sheet_title` | 否 | XMind 画布名称，默认「测试点」 |
| `root_title` | 是 | 中心主题（Story / 功能名） |
| `tree` | 是 | 一级分支数组 |

### 节点类型

1. **分支**：`{ "title": "分支名", "children": [...] }`
2. **叶子（推荐）**：`{ "title": "一句话描述", "source": "AC-01", "priority": "P0" }`
3. **叶子（兼容旧版）**：字符串；若含 `TP-ID |` 前缀，生成时自动剥离

`children` 可混用对象叶子、字符串叶子与分支，递归嵌套。

### 叶子字段

| 字段 | 必填 | 说明 |
|------|------|------|
| `title` | ✅ | 测试点一句话描述 |
| `source` | 推荐 | 与测试点 MD「来源」列一致：`AC-0x` / `需求描述` / `QA扩展` |
| `priority` | 推荐 | `P0` / `P1` / `P2` / `P3`；含待确认可写 `P0 / 待确认` |

**不写 TP-ID**。追溯 ID 保留在 `acceptance.md` 的 `TP-ID` 列；展开功能用例时以 MD 为准。

### 从测试点 MD 转树 JSON

读取 `docs/sprints/{sprint}/features/{slug}/acceptance.md` 中各表：

| MD 列 | JSON 叶子字段 |
|-------|---------------|
| 测试点 | `title` |
| 来源 | `source` |
| 优先级 | `priority` |
| TP-ID | **不写入** XMind / tree JSON |

## XMind 叶子展示格式

脚本将叶子渲染为：

```text
[优先级][来源] 一句话描述
```

示例：

```text
[P0][AC-03] Applications 列表展示 Name、Email、Applied At、Status、Actions
[P1][QA扩展] 列表默认排序：Pending 排在 Rejected 之前
[P0][需求描述] 用户首次提交申请后，系统立即向 Tenant Admin 发送通知邮件
```

## 层级约定（Large 需求）

按**产品页面 / 模块目录**组织：

```text
中心主题（Story 名）
├── 页面或模块（如 Account 管理）
│   ├── 功能子区（如 Applications Tab）
│   │   └── 测试点叶子
│   └── 功能子区（如 审批操作）
└── 其他模块
```

原则：

- 中间层 = 用户导航路径，与 UI 结构对齐
- 叶子层 = 一条测试点主题（粗颗粒度）
- 不把单控件拆成多个叶子

## 依赖

```bash
pip install xmind
```

生成：

```bash
# 1. MD → tree JSON（可选）
python .cursor/skills/test-points-xmind/scripts/md_to_tree.py \
  --feature-slug {feature-slug}

# 2. tree JSON → XMind
python .cursor/skills/test-points-xmind/scripts/generate_xmind.py \
  --feature-slug {feature-slug}
```

校验 zip（推荐）：

```bash
python -c "import zipfile; z=zipfile.ZipFile('docs/sprints/_examples/features/product-asset-tag/xmind/product-asset-tag-test-points.xmind'); print(z.namelist())"
```

## 与上下游 Skill 的关系

| 阶段 | Skill | 产出 |
|------|-------|------|
| 1 | `story-acceptance-design` | `acceptance.md`（含 TP-ID、来源、优先级） |
| 2 | `test-points-xmind` | tree JSON + XMind（叶子无 TP-ID，含来源与优先级） |
| 3 | `functional-testcase-md` | 功能测试用例 MD（**以测试点 MD 为输入**，TP-ID 进标签列） |
