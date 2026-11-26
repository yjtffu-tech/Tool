import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { VideoToGifClient } from "./video-to-gif-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线视频转 GIF 动图工具 | 乐云工具箱",
  description: "把短视频片段转成高清循环 GIF，本地 FFmpeg 处理，文件不上传。",
  alternates: { canonical: canonicalUrl("/tools/video-to-gif") },
};

export default function Page() {
  return (
    <ToolPage slug="video-to-gif" content={content}>
      <VideoToGifClient />
    </ToolPage>
  );
}
