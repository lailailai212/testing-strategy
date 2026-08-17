# feishu-bug-fix-verify — 样例

## 样例 1：修复后复验（默认不写飞书评论）

**用户**：

```text
验证这个 Bug 修复了没：https://project.feishu.cn/obis/bug/detail/7068955890
```

**Agent**：

1. `get_workitem_brief({ url, fields: ["_all"] })` 解析 Description、Sprint、环境  
2. 门禁：SIT URL、账号、预期齐全 → 通过  
3. Playwright（或 DevTools）登录 → 直达证书 Audit → Filter Operator Name = `future` → Search  
4. 对照预期截图 → 落盘  
   `docs/execution/OBIS-20260727-20260807/evidence/bug-verify/7068955890/20260807-1100-operator-name-filter.png`  
5. 追加 `bug-verify-log.md`  
6. **不**调用 `add_comment`  
7. `browser_close`（及必要的 DevTools 清理）  
8. 回复：`Fixed` / `Still Repro` / `Blocked` + 证据路径 +「浏览器已关闭」

## 样例 2：显式要求回写评论

**用户**：

```text
obis 7068955890 复验，comment=true
```

**差异**：判定与截图完成后，额外 `add_comment`，log 中「飞书评论：已写」。其余同样例 1，结束后仍须关浏览器。

## 样例 3：门禁 Blocked（无直达 URL）

**用户**：

```text
复验飞书 Bug 7068955890
```

Description 无入口 URL、也无法唯一推断 → **Blocked**，说明缺项；若尚未开浏览器则不必打开；若已打开则仍须关闭。不写飞书评论。

## 样例 4：首次确认复现（非修复回归）

**用户**：

```text
按 feishu-bug-fix-verify 确认这条 Bug 能否复现：{url}
```

流程相同；结论用 `Still Repro`（可复现）或 `Fixed`（已不符合「实际结果」、现象消失——若用户本意是查复现，摘要写明「未能复现 / 环境已变」亦可标 Blocked 并说明）。仍强制截图与关浏览器。
