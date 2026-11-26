import type { Metadata } from "next";
import { LegalPage } from "@/components/legal/legal-page";
import { canonicalUrl } from "@/lib/site-config";

export const metadata: Metadata = {
  title: "开源致谢 - 乐云工具箱",
  description: "乐云工具箱使用的第三方开源组件、版本、协议与项目链接。",
  alternates: { canonical: canonicalUrl("/open-source") },
};

/** 主要第三方依赖。协议由 license-checker 实测（production，111 包）。 */
const DEPS = [
  ["Next.js", "15.5.20", "MIT", "https://github.com/vercel/next.js"],
  ["React / React DOM", "19.2.7", "MIT", "https://react.dev/"],
  ["@ffmpeg/ffmpeg", "0.12.15", "MIT", "https://github.com/ffmpegwasm/ffmpeg.wasm"],
  ["@ffmpeg/util", "0.12.2", "MIT", "https://github.com/ffmpegwasm/ffmpeg.wasm"],
  ["pdf-lib", "1.17.1", "MIT", "https://github.com/Hopding/pdf-lib"],
  ["@cantoo/pdf-lib", "2.7.4", "MIT", "https://github.com/cantoo-gmbh/pdf-lib"],
  ["pdfjs-dist", "4.10.38", "Apache-2.0", "https://github.com/mozilla/pdf.js"],
  ["jsQR", "1.4.0", "Apache-2.0", "https://github.com/cozmo/jsQR"],
  ["qrcode", "1.5.4", "MIT", "https://github.com/soldair/node-qrcode"],
  ["JSZip", "3.10.1", "MIT OR GPL-3.0-or-later", "https://github.com/Stuk/jszip"],
  ["Lucide", "0.468.0", "ISC", "https://github.com/lucide-icons/lucide"],
  ["Geist Fonts", "1.7.2", "MIT", "https://github.com/vercel/geist-font"],
  ["next-themes", "0.4.6", "MIT", "https://github.com/pacocoursey/next-themes"],
  ["@vercel/analytics", "2.0.1", "MIT", "https://github.com/vercel/analytics"],
];

export default function Page() {
  return (
    <LegalPage
      title="开源致谢"
      lastUpdated="2026 年 11 月 26 日"
      intro="本站的许多功能由开源项目提供。以下列出主要第三方组件的名称、版本、协议与项目链接。"
    >
      <table>
        <thead>
          <tr><th>组件</th><th>版本</th><th>协议</th><th>项目</th></tr>
        </thead>
        <tbody>
          {DEPS.map(([name, version, license, url]) => (
            <tr key={name}>
              <td>{name}</td>
              <td>{version}</td>
              <td>{license}</td>
              <td><a href={url} target="_blank" rel="noopener noreferrer">链接</a></td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>完整依赖清单</h2>
      <p>
        生产依赖共 111 个包，协议分布：MIT 81、ISC 11、Apache-2.0 5、BSD-3-Clause 3、0BSD 2，
        其余为双协议或特殊协议。可用 <code>npx license-checker --production --summary</code> 复核。
      </p>

      <h2>注意事项</h2>
      <ul>
        <li>首次使用视频工具时，浏览器会从公共组件源下载约 31 MB 的 FFmpeg 引擎并缓存。</li>
        <li>JSZip 采用 MIT 或 GPL-3.0-or-later 双协议，本站按 MIT 分支使用。</li>
        <li>@img/sharp-win32-x64 含 LGPL-3.0-or-later 组件，仅用于构建期，不随页面分发给用户。</li>
      </ul>

      <p>
        如需完整协议信息，请查看仓库中的 LICENSE 与各依赖包自带的授权文件。
      </p>
    </LegalPage>
  );
}
