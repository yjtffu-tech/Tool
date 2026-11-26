import type { MetadataRoute } from "next";

/** robots.txt served at /robots.txt. The entire site is disallowed. */
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      disallow: "/",
    },
  };
}
