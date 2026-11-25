"""交付前自检：逐项实测，输出 PASS/FAIL，不做预估。"""
import os
import re
import json

ERRORS = []
checks = []

def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    if not ok:
        ERRORS.append(f"{name}: {detail}")

# 1. 品牌串归零（参与构建的代码）
brand = re.compile(r"FreeTools|FirstLink|freetools\.click|firstlinkai", re.I)
hits = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".next")]
    for f in files:
        if f.endswith((".ts", ".tsx", ".css", ".json", ".mjs")):
            p = os.path.join(root, f)
            try:
                s = open(p, encoding="utf-8").read()
            except Exception:
                continue
            if brand.search(s):
                hits.append(p)
check("品牌串归零", len(hits) == 0, f"残留 {len(hits)}: {hits[:5]}")

# 2. registry 只有 14 条
reg = open("lib/tools-registry.ts", encoding="utf-8").read()
slugs = re.findall(r'slug: "([^"]+)"', reg)
check("registry=14 工具", len(slugs) == 14, f"实际 {len(slugs)}: {slugs}")

# 3. app/tools 目录只有 14（+_shared）
dirs = [d for d in os.listdir("app/tools") if os.path.isdir(os.path.join("app/tools", d))]
tool_dirs = [d for d in dirs if d != "_shared"]
check("工具目录=14", len(tool_dirs) == 14, f"实际 {len(tool_dirs)}: {sorted(tool_dirs)}")
check("目录与 registry 一致", set(tool_dirs) == set(slugs), f"差集 {set(tool_dirs) ^ set(slugs)}")

# 4. 86 个工具已移出构建区
removed = "../removed_tools_20261125"
moved = len([d for d in os.listdir(removed) if os.path.isdir(os.path.join(removed, d))]) if os.path.isdir(removed) else 0
check("移出工具=86", moved == 86, f"实际 {moved}")

# 5. 14 篇 content.ts 字数 + 结构 + 无占位符
placeholder = re.compile(r"lorem|placeholder|TODO|TBD|示例文本|xxx", re.I)
counts = []
for slug in slugs:
    p = f"app/tools/{slug}/content.ts"
    if not os.path.exists(p):
        check(f"content {slug}", False, "文件缺失")
        continue
    s = open(p, encoding="utf-8").read()
    # 提取所有中文字符
    cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
    counts.append((slug, cjk))
    low = 600 <= cjk <= 850
    check(f"content {slug} 字数", low, f"CJK={cjk}")
    check(f"content {slug} 结构", all(k in s for k in ["intro:", "steps:", "useCases:", "faqs:"]), "缺字段")
    check(f"content {slug} FAQ≥4", s.count("q:") >= 4, f"FAQ={s.count('q:')}")
    if placeholder.search(s):
        check(f"content {slug} 占位符", False, "发现占位符")

# 6. metadata 标题中文
for slug in slugs:
    s = open(f"app/tools/{slug}/page.tsx", encoding="utf-8").read()
    m = re.search(r'title: "([^"]+)"', s)
    ok = bool(m and re.search(r"[\u4e00-\u9fff]", m.group(1)) and "轻盒工具箱" in m.group(1))
    check(f"meta {slug}", ok, m.group(1) if m else "无 title")

# 7. layout lang / title
lay = open("app/layout.tsx", encoding="utf-8").read()
check("html lang=zh-CN", 'lang="zh-CN"' in lay, "缺失")
check("站点标题中文", "轻盒工具箱" in lay, "缺失")

# 8. sitemap 条目 = 17
sm = open("app/sitemap.ts", encoding="utf-8").read()
check("sitemap 无 pricing/download", "/pricing" not in sm and "/download" not in sm, "含废弃路由")
check("sitemap 含合规页", all(x in sm for x in ["/about", "/privacy", "/terms"]), "缺合规页")

# 9. 合规页存在且中文
for page in ["about", "privacy", "terms"]:
    p = f"app/{page}/page.tsx"
    ok = os.path.exists(p) and len(re.findall(r"[\u4e00-\u9fff]", open(p, encoding="utf-8").read())) > 300
    check(f"{page} 页中文", ok, "缺失或字数不足")

# 10. AdSense 合规条款
priv = open("app/privacy/page.tsx", encoding="utf-8").read()
check("隐私政策含 AdSense", "AdSense" in priv, "缺失")
check("隐私政策含 Analytics", "Analytics" in priv, "缺失")

# 11. 无 pricing/download/checkout 路由
for r in ["app/pricing", "app/download", "app/api/checkout"]:
    check(f"无 {r}", not os.path.exists(r), "仍存在")

# 12. title 不应重复品牌（layout template 为 %s，各页自带后缀）
lay_tpl = re.search(r'template: "([^"]*)"', lay)
check("layout template=%s", bool(lay_tpl and lay_tpl.group(1) == "%s"), lay_tpl.group(1) if lay_tpl else "无")
for slug in slugs:
    s = open(f"app/tools/{slug}/page.tsx", encoding="utf-8").read()
    m = re.search(r'title: "([^"]+)"', s)
    t = m.group(1) if m else ""
    check(f"title 不重复 {slug}", t.count("轻盒工具箱") == 1, t)

# 13. 共享 dropzone 与 social 页无英文 UI 片段
dz = open("components/tool/file-dropzone.tsx", encoding="utf-8").read()
check("dropzone 中文", "拖入" in dz and "本地处理，绝不上传" in dz, "英文残留")
ecc = open("app/tools/qr-code/qr-code-client.tsx", encoding="utf-8").read()
check("QR 纠错中文", "低（约 7%）" in ecc and "高（约 30%）" in ecc, "英文残留")
soc = open("app/tools/social-preview/social-preview-client.tsx", encoding="utf-8").read()
prev = open("app/tools/social-preview/previews.tsx", encoding="utf-8").read()
check("social 中文", "占位图" in soc and "这些预览是本地生成的" in soc, "英文残留")
check("previews 中文", "谷歌搜索" in prev and "未命名页面" in prev, "英文残留")

# 14. 构建产物路由数
if os.path.isdir(".next/server/app"):
    htmls = []
    for root, dirs, files in os.walk(".next/server/app"):
        for f in files:
            if f.endswith(".html"):
                htmls.append(os.path.relpath(os.path.join(root, f), ".next/server/app"))
    check("构建 HTML 存在", len(htmls) >= 17, f"HTML 数 {len(htmls)}")

# 输出
print("=" * 60)
for name, ok, detail in checks:
    shown = "" if ok else detail
    print(f"{'PASS' if ok else 'FAIL':5} {name:36} {shown}")
print("=" * 60)
print(f"TOTAL: {len(checks)}  PASS: {sum(1 for _,o,_ in checks if o)}  FAIL: {len(ERRORS)}")
print(f"CONTENT_CJK_RANGE: {min(n for _,n in counts)} - {max(n for _,n in counts)}")
if ERRORS:
    print("ERRORS:")
    for e in ERRORS:
        print("  -", e)
    raise SystemExit(1)
print("ALL_CHECKS_PASSED")
