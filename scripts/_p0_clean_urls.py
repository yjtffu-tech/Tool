"""P0-2/3：清合规页与页脚的旧域名 URL、统一邮箱。"""
import os

reps = [
    ("https://liteboxtools.com", "https://www.leyunke.com"),
    ("contact@liteboxtools.com", "tool@leyunke.com"),
]
files = [
    "app/about/page.tsx", "app/privacy/page.tsx", "app/terms/page.tsx",
    "components/shell/site-footer.tsx", "README.md",
]
for p in files:
    s = open(p, encoding="utf-8").read()
    new = s
    for old, zh in reps:
        new = new.replace(old, zh)
    if new != s:
        open(p, "w", encoding="utf-8", newline="").write(new)
        print("OK", p)
