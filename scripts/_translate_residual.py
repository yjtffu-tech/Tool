"""第三批汉化：JSX 插值片段、属性文案、词典未覆盖的残留。"""
import os

# 全库精确替换（含 JSX 插值片段与属性）
MAP = [
    # file-dropzone 共享组件
    ('Drop {multiple ? "files" : "a file"} here or click to browse', '拖入{multiple ? "多个文件" : "文件"}，或点击浏览'),
    ("Processed locally. Never uploaded.", "本地处理，绝不上传。"),
    # QR 纠错等级
    ('L: "Low (~7%)"', 'L: "低（约 7%）"'),
    ('M: "Medium (~15%)"', 'M: "中（约 15%）"'),
    ('Q: "Quartile (~25%)"', 'Q: "较高（约 25%）"'),
    ('H: "High (~30%)"', 'H: "高（约 30%）"'),
    ('placeholder="https://example.com or any text"', 'placeholder="输入网址或任意文字"'),
    # social-preview 专属
    ('placeholder="A short summary shown under the title"', 'placeholder="标题下方显示的简短描述"'),
    ('placeholder="https://example.com/page"', 'placeholder="https://example.com/页面"'),
    ("Use placeholder", "使用占位图"),
    ("1200 x 630 recommended", "推荐 1200 x 630 像素"),
    ('Shown as <span class="font-mono">', '显示为 <span class="font-mono">'),
    ("These previews are visual mockups rendered locally. Platforms may crop or restyle cards slightly, but character limits and layouts match the real renderers.", "这些预览是在本地生成的示意图。平台可能对卡片做轻微裁切或样式调整，但字数限制与排版与实际渲染一致。"),
    # video workbench 共享
    ("MP4, MOV, or WebM. Scale the video to a new resolution.", "支持 MP4、MOV 或 WebM，把视频缩放到新分辨率。"),
    ("MP4, MOV, or WebM work best. Trimming runs entirely in your browser.", "推荐 MP4、MOV 或 WebM。裁剪完全在浏览器中完成。"),
    ("MP4, WebM, MOV). Keep it a few seconds for a small GIF.", "MP4、WebM、MOV）。保持几秒时长可得到较小的 GIF。"),
    ("Drop one or more JPGs. Reorder them, then export a single PDF.", "拖入一张或多张 JPG，调整顺序后导出为单个 PDF。"),
]

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".next")]
    for f in files:
        if not f.endswith((".tsx", ".ts")):
            continue
        p = os.path.join(root, f)
        try:
            s = open(p, encoding="utf-8").read()
        except Exception:
            continue
        new = s
        for old, zh in MAP:
            if old in new:
                new = new.replace(old, zh)
        if new != s:
            open(p, "w", encoding="utf-8", newline="").write(new)
            print("CHANGED", p)
