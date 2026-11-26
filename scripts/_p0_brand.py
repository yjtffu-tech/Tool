"""P0-3：旧品牌 → BRAND 常量。中文站统一用 BRAND_ZH；logo 用 BRAND_EN_SHORT。
例外：LICENSE、源码版权头、Third-party NOTICE 不在本脚本范围（本脚本只扫 .ts/.tsx/.md，且排除 scripts）。
"""
import os
import re

# 先处理 logo 特殊位置（用简称）
SPECIAL = {
    "components/shell/app-shell.tsx": [
        ('aria-label="轻盒工具箱首页"', 'aria-label="乐云工具箱首页"'),
        ('<span className="text-sm font-semibold tracking-tight">LiteBox</span>',
         '<span className="text-sm font-semibold tracking-tight">Leyun</span>'),
    ],
    "components/shell/site-footer.tsx": [
        ("&copy; 2026 轻盒工具箱 (LiteBox). All Rights Reserved.", "&copy; 2026 乐云工具箱"),
    ],
}

for p, reps in SPECIAL.items():
    s = open(p, encoding="utf-8").read()
    new = s
    for old, zh in reps:
        if old not in new:
            print("MISS", p, repr(old[:50]))
            continue
        new = new.replace(old, zh)
    if new != s:
        open(p, "w", encoding="utf-8", newline="").write(new)
        print("SPECIAL", p)

# 全库剩余：中文品牌 → 乐云工具箱；英文 LiteBox → Leyun Tools（meta/法律用全称）
changed = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".next", "scripts")]
    for f in files:
        if not f.endswith((".ts", ".tsx", ".md")):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding="utf-8").read()
        new = s.replace("轻盒工具箱", "乐云工具箱").replace("LiteBox", "Leyun Tools")
        if new != s:
            open(p, "w", encoding="utf-8", newline="").write(new)
            changed.append(p)
print("CHANGED:", len(changed))
for p in changed[:10]:
    print("  ", p)

# 终检：用户可见文件不得含旧品牌
bad = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".next", "scripts")]
    for f in files:
        if f.endswith((".ts", ".tsx", ".md")):
            p = os.path.join(root, f)
            s = open(p, encoding="utf-8").read()
            if re.search(r"轻盒工具箱|LiteBox", s):
                bad.append(p)
print("OLD_BRAND_REMAINING:", len(bad), bad[:10])
if bad:
    raise SystemExit(1)
