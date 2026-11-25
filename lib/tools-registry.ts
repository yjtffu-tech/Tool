import {
  Combine,
  Crop,
  Eraser,
  FileArchive,
  FileImage,
  FileStack,
  FileVideo2,
  Film,
  Images,
  LayoutTemplate,
  Minimize2,
  QrCode,
  Scaling,
  Scissors,
  type LucideIcon,
} from "lucide-react";

/** 中文分类。侧边栏、首页、搜索均按此顺序渲染。 */
export const TOOL_CATEGORIES = [
  "视频处理",
  "图片处理",
  "PDF 与文档",
  "自媒体与实用工具",
] as const;

export type ToolCategory = (typeof TOOL_CATEGORIES)[number];

/** "live" 工具拥有真实引擎；"soon" 渲染 ComingSoonTool 占位页。 */
export type ToolStatus = "live" | "soon";

export interface ToolDef {
  slug: string;
  name: string;
  description: string;
  category: ToolCategory;
  icon: LucideIcon;
  keywords: string[];
  /** 省略时默认 "live"。 */
  status?: ToolStatus;
  /** 驱动该工具的本地引擎，展示在页面徽标上。 */
  engine?: string;
}

/**
 * 全站工具唯一数据源。侧边栏、首页、命令搜索、工具页头均读取此处。
 * 只保留 14 个已完整汉化、面向华人高频需求的工具。
 */
export const TOOLS: ToolDef[] = [
  // ── 视频处理 ──────────────────────────────────────────────
  {
    slug: "video-converter",
    name: "视频格式转换",
    description: "在浏览器内把视频转成 MP4、WebM、MOV 或 MKV，无需上传。",
    category: "视频处理",
    icon: FileVideo2,
    keywords: ["视频", "格式转换", "mp4", "webm", "mov", "mkv", "ffmpeg"],
    engine: "FFmpeg (WebAssembly)",
  },
  {
    slug: "resize-video",
    name: "视频尺寸调整与压缩",
    description: "调整视频分辨率与体积，适配微信、小红书等平台的上传限制。",
    category: "视频处理",
    icon: Scaling,
    keywords: ["视频", "压缩", "尺寸", "分辨率", "微信", "小红书"],
    engine: "FFmpeg (WebAssembly)",
  },
  {
    slug: "trim-video",
    name: "视频裁剪",
    description: "精确截取视频片段，设定起止时间后本地导出。",
    category: "视频处理",
    icon: Scissors,
    keywords: ["视频", "裁剪", "截取", "剪辑", "ffmpeg"],
    engine: "FFmpeg (WebAssembly)",
  },
  {
    slug: "video-to-gif",
    name: "视频转 GIF",
    description: "把短视频片段转成循环播放的 GIF 动图，双通道调色板更清晰。",
    category: "视频处理",
    icon: Film,
    keywords: ["视频", "gif", "动图", "表情包", "转换"],
    engine: "FFmpeg (WebAssembly)",
  },

  // ── 图片处理 ──────────────────────────────────────────────
  {
    slug: "compress-image-size",
    name: "图片无损压缩",
    description: "压缩 JPG、PNG、WebP 图片体积，画质可控，全部本地完成。",
    category: "图片处理",
    icon: Minimize2,
    keywords: ["图片", "压缩", "jpg", "png", "webp", "体积"],
    engine: "Canvas",
  },
  {
    slug: "image-format-converter",
    name: "图片格式转换",
    description: "JPG、PNG、WebP 互相转换，保留清晰度，不上传原图。",
    category: "图片处理",
    icon: Images,
    keywords: ["图片", "格式转换", "jpg", "png", "webp"],
    engine: "Canvas",
  },
  {
    slug: "image-cropper",
    name: "图片裁剪",
    description: "自由裁剪图片或按常用比例裁切，适配封面、头像与商品图。",
    category: "图片处理",
    icon: Crop,
    keywords: ["图片", "裁剪", "比例", "封面", "头像"],
    engine: "HTML5 Canvas",
  },
  {
    slug: "exif-remover",
    name: "清除照片隐私信息",
    description: "一键清除照片 EXIF 元数据，抹掉拍摄位置与设备信息。",
    category: "图片处理",
    icon: Eraser,
    keywords: ["exif", "隐私", "照片", "元数据", "定位"],
    engine: "Canvas",
  },

  // ── PDF 与文档 ────────────────────────────────────────────
  {
    slug: "merge-pdf",
    name: "PDF 合并",
    description: "把多个 PDF 按顺序合并成一个文件，支持拖拽排序。",
    category: "PDF 与文档",
    icon: Combine,
    keywords: ["pdf", "合并", "拼接", "文档", "发票"],
    engine: "pdf-lib",
  },
  {
    slug: "split-pdf",
    name: "PDF 拆分",
    description: "按页码范围拆分 PDF，提取你需要的页面并单独下载。",
    category: "PDF 与文档",
    icon: FileStack,
    keywords: ["pdf", "拆分", "提取页面", "页码"],
    engine: "pdf-lib",
  },
  {
    slug: "compress-pdf",
    name: "PDF 压缩",
    description: "减小 PDF 文件体积，方便邮件与报关系统上传，内容不外泄。",
    category: "PDF 与文档",
    icon: FileArchive,
    keywords: ["pdf", "压缩", "减重", "邮件", "报关"],
    engine: "pdf-lib",
  },
  {
    slug: "jpg-to-pdf",
    name: "图片转 PDF",
    description: "把多张 JPG、PNG 图片按顺序合成一个 PDF 文档。",
    category: "PDF 与文档",
    icon: FileImage,
    keywords: ["图片", "pdf", "转pdf", "扫描件", "发票"],
    engine: "pdf-lib",
  },

  // ── 自媒体与实用工具 ──────────────────────────────────────
  {
    slug: "social-preview",
    name: "社交媒体封面预览",
    description: "预览标题与封面在微信、微博、小红书等平台的呈现效果。",
    category: "自媒体与实用工具",
    icon: LayoutTemplate,
    keywords: ["封面", "预览", "自媒体", "小红书", "公众号", "社交媒体"],
    engine: "Canvas",
  },
  {
    slug: "qr-code",
    name: "二维码生成器",
    description: "生成可自定义的二维码，支持文字、链接与联系方式。",
    category: "自媒体与实用工具",
    icon: QrCode,
    keywords: ["二维码", "qr", "生成", "链接", "名片"],
    engine: "qrcode",
  },
];

export function getTool(slug: string): ToolDef | undefined {
  return TOOLS.find((t) => t.slug === slug);
}

export function getToolsByCategory(category: ToolCategory): ToolDef[] {
  return TOOLS.filter((t) => t.category === category).sort(
    (a, b) => (isLive(a) ? 0 : 1) - (isLive(b) ? 0 : 1),
  );
}

export function isLive(tool: ToolDef): boolean {
  return tool.status !== "soon";
}

/** 渲染 ComingSoonTool 占位页的 slug 列表。当前为空。 */
export const SOON_SLUGS = TOOLS.filter((t) => t.status === "soon").map(
  (t) => t.slug,
);

/** 拥有可用引擎的工具数量，用于首页标题与搜索提示。 */
export const LIVE_TOOL_COUNT = TOOLS.filter(isLive).length;
