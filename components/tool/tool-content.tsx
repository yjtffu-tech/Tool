import Link from "next/link";
import {
  Check,
  CircleDollarSign,
  HardDriveDownload,
  Infinity as InfinityIcon,
  MonitorSmartphone,
  ShieldCheck,
  Zap,
} from "lucide-react";
import type { ToolContent } from "@/lib/tool-content";
import { getToolsByCategory, isLive, type ToolDef } from "@/lib/tools-registry";
import { FaqAccordion } from "./faq-accordion";

/** Shared, honest value props — every tool is genuinely client-side. */
const WHY = [
  {
    icon: ShieldCheck,
    title: "100% 隐私保护",
    body: "你的文件只在浏览器内部处理，绝不会上传到任何服务器。",
  },
  {
    icon: CircleDollarSign,
    title: "免费，无需注册",
    body: "无需注册、没有水印、没有付费墙。打开工具即可使用。",
  },
  {
    icon: Zap,
    title: "即时处理",
    body: "无需上传、无需排队、无需服务器往返——放入文件立刻开始处理。",
  },
  {
    icon: MonitorSmartphone,
    title: "在浏览器中运行",
    body: "基于开放网页标准，任何现代桌面浏览器都能使用，无需安装。",
  },
  {
    icon: InfinityIcon,
    title: "无文件大小限制",
    body: "文件不离开你的设备，因此没有服务器端大小限制——只受本机内存约束。",
  },
  {
    icon: HardDriveDownload,
    title: "结果归你所有",
    body: "结果以干净的标准格式直接下载到你的设备。",
  },
];

function RelatedTools({ tool }: { tool: ToolDef }) {
  const related = getToolsByCategory(tool.category)
    .filter((t) => t.slug !== tool.slug && isLive(t))
    .slice(0, 8);
  if (related.length === 0) return null;

  return (
    <section>
      <h2 className="text-lg font-semibold tracking-tight">相关工具</h2>
      <div className="mt-3 flex flex-wrap gap-2">
        {related.map((t) => {
          const Icon = t.icon;
          return (
            <Link
              key={t.slug}
              href={`/tools/${t.slug}`}
              className="inline-flex items-center gap-1.5 rounded-full border border-border bg-card px-3 py-1.5 text-sm text-foreground transition-colors hover:border-accent/50 hover:bg-muted"
            >
              <Icon className="h-3.5 w-3.5 text-accent" aria-hidden />
              {t.name}
            </Link>
          );
        })}
      </div>
    </section>
  );
}

/**
 * Long-form content rendered beneath a tool: what it does, how to use it,
 * common uses, why LiteBox, FAQs, and related tools. 123apps-style structure,
 * LiteBox design system.
 */
export function ToolContentSections({
  tool,
  content,
}: {
  tool: ToolDef;
  content: ToolContent;
}) {
  return (
    <div className="mt-14 space-y-14 border-t border-border pt-10">
      {/* What it does */}
      <section className="max-w-3xl">
        <h2 className="text-lg font-semibold tracking-tight">
          什么是{tool.name}？
        </h2>
        <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
          {content.intro}
        </p>
      </section>

      {/* How to use */}
      <section>
        <h2 className="text-lg font-semibold tracking-tight">
          如何使用{tool.name}
        </h2>
        <ol className="mt-5 grid gap-5 sm:grid-cols-2">
          {content.steps.map((step, i) => (
            <li key={i} className="flex gap-3">
              <span
                className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-accent text-sm font-semibold text-accent-foreground"
                aria-hidden
              >
                {i + 1}
              </span>
              <div className="min-w-0">
                <p className="text-sm font-medium text-foreground">{step.title}</p>
                <p className="mt-0.5 text-sm leading-relaxed text-muted-foreground">
                  {step.body}
                </p>
              </div>
            </li>
          ))}
        </ol>
      </section>

      {/* Common uses */}
      {content.useCases.length > 0 && (
        <section className="max-w-3xl">
          <h2 className="text-lg font-semibold tracking-tight">常见用途</h2>
          <ul className="mt-4 grid gap-2.5 sm:grid-cols-2">
            {content.useCases.map((use, i) => (
              <li key={i} className="flex items-start gap-2.5 text-sm text-muted-foreground">
                <Check className="mt-0.5 h-4 w-4 shrink-0 text-accent" aria-hidden />
                <span>{use}</span>
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Why LiteBox */}
      <section>
        <h2 className="text-lg font-semibold tracking-tight">为什么选择轻盒工具箱</h2>
        <div className="mt-5 grid gap-x-8 gap-y-6 sm:grid-cols-2 lg:grid-cols-3">
          {WHY.map(({ icon: Icon, title, body }) => (
            <div key={title} className="flex flex-col gap-1.5">
              <Icon className="h-5 w-5 text-accent" aria-hidden />
              <p className="text-sm font-semibold text-foreground">{title}</p>
              <p className="text-sm leading-relaxed text-muted-foreground">{body}</p>
            </div>
          ))}
        </div>
      </section>

      {/* FAQ */}
      {content.faqs.length > 0 && (
        <section className="max-w-3xl">
          <h2 className="text-lg font-semibold tracking-tight">
            常见问题
          </h2>
          <div className="mt-5">
            <FaqAccordion faqs={content.faqs} />
          </div>
        </section>
      )}

      <RelatedTools tool={tool} />
    </div>
  );
}
