import { api, type Microtype } from "@/lib/api";
import { ActivateButton } from "./ActivateButton";

export default async function MicrotypesPage({
  searchParams,
}: {
  searchParams: { status?: string };
}) {
  let microtypes: Microtype[] = [];
  let error: string | null = null;
  try {
    microtypes = await api.listMicrotypes(searchParams.status);
  } catch (e) {
    error = (e as Error).message;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold">Microtypes</h1>
        <div className="text-sm space-x-3">
          <a href="/microtypes" className={!searchParams.status ? "font-semibold" : "text-blue-600"}>
            All
          </a>
          <a
            href="/microtypes?status=active"
            className={searchParams.status === "active" ? "font-semibold" : "text-blue-600"}
          >
            Active
          </a>
          <a
            href="/microtypes?status=candidate"
            className={searchParams.status === "candidate" ? "font-semibold" : "text-blue-600"}
          >
            Candidate
          </a>
        </div>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          {error}
        </div>
      )}

      <table className="w-full bg-white border text-sm">
        <thead className="bg-zinc-100">
          <tr>
            <th className="text-left px-3 py-2">Scene</th>
            <th className="text-left px-3 py-2">Audience</th>
            <th className="text-left px-3 py-2">Ingredient</th>
            <th className="text-left px-3 py-2">Emotion</th>
            <th className="text-left px-3 py-2">Restriction</th>
            <th className="text-left px-3 py-2">Status</th>
            <th className="text-left px-3 py-2">Action</th>
          </tr>
        </thead>
        <tbody>
          {microtypes.length === 0 && (
            <tr>
              <td colSpan={7} className="text-zinc-500 px-3 py-4">
                no microtypes — run `make seed`
              </td>
            </tr>
          )}
          {microtypes.map((m) => (
            <tr key={m.id} className="border-t hover:bg-zinc-50">
              <td className="px-3 py-2 font-mono text-xs">{m.scene}</td>
              <td className="px-3 py-2 font-mono text-xs">{m.audience}</td>
              <td className="px-3 py-2 font-mono text-xs">{m.ingredient}</td>
              <td className="px-3 py-2 font-mono text-xs">{m.emotion}</td>
              <td className="px-3 py-2 font-mono text-xs">{m.restriction}</td>
              <td className="px-3 py-2">
                <StatusBadge status={m.status} proposed={m.proposed_by_agent} />
              </td>
              <td className="px-3 py-2">
                {m.status === "candidate" && <ActivateButton microtypeId={m.id} />}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function StatusBadge({ status, proposed }: { status: string; proposed: boolean }) {
  const cls =
    status === "active"
      ? "bg-emerald-100 text-emerald-700"
      : status === "candidate"
        ? "bg-amber-100 text-amber-800"
        : "bg-zinc-100 text-zinc-600";
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-mono ${cls}`}>
      {status}
      {proposed && status === "candidate" && " (A6)"}
    </span>
  );
}
