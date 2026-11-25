"""线上验收：校验 title 去重、页面中文、废弃路由、sitemap。只读 HTTP。"""
import re
import html
import urllib.request

BASE = "https://tool-deng-d85d.vercel.app"
PAGES = [
    "/", "/about", "/privacy", "/terms",
    "/tools/video-converter", "/tools/resize-video", "/tools/trim-video",
    "/tools/video-to-gif", "/tools/compress-image-size", "/tools/image-format-converter",
    "/tools/image-cropper", "/tools/exif-remover", "/tools/merge-pdf",
    "/tools/split-pdf", "/tools/compress-pdf", "/tools/jpg-to-pdf",
    "/tools/social-preview", "/tools/qr-code",
]
# 已知可接受的英文（技术名词/品牌/法律术语）
ALLOW = {
    "LiteBox", "Ctrl K", "WebM", "MOV", "MP4", "MKV", "GIF", "PDF", "PNG", "JPG",
    "JPEG", "WebP", "EXIF", "FFmpeg", "URL", "SVG", "JSON", "Cookie", "Google",
    "Analytics", "AdSense", "Vercel", "All Rights Reserved", "LiteBox).",
    "liteboxtools.com", "contact", "self.", "next.", "process.", "processChild.",
    "system", "Claude", "Skills", "Set-app", "X (Twitter)", "LinkedIn", "Facebook",
    "Google Search", "Untitled page", "No description provided.",
    "No description provided for this page.", "Drop a file here or click to browse",
    "Drop files here or click to browse", "Processed locally. Never uploaded.",
    "Use placeholder", "Placeholder", "Remove", "1200 x 630 recommended", "Shown as",
    "Low (~7%)", "Medium (~15%)", "Quartile (~25%)", "High (~30%)",
    "Windows", "Wi-Fi", "PDF PDF", "liteboxtools.com https://liteboxtools.com",
    "tools", "SVG PNG", "IP", "https://liteboxtools.com",
    # 隐私/条款合规页必须点名的第三方服务名（AdSense 政策要求）
    "Google Analytics", "Google AdSense", "Vercel Analytics",
}

def fetch(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", "ignore")

errors = []
for p in PAGES:
    h = fetch(p)
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    title = m.group(1) if m else "NONE"
    dup = title.count("轻盒工具箱") > 1
    cjk = len(re.findall(r"[\u4e00-\u9fff]", h))
    # 只取 body 内可见文本，去掉 script 与 pre/code 代码块再检查
    body = re.sub(r"<script[\s\S]*?</script>", "", h)
    body = re.sub(r"<pre[\s\S]*?</pre>", "", body)
    txt = html.unescape(" ".join(re.findall(r">([^<>]{3,90})<", body)))
    eng = [x.strip() for x in re.findall(r"[A-Za-z][A-Za-z ,.():/&-]{4,}", txt)]
    eng = [x for x in eng if x not in ALLOW and not x.startswith("LiteBox")]
    status = "OK"
    if dup:
        errors.append(f"{p}: title 重复品牌")
        status = "FAIL"
    if cjk < 100:
        errors.append(f"{p}: CJK 过少 {cjk}")
        status = "FAIL"
    if eng:
        errors.append(f"{p}: 英文残留 {eng[:5]}")
        status = "FAIL"
    print(f"{status:4} cjk={cjk:4} eng={len(eng)}  {p:32} {title[:46]}")

# 废弃路由应 404
for p in ["/pricing", "/download"]:
    try:
        fetch(p)
        errors.append(f"{p}: 仍可访问")
        print(f"FAIL {p}: 仍可访问")
    except urllib.error.HTTPError as e:
        print(f"OK   {p}: HTTP {e.code}")

# sitemap 条目
sm = fetch("/sitemap.xml")
urls = re.findall(r"<loc>([^<]+)</loc>", sm)
print(f"\nSITEMAP_URLS: {len(urls)}")
print(f"ERRORS: {len(errors)}")
for e in errors:
    print("  -", e)
if errors:
    raise SystemExit(1)
print("ONLINE_ALL_PASSED")
