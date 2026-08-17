# KMS Create Key（Step 1 Basics）页面元素 Baseline

> **环境**：`https://iot-admin-sit.snowballtech.com/key/create`  
> **扫描时间**：2026-06-15  
> **账号**：`future.wei@snowballtech.com`  
> **向导步骤**：Step 1/3 — **Basics**（扫描范围仅 Step1；Step2/3 未展开）  
> **MeterSphere 模块**：`/Cloud/KMS/Create Key`  
> **截图**：[`screenshots/create-key-step1-basics.png`](screenshots/create-key-step1-basics.png)  
> **A11y 快照**：[`snapshots/create-key-step1-a11y-snapshot.yml`](snapshots/create-key-step1-a11y-snapshot.yml)

## 页面结构

```text
面包屑：KMS / Create Key
向导步骤条：1 Basics (active) → 2 Generation Method → 3 Permission
表单区 Basic（Step 1/3）
├── Key Name *          [textbox: Please enter value]
├── Environment *       [select: PROD 默认]
├── Key Type *          [select: Please Select]
├── Key Spec *          [select: Please Select]
├── Notes               [textarea: Please enter value]
└── Validity Period *
    ├── Radio: Years (checked) | Date | Unlimited
    ├── Spinbutton: 25（默认）
    └── 提示文案: Now ~ 2051-06-15 23:59:59
底栏：[Cancel]  [Continue]
```

## 关键交互元素

| 区域 | 元素 | 默认值/状态 | 推荐 Locator（Playwright） | 稳定度 |
|------|------|-------------|---------------------------|--------|
| 向导 | Step 1 Basics | active | `getByText('Basics')` | 中 |
| 向导 | Step 2 Generation Method | wait | `getByText('Generation Method')` | 中 |
| 向导 | Step 3 Permission | wait | `getByText('Permission')` | 中 |
| 表单 | Key Name | 空，必填 | `.arco-form-item` + `filter({ hasText: 'Key Name' })` → `getByRole('textbox')` | 高 |
| 表单 | Environment | **PROD**，必填 | `filter({ hasText: 'Environment' })` → `.arco-select` | 高 |
| 表单 | Key Type | 空，必填 | `filter({ hasText: 'Key Type' })` → `.arco-select` | 高 |
| 表单 | Key Spec | 空，必填 | `filter({ hasText: 'Key Spec' })` → `.arco-select` | 高 |
| 表单 | Notes | 空，选填 | `filter({ hasText: 'Notes' })` → `getByRole('textbox')` | 高 |
| 有效期 | Years 单选 | **默认选中** | `getByRole('radio', { name: 'Years' })` | 高 |
| 有效期 | Date 单选 | 未选中 | `getByRole('radio', { name: 'Date' })` | 高 |
| 有效期 | Unlimited 单选 | 未选中，**可见** | `getByRole('radio', { name: 'Unlimited' })` | 高 |
| 有效期 | 年限输入 | **25**，spinbutton | `getByRole('spinbutton')` | 高 |
| 有效期 | 范围提示 | Now ~ … | `getByText(/Now ~/)` | 中 |
| 底栏 | Cancel | enabled | `getByRole('button', { name: 'Cancel' })` | 高 |
| 底栏 | Continue | enabled | `getByRole('button', { name: 'Continue' })` | 高 |

## Validity Period 细节（配额 Story 相关）

| 模式 | 控件类型 | SIT 实测 | Story（自注册免费版） |
|------|----------|----------|----------------------|
| Years | `role=spinbutton`，placeholder `Please enter value` | 默认 25；可见 Unlimited | 应隐藏 Unlimited；≤2 年 |
| Date | 切换 radio 后出现日期选择器（本次未切换） | 可见 Date 选项 | ≤ 当前+2 年 |
| Unlimited | radio 可见 | **可见** | **应隐藏** |
| 提交校验 | 点击 **Continue** 进入 Step2 | 文案为 Continue | Story 写 **Next** |

**错误提示**（超限场景，本次未触发）：Story 约定为 `Trial max validity is 2 years` / `免费版有效年限最长 2 年`。

## 下拉框（Arco Select）操作提示

Environment / Key Type / Key Spec 均为 Arco Select，DOM 结构：

```text
.arco-form-item → .arco-select-view → input.arco-select-view-input[placeholder="Please Select"]
```

推荐模式：

```python
# 示例：选择 Key Type
page.locator(".arco-form-item").filter(has_text="Key Type").locator(".arco-select").click()
page.get_by_role("option", name="...").click()  # 展开后选项
```

## 与 Story / 用例差异（重要）

| 项 | Story/用例 | SIT 实测 |
|----|------------|----------|
| 下一步按钮 | Next | **Continue** |
| Unlimited | 不可见 | **可见** |
| 默认有效期 | — | **25 Years** |
| 免费版 2 年限制 | 失焦/提交校验 | 需自注册免费版租户验证 |

## Fragile 汇总

- 页面**无** `data-testid`；Key Name 与 Notes 共用 placeholder `Please enter value`，须用 **form-item label 父级** 区分
- Key Type / Key Spec 两个 Select 结构相同，不能单靠 `getByPlaceholder('Please Select')`
- Validity 区域内 Years/Date/Unlimited 三个 radio 建议用 `getByRole('radio', { name: '...' })`

## Step 1 补充：Asymmetric 密钥 Usage 字段（实测）

选择 **Key Type = Asymmetric** 且选定 **Key Spec** 后，Step 1 会动态出现 **Usage** 必填项：

| 选项 | 类型 | 说明 |
|------|------|------|
| Sign / Verify | checkbox | 至少勾选一项方可 Continue |
| Encrypt / Decrypt | checkbox | 与上组合多选 |

未勾选 Usage 点击 **Continue** 时展示：`Usage is required.`

**Key Spec 下拉选项（Asymmetric）**：RSA-2048、RSA-3072、RSA-4096、ECC-P256、ECC-P384、ECC-P521、ECC-P256K、EC_ED25519

## 入口路径

`KMS Key List` → 点击 **Create Key** → `/key/create`（直接进入 Step1 Basics）

## 后续步骤

- Step 2：[`create-key-step2-baseline.md`](create-key-step2-baseline.md)
- Step 3：[`create-key-step3-baseline.md`](create-key-step3-baseline.md)
