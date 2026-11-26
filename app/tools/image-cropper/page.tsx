import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { ImageCropperClient } from "./image-cropper-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线图片裁剪工具 | 乐云工具箱",
  description:
    "按比例或自由裁剪图片，适配头像与封面图，浏览器本地处理。",
};

export default function Page() {
  return (
    <ToolPage slug="image-cropper" content={content}>
      <ImageCropperClient />
    </ToolPage>
  );
}
