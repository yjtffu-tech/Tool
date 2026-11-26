import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { ResizeVideoClient } from "./resize-video-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线视频尺寸调整与压缩工具 | 乐云工具箱",
  description:
    "调整视频分辨率与体积，适配常见平台上传要求，本地处理。",
  alternates: { canonical: canonicalUrl("/tools/resize-video") },
};

export default function Page() {
  return (
    <ToolPage slug="resize-video" content={content}>
      <ResizeVideoClient />
    </ToolPage>
  );
}
