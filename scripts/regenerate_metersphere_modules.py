"""Regenerate metersphere-modules.json from path/count tuples (DOM snapshot 2026-06-11)."""
from __future__ import annotations

import json
from pathlib import Path

# (path, case_count, is_leaf) — parsed from MeterSphere expandall tree DOM
ENTRIES: list[tuple[str, int, bool]] = [
    ("/未规划用例", 9, True),
    ("/Cloud", 1813, False),
    ("/Cloud/Login & Profile", 22, False),
    ("/Cloud/Login & Profile/Login", 8, True),
    ("/Cloud/Login & Profile/My Profile", 14, True),
    ("/Cloud/Product", 562, False),
    ("/Cloud/Product/Product List", 26, False),
    ("/Cloud/Product/Product List/Version", 1, True),
    ("/Cloud/Product/Product List/Module", 2, True),
    ("/Cloud/Product/Header", 22, False),
    ("/Cloud/Product/Header/Settings", 15, True),
    ("/Cloud/Product/Overview", 31, True),
    ("/Cloud/Product/Assets", 148, True),
    ("/Cloud/Product/Version", 49, False),
    ("/Cloud/Product/Version/Create", 22, True),
    ("/Cloud/Product/Version/List", 16, True),
    ("/Cloud/Product/Batch", 55, False),
    ("/Cloud/Product/Batch/Detail", 3, True),
    ("/Cloud/Product/Batch/Create", 11, True),
    ("/Cloud/Product/Batch/List", 13, True),
    ("/Cloud/Product/Vulnerability & SBOM", 188, False),
    ("/Cloud/Product/Vulnerability & SBOM/Vulnerability", 88, True),
    ("/Cloud/Product/Vulnerability & SBOM/SBOM", 100, True),
    ("/Cloud/Product/OTA", 0, True),
    ("/Cloud/Product/Device", 19, False),
    ("/Cloud/Product/Device/List", 10, True),
    ("/Cloud/Product/Device/Profile", 7, True),
    ("/Cloud/Product/Device/Logs", 2, True),
    ("/Cloud/Product/Member", 24, True),
    ("/Cloud/KMS", 411, False),
    ("/Cloud/KMS/Create Key", 64, False),
    ("/Cloud/KMS/Create Key/Basic", 23, True),
    ("/Cloud/KMS/Create Key/Generation Method", 24, True),
    ("/Cloud/KMS/Create Key/Permission", 16, True),
    ("/Cloud/KMS/Key Detail", 92, False),
    ("/Cloud/KMS/Key Detail/Overview", 0, True),
    ("/Cloud/KMS/Key Detail/Usage Count", 15, False),
    ("/Cloud/KMS/Key Detail/Usage Count/Product", 6, True),
    ("/Cloud/KMS/Key Detail/Usage Count/User", 7, True),
    ("/Cloud/KMS/Key Detail/Permission", 22, True),
    ("/Cloud/KMS/Key Detail/Operation Log", 17, True),
    ("/Cloud/KMS/Key List", 45, True),
    ("/Cloud/PKI", 393, False),
    ("/Cloud/PKI/PKI List", 71, True),
    ("/Cloud/PKI/Google Cast", 22, True),
    ("/Cloud/PKI/Cert & Template Detail", 162, False),
    ("/Cloud/PKI/Cert & Template Detail/Navigation Bar", 15, True),
    ("/Cloud/PKI/Cert & Template Detail/Overview", 50, True),
    ("/Cloud/PKI/Cert & Template Detail/Usage Count", 31, False),
    ("/Cloud/PKI/Cert & Template Detail/Usage Count/User", 4, True),
    ("/Cloud/PKI/Cert & Template Detail/Usage Count/Usage", 11, False),
    ("/Cloud/PKI/Cert & Template Detail/Usage Count/Usage/Product", 5, True),
    ("/Cloud/PKI/Cert & Template Detail/Usage Count/Usage/User", 5, True),
    ("/Cloud/PKI/Cert & Template Detail/Usage Count/Product", 16, True),
    ("/Cloud/PKI/Cert & Template Detail/Verification Service", 23, True),
    ("/Cloud/PKI/Cert & Template Detail/End Entity Cert List", 22, True),
    ("/Cloud/PKI/Cert & Template Detail/Audit", 21, True),
    ("/Cloud/PKI/Create Certificate", 72, False),
    ("/Cloud/PKI/Create Certificate/Step1 Basics", 26, True),
    ("/Cloud/PKI/Create Certificate/Step2 Certificate Profile", 31, True),
    ("/Cloud/PKI/Create Certificate/Step3 Permission", 15, True),
    ("/Cloud/PKI/CSR Configuration", 16, True),
    ("/Cloud/PKI/Matter", 23, True),
    ("/Cloud/PKI/Custom", 27, True),
    ("/Cloud/Ecosystem", 122, False),
    ("/Cloud/Ecosystem/Factory", 119, False),
    ("/Cloud/Ecosystem/Factory/Factory List", 4, True),
    ("/Cloud/Ecosystem/Factory/Factory Info", 53, True),
    ("/Cloud/Ecosystem/Factory/Station", 45, True),
    ("/Cloud/Ecosystem/Factory/Batch", 7, True),
    ("/Cloud/Ecosystem/U-Safe List", 3, True),
    ("/Cloud/Records", 46, False),
    ("/Cloud/Records/Device History", 32, True),
    ("/Cloud/Records/DAC Report", 14, True),
    ("/Cloud/Admin", 75, False),
    ("/Cloud/Admin/Account", 41, True),
    ("/Cloud/Admin/Group", 34, True),
    ("/Cloud/Operation", 85, False),
    ("/Cloud/Operation/Tenant", 45, True),
    ("/Cloud/Operation/Role", 16, True),
    ("/Cloud/Operation/User(SNB)", 16, True),
    ("/Cloud/Operation/DAC Toup", 8, True),
    ("/Cloud/System", 13, False),
    ("/Cloud/System/Language", 3, True),
    ("/Cloud/System/Resources", 7, True),
    ("/Cloud/System/Parameters", 3, True),
    ("/Cloud/Archived", 76, False),
    ("/Cloud/Archived/全局UI&UE", 8, True),
    ("/Cloud/Archived/Basic", 49, True),
    ("/Cloud/Archived/Certificate", 12, True),
    ("/Cloud/Archived/U-Safe Account", 3, True),
    ("/Cloud/Archived/U-Safe List (SNB)", 4, True),
    ("/Cloud/UI Check", 0, False),
    ("/Cloud/UI Check/OBIS-20260608-20260618", 0, True),
    ("/Edge", 67, False),
    ("/Edge/Login", 4, True),
    ("/Edge/Factory", 19, True),
    ("/Edge/Batch", 14, True),
    ("/Edge/Station", 12, True),
    ("/Edge/Interface", 9, True),
    ("/Edge/全局UI&UE", 0, True),
    ("/Edge/Auth", 9, True),
    ("/Client", 156, False),
    ("/Client/Programing Station", 116, False),
    ("/Client/Programing Station/login", 37, True),
    ("/Client/Programing Station/Programing", 60, True),
    ("/Client/Programing Station/Batch Detail", 7, True),
    ("/Client/Programing Station/Channel Configuration", 6, True),
    ("/Client/Programing Station/Others", 3, True),
    ("/Client/Programing Station/Programing CLI", 3, True),
    ("/Client/CHIP", 27, False),
    ("/Client/CHIP/Qorvo", 9, True),
    ("/Client/CHIP/Telink", 9, True),
    ("/Client/CHIP/Silicon Labs", 9, True),
    ("/Client/SNB-CLI", 13, True),
    ("/Super Admin Platform", 83, False),
    ("/Super Admin Platform/OBIS Biz", 16, False),
    ("/Super Admin Platform/OBIS Biz/Tenant", 4, True),
    ("/Super Admin Platform/OBIS Biz/Role", 6, True),
    ("/Super Admin Platform/OBIS Biz/User(SNB)", 4, True),
    ("/Super Admin Platform/OBIS Biz/DAC Topup", 2, True),
    ("/Super Admin Platform/OBIS System", 59, False),
    ("/Super Admin Platform/OBIS System/Resource", 6, True),
    ("/Super Admin Platform/OBIS System/Parameters", 4, True),
    ("/Super Admin Platform/OBIS System/Language", 6, True),
    ("/Super Admin Platform/OBIS System/Certificate Specification", 40, False),
    ("/Super Admin Platform/OBIS System/Certificate Specification/Cert Spec List", 30, True),
    ("/Super Admin Platform/OBIS System/Certificate Specification/Create Cert Spec", 10, False),
    (
        "/Super Admin Platform/OBIS System/Certificate Specification/Create Cert Spec/step1 Basics",
        10,
        True,
    ),
    (
        "/Super Admin Platform/OBIS System/Certificate Specification/Create Cert Spec/step2 Attribute Constraint",
        0,
        False,
    ),
    (
        "/Super Admin Platform/OBIS System/Certificate Specification/Create Cert Spec/step2 Attribute Constraint/Leaf Cert",
        0,
        True,
    ),
    (
        "/Super Admin Platform/OBIS System/Certificate Specification/Create Cert Spec/step2 Attribute Constraint/Root",
        0,
        True,
    ),
    (
        "/Super Admin Platform/OBIS System/Certificate Specification/Create Cert Spec/step2 Attribute Constraint/Intermediate CA",
        0,
        True,
    ),
    ("/Super Admin Platform/OBIS System/U-Safe Account", 3, True),
    ("/Super Admin Platform/SA System", 8, False),
    ("/Super Admin Platform/SA System/超管用户管理", 2, True),
    ("/Super Admin Platform/SA System/超管角色管理", 3, True),
    ("/Super Admin Platform/SA System/超管资源管理", 3, True),
]


def level_of(path: str) -> int:
    if path == "/未规划用例":
        return 0
    return path.count("/") - 1


def name_of(path: str) -> str:
    return path.rsplit("/", 1)[-1]


def build_tree(entries: list[tuple[str, int, bool]]) -> list[dict]:
    meta = {p: {"case_count": c, "is_leaf": leaf} for p, c, leaf in entries}
    children: dict[str, list[str]] = {}
    roots: list[str] = []

    for path in meta:
        if path == "/未规划用例":
            roots.append(path)
            continue
        parts = path.strip("/").split("/")
        if len(parts) == 1:
            roots.append(path)
        else:
            parent = "/" + "/".join(parts[:-1])
            children.setdefault(parent, []).append(path)

    def node(path: str) -> dict:
        d: dict = {
            "path": path,
            "level": level_of(path),
            "name": name_of(path),
            "case_count": meta[path]["case_count"],
            "is_leaf": meta[path]["is_leaf"],
        }
        if path == "/未规划用例":
            d["type"] = "system_default"
        kids = sorted(children.get(path, []))
        if kids:
            d["is_leaf"] = False
            d["children"] = [node(k) for k in kids]
        return d

    return [node(r) for r in sorted(roots, key=lambda p: (p != "/未规划用例", p))]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "docs/modules/metersphere-modules.json"
    paths = [p for p, _, _ in ENTRIES]
    data = {
        "source": "MeterSphere 用例模块树（页面 DOM 快照，2026-06-11，全量展开）",
        "path_format": "以 / 开头；大小写、空格、&、中英文均敏感，须与 MeterSphere 完全一致",
        "hierarchy_rules": [
            "level 0：项目根模块（parentid=NONE）",
            "level N：第 N 层子模块",
            "未规划用例：系统默认节点，不建议新业务挂载",
        ],
        "coverage_note": "自 MeterSphere 页面 expandall=true 快照解析，含 Cloud/Edge/Client/Super Admin Platform 全展开子模块。",
        "valid_paths": paths,
        "modules": build_tree(ENTRIES),
        "not_in_tree_yet": {
            "note": "以下细分子模块尚未在 MeterSphere 创建；Product 相关用例当前统一挂在 /Cloud/Product 下已有模块",
            "paths": [
                "/Cloud/Product/Assets/Assign Security Key",
                "/Cloud/Product/Assets/Assign Certificate",
                "/Cloud/Product/Assets/Tag 新增与删除（Key/Certificate 共用）",
                "/Cloud/Product/Assets/Asset 列表展示",
            ],
        },
    }
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(paths)} paths -> {out}")


if __name__ == "__main__":
    main()
