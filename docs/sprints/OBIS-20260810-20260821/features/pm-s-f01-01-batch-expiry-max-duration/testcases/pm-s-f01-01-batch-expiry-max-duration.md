# PM-S-F01-01 Batch Expiry Max. Duration 默认值 — 功能测试用例

> 来源：`docs/sprints/OBIS-20260810-20260821/features/pm-s-f01-01-batch-expiry-max-duration/acceptance.md`  
> 飞书 Story：[7067202174](https://project.feishu.cn/obis/userstory/detail/7067202174)  
> **变更类型**：UI/UX → 用例以 `【UI】` 为主；可改非默认值落库用 `【Functional】`  
> 用例数：5（P0 × 1，P1 × 3，P2 × 1）；类型分布：UI × 3，Functional × 2  
> UI 参考：`baseline/screenshots/ref-create-product-batch-expiry.png`（改后：Max Duration = 90）  
> 入口：Product 列表 → **Create Product** → **Batch Expiry Duration**；有效性验证走产品详情 → **Create Batch** → Expiry Time  
> 产品规则：仅改 Max Duration 默认值 30→90；Default Duration / Min Duration / 单位（Days）与校验范围不变；存量 Product 不回填；Create Batch 的 Expiry 不得超过 Product Max Duration  
> 用例名称：`【{模块 slug}】【{UI|Functional|E2E}】{子功能} - {描述}`（`/Cloud/Product` → `Product`）  
> 备注约定：来自 AC 写 `来源 AC-0x: {AC 原文}`；否则 `来源 需求描述:` / `来源 QA扩展:`  
> 标签：`Batch Expiry Max Duration`（禁止写入 TP/AC 编号）

### 场景与 TP 覆盖

| 用例场景 | 覆盖 TP |
|----------|---------|
| 打开 Create Product：Max Duration 默认 90（对照改前 30） | TP-PROD-BED-01、TP-PROD-BED-02 |
| 同分区其余字段/单位未误改 | TP-PROD-BED-03 |
| 用户改 Max 为非默认合法值并创建成功 | TP-PROD-BED-04 |
| 中英文默认值一致 | TP-PROD-BED-05 |
| Create Batch：Expiry 受 Max Duration=90 约束（界内成功 / 超限阻断） | TP-PROD-BED-06 |

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Product】【UI】Create Product - Max Duration 默认值为 90 天 | /Cloud/Product | Batch Expiry Max Duration | P0 | 1. 已登录且具备创建 Product 权限<br>2. 可进入 Product 列表并打开 Create Product<br>3. 已知改前基线：同入口 Max Duration 默认为 **30**（Days） | [1] 进入 Product 列表，点击打开 **Create Product**<br>[2] 滚动至 **Batch Expiry Duration** 分区，定位 **Max Duration** 输入框与右侧单位<br>[3] 不做任何编辑，直接读取 Max Duration 当前展示值<br>[4] 关闭后再次打开 Create Product，再次读取 Max Duration 初始值 | [1] Create Product 弹窗/表单打开<br>[2] Max Duration 可见，单位为 **Days**<br>[3] 默认值为 **90**（非 30）；无需手动修改即可看到新默认值<br>[4] 再次打开仍默认为 **90**，与改前基线 30 形成对照 | 来源 AC-01: 用户进入 Create Product 页面时，Batch Expiry Duration 的 Max. Duration 字段默认值应为 90 天（改前为 30 天）。 |
| 【Product】【UI】Create Product - Batch Expiry 其余字段与单位未变 | /Cloud/Product | Batch Expiry Max Duration | P1 | 1. 已登录且可打开 Create Product<br>2. 对照 baseline 截图：Default Duration=30、Min Duration=1、单位 Days | [1] 打开 **Create Product**，定位 **Batch Expiry Duration**<br>[2] 读取 **Default Duration** 默认值与单位<br>[3] 读取 **Min Duration** 默认值与单位<br>[4] 抽检 Max/Min 合法性：将 Max 改为小于 Min（如 Min=1 时将 Max 改为 0 或空后失焦/提交），观察是否仍有阻断；再改回合法区间 | [1] 分区可见（含 Default / Min / Max）<br>[2] Default Duration 默认为 **30**，单位 **Days**（与改前一致）<br>[3] Min Duration 默认为 **1**，单位 **Days**（与改前一致）<br>[4] 非法 Max/Min 关系仍被校验阻断；单位始终为天；除 Max 默认值外无新增/缺失字段 | 来源 AC-01（P1）: 用户进入 Create Product 页面时，Min. Duration、Batch Expiry Duration 其余字段、校验范围与单位应与改动前一致，仅 Max. Duration 默认值变化。<br>来源 需求描述: 本期只改 Max. Duration 默认值；Min. Duration、校验范围、单位及其他 Batch Expiry 字段均不变。 |
| 【Product】【Functional】Create Product - Max Duration 可改为非默认值并落库 | /Cloud/Product | Batch Expiry Max Duration | P1 | 1. 已登录且可创建 Product<br>2. 准备唯一 Product Name 及必填项（Vendor、Max.Volume 等）<br>3. 选定合法非默认 Max Duration（如 **60**，且 ≥ Min、符合校验） | [1] 打开 Create Product，确认 Max Duration 初始为 90<br>[2] 将 Max Duration 改为 **60**（或其它非 90 合法值）<br>[3] 填写其余必填项并提交创建<br>[4] 打开该 Product 的编辑/详情中 Batch Expiry Duration 配置（或等价入口），读取已保存的 Max Duration | [1] 初始默认为 90<br>[2] 可成功改为 60，控件接受输入<br>[3] 创建成功<br>[4] 落库/回显为用户输入的 **60**，**非**被强制改回 90 | 来源 QA扩展: 用户可将 Max. Duration 改为非默认合法值并提交成功；成功落库值为用户输入值而非强制 90 |
| 【Product】【UI】Create Product - 中英文 Max Duration 默认均为 90 | /Cloud/Product | Batch Expiry Max Duration | P2 | 1. 环境可切换中/英文<br>2. 已登录且可打开 Create Product | [1] 英文界面下打开 Create Product，读取 Max Duration 默认值与单位<br>[2] 切回中文界面，再次打开 Create Product 读取 Max Duration | [1] 英文下 Max Duration 默认为 **90**，单位为天（Days）<br>[2] 中文下同样为 **90**；中英默认值一致 | 来源 QA扩展: 中/英文界面下 Max. Duration 默认值均为 90 天 |
| 【Product-Batch】【Functional】Create Batch - Expiry 受 Max Duration=90 约束有效 | /Cloud/Product/Batch/Create | Batch Expiry Max Duration | P1 | 1. 已登录且可创建 Product / Batch<br>2. 已用 Create Product **保持 Max Duration=90**（默认不改）创建目标 Product，并具备可创建 Batch 的 Version / Factory 等前置<br>3. 已知「今天 + N 天」的日期换算方式（含时区/日终 23:59:59 若产品有） | [1] 进入该 Product → **Create Batch**<br>[2] 将 **Expiry Time** 设为不超过 Max 的边界合法日（建议 **今天 + 90 天**，或界面允许的最大可选日），填写其余必填项后提交<br>[3] 再次进入 Create Batch，将 Expiry Time 设为超出 Max（建议 **今天 + 91 天**，或超过可选上限），尝试提交<br>[4]（可选）将 Expiry Time 设为 Default Duration 对应日（今天 + 30 天）并提交，确认默认时长仍可用 | [1] Create Batch 表单打开，Expiry Time 可编辑<br>[2] **界内**创建成功；Batch 列表/详情中 Expiry 与所选日期一致<br>[3] **超限被阻断**（不可选该日，或提交失败并提示超出 Max Duration / 有效期上限）；不产生超限 Batch<br>[4] 今天 + 30 天可成功创建（Default Duration 未因 Max 改 90 而失效） | 来源 QA扩展: 使用 Max Duration 默认 90 创建的 Product：Create Batch 时 Expiry Time 在上限内可成功，超出 Max Duration（>90 天）应被阻断，证明有效期约束生效 |

---

## 待确认（执行时）

- [ ] 创建成功后核对 Max Duration 落库的入口（Edit Product / 产品设置 / 其它）以环境实际为准
- [ ] Max/Min 非法组合的具体校验文案与改前基线对齐方式（若无改前环境，以开发说明为准）
- [ ] 截图中 **Default Duration=30** 为本期不改字段；勿与 Max Duration 混淆
- [ ] Create Batch 超限表现是「日期不可选」还是「可选但提交报错」（以现网交互为准，两种均视为约束生效）
