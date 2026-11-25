import { ShieldCheck } from "lucide-react";
import { cn } from "@/lib/utils";

export function PrivacyBadge({ className }: { className?: string }) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full border border-accent/30 bg-accent-muted/40 px-2.5 py-1 text-[11px] font-medium text-foreground",
        className,
      )}
      title="一切都在你的浏览器中本地处理，文件绝不上传。"
    >
      <ShieldCheck className="h-3.5 w-3.5 text-accent" aria-hidden />
      <span className="hidden sm:inline">100% 本地浏览器处理：您的文件绝不会上传至任何服务器</span>
      <span className="sm:hidden">100% 本地处理</span>
    </span>
  );
}
