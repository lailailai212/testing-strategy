# MeterSphere 模块树

全局合法模块路径：[`metersphere-modules.json`](metersphere-modules.json)（`valid_paths`）。

维护：

```bash
python scripts/regenerate_metersphere_modules.py
```

Per-feature 的 TP→模块映射放在各 Feature 包：

```text
docs/sprints/{sprint}/features/{slug}/testcases/module-mapping.json
```
