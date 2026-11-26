import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { VideoConverterClient } from "./video-converter-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线视频格式转换工具 | 轻盒工具箱",
  description:
    "在浏览器内转换 MP4、WebM、MOV 等常见视频格式，文件不上传。",
};

export default function Page() {
  return (
    <ToolPage slug="video-converter" content={content}>
      <VideoConverterClient />
    </ToolPage>
  );
}
