import Link from "next/link";
import { ShieldCheck } from "lucide-react";

/** 全站页脚：版权声明、隐私提示与合规页面入口。 */
export function SiteFooter() {
  return (
    <footer className="border-t border-border px-4 py-6 sm:px-6">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-4 sm:flex-row sm:justify-between">
        <div className="flex flex-col items-center gap-1 sm:items-start">
          <p className="text-xs text-muted-foreground">
            &copy; 2026 乐云工具箱
          </p>
          <p className="inline-flex items-center gap-1.5 text-xs text-muted-foreground">
            <ShieldCheck className="h-3.5 w-3.5 shrink-0 text-accent" aria-hidden />
            100% 本地浏览器处理：您的文件绝不会上传至任何服务器
          </p>
        </div>

        <nav className="flex flex-wrap items-center justify-center gap-x-5 gap-y-2">
          <Link href="/about" className="text-xs text-muted-foreground transition-colors hover:text-foreground">关于我们</Link>
          <Link href="/privacy" className="text-xs text-muted-foreground transition-colors hover:text-foreground">隐私政策</Link>
          <Link href="/terms" className="text-xs text-muted-foreground transition-colors hover:text-foreground">使用条款</Link>
          <a href="mailto:tool@leyunke.com" className="text-xs text-muted-foreground transition-colors hover:text-foreground">联系我们</a>
        </nav>
      </div>
    </footer>
  );
}
