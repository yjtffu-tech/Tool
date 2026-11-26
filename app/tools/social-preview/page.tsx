import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { SocialPreviewClient } from "./social-preview-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线社交媒体封面预览工具 | 乐云工具箱",
  description: "预览标题与封面在微信、小红书等平台的呈现效果，本地处理不上传素材。",
  alternates: { canonical: canonicalUrl("/tools/social-preview") },
};

export default function Page() {
  return (
    <ToolPage slug="social-preview" content={content}>
      <SocialPreviewClient />
    </ToolPage>
  );
}
