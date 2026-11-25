import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { SplitPdfClient } from "./split-pdf-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线 PDF 拆分工具 | 轻盒工具箱",
  description:
    "Pick pages from a thumbnail grid and extract them to a new PDF. 100% in your browser.",
};

export default function Page() {
  return (
    <ToolPage slug="split-pdf" content={content}>
      <SplitPdfClient />
    </ToolPage>
  );
}
