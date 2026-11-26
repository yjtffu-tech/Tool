import type { Metadata } from "next";
import { LegalPage } from "@/components/legal/legal-page";
import { LIVE_TOOL_COUNT } from "@/lib/tools-registry";

export const metadata: Metadata = {
  title: "隐私政策 - 乐云工具箱",
  description:
    "乐云工具箱如何处理数据：所有文件都在你的浏览器中本地处理，绝不上传；同时说明 Google Analytics 与 Google AdSense Cookie 的使用。",
};

export default function Page() {
  return (
    <LegalPage
      title="隐私政策"
      lastUpdated="2026 年 11 月 25 日"
      intro="乐云工具箱的设计原则是：你的文件永远不离开你的设备。本政策说明我们处理哪些极有限的数据，以及为什么。"
    >
      <h2>一、我们是谁</h2>
      <p>
        乐云工具箱（英文名 Leyun Tools，以下简称「我们」）运营网站{" "}
        <a href="https://www.leyunke.com">https://www.leyunke.com</a> 及其上的全部工具。
        隐私相关问题或请求，请发送邮件至{" "}
        <a href="mailto:tool@leyunke.com">tool@leyunke.com</a>。
      </p>

      <h2>二、你的文件永不离开设备</h2>
      <p>这是本页最重要的一条，因此放在最前面。</p>
      <p>
        本站全部 {LIVE_TOOL_COUNT} 款工具都 <strong>100% 在你的浏览器内运行</strong>，
        使用 WebAssembly、HTML5 Canvas 与 Web Audio API 等技术。你上传的视频、音频、PDF、
        图片、文档和文字，全部在你自己的设备上打开、处理并下载。
      </p>
      <ul>
        <li>你的文件<strong>绝不会被上传、传输、接收、查看、存储</strong>，我们也无法访问。</li>
        <li>我们不运行接收文件的服务器。<strong>本站没有文件上传接口。</strong></li>
        <li>因此我们<strong>无法</strong>访问、恢复或删除你的文件——因为我们从未拥有过它们。你始终保有完全控制权。</li>
      </ul>
      <p>
        你可以自行验证：打开浏览器的开发者工具，切到 Network（网络）标签，然后运行任意工具。
        你不会看到你的文件被发送到任何地方。首次使用视频工具时浏览器会从公共组件源下载约 31 MB 的
        FFmpeg 引擎，这是唯一的网络请求，且不包含你的任何文件。
      </p>

      <h2>三、Cookie 与第三方服务</h2>
      <p>
        为了满足网站运营与广告投放的需要，本站使用以下第三方服务。它们可能在你访问时设置 Cookie
        或使用类似技术：
      </p>
      <ul>
        <li>
          <strong>Google Analytics（谷歌分析）</strong>：用于统计访问量与使用趋势，了解哪些工具更受欢迎。
          我们启用了 IP 匿名化，并尽可能减少数据留存。Google Analytics 可能使用 Cookie 区分匿名访客。
        </li>
        <li>
          <strong>Google AdSense</strong>：用于在页面展示广告、衡量广告效果并向你提供相关广告。
          AdSense 及其合作伙伴可能使用 Cookie 或设备标识符来投放和个性化广告。
        </li>
        <li>
          <strong>Vercel Analytics</strong>：用于无 Cookie 的匿名流量统计，不跨站追踪访客。
        </li>
      </ul>
      <p>
        上述 Cookie 与你的本地文件处理完全无关——它们只用于统计与广告，不会读取你放入工具的文件内容。
      </p>

      <h2>四、如何管理 Cookie 与广告偏好</h2>
      <p>
        你可以通过浏览器设置删除或阻止 Cookie，也可以访问{" "}
        <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener noreferrer">
          Google 广告设置
        </a>{" "}
        管理个性化广告偏好，或通过浏览器安装广告拦截扩展。禁用 Cookie 不会影响工具本身的使用——
        所有工具仍然可以正常工作。
      </p>
      <p>
        欧洲经济区、英国及加州访客可依据当地法规（GDPR、CCPA 等）行使访问、删除、反对处理等权利。
        如需行使相关权利，请通过上面的邮箱联系我们；涉及 Google 服务收集的数据，也可直接向 Google 提出请求。
      </p>

      <h2>五、我们存储什么</h2>
      <p>
        我们不在服务器上存储你的文件，也不要求你注册账号，因此不会保存你的姓名、邮箱或文件副本。
        你的浏览器可能会在本地缓存中保存已下载的 FFmpeg 引擎以提升速度，这些数据仅存在于你的设备上，
        可随时通过清除浏览器缓存删除。
      </p>

      <h2>六、儿童隐私</h2>
      <p>
        本站不面向 13 岁以下的儿童，也不会有意收集儿童个人信息。如果你发现儿童向我们提供了个人信息，
        请通过上述邮箱联系我们，我们会及时处理。
      </p>

      <h2>七、政策更新</h2>
      <p>
        我们可能随业务发展更新本政策。更新后的版本会公布在本页并标注新的更新日期。继续使用本站即表示你接受更新后的政策。
      </p>

      <h2>八、联系我们</h2>
      <p>
        对本政策有任何疑问，请发送邮件至{" "}
        <a href="mailto:tool@leyunke.com">tool@leyunke.com</a>。
      </p>
    </LegalPage>
  );
}
