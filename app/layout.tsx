import type { Metadata, Viewport } from "next";
import { Analytics } from "@vercel/analytics/next";
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import { Providers } from "@/components/providers";
import { AppShell } from "@/components/shell/app-shell";
import "./globals.css";

const TITLE = "轻盒工具箱 - 免费在线工具，100% 本地浏览器处理";
const DESCRIPTION =
  "轻盒工具箱提供视频转换、图片压缩、PDF 合并拆分等 14 款免费在线工具。全部在浏览器本地运行，文件不上传、无需注册、无水印。";

export const metadata: Metadata = {
  metadataBase: new URL("https://liteboxtools.com"),
  title: {
    default: TITLE,
    // 各页面 title 已自带品牌后缀，此处不再追加，避免 "A | 轻盒工具箱 | 轻盒工具箱"
    template: "%s",
  },
  description: DESCRIPTION,
  applicationName: "轻盒工具箱",
  keywords: [
    "在线工具", "视频转换", "图片压缩", "PDF合并", "PDF拆分", "二维码生成",
    "免费工具", "本地处理", "隐私保护", "轻盒工具箱", "LiteBox",
  ],
  openGraph: {
    siteName: "轻盒工具箱",
    locale: "zh_CN",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
  },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fafafa" },
    { media: "(prefers-color-scheme: dark)", color: "#050505" },
  ],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="zh-CN"
      suppressHydrationWarning
      className={`${GeistSans.variable} ${GeistMono.variable}`}
    >
      <body>
        <Providers>
          <AppShell>{children}</AppShell>
        </Providers>
        <Analytics />
      </body>
    </html>
  );
}
