# config — 环境 · 凭证 · 约定

集中维护测试环境地址、高权限账号、租户信息、Figma 链接与造数命名约定，避免这些信息散落在 baseline、用例和脚本里。

## 文件

| 文件 | 是否提交 | 内容 |
|---|---|---|
| `env.example.yaml` | ✅ 提交 | 字段模板，全占位符 |
| `env.local.yaml` | ❌ **已 gitignore** | 真实地址、账号、验证码、租户映射 |
| `conventions.md` | ✅ 提交 | 租户 / 账号代号、命名前缀、造数与清理纪律 |

## 首次使用

```powershell
Copy-Item config/env.example.yaml config/env.local.yaml
```

```bash
cp config/env.example.yaml config/env.local.yaml
```

然后填入真实值。凭证从密码管理器或团队负责人处领取，不要相互转发文件。

## 校验没有误提交

```bash
git check-ignore -v config/env.local.yaml   # 应输出匹配到的 .gitignore 规则
git status --porcelain config/              # 不应出现 env.local.yaml
```

## 引用方式

文档与用例中需要凭证时，写「见 `config/env.local.yaml`」，**不要**写明文。代号（`t1` / `A3` / `D1` 等）的含义见 [`conventions.md`](conventions.md)。

## 相关

- 执行与数据准备产物：[`docs/execution/`](../docs/execution/)
- 当前 Sprint 数据准备清单：[`docs/execution/OBIS-20260727-20260807/data-prep.md`](../docs/execution/OBIS-20260727-20260807/data-prep.md)
