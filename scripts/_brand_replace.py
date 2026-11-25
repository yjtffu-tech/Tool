"""一次性品牌替换：FreeTools -> 轻盒工具箱 / LiteBox，freetools.click -> liteboxtools.com。
只处理仍参与构建的文件；pricing/download/checkout/README/LICENSE 由人工单独处理。
"""
import os
import re

SKIP_DIRS = {".git", "node_modules", "backup", "removed_tools"}
SKIP_FILES = {"README.md", "LICENSE"}

# 长串优先，避免 freetools.click 被 freetools 先替换
RULES = [
    ("privacy@freetools.click", "contact@liteboxtools.com"),
    ("www.freetools.click", "liteboxtools.com"),
    ("freetools.click", "liteboxtools.com"),
    ("FreeTools", "LiteBox"),
    ("FirstLink AI", "LiteBox"),
    ("FirstLink", "LiteBox"),
    ("freetools", "litebox"),
]

EXT = (".ts", ".tsx", ".css", ".json", ".mjs")

changed = []
hits = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for name in files:
        if not name.endswith(EXT) or name in SKIP_FILES:
            continue
        path = os.path.join(root, name)
        # 跳过将被删除的路由目录（本脚本跑在删除之前，故显式跳过）
        if path.startswith((".\\app\\pricing", ".\\app\\download", ".\\app\\api\\checkout")):
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        new = text
        local = 0
        for old, rep in RULES:
            n = new.count(old)
            if n:
                new = new.replace(old, rep)
                local += n
        if local:
            open(path, "w", encoding="utf-8", newline="").write(new)
            changed.append((path, local))
            hits += local

print("FILES_CHANGED:", len(changed))
print("REPLACEMENTS:", hits)
for p, n in sorted(changed):
    print(f"  {n:3}  {p}")
