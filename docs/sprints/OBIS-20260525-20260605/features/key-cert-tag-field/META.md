# META — key-cert-tag-field

- feature-slug: `key-cert-tag-field`
- sprint: `OBIS-20260525-20260605`（飞书 Sprint 字段）
- story-id: `6996267987`
- story-path: —
- status: `cases-ready`

## Layout

```text
features/key-cert-tag-field/
├── META.md
├── acceptance.md
└── testcases/
    └── key-cert-tag-field.md
```

## Notes

- 飞书：[User Story #6996267987](https://project.feishu.cn/obis/userstory/detail/6996267987)（key和cert增加tag字段与数据迁移）
- 本包为 **2026-08-11 产品评论补测**：空格约束、长度 1024、不支持删除。主路径黄金样例仍见 `docs/sprints/_examples/features/product-asset-tag/`；其中「Tag 删除后下拉不再展示」与产品结论冲突，**以本包「无删除入口」为准**。
- 评论中 pixiu #104904 Step 1 ERROR 为执行记录核实项，不新增用例。
