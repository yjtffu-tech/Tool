import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { ImageFormatConverterClient } from "./image-format-converter-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线图片格式转换工具 | 乐云工具箱",
  description:
    "在 JPG、PNG、WebP 等常见图片格式之间转换，本地完成。",
  alternates: { canonical: canonicalUrl("/tools/image-format-converter") },
};

export default function Page() {
  return (
    <ToolPage slug="image-format-converter" content={content}>
      <ImageFormatConverterClient />
    </ToolPage>
  );
}
