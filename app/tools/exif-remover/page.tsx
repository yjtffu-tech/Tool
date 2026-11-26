import type { Metadata } from "next";
import { ToolPage } from "@/components/tool/tool-page";
import { ExifRemoverClient } from "./exif-remover-client";
import content from "./content";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "在线照片隐私信息清除工具 | 乐云工具箱",
  description:
    "清除照片中的拍摄位置与设备信息，减少隐私泄露风险。",
  alternates: { canonical: canonicalUrl("/tools/exif-remover") },
};

export default function Page() {
  return (
    <ToolPage slug="exif-remover" content={content}>
      <ExifRemoverClient />
    </ToolPage>
  );
}
