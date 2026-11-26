<div align="center">

# 🧰 轻盒工具箱 (LiteBox)

### 面向华人用户的免费在线工具站 —— 14 款高频工具，100% 在浏览器中本地处理。

**你放入的文件绝不会离开设备。** 无上传、无账号、无水印。打开工具即可使用。

站点：https://www.leyunke.com

</div>

---

## 为什么是轻盒工具箱

大多数「免费在线工具」会把你的文件上传到服务器处理。轻盒工具箱相反：每个工具都用浏览器原生能力（WebAssembly、Canvas、Web Audio API、File API）在你的电脑上完成处理。文件不经由任何服务器，你无需信任我们「会保管好文件」——因为我们技术上根本没有机会接触它们。

- 100% 本地浏览器处理，文件不上传
- 完全免费，无需注册，无水印
- 14 款工具全部完整汉化，含华人常见场景与参数建议
- 仅首次使用视频工具时下载 FFmpeg 引擎（约 31 MB），此后缓存

## 工具列表（14 款）

**视频处理**：视频格式转换 · 视频尺寸调整与压缩 · 视频裁剪 · 视频转 GIF

**图片处理**：图片无损压缩 · 图片格式转换 · 图片裁剪 · 清除照片隐私信息（EXIF）

**PDF 与文档**：PDF 合并 · PDF 拆分 · PDF 压缩 · 图片转 PDF

**自媒体与实用工具**：社交媒体封面预览 · 二维码生成器

## 技术栈

Next.js 15 (App Router) · React 19 · TypeScript (strict) · Tailwind CSS v4 · next-themes · Lucide icons

本地引擎：`@ffmpeg/ffmpeg`（WebAssembly）、`pdf-lib`、`pdfjs-dist`、`jszip`、Canvas、Web Audio API、Web Crypto API、qrcode。所有重型库按需动态导入。

## 本地运行

```bash
npm install
npm run dev        # http://localhost:3000
npm run build      # 生产构建
npm run typecheck  # 类型检查
```

无需环境变量。仓库中 `.env.example` 仅描述可选配置，留空即可。

## 目录约定

- `lib/tools-registry.ts` — 工具唯一数据源（slug、名称、描述、分类、图标、关键词）。侧栏、首页、搜索、sitemap 全部由它生成。
- `app/tools/<slug>/` — 每个工具一个独立目录，含 `page.tsx`、客户端实现、`content.ts`（中文长文说明）、OG 图。
- `components/tool/` — 共享壳体（文件上传区、Canvas 工具、文本工具、FAQ 等）。
- `components/shell/` — 全站导航、页脚、搜索、隐私徽标。

新增工具：在 registry 加一条 + 建一个 `app/tools/<slug>/` 目录，导航与 sitemap 自动同步。

## 合规页面

- `/privacy` 隐私政策（含 Google Analytics 与 Google AdSense Cookie 说明）
- `/terms` 使用条款
- `/about` 关于我们

联系邮箱：tool@leyunke.com

## License

MIT License. 详见 [LICENSE](./LICENSE)。
