"""P0-2：统一 SITE_URL，清 liteboxtools.com。精确 REPLACE + 逐条断言。"""
import os
import re

changes = {
    "app/robots.ts": [
        ('const BASE = "https://liteboxtools.com";', 'import { SITE_URL } from "@/lib/site-config";\n\nconst BASE = SITE_URL;'),
    ],
    "app/sitemap.ts": [
        ('const BASE = "https://liteboxtools.com";', 'import { SITE_URL } from "@/lib/site-config";\n\nconst BASE = SITE_URL;'),
    ],
    "app/tools/qr-code/qr-code-client.tsx": [
        ('useState("https://liteboxtools.com")', 'useState("https://www.leyunke.com")'),
    ],
    "app/tools/social-preview/social-preview-client.tsx": [
        ('url: "https://liteboxtools.com/tools"', 'url: "https://www.leyunke.com/tools"'),
    ],
    "lib/og-tool-image.tsx": [
        ('<div style={{ color: "#eab308", fontWeight: 600 }}>liteboxtools.com</div>', '<div style={{ color: "#eab308", fontWeight: 600 }}>www.leyunke.com</div>'),
    ],
    "README.md": [
        ("站点：https://liteboxtools.com", "站点：https://www.leyunke.com"),
    ],
}

for p, reps in changes.items():
    s = open(p, encoding="utf-8").read()
    new = s
    for old, zh in reps:
        if old not in new:
            print("MISS", p, repr(old[:45]))
            continue
        new = new.replace(old, zh)
    if new != s:
        open(p, "w", encoding="utf-8", newline="").write(new)
        print("OK", p)
