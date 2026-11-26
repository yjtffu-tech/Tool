"""固定审计脚本：用 HTML 解析器对线上响应逐页检查。
用法：python scripts/audit.py [url] [phase]
  url   : 默认 https://www.leyunke.com
  phase : p0（默认）| p1 | p2 ... 不同阶段检查不同项
输出 PASS/FAIL 与汇总，作为阶段验收证据。
"""
import re
import sys
import urllib.request
from html.parser import HTMLParser

BASE = sys.argv[1] if len(sys.argv) > 1 else "https://www.leyunke.com"
PHASE = sys.argv[2] if len(sys.argv) > 2 else "p0"

PAGES = [
    "/", "/about", "/privacy", "/terms",
    "/tools/video-converter", "/tools/resize-video", "/tools/trim-video",
    "/tools/video-to-gif", "/tools/compress-image-size", "/tools/image-format-converter",
    "/tools/image-cropper", "/tools/exif-remover", "/tools/merge-pdf",
    "/tools/split-pdf", "/tools/compress-pdf", "/tools/jpg-to-pdf",
    "/tools/social-preview", "/tools/qr-code",
]

BANNED = ["liteboxtools.com", "FirstLink", "轻盒工具箱", "LiteBox"]
LEGACY = ["SVG 波形", "Web Audio", "fifteen", "pixels 本身"]

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = {}
        self.link = []
        self.lang = ""
        self.text = []
        self._in_title = False
        self._in_script = False
        self._in_pre = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag == "link":
            self.link.append(a)
        elif tag == "script":
            self._in_script = True
        elif tag == "pre":
            self._in_pre = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script":
            self._in_script = False
        elif tag == "pre":
            self._in_pre = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self._in_script and not self._in_pre:
            self.text.append(data)

    def visible_text(self):
        return " ".join(self.text)

def fetch(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "Mozilla/5.0 (audit)"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", "ignore")

errors = []
checks = []

def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    if not ok:
        errors.append(f"{name}: {detail}")

for path in PAGES:
    try:
        html = fetch(path)
    except Exception as e:
        check(f"fetch {path}", False, str(e))
        continue
    p = MetaParser()
    p.feed(html)
    is_tool = path.startswith("/tools/")
    is_static = path in ("/about", "/privacy", "/terms")
    title = p.title.strip()
    desc = p.meta.get("description", "")
    cjk_title = len(re.findall(r"[\u4e00-\u9fff]", title))
    cjk_desc = len(re.findall(r"[\u4e00-\u9fff]", desc))
    txt = p.visible_text()

    check(f"{path} title 非空", bool(title), title[:40])
    check(f"{path} title 中文", cjk_title > 0, f"CJK={cjk_title}")
    check(f"{path} desc 非空", bool(desc), desc[:40])
    check(f"{path} desc 中文", cjk_desc > 0, f"CJK={cjk_desc}")
    check(f"{path} lang=zh-CN", p.lang == "zh-CN", p.lang)
    # P0 阶段必须自指 canonical；hreflang 到 P1 才要求
    canon = [a.get("href", "") for a in p.link if a.get("rel", "").lower() == "canonical"]
    check(f"{path} canonical 自指", bool(canon) and BASE + path in canon[0], str(canon[:1]))
    if PHASE != "p0":
        alts = [a.get("hreflang", "") for a in p.link if a.get("rel", "").lower() == "alternate" and a.get("hreflang")]
        check(f"{path} hreflang 三语", {"zh-CN", "en", "x-default"}.issubset(set(alts)), str(alts))
    for b in BANNED:
        check(f"{path} 无旧词 {b}", b not in html and b not in txt, "")
    for b in LEGACY:
        check(f"{path} 无遗留词 {b}", b not in txt, "")

# 废弃路由
for path in ["/pricing", "/download"]:
    try:
        fetch(path)
        check(f"{path} 已下线", False, "仍可访问")
    except urllib.error.HTTPError as e:
        check(f"{path} 已下线", e.code in (301, 302, 404), f"HTTP {e.code}")

print("=" * 64)
print(f"AUDIT  base={BASE}  phase={PHASE}  pages={len(PAGES)}")
print("=" * 64)
for name, ok, detail in checks:
    if not ok:
        print(f"FAIL  {name:44} {detail}")
passed = sum(1 for _, ok, _ in checks if ok)
print("=" * 64)
print(f"TOTAL: {len(checks)}  PASS: {passed}  FAIL: {len(errors)}")
if errors:
    for e in errors:
        print("  -", e)
    raise SystemExit(1)
print("AUDIT_ALL_PASSED")
