import Link from "next/link";

export default function HomePage() {
  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-semibold">Agentic Insight Platform</h1>
      <p className="text-zinc-600">
        v6 — 9 Agent 自动化流水线。把 1 个抖音 URL 跑成"拆解 → 4 路交叉 → microtype 归类 →
        反向生成 → 多 LLM 自盲评 → DSPy prompt 自优化"，0 人工介入。
      </p>
      <ul className="grid grid-cols-2 gap-3 max-w-2xl">
        <li>
          <Link
            href="/cases"
            className="block bg-white border rounded-lg p-4 hover:border-zinc-400"
          >
            <div className="font-medium">Cases</div>
            <div className="text-sm text-zinc-500">
              已入库 case + 9 段拆解 + 原子 + 4 路交叉验证
            </div>
          </Link>
        </li>
        <li>
          <Link
            href="/alerts"
            className="block bg-white border rounded-lg p-4 hover:border-zinc-400"
          >
            <div className="font-medium">HITL Alerts</div>
            <div className="text-sm text-zinc-500">
              低置信度 / 新 microtype 候选 / 合规边界 等告警处理
            </div>
          </Link>
        </li>
      </ul>
    </div>
  );
}
