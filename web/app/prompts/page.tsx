import { api, type PromptVersion } from "@/lib/api";

export default async function PromptVersionsPage() {
  let versions: PromptVersion[] = [];
  let error: string | null = null;
  try {
    versions = await api.listPromptVersions();
  } catch (e) {
    error = (e as Error).message;
  }

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold">DSPy Prompt Versions</h1>
      <p className="text-sm text-zinc-500">
        A9 Critic 每累计 5 个 critic_scores 触发一次 dspy_opt.maybe_optimize；
        新 prompt 在 holdout 上若不优于旧 prompt 则不写入（回滚机制）。
      </p>
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          {error}
        </div>
      )}
      <table className="w-full bg-white border text-sm">
        <thead className="bg-zinc-100">
          <tr>
            <th className="text-left px-3 py-2">Agent</th>
            <th className="text-left px-3 py-2">Version</th>
            <th className="text-left px-3 py-2">Created</th>
            <th className="text-left px-3 py-2">Metric</th>
          </tr>
        </thead>
        <tbody>
          {versions.length === 0 && (
            <tr>
              <td colSpan={4} className="text-zinc-500 px-3 py-4">
                no prompt versions yet — DSPy will trigger after 5 critic_scores
              </td>
            </tr>
          )}
          {versions.map((v) => (
            <tr key={v.id} className="border-t hover:bg-zinc-50">
              <td className="px-3 py-2 font-mono text-xs">{v.agent}</td>
              <td className="px-3 py-2 font-mono text-xs">{v.version}</td>
              <td className="px-3 py-2 text-zinc-500">
                {new Date(v.created_at).toLocaleString("zh-CN")}
              </td>
              <td className="px-3 py-2">
                {v.metric ? (
                  <pre className="text-xs">{JSON.stringify(v.metric, null, 0).slice(0, 200)}</pre>
                ) : (
                  <span className="text-zinc-400">—</span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
