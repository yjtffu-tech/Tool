"""汉化 14 个工具客户端与共享组件内的英文 UI。精确 REPLACE，逐条断言命中。"""
import os

MAP = [
    # 通用
    ("Start", "开始"),
    ("Result", "结果"),
    ("Ready", "就绪"),
    ("Failed to load", "加载失败"),
    ("Enter", "回车"),
    ("Output", "输出"),
    ("Pages", "页数"),
    ("Image", "图片"),
    ("Appearance", "外观"),
    ("Content", "内容"),
    ("Format JSON, generate SVG waves, build CSS animations, and more. Every tool runs entirely in your browser. No uploads, no tracking, no signup.", "格式化 JSON、生成 SVG 波形、制作 CSS 动画等。所有工具都在浏览器中运行，不上传、不追踪、无需注册。"),
    ("LiteBox, free private browser utilities", "轻盒工具箱，免费私密的浏览器工具"),
    # compress-image-size
    ("Compression settings", "压缩设置"),
    ("Target quality", "目标画质"),
    ("Max width scaling (pixels)", "最大宽度缩放（像素）"),
    ("Original", "原图"),
    ("Compressed", "已压缩"),
    ("Compressed preview", "压缩预览"),
    ("Canvas is unavailable in this browser.", "当前浏览器不支持 Canvas。"),
    ("Could not decode that image file.", "无法解析该图片文件。"),
    ("PNG, JPG, or WebP. Compress it with a live quality preview.", "支持 PNG、JPG 或 WebP，可实时预览压缩效果。"),
    ("That file isn't an image. Drop a PNG, JPG, or WebP file.", "该文件不是图片，请拖入 PNG、JPG 或 WebP 文件。"),
    ("That file isn't an image.", "该文件不是图片。"),
    # compress-pdf
    ("Compress PDF", "压缩 PDF"),
    ("Compressing", "压缩中"),
    ("Image quality", "图片画质"),
    ("Resolution", "分辨率"),
    ("Could not compress this PDF. It may be encrypted or corrupted.", "无法压缩此 PDF，文件可能已加密或损坏。"),
    ("PDF only. Best for scanned or image-heavy documents.", "仅支持 PDF，适合扫描件或图片较多的文档。"),
    ("That file isn't a PDF.", "该文件不是 PDF。"),
    # exif-remover
    ("Canvas is not supported in this browser.", "当前浏览器不支持 Canvas。"),
    ("Output format", "输出格式"),
    ("JPEG quality", "JPEG 画质"),
    ("JPEG (smaller, keep as photo)", "JPEG（体积更小，保留照片外观）"),
    ("PNG (lossless, no metadata)", "PNG（无损，不含元数据）"),
    ("JPEG, PNG, or WebP. Re-encoding the pixels drops all embedded metadata.", "支持 JPEG、PNG 或 WebP。重新编码像素会去掉所有内嵌元数据。"),
    # image-cropper
    ("Crop area", "裁剪区域"),
    ("Aspect ratio", "宽高比"),
    ("Width", "宽度"),
    ("Height", "高度"),
    ("Free", "自由"),
    ("Export", "导出"),
    ("Canvas", "画布"),
    ("Drag to select the crop area", "拖动鼠标选择裁剪区域"),
    ("Drag a box on the image, or type exact values above.", "在图片上拖动选框，或在上方输入精确数值。"),
    ("PNG, JPEG, or WebP. Then drag on the image to select the crop area.", "支持 PNG、JPEG 或 WebP，然后在图片上拖动选择裁剪区域。"),
    ("That file is not an image. Drop a PNG, JPEG, or WebP file.", "该文件不是图片，请拖入 PNG、JPEG 或 WebP 文件。"),
    # image-format-converter
    ("Conversion", "转换"),
    ("Source format", "源格式"),
    ("Target format", "目标格式"),
    ("AVIF", "AVIF"),
    ("JPEG", "JPEG"),
    ("WebP", "WebP"),
    ("Canvas is unavailable in this browser.", "当前浏览器不支持 Canvas。"),
    ("Drop an image, then pick a target format: PNG, JPEG, or WebP.", "拖入图片，然后选择目标格式：PNG、JPEG 或 WebP。"),
    ("This browser couldn't encode that format. Try PNG or JPEG instead.", "当前浏览器无法编码该格式，请改用 PNG 或 JPEG。"),
    # merge-pdf
    ("Unreadable or encrypted PDF", "无法读取或已加密的 PDF"),
    ("Add more PDFs to the merge", "添加更多要合并的 PDF"),
    ("Select two or more PDFs. Reorder them, then merge into a single file.", "选择两份或更多 PDF，调整顺序后合并为一个文件。"),
    ("Those files aren't PDFs. Drop one or more .pdf files.", "这些文件不是 PDF，请拖入一个或多个 .pdf 文件。"),
    # split-pdf
    ("Select pages", "选择页面"),
    ("Page range", "页码范围"),
    ("Extract", "提取"),
    ("Building PDF", "生成 PDF 中"),
    ("Reading PDF", "读取 PDF 中"),
    ("Reading file", "读取文件中"),
    ("One PDF with selected pages", "把所选页面合成一个 PDF"),
    ("Each selected page as its own PDF", "每个所选页面单独导出为 PDF"),
    ("PDF only. Pages appear as thumbnails you can pick from.", "仅支持 PDF，页面会以缩略图形式显示供你勾选。"),
    ("Could not read this file. It may be corrupted or not a valid PDF.", "无法读取该文件，它可能已损坏或不是有效的 PDF。"),
    ("Extraction failed. The PDF may be encrypted or corrupted.", "提取失败，PDF 可能已加密或损坏。"),
    ("This PDF is password protected. Remove the password and try again.", "此 PDF 受密码保护，请先解除密码再试。"),
    ("PasswordException", "密码异常"),
    # qr-code
    ("QR code", "二维码"),
    ("Generated QR code preview", "生成的二维码预览"),
    ("Text or URL", "文字或网址"),
    ("Size", "尺寸"),
    ("Foreground", "前景色"),
    ("Background", "背景色"),
    ("Error correction", "纠错等级"),
    ("Could not export the QR code as PNG.", "无法将二维码导出为 PNG。"),
    ("Could not export the QR code as SVG.", "无法将二维码导出为 SVG。"),
    ("Could not generate a QR code from that input.", "无法根据输入内容生成二维码。"),
    # resize-video
    ("Resize video", "调整视频尺寸"),
    ("Preset", "预设"),
    ("Custom", "自定义"),
    ("Width (px)", "宽度（像素）"),
    ("Height (px)", "高度（像素）"),
    # social-preview
    ("Page details", "页面信息"),
    ("Page title", "页面标题"),
    ("Meta description", "页面描述"),
    ("Social image", "社交封面图"),
    ("Selected social", "当前平台"),
    ("Meta tags", "元标签"),
    ("Placeholder social image", "占位社交封面"),
    ("Your page title", "你的页面标题"),
    ("Could not create a canvas placeholder in this browser.", "当前浏览器无法创建 Canvas 占位图。"),
    ("That file is not an image. Drop a PNG, JPG, or WebP.", "该文件不是图片，请拖入 PNG、JPG 或 WebP 文件。"),
    # trim-video
    ("Trim", "裁剪"),
    ("Trim range", "裁剪范围"),
    ("Mode", "模式"),
    ("Fast copy (keyframe aligned)", "快速复制（按关键帧对齐）"),
    ("Precise re-encode", "精确重新编码"),
    ("No re-encoding, nearly instant. Cut points snap to the nearest keyframes, so the clip may start slightly early.", "不重新编码，几乎瞬间完成。切点会对齐到最近的关键帧，因此片段可能提前一点点开始。"),
    ("Trimming failed. Fast copy cannot handle every codec. Try the precise re-encode mode.", "裁剪失败。快速复制无法处理所有编码，请尝试精确重新编码模式。"),
    ("Trimming failed. This video codec may not be supported by the in-browser engine.", "裁剪失败。浏览器内置引擎可能不支持该视频编码。"),
    # video-converter
    ("Drop a video and pick a target container/codec.", "拖入视频后选择目标封装格式与编码。"),
    # video-to-gif
    ("Start time (seconds)", "开始时间（秒）"),
    ("Duration (seconds)", "持续时长（秒）"),
    ("Frame rate", "帧率"),
    ("Generated GIF preview", "生成的 GIF 预览"),
    ("That file isn't a video.", "该文件不是视频。"),
    ("Could not make the GIF. Check that the start time falls inside the clip and try a shorter duration.", "无法生成 GIF。请确认开始时间在视频时长内，并尝试缩短持续时间。"),
    # 共享组件
    ("Add more images", "添加更多图片"),
    ("Move up", "上移"),
    ("Move down", "下移"),
    ("Remove", "移除"),
    ("Page layout", "页面布局"),
    ("Fit page to each image", "每页适配一张图片"),
    ("Page size", "页面尺寸"),
    ("US Letter (centered)", "美式信纸（居中）"),
    ("Could not build the PDF. One of the images may be unreadable.", "无法生成 PDF，其中某张图片可能无法读取。"),
    ("Those files aren't images.", "这些文件不是图片。"),
]

TARGETS = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".next")]
    for f in files:
        if f.endswith((".tsx", ".ts")) and f != "content.ts":
            p = os.path.join(root, f)
            if "app/tools" in p.replace("\\", "/") or "components" in p.replace("\\", "/"):
                TARGETS.append(p)

hit = {}
for p in TARGETS:
    try:
        s = open(p, encoding="utf-8").read()
    except Exception:
        continue
    new = s
    for old, zh in MAP:
        for q in ('"', "'", "`"):
            token = q + old + q
            if token in new:
                new = new.replace(token, q + zh + q)
                hit[old] = hit.get(old, 0) + 1
        # JSX 文本节点 >Text<
        if ">" + old + "<" in new:
            new = new.replace(">" + old + "<", ">" + zh + "<")
            hit[old] = hit.get(old, 0) + 1
    if new != s:
        open(p, "w", encoding="utf-8", newline="").write(new)

print("TRANSLATED:", len(hit), "strings /", sum(hit.values()), "occurrences")
for k, v in sorted(hit.items()):
    print(f"  {v:3}  {k}")
