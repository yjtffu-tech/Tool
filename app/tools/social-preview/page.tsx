import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { SocialPreviewClient } from "./social-preview-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线社交媒体封面预览工具 | 乐云工具箱",
  description: "预览标题与封面在微信、小红书等平台的呈现效果，本地处理不上传素材。",
};

export default function Page() {
  return (
    <ToolPage slug="social-preview" content={content}>
      <SocialPreviewClient />
    </ToolPage>
  );
}
