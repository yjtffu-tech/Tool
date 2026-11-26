"""P0-4 配套：给 17 个页面加自指 canonical（Next 不会自动继承 layout 的）。"""
import os
import re

# 需要改的页面：14 工具 + about/privacy/terms
pages = []
for d in sorted(os.listdir("app/tools")):
    p = f"app/tools/{d}/page.tsx"
    if os.path.isfile(p):
        pages.append((p, f"/tools/{d}"))
for d in ["about", "privacy", "terms"]:
    pages.append((f"app/{d}/page.tsx", f"/{d}"))

for p, path in pages:
    s = open(p, encoding="utf-8").read()
    if "canonicalUrl(" in s:
        continue
    # 在 metadata 对象里 description 行之后插入 alternates
    if 'import { BRAND_ZH, SITE_URL, canonicalUrl }' not in s and 'canonicalUrl' not in s:
        # 加 import（放在第一行 import 之后）
        lines = s.splitlines()
        idx = 0
        for i, line in enumerate(lines):
            if line.startswith("import "):
                idx = i + 1
        lines.insert(idx, 'import { canonicalUrl } from "@/lib/site-config";')
        s = "\n".join(lines) + "\n"
    # 在 metadata 对象末尾的 }; 之前插入
    m = re.search(r'(export const metadata: Metadata = \{)([\s\S]*?)(\n\};)', s)
    if not m:
        print("MISS meta", p)
        continue
    body = m.group(2)
    insert = f'\n  alternates: {{ canonical: canonicalUrl("{path}") }},'
    new_body = body + insert
    s = s[:m.start(2)] + new_body + s[m.end(2):]
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("OK", p)
