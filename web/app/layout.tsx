import "./globals.css";
import type { ReactNode } from "react";
import Link from "next/link";

export const metadata = {
  title: "Agentic Insight",
  description: "v6 — 9 Agent 内容洞察自动化",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="zh-CN">
      <body className="bg-zinc-50 text-zinc-900 min-h-screen">
        <header className="border-b bg-white">
          <nav className="max-w-6xl mx-auto px-6 py-3 flex items-center gap-6 text-sm">
            <Link href="/" className="font-semibold">Agentic Insight</Link>
            <Link href="/cases" className="hover:underline">Cases</Link>
            <Link href="/atoms" className="hover:underline">Atoms</Link>
            <Link href="/microtypes" className="hover:underline">Microtypes</Link>
            <Link href="/scripts" className="hover:underline">Scripts</Link>
            <Link href="/prompts" className="hover:underline">Prompts</Link>
            <Link href="/alerts" className="hover:underline">Alerts</Link>
            <a
              href="http://localhost:8233"
              target="_blank"
              rel="noreferrer"
              className="ml-auto text-zinc-500 hover:underline"
            >
              Temporal UI ↗
            </a>
          </nav>
        </header>
        <main className="max-w-6xl mx-auto px-6 py-6">{children}</main>
      </body>
    </html>
  );
}
