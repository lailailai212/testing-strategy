# SEMS 四个生命周期接口测试说明

## 1. 状态映射

| 状态值 | 状态 |
|---|---|
| 1 | Draft |
| 2 | Active |
| 3 | Locked |
| 4 | Revoked |
| 5 | Archived |
| 6 | Destroyed |

四个接口都支持两种 `businessProfileId` 格式：

- 裸 ID：`123`
- 业务 ID：`SEP_123`

四个接口都会进行登录态和 ARBAC 权限校验，并使用 Redis 10 秒防重复提交锁。Archive、Lock、Unlock、Revoke 会写统一生命周期审计、人工请求幂等记录和状态 outbox；Destroy 是物理删除流程，只有审计和人工请求记录，不写状态 outbox。

## 2. Archive

### 状态变化

仅允许 `Locked` 或 `Revoked` 归档：

```sql
UPDATE sems_se_profile
SET status = 5,
    lock_sources = '[]',
    version = version + 1,
    updator = ?
WHERE id = ?
  AND version = ?
  AND status IN (3, 4);
```

### 数据记录

- `sems_profile_lifecycle_audit`
  - `action = 'archive'`
  - `result = 'success'`
  - `from_status = 'Locked'` 或 `Revoked`
  - `to_status = 'Archived'`
  - `trigger_reason = 'manual_archived'`
- `sems_profile_lifecycle_request`
  - `action = 'archive'`
  - `result_type = 'success'`
  - 保存完整响应 JSON
- `sems_profile_state_outbox`
  - `event_type = 'se_profile.archived'`
  - `aggregate_id = 'SEP_<physicalId>'`
  - `delivery_status = 'pending'`

不写 `sems_profile_source_event`，不调用 KMS 或 GPCA 接口。

## 3. Lock / Unlock

### Lock

仅允许 `Active` 锁定：

```sql
UPDATE sems_se_profile
SET status = 3,
    lock_sources = '[{"type":"manual","source_id":null,"locked_at":"..."}]',
    version = version + 1,
    updator = ?
WHERE id = ?
  AND version = ?
  AND status = 2;
```

写入：

- `sems_profile_lifecycle_audit`：`action = 'lock'`、`trigger_reason = 'manual_locked'`
- `sems_profile_lifecycle_request`：`action = 'lock'`、`result_type = 'success'`
- `sems_profile_state_outbox`：`event_type = 'se_profile.locked'`

### Unlock

仅当 `lock_sources` 严格只包含一个 `manual` 锁源时允许解锁：

```sql
UPDATE sems_se_profile
SET status = 2,
    lock_sources = '[]',
    version = version + 1,
    updator = ?
WHERE id = ?
  AND version = ?
  AND status = 3;
```

写入：

- `sems_profile_lifecycle_audit`：`action = 'unlock'`、`trigger_reason = 'manual_unlocked'`
- `sems_profile_lifecycle_request`：`action = 'unlock'`、`result_type = 'success'`
- `sems_profile_state_outbox`：`event_type = 'se_profile.unlocked'`

如果存在级联锁源，手动 Unlock 会被拒绝。人工 Lock / Unlock 不调用 KMS、GPCA 或 ARBAC 变更接口，只进行 ARBAC 权限校验。

## 4. Revoke

仅允许 `Active` 或 `Locked` 吊销：

```sql
UPDATE sems_se_profile
SET status = 4,
    revoke_reason = 'manual_revoked',
    lock_sources = '[]',
    version = version + 1,
    updator = ?
WHERE id = ?
  AND version = ?
  AND status IN (2, 3);
```

写入：

- `sems_profile_lifecycle_audit`
  - `action = 'revoke'`
  - `result = 'success'`
  - `trigger_reason = 'manual_revoked'`
  - 保存吊销前后的 `lock_sources`
- `sems_profile_lifecycle_request`
  - `action = 'revoke'`
  - `result_type = 'success'`
- `sems_profile_state_outbox`
  - `event_type = 'se_profile.revoked'`

手动 Revoke 不接收 `reason`，后端固定保存 `manual_revoked`。不写 `sems_profile_source_event`，不调用 KMS 或 GPCA 接口。

## 5. Destroy

Destroy 是 Draft 的物理删除，不是状态更新。

### 清理对象存储

- CAP 文件：`StorageFactory.getClient().delete(objectKey)`
- SCP11c 脚本文件：`StorageFactory.getClient().delete(objectKey)`

### 清理数据库

```sql
DELETE FROM sems_scp11c_script
WHERE org_code = ?
  AND se_profile_id = ?;

DELETE FROM sems_reference_record_field
WHERE se_profile_id = ?;

DELETE FROM sems_reference_record
WHERE se_profile_id = ?;

DELETE FROM sems_reference_record_field_struct
WHERE se_profile_id = ?;

DELETE FROM sems_se_profile_node
WHERE se_profile_id = ?;

DELETE FROM sems_se_profile
WHERE id = ?
  AND status = 1
  AND del_flag = 2;
```

引用数据清理使用 Profile 的物理 ID；接口同时兼容裸 ID 和 `SEP_<physicalId>` 业务 ID。

### ARBAC Policy 清理

当前实现会清理：

```text
se_profile:<physicalId>
se_profile:SEP_<physicalId>
se_profile_amsd:<amsdNodeUuid>
```

### 不删除的数据

- `sems_se_profile_definition`
- `sems_sd_cert_archive`

当前实现发现 Definition 或 SD 归档数据存在时，会返回 `151072` 阻止 Destroy，而不是删除这些数据。

### Destroy 记录

- 写入 `sems_profile_lifecycle_audit`
  - `action = 'destroy'`
  - 记录 `result`
  - 保存 `client_request_id`
- 写入 `sems_profile_lifecycle_request`
  - `action = 'destroy'`
  - `result_type` 可为 `processing`、`retryable_failed`、`terminal_error`、`success`

不写：

- `sems_profile_state_outbox`
- `sems_profile_source_event`

## 6. E4-S6 级联入口

S10 / S11 支持 E4-S6 的内部级联入口。级联请求会额外写入 `sems_profile_source_event`，包含：

```text
event_id
source_type
source_id
source_state
processing_result
response_json
processed_at
```

真正发生状态变化时，同时写入 `sems_profile_state_outbox`，例如：

```text
cascade_lock   -> se_profile.locked
cascade_unlock -> se_profile.unlocked
cascade_revoke -> se_profile.revoked
```

当前 E4-S6 的上游 Resolver / Authority 接口是扩展点。前端不调用这些级联入口，当前代码也没有直接调用 KMS / GPCA 的级联逻辑。

## 7. 手工验证 SQL

```sql
SET @profile_id = 123;

SELECT id, status, lock_sources, revoke_reason, version, updator
FROM sems_se_profile
WHERE id = @profile_id;

SELECT id, se_profile_id, action, result, from_status, to_status,
       trigger_reason, actor_type, actor_id, client_request_id,
       event_id, operated_at, error_code
FROM sems_profile_lifecycle_audit
WHERE se_profile_id = @profile_id
ORDER BY operated_at DESC;

SELECT id, se_profile_id, action, result_type, client_request_id,
       error_code, created_at
FROM sems_profile_lifecycle_request
WHERE se_profile_id = @profile_id
ORDER BY created_at DESC;

SELECT event_id, event_type, aggregate_id, delivery_status,
       retry_count, created_at
FROM sems_profile_state_outbox
WHERE aggregate_id IN (CONCAT('SEP_', @profile_id), CAST(@profile_id AS CHAR))
ORDER BY created_at DESC;

SELECT id, se_profile_id, event_id, source_type, source_id,
       processing_result, processed_at
FROM sems_profile_source_event
WHERE se_profile_id = @profile_id
ORDER BY processed_at DESC;
```

## 8. 接口调用样例

公共请求头：

```http
Content-Type: application/json
Authorization: Bearer <登录态Token>
```

### Archive

```bash
curl -X POST \
  "http://localhost:8000/iot-admin-service/sems/profiles/SEP_123/archive" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"clientRequestId":"7f3a9c2e-1b4d-4e6a-8c0f-2d5e9a1b3c7d"}'
```

### Lock

```bash
curl -X POST \
  "http://localhost:8000/iot-admin-service/sems/profiles/SEP_123/lock" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"clientRequestId":"2b42025c-d1dd-4ff8-bca8-633ec924364f"}'
```

### Unlock

```bash
curl -X POST \
  "http://localhost:8000/iot-admin-service/sems/profiles/SEP_123/unlock" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"clientRequestId":"3c53136d-e2ee-5ff9-cd94-744fd935475g"}'
```

### Revoke

```bash
curl -X POST \
  "http://localhost:8000/iot-admin-service/sems/profiles/SEP_123/revoke" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"clientRequestId":"4d64247e-f3ff-601a-de05-855ge046586h"}'
```

### Destroy

```bash
curl -X POST \
  "http://localhost:8000/iot-admin-service/sems/profiles/SEP_123/destroy" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"clientRequestId":"5e75358f-a4aa-712b-ef16-966hf157697i"}'
```

请求路径中的 `SEP_123` 可以替换为 `123`。四个接口的 `clientRequestId` 都由前端生成；同一次请求发生网络重试时必须复用原 UUID。

> 测试注意：上面的部分示例 UUID 为便于展示而使用，实际请求请使用合法 UUID。
