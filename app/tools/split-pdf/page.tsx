import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { SplitPdfClient } from "./split-pdf-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线 PDF 拆分工具 | 轻盒工具箱",
  description:
    "按页码范围或逐页导出拆分 PDF，文件不上传。",
};

export default function Page() {
  return (
    <ToolPage slug="split-pdf" content={content}>
      <SplitPdfClient />
    </ToolPage>
  );
}
