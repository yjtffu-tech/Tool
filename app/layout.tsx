import type { Metadata, Viewport } from "next";
import { Analytics } from "@vercel/analytics/next";
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import { Providers } from "@/components/providers";
import { AppShell } from "@/components/shell/app-shell";
import { BRAND_ZH, SITE_URL, canonicalUrl } from "@/lib/site-config";
import "./globals.css";

const TITLE = `${BRAND_ZH} - 免费在线工具，文件在设备上处理`;
const DESCRIPTION =
  `${BRAND_ZH}提供视频转换、图片压缩、PDF 合并拆分等 14 款免费在线工具。文件在你的设备上处理，不会上传到我们的服务器。`;

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: TITLE,
    // 各页面 title 已自带品牌后缀，此处不再追加，避免双重后缀
    template: "%s",
  },
  description: DESCRIPTION,
  applicationName: BRAND_ZH,
  alternates: {
    canonical: canonicalUrl("/"),
  },
  keywords: [
    "在线工具", "视频转换", "图片压缩", "PDF合并", "PDF拆分", "二维码生成",
    "免费工具", "本地处理", "隐私保护", BRAND_ZH, "Leyun Tools",
  ],
  openGraph: {
    siteName: BRAND_ZH,
    locale: "zh_CN",
    type: "website",
    url: canonicalUrl("/"),
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
