# 测试环境与造数约定

> 本文件**可提交**，只写约定，不写凭证。
> 真实账号、验证码、租户名映射一律放 `config/env.local.yaml`（已 gitignore）。

## 租户代号

用例文档与数据台账统一使用代号，避免真实租户名散落在各处：

| 代号 | 含义 | 关键特征 |
|---|---|---|
| `t1` | 主测试租户 | 会上线 OTA & Vulnerability；需含雪球超级管理员、雪球租户数据管理员、System Manager、Product Manager 四类 Role |
| `t2` | 对照租户 | **不**上线 OTA & Vulnerability（宜家及其关联租户），所有 Role 均不配置两项权限 |
| `t3` | 第二 Organization 来源 | 仅用于 Audit 的 Organization 列展示与筛选，需要其用户在 t1 资源上留下审计日志 |

代号到真实租户名的映射见 `env.local.yaml` 的 `tenants` 段。

## 账号代号

数据台账中的账号统一用「字母 + 序号」代号，含义与 Sprint 数据准备清单一致：

| 前缀 | 类别 | 是否可复用 |
|---|---|---|
| `A` | 权限与角色类、Transfer 操作人与目标 | 可复用；Transfer 后身份会变，需在台账记录当前状态 |
| `D` | 一次性可删账号 | **不可复用**，执行后销毁 |
| `R` | `+n` 角色数量档位账号 | 可复用 |
| `P` | OTA / Vulnerability 权限对照账号 | 可复用；可通过改 Role 权限切换档位 |

## 命名前缀

所有由测试造出的数据统一加 Sprint 前缀，便于识别与批量清理：

```text
账号邮箱   {prefix}{purpose}@{domain}      如 qa0807-kms-admin@example.com
资源名称   {prefix}{module}-{seq}          如 qa0807-kms-key-01
```

`{prefix}` 取当前 Sprint 的短标识（如 `0807` Sprint 用 `qa0807-`），实际值在 `env.local.yaml` 的 `naming.prefix`。

**禁止**在共享环境上直接改动非本前缀的既有数据。

## 造数与清理纪律

1. **先登记后使用**：造出的每个账号 / 资源必须写入对应 Sprint 的 `data-ledger.md`，含真实标识、直达 URL、当前身份状态。
2. **不可逆操作留痕**：Transfer Admin、删除账号等执行后，立即在台账更新身份变化并标注执行时间，避免后续用例基于过期认知。
3. **一次性账号预留余量**：删除类账号建议每类多备 1 个，供回归重跑。
4. **Sprint 收尾清理**：按前缀清理造出的资源；已删除的账号无法回收，在台账标记为「已销毁」而非删除记录行。

## 凭证红线

- `config/env.local.yaml` 与任何 `*.local.yaml` **禁止提交**，已在 `.gitignore` 中忽略。
- 文档、用例、baseline、脚本中**不得**出现明文邮箱密码或验证码，需要时写「见 `config/env.local.yaml`」。
- 新同学入组：从密码管理器或团队负责人处领取凭证后自行填入本地 `env.local.yaml`，不要相互转发文件。
