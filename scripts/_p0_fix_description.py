"""P0-1：修 11 页英文 description。精确 REPLACE，逐条断言命中，兼容多行格式。
只求中文、准确、不含未验证绝对词；P4 会重写。
"""
import re
import os

NEW = {
    "video-converter": "在浏览器内转换 MP4、WebM、MOV 等常见视频格式，文件不上传。",
    "resize-video": "调整视频分辨率与体积，适配常见平台上传要求，本地处理。",
    "trim-video": "按起止时间截取视频片段，在浏览器本地完成，无需上传原片。",
    "compress-image-size": "压缩 JPG、PNG、WebP 图片体积，可预览画质，本地处理。",
    "image-format-converter": "在 JPG、PNG、WebP 等常见图片格式之间转换，本地完成。",
    "image-cropper": "按比例或自由裁剪图片，适配头像与封面图，浏览器本地处理。",
    "exif-remover": "清除照片中的拍摄位置与设备信息，减少隐私泄露风险。",
    "merge-pdf": "把多份 PDF 按指定顺序合并为一个文件，拖拽排序，本地处理。",
    "split-pdf": "按页码范围或逐页导出拆分 PDF，文件不上传。",
    "compress-pdf": "减小 PDF 文件体积，便于邮件与系统上传，内容不外泄。",
    "jpg-to-pdf": "把多张 JPG、PNG 图片按顺序合成 PDF，浏览器本地完成。",
}

changed = []
for slug, desc in NEW.items():
    p = os.path.join("app", "tools", slug, "page.tsx")
    s = open(p, encoding="utf-8").read()
    # 匹配 description: 后跟任意空白（含换行）再跟引号字符串
    pat = re.compile(r'(description:\s*)"[^"]*"', re.S)
    m = pat.search(s)
    if not m:
        print("MISS", slug, "no description")
        continue
    new_s = pat.sub(lambda mm: mm.group(1) + '"' + desc + '"', s, count=1)
    if new_s == s:
        print("NOCHANGE", slug)
        continue
    open(p, "w", encoding="utf-8", newline="").write(new_s)
    changed.append(slug)

print("CHANGED:", len(changed), changed)
# 复核：全部 14 页 description 必须含中文
bad = []
for d in sorted(os.listdir("app/tools")):
    p = f"app/tools/{d}/page.tsx"
    if not os.path.isfile(p):
        continue
    s = open(p, encoding="utf-8").read()
    m = re.search(r'description:\s*"([^"]*)"', s, re.S)
    desc = m.group(1) if m else ""
    cjk = len(re.findall(r"[\u4e00-\u9fff]", desc))
    print(f"{cjk:3}  {d:24} {desc[:50]}")
    if cjk == 0:
        bad.append(d)
print("BAD:", bad)
if bad:
    raise SystemExit(1)
