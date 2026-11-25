import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { TrimVideoClient } from "./trim-video-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线视频裁剪工具 | 轻盒工具箱",
  description:
    "Cut video clips locally with in-browser FFmpeg. Your video never leaves this device.",
};

export default function Page() {
  return (
    <ToolPage slug="trim-video" content={content}>
      <TrimVideoClient />
    </ToolPage>
  );
}
