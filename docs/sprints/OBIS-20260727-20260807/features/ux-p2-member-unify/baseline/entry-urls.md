# 入口 URL（SIT · 雪球）

`base` = `https://iot-admin-sit.snowballtech.com`（以 `env.local.yaml` 为准）

## 列表入口（已实测可达）

| 模块 | Path | 全 URL |
|------|------|--------|
| Product List | `/product/list` | `{base}/product/list` |
| KMS Key List | `/key/list` | `{base}/key/list` |
| PKI List | `/pki/list` | `{base}/pki/list` |
| Factory List | `/factory/list` | `{base}/factory/list` |
| Account | `/user/list` | `{base}/user/list` |
| Group | `/user/group/list` | `{base}/user/group/list` |
| Role | `/system/role/list` | `{base}/system/role/list` |
| User (SNB) | `/system/user/list` | `{base}/system/user/list` |

## 详情 URL 模式（已实测）

| 资源 | 模式 | 样本 |
|------|------|------|
| KMS Key Detail | `/key/{numericId}` | `/key/2081648131348414465`（Name=`test permission`，KID=`KID-SAdba2d91445`） |
| Key Detail Tab | 同 URL，点 Tab：`Overview` / `Usage` / `Audit` / `Member` | Member 无独立 path |

> PKI / Factory / Group / Product 详情 ID 模式待点进一条后回填台账「直达 URL」列。

## 登录

1. `{base}/login`  
2. Email + Verification Code（万能码见 `env.local.yaml`；已注册账号可直接填码，无需 Send Code）  
3. 确认租户为 **雪球**（非 HW）后再进业务页
