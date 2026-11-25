import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { ResizeVideoClient } from "./resize-video-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线视频尺寸调整与压缩工具 | 轻盒工具箱",
  description:
    "Scale a video to a new resolution or preset. Runs 100% in your browser — no uploads.",
};

export default function Page() {
  return (
    <ToolPage slug="resize-video" content={content}>
      <ResizeVideoClient />
    </ToolPage>
  );
}
