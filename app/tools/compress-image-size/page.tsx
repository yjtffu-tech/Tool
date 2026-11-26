import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { CompressImageSizeClient } from "./compress-image-size-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线图片无损压缩工具 | 乐云工具箱",
  description:
    "压缩 JPG、PNG、WebP 图片体积，可预览画质，本地处理。",
  alternates: { canonical: canonicalUrl("/tools/compress-image-size") },
};

export default function Page() {
  return (
    <ToolPage slug="compress-image-size" content={content}>
      <CompressImageSizeClient />
    </ToolPage>
  );
}
