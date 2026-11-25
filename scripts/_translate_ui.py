"""批量汉化 UI 文案：只对引号内的自然语言串做精确 REPLACE，不动代码标识符。
逐条断言命中；未命中的条目在报告里列出，便于人工核查。
"""
import os

# (old, new) —— 精确串，长串优先
MAP = [
    # shell
    ("LiteBox home", "轻盒工具箱首页"),
    ("Search tools...", "搜索工具..."),
    ("Search tools", "搜索工具"),
    ("Collapse sidebar", "收起侧边栏"),
    ("Expand sidebar", "展开侧边栏"),
    ("Open menu", "打开菜单"),
    ("Close menu", "关闭菜单"),
    ("Download the Android app", "下载安卓应用"),
    ("Switch to dark mode", "切换到深色模式"),
    ("Switch to light mode", "切换到浅色模式"),
    ("Toggle theme", "切换主题"),
    ("Everything runs locally in your browser. Nothing is uploaded.", "一切都在你的浏览器中本地处理，文件绝不上传。"),
    ("Tools", "工具"),
    ("Pricing", "价格"),
    ("Get the app", "下载应用"),
    ("Android app", "安卓应用"),
    # tool 通用
    ("Copied", "已复制"),
    ("Copy", "复制"),
    ("Options", "选项"),
    ("Preview", "预览"),
    ("Input", "输入"),
    ("Output", "输出"),
    ("Could not decode that image.", "无法解析该图片。"),
    ("Processing failed.", "处理失败。"),
    ("That file isn't an image.", "该文件不是图片。"),
    ("Could not process this input.", "无法处理此输入。"),
    ("Related tools", "相关工具"),
    ("What is ", "什么是"),
    ("How to use ", "如何使用"),
    ("Common uses", "常见用途"),
    ("Why choose LiteBox", "为什么选择轻盒工具箱"),
    ("Frequently asked questions", "常见问题"),
    ("100% private", "100% 隐私保护"),
    ("Free, no account", "免费，无需注册"),
    ("Instant", "即时处理"),
    ("Runs in your browser", "在浏览器中运行"),
    ("No upload size caps", "无文件大小限制"),
    ("Yours to keep", "结果归你所有"),
    # tool 通用正文
    ("Your files are processed inside your browser and are never uploaded to a server.", "你的文件只在浏览器内部处理，绝不会上传到任何服务器。"),
    ("No sign-up, no watermark, no paywalled “premium” tier. Just open a tool and use it.", "无需注册、没有水印、没有付费墙。打开工具即可使用。"),
    ("No upload, no queue, no server round-trip — work starts the moment you drop a file.", "无需上传、无需排队、无需服务器往返——放入文件立刻开始处理。"),
    ("Built on open web standards. Works on any modern desktop browser, nothing to install.", "基于开放网页标准，任何现代桌面浏览器都能使用，无需安装。"),
    ("Nothing leaves your device, so there’s no server file-size limit — only your machine’s memory.", "文件不离开你的设备，因此没有服务器端大小限制——只受本机内存约束。"),
    ("Results download straight to your device in clean, standard file formats.", "结果以干净的标准格式直接下载到你的设备。"),
]

TARGETS = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".next", "removed_tools_20261125")]
    for f in files:
        if f.endswith((".ts", ".tsx")):
            p = os.path.join(root, f)
            if p.startswith((".\\app\\tools\\", ".\\lib\\tool-content")) and "/content.ts" in p.replace("\\", "/"):
                continue  # content.ts 已整体重写
            TARGETS.append(p)

hit = {}
missed = []
for p in TARGETS:
    try:
        s = open(p, encoding="utf-8").read()
    except Exception:
        continue
    new = s
    local = 0
    for old, zh in MAP:
        # 仅替换引号包裹的完整串，避免误伤标识符
        for q in ('"', "'", "`"):
            token = q + old + q
            if token in new:
                new = new.replace(token, q + zh + q)
                local += new.count(q + zh + q) - (s.count(q + zh + q) if s else 0)
                hit[old] = hit.get(old, 0) + 1
    if new != s:
        open(p, "w", encoding="utf-8", newline="").write(new)

print("TRANSLATED_STRINGS:", len(hit))
for k, v in sorted(hit.items()):
    print(f"  {v:3}  {k}")
