"""第四批：social-preview 与 previews.tsx 残余英文。"""
import os

# social-preview-client
p = "app/tools/social-preview/social-preview-client.tsx"
s = open(p, encoding="utf-8").read()
s = s.replace("                    Placeholder\n", "                    占位图\n")
s = s.replace("                    Remove\n", "                    移除\n")
s = s.replace(
    "            These previews are visual mockups rendered locally. Platforms may crop\n            or restyle cards slightly, but character limits and layouts match the\n            real renderers.",
    "            这些预览是本地生成的示意图。平台可能对卡片做轻微裁切或样式调整，但字数限制与排版与实际渲染一致。",
)
open(p, "w", encoding="utf-8", newline="").write(s)

# previews.tsx
p = "app/tools/social-preview/previews.tsx"
s = open(p, encoding="utf-8").read()
repl = [
    ('label="Google Search"', 'label="谷歌搜索"'),
    ('label="X (Twitter)"', 'label="X（推特）"'),
    ('label="LinkedIn"', 'label="领英"'),
    ('label="Facebook"', 'label="脸书"'),
    ('"Untitled page"', '"未命名页面"'),
    ('"No description provided for this page."', '"暂无页面描述。"'),
    ('"No description provided."', '"暂无描述。"'),
]
for old, zh in repl:
    s = s.replace(old, zh)
open(p, "w", encoding="utf-8", newline="").write(s)
print("social-preview residual translated")
