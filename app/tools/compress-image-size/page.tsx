import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { CompressImageSizeClient } from "./compress-image-size-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线图片无损压缩工具 | 轻盒工具箱",
  description:
    "压缩 JPG、PNG、WebP 图片体积，可预览画质，本地处理。",
};

export default function Page() {
  return (
    <ToolPage slug="compress-image-size" content={content}>
      <CompressImageSizeClient />
    </ToolPage>
  );
}
