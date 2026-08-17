# Bug 修复验证日志 · `OBIS-20260727-20260807`

> 由 feishu-bug-fix-verify 追加。禁止写入 OTP / Token / Cookie。

### BUG-7068955890 · 2026-08-07 12:00

- 结论：`Fixed`
- 标题：【IoT-PKI】PKI Audit Filter 中Operator  Name字段的过滤未根据用户输入用户名字段生效, 根据实际效果判断过滤作用的是Operator Email
- 链接：https://project.feishu.cn/obis/bug/detail/7068955890
- 环境：sit
- 入口：https://iot-admin-sit.snowballtech.com/cert/05DAA7C3-6AAA-4B4D-BE47-A2F1C04C0B4F
- 账号：future.wei@snowballtech.com
- 证据：`evidence/bug-verify/7068955890/20260807-1200-operator-name-filter.png`
- 摘要：Audit Filter 选择 Operator Name、Value=`future` 后，列表仅返回 Operator Name 含 future 的 2 条（Future Wei_modify 123）；不再返回邮箱含 future 但姓名为 test_user modified 的记录。接口 `creatorName=future` 响应 total=2，与预期一致。
- 飞书评论：已写（含复验步骤、结果与证据截图）
- 浏览器：已关闭

### BUG-7068043532 · 2026-08-07 16:42

- 结论：`Fixed`
- 标题：【IoT-UI】Audit Log页面Columns设置尝试调整非固定列失败，如Operation Details和Operation Time应可以调整彼此顺序
- 链接：https://project.feishu.cn/obis/bug/detail/7068043532
- 环境：sit
- 入口：https://iot-admin-sit.snowballtech.com/user/group/2085250293492011010
- 账号：future.wei@snowballtech.com
- 证据：`evidence/bug-verify/7068043532/20260807-1642-columns-reorder.png`
- 摘要：Group Audit → Columns 中可拖拽将 Operation Detail 移至 Operation Time 之后；Save 后表头顺序为 Operator / Organization / Operation Type / Operation Time / Operation Detail，与面板调整一致。
- 飞书评论：已写（含复验步骤、结果与证据截图）
- 浏览器：已关闭
