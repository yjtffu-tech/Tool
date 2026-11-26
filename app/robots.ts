import type { MetadataRoute } from "next";

import { SITE_URL } from "@/lib/site-config";

const BASE = SITE_URL;

/** robots.txt served at /robots.txt. Everything is crawlable except the API. */
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
      disallow: "/api/",
    },
    sitemap: `${BASE}/sitemap.xml`,
    host: BASE,
  };
}
