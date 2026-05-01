import Link from "next/link";
import { api, type ScriptListItem } from "@/lib/api";

export default async function ScriptsPage() {
  let scripts: ScriptListItem[] = [];
  let error: string | null = null;
  try {
    scripts = await api.listScripts();
  } catch (e) {
    error = (e as Error).message;
  }

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold">Generated Scripts</h1>
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          {error}
        </div>
      )}
      <div className="text-sm text-zinc-500">{scripts.length} scripts</div>
      <div className="space-y-3">
        {scripts.map((s) => (
          <Link
            key={s.id}
            href={`/scripts/${s.id}`}
            className="block bg-white border rounded p-3 hover:border-zinc-400"
          >
            <div className="flex items-center gap-2 text-xs text-zinc-500 mb-2">
              <span>prompt={s.prompt_version}</span>
              <span>·</span>
              <span>{s.llm_model}</span>
              <span>·</span>
              <span>{new Date(s.generated_at).toLocaleString("zh-CN")}</span>
              {s.for_internal_research_only && (
                <span className="px-1.5 py-0.5 rounded bg-amber-100 text-amber-800 text-xs">
                  internal-only (PoC)
                </span>
              )}
            </div>
            <div className="text-sm whitespace-pre-line line-clamp-4">{s.output}</div>
          </Link>
        ))}
      </div>
    </div>
  );
}
