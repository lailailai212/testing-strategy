# key和cert Tag 字段 — 评论补测用例

> 来源：`acceptance.md`（同 feature 包）  
> 需求：[飞书 User Story #6996267987](https://project.feishu.cn/obis/userstory/detail/6996267987) key和cert增加tag字段与数据迁移  
> 变更类型：Hybrid（主 Logic：空格 / 1024 长度；次 UI：无删除入口）  
> 用例数：3（P0 × 3；Functional × 2，UI × 1）  
> 入口规则：**Assign Key** → Product Assets **Keys** 区域；**Assign Certificate** → Product Assets **Certificates** 区域（现网区域名以页面为准，历史文案可能为 Certifications）  
> 产品规则：Tag **不支持空格**（空格忽略或拦截，不得落库带空格名称）；长度上限 **1024**；**不支持删除**；Cert Tag 必填且含系统默认 google certificate config / matter config；Key Tag 非必填且无系统默认项；自定义 Tag 产品级共用  
> 补测说明：本表只覆盖 2026-08-11 产品评论指出的遗漏点。主路径样例见 `docs/sprints/_examples/features/product-asset-tag/testcases/product-asset-tag.md`；该样例中「Tag 删除 - 删除后下拉不再展示」与产品结论冲突，**以本表无删除入口为准**  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：`/Cloud/Product/Assets`  
> 标签列：`Key Cert Tag`  
> 备注列：来自评论/产品结论时写「来源」+ 原文要点；一条用例一个用户场景，步骤 ≤ 10

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Product-Assets】【Functional】Tag 新增 - Assign Key/Cert 含空格被忽略或拦截 | /Cloud/Product/Assets | Key Cert Tag | P0 | 1. 已登录且具备该产品 Asset 写权限<br>2. 已进入目标产品 **Assets**<br>3. Keys / Certificates 均有可 Assign 的资源（Cert 测空格时 Tag 仍须能提交，可用系统默认 Tag 对照）<br>4. 准备名称 `Tag Test`（中间含空格），确认产品下尚无同名去空格结果 `TagTest`（若已有则换一组如 `Spc Demo`） | [1] **Keys** → **Assign Key**，展开 Tag 下拉，在新增输入框键入 `Tag Test`，点击 Add<br>[2] 查看刚添加的 Tag 展示值；必要时提交 Assign 后看 Keys 列表 Tag 列<br>[3] 关闭后 **Certificates** → **Assign Certificate**，同样键入 `Tag Test`（或同组含空格名）并 Add<br>[4] 查看 Cert 侧 Tag 展示值与下拉选项 | [1] 可打开 Assign Key；输入过程空格被忽略或无法键入，或 Add 后名称不含空格<br>[2] 落库/选中的 Tag **不含空格**（如 `TagTest`）；不出现名为 `Tag Test` 的 Tag<br>[3] Assign Certificate 行为与 Key 一致<br>[4] 两侧均无带空格的 Tag 名称 | 来源 需求评论: 产品已明确「Tag 不支持空格」；补充用例：Assign Key/Cert 时输入含空格 Tag，确认系统忽略空格或拦截（与产品结论一致）。 |
| 【Product-Assets】【Functional】Tag 新增 - 长度 1024 可添加且超长被拦截 | /Cloud/Product/Assets | Key Cert Tag | P0 | 1. 已登录且具备该产品 Asset 写权限<br>2. 已进入目标产品 **Assets**，打开 **Assign Certificate** 或 **Assign Key** 并展开 Tag 新增<br>3. 准备 1024 个合法非空格字符（如字母重复），以及在此基础上再加 1 个字符得到 1025 长度字符串；两名称均未在该产品存在 | [1] 在 Tag 新增输入框粘贴 **1024** 字符，点击 Add<br>[2] 确认下拉/选中值为 1024 长度（可只核对角标或首尾+长度）<br>[3] 再粘贴 **1025** 字符，尝试 Add（若输入框拒绝继续键入则记录）<br>[4] 重新打开 Tag 下拉，确认没有 1025 长度的 Tag | [1][2] 1024 长度 Add 成功，Tag 可用<br>[3] 1025 被截断到 1024、出现错误提示、或 Add 不可用/无法输入第 1025 字<br>[4] 产品下不存在长度为 1025 的 Tag | 来源 需求评论: 开发已回复「只有长度限制 1024」；补充用例：输入 1025+ 字符，确认系统行为（截断/报错/拦截）。 |
| 【Product-Assets】【UI】Tag - Assign 弹窗与 Asset 列表无删除入口 | /Cloud/Product/Assets | Key Cert Tag | P0 | 1. 已登录且可查看/编辑该产品 Assets<br>2. 产品下至少有 1 个自定义 Tag，且 Keys、Certificates 列表至少各有 1 条记录（便于看 Tag 列） | [1] 打开 **Assign Key**，展开 Tag 下拉，查看每个选项及输入区<br>[2] 打开 **Assign Certificate**，展开 Tag 下拉（含 google certificate config / matter config 与自定义 Tag）<br>[3] 回到 Assets **Keys** 列表，查看 Tag 列及行内操作<br>[4] 查看 **Certificates** 列表 Tag 列及行内操作 | [1] Assign Key 无 Tag 删除按钮、删除图标或选项旁删除 ×<br>[2] Assign Certificate 同样无删除入口；系统默认项也不可删<br>[3] Keys 列表 Tag 列只读展示，无删除 Tag 操作<br>[4] Certificates 列表同样无删除 Tag 操作 | 来源 需求评论: 产品已明确「目前不支持」（删除）；补充用例：检查 Assign 弹窗、Asset 列表均无 Tag 删除操作入口。 |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | Assign Key/Cert 输入含空格 Tag | TP-TAG-SPC-01、TP-TAG-SPC-02 |
| 2 | 1024 可添加、1025 拦截 | TP-TAG-LEN-01、TP-TAG-LEN-02 |
| 3 | 弹窗与列表无删除入口 | TP-TAG-DEL-01、TP-TAG-DEL-02 |

**6 条补测 TP 均已被 1 条用例覆盖。**
