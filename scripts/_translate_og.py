"""汉化 OG 图片 alt 与通用 OG 文案。"""
import os
import glob

ALT = {
    "video-converter": "在线视频格式转换工具",
    "resize-video": "在线视频尺寸调整与压缩工具",
    "trim-video": "在线视频裁剪工具",
    "video-to-gif": "在线视频转 GIF 动图工具",
    "compress-image-size": "在线图片无损压缩工具",
    "image-format-converter": "在线图片格式转换工具",
    "image-cropper": "在线图片裁剪工具",
    "exif-remover": "在线照片隐私信息清除工具",
    "merge-pdf": "在线 PDF 合并工具",
    "split-pdf": "在线 PDF 拆分工具",
    "compress-pdf": "在线 PDF 压缩工具",
    "jpg-to-pdf": "在线图片转 PDF 工具",
    "social-preview": "在线社交媒体封面预览工具",
    "qr-code": "在线二维码生成器",
}

for slug, zh in ALT.items():
    p = f"app/tools/{slug}/opengraph-image.tsx"
    s = open(p, encoding="utf-8").read()
    import re
    s2 = re.sub(r'export const alt = "[^"]*";', f'export const alt = "{zh} | 轻盒工具箱";', s, count=1)
    open(p, "w", encoding="utf-8", newline="").write(s2)

p = "lib/og-tool-image.tsx"
s = open(p, encoding="utf-8").read()
s = s.replace('tool?.name ?? "LiteBox"', 'tool?.name ?? "轻盒工具箱"')
s = s.replace('tool?.description ?? "Free, private, in-browser tools. Nothing ever leaves your device."', 'tool?.description ?? "免费、私密、浏览器本地运行的在线工具，文件绝不离开你的设备。"')
s = s.replace("<div>Runs 100% in your browser — no uploads</div>", "<div>100% 浏览器本地运行 — 无需上传</div>")
s = s.replace("// Fall back to generic LiteBox copy rather than throwing — a throw here", "// 回退到通用中文文案，避免抛出异常")
open(p, "w", encoding="utf-8", newline="").write(s)
print("OG translated:", len(ALT), "alts + shared copy")
