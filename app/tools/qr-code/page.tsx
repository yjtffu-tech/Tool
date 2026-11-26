import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { QrCodeClient } from "./qr-code-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线二维码生成器 | 乐云工具箱",
  description: "把文字、网址或联系方式生成可自定义二维码，本地生成不上传内容。",
  alternates: { canonical: canonicalUrl("/tools/qr-code") },
};

export default function Page() {
  return (
    <ToolPage slug="qr-code" content={content}>
      <QrCodeClient />
    </ToolPage>
  );
}
