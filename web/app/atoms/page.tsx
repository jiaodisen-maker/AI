import { api, type Atom } from "@/lib/api";

export default async function AtomsPage({
  searchParams,
}: {
  searchParams: { q?: string; type?: string; grade?: string };
}) {
  let atoms: Atom[] = [];
  let error: string | null = null;
  try {
    atoms = await api.searchAtoms({
      q: searchParams.q,
      atom_type: searchParams.type,
      grade: searchParams.grade,
    });
  } catch (e) {
    error = (e as Error).message;
  }

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold">Atoms</h1>

      <form className="bg-white border rounded p-3 flex gap-2 text-sm" method="get">
        <input
          name="q"
          defaultValue={searchParams.q || ""}
          placeholder="文本子串"
          className="border rounded px-2 py-1 flex-1"
        />
        <select name="type" defaultValue={searchParams.type || ""} className="border rounded px-2 py-1">
          <option value="">all types</option>
          <option value="hook">hook</option>
          <option value="pain">pain</option>
          <option value="trust">trust</option>
          <option value="cta">cta</option>
        </select>
        <select name="grade" defaultValue={searchParams.grade || ""} className="border rounded px-2 py-1">
          <option value="">all grades</option>
          <option value="G">G (绿)</option>
          <option value="Y">Y (黄)</option>
          <option value="R">R (红)</option>
        </select>
        <button className="bg-zinc-800 text-white rounded px-3 py-1">Search</button>
      </form>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          {error}
        </div>
      )}

      <div className="text-sm text-zinc-500">{atoms.length} results</div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {atoms.map((a) => (
          <div key={a.id} className="bg-white border rounded p-3 text-sm">
            <div className="flex items-center gap-2 mb-1">
              <span className="font-mono text-xs uppercase text-zinc-500">{a.atom_type}</span>
              <GradeBadge grade={a.compliance_grade} />
              {a.created_by_agent && a.created_by_agent !== "a2" && (
                <span className="text-xs text-amber-700">by {a.created_by_agent}</span>
              )}
            </div>
            <div>{a.content}</div>
            {a.feasibility_4d && Object.keys(a.feasibility_4d).length > 0 && (
              <pre className="mt-2 bg-zinc-50 border rounded p-2 text-xs">
                {JSON.stringify(a.feasibility_4d, null, 2).slice(0, 400)}
              </pre>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

function GradeBadge({ grade }: { grade: string | null }) {
  if (!grade) return <span className="text-xs text-zinc-400">?</span>;
  const cls =
    grade === "R"
      ? "bg-red-100 text-red-700"
      : grade === "Y"
        ? "bg-amber-100 text-amber-800"
        : "bg-emerald-100 text-emerald-700";
  return <span className={`px-1.5 py-0.5 rounded text-xs font-mono ${cls}`}>{grade}</span>;
}
