import Link from "next/link";
import { api, type ScriptDetail } from "@/lib/api";

const DIM_LABELS: Record<string, string> = {
  hook: "钩子",
  pain: "痛点",
  trust: "信任",
  cta: "CTA",
  compliance: "合规",
  creativity: "原创",
  exec: "可执行",
};

export default async function ScriptDetailPage({ params }: { params: { id: string } }) {
  let detail: ScriptDetail | null = null;
  let error: string | null = null;
  try {
    detail = await api.getScript(params.id);
  } catch (e) {
    error = (e as Error).message;
  }

  if (error || !detail) {
    return (
      <div className="space-y-3">
        <Link href="/scripts" className="text-sm text-blue-600">← Scripts</Link>
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          {error || "Script not found"}
        </div>
      </div>
    );
  }

  const { script, critic_scores } = detail;

  // 聚合 3 家 evaluator 得分均值
  const dims = Object.keys(DIM_LABELS);
  const avg: Record<string, number> = {};
  for (const d of dims) {
    const vals = critic_scores
      .map((c) => c.scores?.[d])
      .filter((v): v is number => typeof v === "number");
    if (vals.length > 0) {
      avg[d] = Number((vals.reduce((a, b) => a + b, 0) / vals.length).toFixed(1));
    }
  }

  return (
    <div className="space-y-6">
      <Link href="/scripts" className="text-sm text-blue-600">← Scripts</Link>

      <div className="bg-white border rounded p-4 space-y-2">
        <div className="text-xs text-zinc-500">
          prompt={script.prompt_version} · model={script.llm_model} ·{" "}
          {new Date(script.generated_at).toLocaleString("zh-CN")}
          {script.for_internal_research_only && (
            <span className="ml-2 px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">
              internal-only
            </span>
          )}
        </div>
        <div className="whitespace-pre-line text-sm">{script.output}</div>
      </div>

      <div className="bg-white border rounded p-4 space-y-3">
        <h2 className="font-semibold">Critic Scores ({critic_scores.length} evaluators)</h2>

        <div className="grid grid-cols-7 gap-2 text-center text-xs">
          {dims.map((d) => (
            <div key={d} className="bg-zinc-50 rounded p-2">
              <div className="text-zinc-500">{DIM_LABELS[d]}</div>
              <div className="text-lg font-semibold">{avg[d]?.toFixed(1) || "—"}</div>
            </div>
          ))}
        </div>

        <table className="w-full text-sm border-t">
          <thead>
            <tr className="text-xs text-zinc-500">
              <th className="text-left py-1">Evaluator</th>
              {dims.map((d) => (
                <th key={d} className="px-2">{DIM_LABELS[d]}</th>
              ))}
              <th className="px-2">Conf</th>
            </tr>
          </thead>
          <tbody>
            {critic_scores.map((c) => (
              <tr key={c.id} className="border-t">
                <td className="py-1 font-mono text-xs">{c.evaluator_model}</td>
                {dims.map((d) => (
                  <td key={d} className="text-center">
                    {c.scores?.[d] ?? "—"}
                  </td>
                ))}
                <td className="text-center">{c.confidence?.toFixed(2) ?? "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
