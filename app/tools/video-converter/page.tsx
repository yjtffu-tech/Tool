import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { VideoConverterClient } from "./video-converter-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线视频格式转换工具 | 轻盒工具箱",
  description:
    "Convert between MP4, WebM, MOV, and MKV. Runs 100% in your browser — no uploads.",
};

export default function Page() {
  return (
    <ToolPage slug="video-converter" content={content}>
      <VideoConverterClient />
    </ToolPage>
  );
}
