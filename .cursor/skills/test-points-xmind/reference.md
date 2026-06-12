# Reference — Test Points XMind

## 固定产出目录

本 skill 生成的文件**必须**落在仓库固定目录，便于版本管理与协作 diff。

| 产物 | 路径模板 |
|------|----------|
| 树 JSON | `docs/generate_doc/test-points-xmind/trees/{feature-slug}.tree.json` |
| XMind | `docs/generate_doc/test-points-xmind/{feature-slug}-test-points.xmind` |

- `{feature-slug}`：小写英文连字符（例：`product-asset-tag`）
- 禁止写入：项目根、任意 `scripts/`、skill 目录内（`examples/` 下的参考 JSON 除外）
- 生成脚本支持 `--feature-slug {slug}` 自动解析上述路径

## JSON 树结构

| 字段 | 必填 | 说明 |
|------|------|------|
| `sheet_title` | 否 | XMind 画布名称，默认「测试点」 |
| `root_title` | 是 | 中心主题（Story / 功能名） |
| `tree` | 是 | 一级分支数组 |

### 节点类型

1. **叶子**：字符串，格式 `TP-ID | 一句话描述`
2. **分支**：对象 `{ "title": "分支名", "children": [...] }`

`children` 可混用字符串与对象，递归嵌套。

## 层级约定（Large 需求）

按**产品页面 / 模块目录**组织，而非按控件拆条：

```text
中心主题（Story 名）
├── 页面或模块（如 Product Asset）
│   ├── 功能子区（如 Assign Security Key）
│   │   └── 测试点叶子
│   └── 功能子区（如 Asset 列表展示）
└── 其他页面（如 Version 详情页）
```

原则：

- 中间层 = 用户导航路径（目录、Tab、弹窗名），与 UI 结构对齐
- 叶子层 = 测试点（粗颗粒度，一条主题一个 TP-ID）
- 不把「控件可见」「单选」「下拉展开」拆成多个叶子

## TP-ID 命名

| 段 | 含义 | 示例 |
|----|------|------|
| 前缀 | `TP` | 固定 |
| 模块缩写 | 页面/模块 | `PA` = Product Asset，`VER` = Version，`PD` = Product Detail |
| 子区缩写 | 可选 | `KEY`、`CERT`、`TAG`、`LIST` |
| 序号 | 两位数字 | `01` |

示例：`TP-PA-KEY-01`、`TP-VER-02`

## 叶子标题格式

```text
TP-{模块}-{子区}-{序号} | {一句话测试点}
```

- `|` 分隔 ID 与描述（XMind 里一眼可扫）
- 描述用分号串联同条测试点内的多个检查项，不拆成多个叶子

## 依赖

```bash
pip install xmind
```

生成后校验（推荐）：

```bash
python -c "import zipfile; z=zipfile.ZipFile('docs/generate_doc/test-points-xmind/foo.xmind'); print(z.namelist())"
```

**期望包含**（XMind 桌面版可打开）：

```text
content.xml
meta.xml
styles.xml
comments.xml
META-INF/manifest.xml
```

> Python `xmind` 库默认只写前三个 XML；`generate_xmind.py` 会自动补 `meta.xml` 与 `META-INF/manifest.xml`。  
> 重新生成时会**覆盖**已有 `.xmind`，避免在旧文件上叠加导致内容重复。

## 与 story-acceptance-design 的关系

| 阶段 | Skill | 产出 |
|------|-------|------|
| 1 | `story-acceptance-design` | 验收条目 / 测试点表（Markdown） |
| 2 | `test-points-xmind` | 同上结构的 XMind 脑图 |

先有条目表再导图；若用户只要求 XMind 且尚无测试点，先按 `story-acceptance-design` 粗颗粒度规则写条目，再转树。
