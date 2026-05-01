import Link from "next/link";
import { api, type CaseListItem } from "@/lib/api";

export default async function CasesPage() {
  let cases: CaseListItem[] = [];
  let error: string | null = null;
  try {
    cases = await api.listCases();
  } catch (e) {
    error = (e as Error).message;
  }

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold">Cases</h1>
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          API error: {error}
        </div>
      )}
      <table className="w-full bg-white border text-sm">
        <thead className="bg-zinc-100">
          <tr>
            <th className="text-left px-3 py-2">Brand / SKU</th>
            <th className="text-left px-3 py-2">Category</th>
            <th className="text-left px-3 py-2">Lineage</th>
            <th className="text-left px-3 py-2">Ingested</th>
            <th className="text-left px-3 py-2">URL</th>
          </tr>
        </thead>
        <tbody>
          {cases.length === 0 && !error && (
            <tr>
              <td className="text-zinc-500 px-3 py-4" colSpan={5}>
                no cases yet — POST /ingest from API or scripts/demo_ingest.py
              </td>
            </tr>
          )}
          {cases.map((c) => (
            <tr key={c.id} className="border-t hover:bg-zinc-50">
              <td className="px-3 py-2">
                <Link href={`/cases/${c.id}`} className="text-blue-600 hover:underline">
                  {c.brand || "—"} / {c.sku || "—"}
                </Link>
              </td>
              <td className="px-3 py-2">{c.category || "—"}</td>
              <td className="px-3 py-2">
                <LineageBadge lineage={c.data_lineage} />
              </td>
              <td className="px-3 py-2 text-zinc-500">
                {new Date(c.ingested_at).toLocaleString("zh-CN")}
              </td>
              <td className="px-3 py-2 text-zinc-500 truncate max-w-xs">{c.url}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function LineageBadge({ lineage }: { lineage: string }) {
  const cls =
    lineage === "poc_crawled"
      ? "bg-amber-100 text-amber-800"
      : lineage === "oauth"
        ? "bg-emerald-100 text-emerald-800"
        : lineage === "public_api"
          ? "bg-sky-100 text-sky-800"
          : "bg-zinc-100 text-zinc-700";
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-mono ${cls}`}>
      {lineage}
    </span>
  );
}
