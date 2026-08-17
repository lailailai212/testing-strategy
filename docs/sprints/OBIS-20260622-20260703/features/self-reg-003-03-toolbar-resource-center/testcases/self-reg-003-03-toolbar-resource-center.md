# 【自注册】003-03 常驻工具栏与资源中心 功能测试用例

> 来源：Story `story/obis-7007250530-【自注册】003-03-常驻工具栏与资源中心/`（AC-01～AC-10）  
> 需求：【自注册】003-03: 常驻工具栏与资源中心（Story #7007250530）  
> 用例数：13（P0 × 11，P1 × 1，P2 × 1；UI × 5，Functional × 1，E2E × 7）  
> **与 `welcome-content-management.md`（Story #003-04）分工**：外链模块点击跳转、预置文章/FAQ 列表、中英文文案与 docs URL、Downloads Drawer 字段与排序、分类禁用/空态/配置生效等 → **见 Welcome 内容管理**；本文件仅保留 **003-03 独有**验收项  
> UI 参考：Figma [node-id=9022-103695](https://www.figma.com/design/GomFi4IUgj6MTO7S73h26Q/OBIS-Planning%E8%AE%BE%E8%A1%88%E7%A8%BF%E6%96%87%E4%BB%B6?node-id=9022-103695)  
> 测试账号：**Trial_Only_User**（全部租户未签约，可见 Contact Us）；**Mixed_Tenant_User**（含 ≥1 已签约租户，不可见 Contact Us）  
> 所属模块：统一 **`/Cloud/Welcome`**（底部工具栏 + 页头 **Docs / Contact Us / 全屏 / 语言** 均属 Welcome 页）  
> 公共入口：OBIS Cloud → **Welcome**  
> Contact Us（2026-06-25 评论）：新窗口外链；中文 `https://www.snowballtech.com/zh/contact-us`；英文 `https://www.snowballtech.com/contact-us`  
> Docs：英文 `https://docs-sit.snowballtech.com/docs/obis`；中文 `https://docs-sit.snowballtech.com/docs/zh-cn/obis`  
> **页头语言切换（UI）**：点击页头右侧 **地球图标** → 下拉菜单 **Language** 含 **中文 / English**（当前语言带 ✓）；**非** Switch 开关（Switch 为其他功能，误点可能导致异常）

| 用例名称 | 所属模块 | 标签 | 用例等级 | 前置条件 | 步骤描述 | 预期结果 |
| --- | --- | --- | --- | --- | --- | --- |
| 【Cloud-Welcome】【UI】Welcome 工具栏布局 - 页面底部常驻四模块等宽网格 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-01;AC-01 | P0 | 1. **Trial 免费版**账号登录<br>2. 进入 **Welcome** 页 | [1] 滚动至页面**底部**工具栏区域<br>[2] 查看四张卡片布局与模块名称 | [1] 工具栏位于 Welcome **底部**且**常驻**可见（非折叠/非其他 Tab）<br>[2] **4** 张卡片 **Quick Start / Operations Manual / Tools & Downloads / FAQ** 呈**等宽网格**排列（具体内容验收见 Welcome 内容管理 TP-WEL-TB-01） |
| 【Cloud-Welcome】【E2E】Welcome Tools 模块 - 头部打开 Drawer 展示全部工具（超出卡片 4 条） | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-02;AC-06 | P0 | 1. **Tools & Downloads** 预置 **&gt;4** 个下载项（卡片默认区仅展示最多 4 条，见 AC-02）<br>2. **Welcome** 页 | [1] 统计卡片默认区可见工具条数<br>[2] 点击 **Tools & Downloads** 卡片**头部**<br>[3] 统计 Drawer 内工具条数 | [1] 卡片列表部 **≤4** 条<br>[2] 打开**列表 Drawer**（非新标签页）<br>[3] Drawer 展示**全部**工具条目；**不分页**；每条含名称 + 简介 + 下载按钮（Drawer 字段细节见 TP-WEL-DL-02） |
| 【Cloud-Welcome】【UI】Welcome Tools 模块 - Drawer 右上角关闭按钮可关闭 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-03;AC-06 | P0 | 1. **Tools & Downloads** Drawer 已打开 | [1] 点击 Drawer 右上角 **关闭按钮** | [1] Drawer **关闭**；回到 Welcome 底部工具栏 |
| 【Cloud-Welcome】【E2E】Welcome Tools 模块 - 卡片默认区下载按钮直接下载无详情页 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-04;AC-07 | P0 | 1. **Tools & Downloads** 卡片默认列表部有工具条目<br>2. 浏览器允许下载 | [1] 在**卡片默认区**（非 Drawer）点击某工具 **下载箭头按钮**<br>[2] 观察是否打开详情 Drawer 或新标签页 | [1] 触发**直接下载**<br>[2] **无**工具详情 Drawer；**无**新标签详情页（Drawer 内下载见 TP-WEL-DL-03） |
| 【Cloud-Welcome】【UI】页头导航 - Docs Contact Us 全屏与语言选择器可见 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-05;AC-09 | P0 | 1. **Trial_Only_User** 登录<br>2. 进入 **Welcome**（或任意 Cloud 页） | [1] 查看页头右侧：面包屑左侧区域不变，关注右侧操作区<br>[2] 点击 **地球图标** 打开语言下拉 | [1] 可见 **Docs / 文档中心**、**Contact Us / 联系我们**、**全屏**按钮、**地球图标**（语言入口）<br>[2] 下拉展示 **中文 / English**，当前项带 ✓ |
| 【Cloud-Welcome】【E2E】页头 Docs - 英文环境打开 EN 文档站 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-06;AC-09 | P0 | 1. 系统语言 **English** | [1] 点击 **Docs**<br>[2] 查看跳转 URL | [1] 新标签或同窗口打开文档站<br>[2] URL 为 **`https://docs-sit.snowballtech.com/docs/obis`**（生产环境 URL 待确认） |
| 【Cloud-Welcome】【E2E】页头 Docs - 中文环境打开 ZH 文档站 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-07;AC-09 | P0 | 1. 系统语言 **中文**（地球图标 → 选 **中文**） | [1] 点击 **Docs / 文档中心** | [1] URL 为 **`https://docs-sit.snowballtech.com/docs/zh-cn/obis`** |
| 【Cloud-Welcome】【UI】页头 Contact Us - 全部租户未签约时展示 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-08;AC-10 | P0 | 1. **Trial_Only_User**：头像下拉**所有** Tenant 均为**未签约 / Free Trial** | [1] 进入 **Welcome** → 查看页头 **Contact Us** | [1] **Contact Us 可见**且可点击 |
| 【Cloud-Welcome】【UI】页头 Contact Us - 存在已签约租户时任何上下文均不展示 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-09;AC-10 | P0 | 1. **Mixed_Tenant_User** 关联 **≥1 已签约** Tenant | [1] 在未签约 Tenant 上下文查看页头<br>[2] 切换到**已签约** Tenant 后再查看 | [1] **Contact Us 不可见**（任一已签约则全局隐藏）<br>[2] 已签约 Tenant 下仍**不展示** |
| 【Cloud-Welcome】【E2E】页头 Contact Us - 中文环境新窗口打开官网联系页 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-10 | P0 | 1. **Trial_Only_User**；语言 **中文**（地球图标 → **中文**）；Contact Us 可见 | [1] 点击 **Contact Us / 联系我们** | [1] **新窗口/新标签**打开（**非**联系销售弹窗）<br>[2] URL **`https://www.snowballtech.com/zh/contact-us`** |
| 【Cloud-Welcome】【E2E】页头 Contact Us - 英文环境新窗口打开官网联系页 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-11 | P0 | 1. **Trial_Only_User**；语言 **English** | [1] 点击 **Contact Us** | [1] 新窗口打开 **`https://www.snowballtech.com/contact-us`** |
| 【Cloud-Welcome】【Functional】页头全屏 - 点击切换全屏显示 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-12 | P1 | 1. 已进入 **Welcome** 页 | [1] 点击 **全屏**按钮<br>[2] 再次点击或 Esc 退出 | [1] 进入**全屏**<br>[2] **退出全屏**恢复 |
| 【Cloud-Welcome】【UI】Welcome 工具栏与页头 - 对照 Figma 壳层布局一致 | /Cloud/Welcome | 003-03常驻工具栏;TP-REG-TBR-13 | P2 | 1. Figma node `9022-103695` 可访问 | [1] 对照 Welcome **底部四卡网格**、Tools Drawer 壳层、页头操作区与 Figma | [1] 布局/间距与 Figma 一致（卡片内具体文案/URL 见 Welcome 内容管理） |

## AC 覆盖说明（去重后）

| Story AC | 本文件用例 | Welcome 内容管理（003-04） |
|----------|------------|---------------------------|
| AC-01 底部 4 模块 | TBR-01 | TP-WEL-TB-01 |
| AC-02 卡片头+列表≤4条 | —（结构由 003-04 内容用例覆盖） | TP-WEL-TB-04、TP-WEL-QS/MN/FQ-01 |
| AC-03 外链头部→列表页 | — | TP-WEL-QS/MN/FQ-03 |
| AC-04 外链条目→详情页 | — | TP-WEL-QS/MN/FQ-02 等 |
| AC-05 外链 URL 随语言 | — | TP-WEL-I18-03 |
| AC-06 Tools Drawer | TBR-02、TBR-03 | TP-WEL-DL-01、DL-02 |
| AC-07 直接下载 | TBR-04 | TP-WEL-DL-03 |
| AC-08 语言切换文案/URL | — | TP-WEL-I18-01～03 |
| AC-09 页头 Docs/全屏/语言 | TBR-05～07、TBR-12 | — |
| AC-10 Contact Us 展示规则 | TBR-08、TBR-09 | — |
| Contact Us 外链交互 | TBR-10、TBR-11 | — |
