import Link from "next/link";
import {
  LIVE_TOOL_COUNT,
  TOOL_CATEGORIES,
  getToolsByCategory,
} from "@/lib/tools-registry";

export default function DashboardPage() {
  return (
    <div className="mx-auto w-full max-w-5xl px-4 py-12 sm:px-6 sm:py-16">
      <div className="mx-auto max-w-2xl text-center">
        <h1 className="text-3xl font-semibold tracking-tight sm:text-4xl">
          轻盒工具箱 - 免费、隐私优先的在线工具
        </h1>
        <p className="mt-3 text-base leading-relaxed text-muted-foreground">
          {LIVE_TOOL_COUNT} 款实用工具，全部在你的浏览器中运行。无需注册、没有水印，你放入的任何文件都不会离开设备。
        </p>
        <p className="mt-4 inline-flex items-center gap-2 rounded-full border border-border bg-muted/50 px-3 py-1.5 text-xs text-muted-foreground">
          100% 本地浏览器处理：您的文件绝不会上传至任何服务器
        </p>
      </div>

      <div className="mt-14 space-y-12">
        {TOOL_CATEGORIES.map((category) => (
          <section key={category}>
            <h2 className="text-lg font-semibold tracking-tight">{category}</h2>
            <div className="mt-4 grid gap-x-6 gap-y-1 sm:grid-cols-2 lg:grid-cols-3">
              {getToolsByCategory(category).map((tool) => {
                const Icon = tool.icon;
                return (
                  <Link
                    key={tool.slug}
                    href={`/tools/${tool.slug}`}
                    className="group flex items-center gap-3 rounded-md px-2 py-2 transition-colors hover:bg-muted"
                  >
                    <Icon
                      className="h-5 w-5 shrink-0 text-muted-foreground transition-colors group-hover:text-accent"
                      aria-hidden
                    />
                    <span className="truncate text-sm text-foreground">{tool.name}</span>
                  </Link>
                );
              })}
            </div>
          </section>
        ))}
      </div>

      <p className="mt-16 border-t border-border pt-6 text-center text-xs text-muted-foreground">
        轻盒工具箱完全免费，所有处理均在本地完成。按 Ctrl K 可快速搜索工具。
      </p>
    </div>
  );
}
