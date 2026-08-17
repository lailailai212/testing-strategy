# OBIS 角色权限矩阵 — 回归测试用例

> 来源：`acceptance.md`（同 feature 包）  
> 需求：OBIS 角色分类与权限说明（产品内 / 工厂赋权路径 + 无权限不显示 + 接口绕过）  
> 变更类型：Logic（主）；UI 仅作「入口不显示」的可观察点  
> 用例数：16（P0 × 11，P1 × 4，P2 × 1；E2E × 7，UI × 6，Functional × 3）  
> 入口规则：产品角色 → Product 详情 **Member** → 行内 **⋮** 编辑；工厂角色 → Factory 详情 **Member** → **Add User** / **Edit User**  
> 产品规则：无权限时写入口 **不显示**；Factory Admin 与 Factory Manager **不是**同一角色；Transfer Admin 不能当作赋 Manager 的主路径  
> 写入口抽样：按角色名对照 IoT Admin 现网（见 acceptance 表）；执行不一致则记缺陷或回写矩阵  
> 账号：前置按角色名；邮箱台账执行前补齐，本文不写 OTP  
> 设计原则：一条用例一个用户场景；步骤 ≤ 10；本包独立，不引用已有权限用例  
> 用例名称格式：`【{模块 slug}】【UI|Functional|E2E】{子功能} - {描述}`  
> 所属模块：`/Cloud/Product/Member`、`/Cloud/Product/Overview`、`/Cloud/Product/Version`、`/Cloud/Product/Batch`、`/Cloud/Product/Assets`、`/Cloud/Ecosystem/Factory/Factory Info`  
> 标签列：`角色权限矩阵回归`  
> 备注列：来自 AC 时写 `来源 AC-0x: {AC 原文}`

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 【Product-Member】【E2E】编辑产品内角色 - ⋮ 改为 Version Manager 后权限生效 | /Cloud/Product/Member | 角色权限矩阵回归 | P0 | 1. 使用该产品 **Owner** 或 **Product Manager** 登录<br>2. 目标用户已在该产品 Member，当前角色不是 Version Manager<br>3. 目标用户可另开会话登录 | [1] 进入产品详情 → **Member**<br>[2] 打开目标用户行 **⋮**，核对可选角色<br>[3] 将该用户改为 **Version Manager** 并保存<br>[4] 目标用户刷新或重新登录，进入同一产品 **Version** Tab，观察 Create Version | [1] Member 列表可见<br>[2] 可选 Owner、Product Manager、Resource Manager、Version Manager、Batch Manager、Member<br>[3] 列表 Role 更新为 Version Manager<br>[4] 可见 Create Version | 来源 AC-01: 具备该产品 Member 管理权限的用户，在 Product 详情 Member 列表通过行内 ⋮ 编辑目标用户的产品内角色（Owner / Product Manager / Resource Manager / Version Manager / Batch Manager / Member），保存后列表 Role 更新，目标用户重新登录或刷新后权限按新角色生效。 |
| 【Product-Member】【UI】无 Member 管理权限 - 不显示 Add 与 ⋮ 编辑 | /Cloud/Product/Member | 角色权限矩阵回归 | P0 | 1. 使用该产品内仅 **Member** 的账号登录<br>2. 可进入同一产品详情 | [1] 进入产品详情 → **Member**<br>[2] 观察列表上方是否有 Add<br>[3] 观察任意成员行是否有 **⋮** 编辑角色 | [1] Member Tab 可打开、列表可查看<br>[2] **不显示** Add<br>[3] **不显示** ⋮ 编辑角色 | 来源 AC-02: 不具备该产品 Member 管理权限的用户进入同一产品 Member Tab 时，不显示 Add 与行内 ⋮ 编辑角色入口。 |
| 【Ecosystem-Factory-Factory-Info】【E2E】Add User - 可分别赋予 Factory Admin 与 Factory Manager | /Cloud/Ecosystem/Factory/Factory Info | 角色权限矩阵回归 | P0 | 1. 使用具备该工厂 Member 管理权限的账号登录<br>2. 同租户有两名尚未加入该工厂的 Active 用户（或一名可先后测，测完还原） | [1] 进入工厂详情 → **Member** → **Add User**<br>[2] 选择用户，角色选 **Factory Admin** 并保存<br>[3] 再 Add User（或换用户），角色选 **Factory Manager** 并保存<br>[4] 核对 Member 列表 Role 列 | [1] Add User 可见可打开<br>[2] 保存成功；该用户 Role 为 Factory Admin<br>[3] 保存成功；该用户 Role 为 Factory Manager<br>[4] Admin 与 Manager 为两个不同 Role 值，不是同一角色 | 来源 AC-03: 具备该工厂 Member 管理权限的用户，在 Factory 详情 Member 通过 Add User 或 Edit User 将用户设为 Factory Admin 或 Factory Manager（二者不是同一角色），保存后列表 Role 与该用户权限按所选角色生效。 |
| 【Ecosystem-Factory-Factory-Info】【E2E】Edit User - 在 Admin 与 Manager 之间切换 | /Cloud/Ecosystem/Factory/Factory Info | 角色权限矩阵回归 | P0 | 1. 有工厂 Member 管理权限账号已登录<br>2. 目标用户已在 Member，当前为 Factory Manager | [1] Member 打开该用户 **Edit User**<br>[2] 改为 **Factory Admin** 并保存<br>[3] 用目标用户会话进入该工厂 Member，观察 Admin 行是否出现 Transfer Admin | [1] Edit User 可打开，角色可选 Admin 与 Manager<br>[2] 列表 Role 变为 Factory Admin<br>[3] 目标用户可见 Transfer Admin（与 Manager 时不同） | 来源 AC-03: 具备该工厂 Member 管理权限的用户，在 Factory 详情 Member 通过 Add User 或 Edit User 将用户设为 Factory Admin 或 Factory Manager（二者不是同一角色），保存后列表 Role 与该用户权限按所选角色生效。 |
| 【Ecosystem-Factory-Factory-Info】【UI】无工厂 Member 管理权限 - 不显示 Add User 与 Edit User | /Cloud/Ecosystem/Factory/Factory Info | 角色权限矩阵回归 | P0 | 1. 使用无该工厂 Member 管理权限的账号登录（如仅 Factory Manager 且现网不允许其加用户，或以未加入工厂的只读账号对照；以现网为准）<br>2. 仍可打开该工厂详情 Member（若完全无法进入工厂则改用可查看但无管理权的账号） | [1] 进入工厂详情 → **Member**<br>[2] 观察是否有 **Add User**<br>[3] 观察成员行是否有 **Edit User** | [1] Member 可打开<br>[2] **不显示** Add User<br>[3] **不显示** Edit User | 来源 AC-04: 不具备该工厂 Member 管理权限的用户进入同一工厂 Member Tab 时，不显示 Add User 与 Edit User。 |
| 【Product-Overview】【UI】仅 Member - 不显示各写入口 | /Cloud/Product/Overview | 角色权限矩阵回归 | P0 | 1. 账号在该产品内角色仅为 **Member**<br>2. 产品已有 Version / Batch / Assets 数据便于对照 | [1] 进入产品 Overview，观察产品名/设置是否可编辑<br>[2] 打开 Assets，观察编辑/Add<br>[3] 打开 Version、Batch，观察 Create Version、Create Batch<br>[4] 打开 Member，观察 Add 与 ⋮ | [1] 可查看 Overview；产品信息编辑入口不显示<br>[2] Assets 编辑/Add **不显示**<br>[3] Create Version、Create Batch **不显示**<br>[4] Add 与 ⋮ **不显示** | 来源 AC-06: 产品内角色为 Member 的用户可进入该产品详情查看，但不显示 Create Version、Create Batch、Assets 编辑/Add、Member Add / ⋮ 编辑。 |
| 【Product-Overview】【E2E】仅 Owner - 四类写入口均可用 | /Cloud/Product/Overview | 角色权限矩阵回归 | P0 | 1. 账号在该产品内仅为 **Owner**（或明确含 Owner 且无其它产品角色亦可）<br>2. 产品允许创建 Version / Batch；Assets 可编辑 | [1] Overview 尝试编辑产品信息并保存（或打开设置）<br>[2] Assets 打开编辑/Add 并保存一条不破坏数据的改动（或仅确认可点后 Cancel）<br>[3] Version 打开 Create Version，填必填项提交或确认向导可进入<br>[4] Batch 打开 Create Batch，确认入口可用<br>[5] Member 打开 ⋮，确认可编辑角色 | [1] 产品信息可编辑<br>[2] Assets 写入口显示且可操作<br>[3] Create Version 显示且可进入创建<br>[4] Create Batch 显示且可进入创建<br>[5] ⋮ 编辑角色显示 | 来源 AC-05: 用户仅拥有某一产品内角色时，只展示该角色职责对应的写入口；无权限的写入口不显示（对照上表抽样）。 |
| 【Product-Version】【E2E】仅 Version Manager - 可创建 Version 且无 Batch/Member 写入口 | /Cloud/Product/Version | 角色权限矩阵回归 | P0 | 1. 账号在该产品内仅为 **Version Manager**<br>2. 创建 Version 所需必填 Asset 已充分 | [1] 进入 Version Tab，点击 Create Version 并完成创建（或走到可提交页）<br>[2] 打开 Batch Tab，观察 Create Batch<br>[3] 打开 Member Tab，观察 Add 与 ⋮ | [1] Create Version 显示；创建成功或向导可提交<br>[2] Create Batch **不显示**<br>[3] Add 与 ⋮ **不显示** | 来源 AC-05: 用户仅拥有某一产品内角色时，只展示该角色职责对应的写入口；无权限的写入口不显示（对照上表抽样）。 |
| 【Product-Batch】【E2E】仅 Batch Manager - 可创建 Batch 且无 Version/Member 写入口 | /Cloud/Product/Batch | 角色权限矩阵回归 | P0 | 1. 账号在该产品内仅为 **Batch Manager**<br>2. 已有可用 Version，满足创建 Batch 前置 | [1] 进入 Batch Tab，点击 Create Batch 并完成创建（或走到可提交页）<br>[2] 打开 Version Tab，观察 Create Version<br>[3] 打开 Member Tab，观察 Add 与 ⋮ | [1] Create Batch 显示；创建成功或向导可提交<br>[2] Create Version **不显示**<br>[3] Add 与 ⋮ **不显示** | 来源 AC-05: 用户仅拥有某一产品内角色时，只展示该角色职责对应的写入口；无权限的写入口不显示（对照上表抽样）。 |
| 【Product-Assets】【E2E】仅 Resource Manager - 可编辑 Assets 且无 Version/Batch/Member 写入口 | /Cloud/Product/Assets | 角色权限矩阵回归 | P0 | 1. 账号在该产品内仅为 **Resource Manager** | [1] 进入 Assets，打开 Chip Config 或 Keys 的编辑/Add，确认可操作后 Cancel 或保存可回滚改动<br>[2] 打开 Version、Batch，观察 Create Version、Create Batch<br>[3] 打开 Member，观察 Add 与 ⋮ | [1] Assets 编辑/Add 显示且可进入编辑<br>[2] Create Version、Create Batch **不显示**<br>[3] Add 与 ⋮ **不显示** | 来源 AC-05: 用户仅拥有某一产品内角色时，只展示该角色职责对应的写入口；无权限的写入口不显示（对照上表抽样）。 |
| 【Product-Overview】【UI】仅 Product Manager - 可管产品与 Member、不显示 Version/Batch 创建 | /Cloud/Product/Overview | 角色权限矩阵回归 | P1 | 1. 账号在该产品内仅为 **Product Manager** | [1] Overview 观察产品信息是否可编辑<br>[2] Member 观察 Add / ⋮<br>[3] Version / Batch 观察 Create Version、Create Batch | [1] 产品信息可编辑<br>[2] Add 或 ⋮ 显示（具备 Member 管理）<br>[3] Create Version、Create Batch **不显示** | 来源 AC-05: 用户仅拥有某一产品内角色时，只展示该角色职责对应的写入口；无权限的写入口不显示（对照上表抽样）。 |
| 【Ecosystem-Factory-Factory-Info】【UI】Factory Admin - 可见 Transfer Admin | /Cloud/Ecosystem/Factory/Factory Info | 角色权限矩阵回归 | P0 | 1. 当前登录用户为该工厂 **Factory Admin** 本人 | [1] 进入工厂 Member<br>[2] 打开本人 Admin 行菜单<br>[3] 点击 Transfer Admin | [1] Member 可见<br>[2] 菜单含 Transfer Admin<br>[3] 弹窗可打开（本条不强制完成移交） | 来源 AC-07: Factory Admin 与 Factory Manager 权限不同：Admin 本人可见 Transfer Admin；Factory Manager 不显示 Transfer Admin。 |
| 【Ecosystem-Factory-Factory-Info】【UI】Factory Manager - 不显示 Transfer Admin | /Cloud/Ecosystem/Factory/Factory Info | 角色权限矩阵回归 | P0 | 1. 当前登录用户为该工厂 **Factory Manager**（不是 Admin） | [1] 进入工厂 Member<br>[2] 打开本人行菜单及 Admin 行菜单（若可见）<br>[3] 全页搜索 Transfer Admin | [1] Member 可打开<br>[2][3] **不显示** Transfer Admin | 来源 AC-07: Factory Admin 与 Factory Manager 权限不同：Admin 本人可见 Transfer Admin；Factory Manager 不显示 Transfer Admin。 |
| 【Product-Version】【Functional】无权限绕过 - 创建 Version/Batch 或改 Member 被拒绝 | /Cloud/Product/Version | 角色权限矩阵回归 | P1 | 1. 使用产品内仅 **Member** 的会话（可抓包或直链）<br>2. 已知创建 Version、创建 Batch、编辑 Member 的请求形态（对照有权限账号）<br>3. 记录当前 Version / Batch / Member 数量 | [1] 用无权限会话直接打开 Create Version 直链（若有）或重放创建 Version 接口<br>[2] 同样尝试创建 Batch<br>[3] 尝试编辑 Member 角色<br>[4] 用有权限账号刷新列表核对是否新增/改角色 | [1][2][3] 被拒绝（403 或业务错误）；页面无对应写入口可提交<br>[4] 无新增 Version/Batch，Member 角色未变 | 来源 AC-08: 无权限用户通过直链或接口发起创建 Version / Batch、编辑产品 Member、Factory Add User 时，请求被拒绝且不落库。 |
| 【Ecosystem-Factory-Factory-Info】【Functional】无权限绕过 - Factory Add User 被拒绝 | /Cloud/Ecosystem/Factory/Factory Info | 角色权限矩阵回归 | P1 | 1. 无该工厂 Member 管理权限的会话<br>2. 已知 Add User / 改角色接口<br>3. 记录当前 Member 名单 | [1] 直链打开 Add User 或重放加用户/改角色请求<br>[2] 刷新 Member 列表 | [1] 请求被拒绝<br>[2] Member 名单与角色未变 | 来源 AC-08: 无权限用户通过直链或接口发起创建 Version / Batch、编辑产品 Member、Factory Add User 时，请求被拒绝且不落库。 |
| 【Product-Member】【Functional】多角色叠加 - 写入口取并集 | /Cloud/Product/Member | 角色权限矩阵回归 | P2 | 1. 同一用户在该产品同时拥有 Version Manager 与 Batch Manager（或 Owner 以外的两角色）<br>2. **并集规则待确认**；若产品规定非并集，以产品结论改本条 | [1] 该用户进入 Version 与 Batch<br>[2] 观察 Create Version 与 Create Batch | [1] 两 Tab 可进<br>[2] 两创建入口均显示（按并集）；若现网只显示其一，记录实际并回写 acceptance | 来源 QA扩展: 同一用户可被赋予多个产品内角色时，写入口取并集（待确认；确认前按现网记录） |

---

## 场景与 TP 覆盖

| # | 用户场景 | 覆盖 TP |
|---|----------|---------|
| 1 | 产品 ⋮ 改角色并生效 | PRD-MEM-01、02 |
| 2 | 无权限不显示产品 Member 编辑 | PRD-MEM-03 |
| 3 | 工厂 Add User 赋两种角色 | FAC-MEM-01 |
| 4 | 工厂 Edit User 切换角色 | FAC-MEM-02 |
| 5 | 无权限不显示工厂 Add/Edit | FAC-MEM-03 |
| 6 | 仅 Member 无写入口 | PRD-CAP-01 |
| 7 | 仅 Owner 四类写入口 | PRD-CAP-02 |
| 8 | 仅 Version Manager | PRD-CAP-03 |
| 9 | 仅 Batch Manager | PRD-CAP-04 |
| 10 | 仅 Resource Manager | PRD-CAP-05 |
| 11 | 仅 Product Manager | PRD-CAP-06 |
| 12 | Factory Admin 可见 Transfer | FAC-CAP-01 |
| 13 | Factory Manager 无 Transfer | FAC-CAP-02 |
| 14 | 产品侧接口绕过 | BYP-01 |
| 15 | 工厂侧接口绕过 | BYP-02 |
| 16 | 多角色并集 | PRD-MEM-04 |

**19 条 TP 均已至少被 1 条用例覆盖。** TP-SYS-01/02 未单独成条：系统层无完整菜单清单，避免臆造模块；需要时再补抽样账号。
