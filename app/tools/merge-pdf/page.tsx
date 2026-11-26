import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { MergePdfClient } from "./merge-pdf-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线 PDF 合并工具 | 轻盒工具箱",
  description:
    "把多份 PDF 按指定顺序合并为一个文件，拖拽排序，本地处理。",
};

export default function Page() {
  return (
    <ToolPage slug="merge-pdf" content={content}>
      <MergePdfClient />
    </ToolPage>
  );
}
