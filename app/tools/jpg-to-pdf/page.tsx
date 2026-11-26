import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { ImagesToPdfClient } from "../_shared/images-to-pdf-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线图片转 PDF 工具 | 乐云工具箱",
  description:
    "把多张 JPG、PNG 图片按顺序合成 PDF，浏览器本地完成。",
};

export default function Page() {
  return (
    <ToolPage slug="jpg-to-pdf" content={content}>
      <ImagesToPdfClient
        accept="image/jpeg,.jpg,.jpeg"
        hint="拖入一张或多张 JPG，调整顺序后导出为单个 PDF。"
      />
    </ToolPage>
  );
}
