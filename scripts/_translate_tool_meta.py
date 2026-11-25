"""把 14 个工具页的 metadata title/description 改成中文 SEO 格式。
格式：在线{中文名} - 免费本地处理 | 轻盒工具箱（按工具类型微调）
"""
import os
import re

# slug -> (中文标题, 中文描述)
META = {
    "video-converter": ("在线视频格式转换工具", "免费把 MP4、WebM、MOV、MKV 互相转换，100% 浏览器本地处理，无需上传，无水印。"),
    "resize-video": ("在线视频尺寸调整与压缩工具", "调整视频分辨率与体积，适配微信、小红书上传限制，本地处理不上传原片。"),
    "trim-video": ("在线视频裁剪工具", "按起止时间精确截取视频片段，浏览器本地完成，无需上传，免费无水印。"),
    "video-to-gif": ("在线视频转 GIF 动图工具", "把短视频片段转成高清循环 GIF，本地 FFmpeg 处理，文件不上传。"),
    "compress-image-size": ("在线图片无损压缩工具", "压缩 JPG、PNG、WebP 图片体积，画质可控，全部本地完成不上传。"),
    "image-format-converter": ("在线图片格式转换工具", "JPG、PNG、WebP 互相转换，保留清晰度，本地处理保护隐私。"),
    "image-cropper": ("在线图片裁剪工具", "自由裁剪或按比例裁切图片，适配封面、头像与商品图，浏览器本地完成。"),
    "exif-remover": ("在线照片隐私信息清除工具", "一键清除照片 EXIF 元数据，抹掉拍摄位置与设备信息，本地处理不上传。"),
    "merge-pdf": ("在线 PDF 合并工具", "把多个 PDF 按顺序合并成一个文件，拖拽排序，浏览器本地处理保护隐私。"),
    "split-pdf": ("在线 PDF 拆分工具", "按页码范围拆分 PDF 或逐页导出，本地完成，原文件不上传。"),
    "compress-pdf": ("在线 PDF 压缩工具", "减小 PDF 文件体积，方便邮件与报关系统上传，内容不外泄。"),
    "jpg-to-pdf": ("在线图片转 PDF 工具", "把多张 JPG、PNG 图片按顺序合成 PDF，扫描件与发票整理利器，本地处理。"),
    "social-preview": ("在线社交媒体封面预览工具", "预览标题与封面在微信、小红书等平台的呈现效果，本地处理不上传素材。"),
    "qr-code": ("在线二维码生成器", "把文字、网址或联系方式生成可自定义二维码，本地生成不上传内容。"),
}

for slug, (title, desc) in META.items():
    p = os.path.join("app", "tools", slug, "page.tsx")
    s = open(p, encoding="utf-8").read()
    # 精确替换 metadata 块里的 title 和 description 行
    s2 = re.sub(r'title: "[^"]*"', f'title: "{title} | 轻盒工具箱"', s, count=1)
    s2 = re.sub(r'description: "[^"]*"', f'description: "{desc}"', s2, count=1)
    if s2 == s:
        print("NOCHANGE", slug)
    else:
        open(p, "w", encoding="utf-8", newline="").write(s2)
        print("OK", slug)
