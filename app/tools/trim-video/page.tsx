import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { TrimVideoClient } from "./trim-video-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线视频裁剪工具 | 乐云工具箱",
  description:
    "按起止时间截取视频片段，在浏览器本地完成，无需上传原片。",
  alternates: { canonical: canonicalUrl("/tools/trim-video") },
};

export default function Page() {
  return (
    <ToolPage slug="trim-video" content={content}>
      <TrimVideoClient />
    </ToolPage>
  );
}
