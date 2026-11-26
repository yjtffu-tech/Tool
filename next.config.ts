import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // All tools run client-side; nothing here needs server runtime config.
  reactStrictMode: true,
  // 全站禁止收录：与 robots.txt、meta robots 三层生效
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "X-Robots-Tag",
            value: "noindex, nofollow, noarchive, nosnippet",
          },
        ],
      },
    ];
  },
};

export default nextConfig;
