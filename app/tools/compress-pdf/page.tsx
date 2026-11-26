import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { CompressPdfClient } from "./compress-pdf-client";
import content from "./content";

export const metadata: Metadata = {
  title: "在线 PDF 压缩工具 | 轻盒工具箱",
  description:
    "减小 PDF 文件体积，便于邮件与系统上传，内容不外泄。",
};

export default function Page() {
  return (
    <ToolPage slug="compress-pdf" content={content}>
      <CompressPdfClient />
    </ToolPage>
  );
}
