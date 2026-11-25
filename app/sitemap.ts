import type { MetadataRoute } from "next";
import { TOOLS } from "@/lib/tools-registry";

const BASE = "https://liteboxtools.com";

/**
 * 站点地图：仅收录首页、三个合规页面与 14 个已完整汉化的工具页。
 * 工具 URL 来自 tools-registry.ts 单一数据源；被隐藏的英文工具不会进入 sitemap。
 */
export default function sitemap(): MetadataRoute.Sitemap {
  const lastModified = new Date().toISOString().split("T")[0];

  const staticRoutes: MetadataRoute.Sitemap = [
    { url: BASE, lastModified, changeFrequency: "weekly", priority: 1.0 },
    { url: `${BASE}/about`, lastModified, changeFrequency: "monthly", priority: 0.5 },
    { url: `${BASE}/privacy`, lastModified, changeFrequency: "yearly", priority: 0.3 },
    { url: `${BASE}/terms`, lastModified, changeFrequency: "yearly", priority: 0.3 },
  ];

  const toolRoutes: MetadataRoute.Sitemap = TOOLS.map((tool) => ({
    url: `${BASE}/tools/${tool.slug}`,
    lastModified,
    changeFrequency: "monthly",
    priority: 0.8,
  }));

  return [...staticRoutes, ...toolRoutes];
}
