import Link from "next/link";
import { api, type Atom, type CaseDetail, type CrossValidation, type Segment } from "@/lib/api";

export default async function CaseDetailPage({ params }: { params: { id: string } }) {
  let detail: CaseDetail | null = null;
  let error: string | null = null;
  try {
    detail = await api.getCase(params.id);
  } catch (e) {
    error = (e as Error).message;
  }

  if (error || !detail) {
    return (
      <div className="space-y-3">
        <Link href="/cases" className="text-sm text-blue-600">← Cases</Link>
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          {error || "Case not found"}
        </div>
      </div>
    );
  }

  const { case: c, segments, atoms, cross_validations } = detail;

  return (
    <div className="space-y-6">
      <div>
        <Link href="/cases" className="text-sm text-blue-600">← Cases</Link>
      </div>

      <div className="bg-white border rounded p-4 space-y-1">
        <div className="text-lg font-semibold">{c.brand || "—"} / {c.sku || "—"}</div>
        <div className="text-sm text-zinc-600">
          {c.category || "no category"} · {c.platform || "—"} · {c.duration_sec || "?"}s
        </div>
        <div className="text-xs text-zinc-500 break-all">{c.url}</div>
        <div className="text-xs">
          lineage=<code>{c.data_lineage}</code> · ingested {new Date(c.ingested_at).toLocaleString("zh-CN")}
        </div>
      </div>

      <CrossValidationsCard items={cross_validations} />

      <SegmentsTimeline items={segments} />

      <AtomsGrid items={atoms} />
    </div>
  );
}

function CrossValidationsCard({ items }: { items: CrossValidation[] }) {
  return (
    <div className="bg-white border rounded p-4 space-y-3">
      <h2 className="font-semibold">4 路交叉验证</h2>
      {items.length === 0 && <div className="text-sm text-zinc-500">no validations yet</div>}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {items.map((v) => (
          <div key={v.id} className="border rounded p-2 text-sm">
            <div className="font-mono text-xs text-zinc-500">{v.agent}</div>
            <div className="font-medium">{v.verdict || "—"}</div>
            <div className="text-xs text-zinc-500">
              conf={v.confidence?.toFixed(2) ?? "—"}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SegmentsTimeline({ items }: { items: Segment[] }) {
  return (
    <div className="bg-white border rounded p-4 space-y-3">
      <h2 className="font-semibold">9 段式拆解</h2>
      {items.length === 0 && <div className="text-sm text-zinc-500">no segments</div>}
      <ol className="space-y-2">
        {items.map((s, i) => (
          <li key={s.id} className="border-l-2 border-zinc-300 pl-3 py-1">
            <div className="text-sm font-mono">
              [{i + 1}] {s.segment_type}{" "}
              <span className="text-xs text-zinc-500">
                ({s.start_sec ?? "?"}s – {s.end_sec ?? "?"}s)
              </span>
            </div>
            <div className="text-sm text-zinc-700 mt-1">{s.asr_text || "—"}</div>
          </li>
        ))}
      </ol>
    </div>
  );
}

function AtomsGrid({ items }: { items: Atom[] }) {
  const groups: Record<string, Atom[]> = { hook: [], pain: [], trust: [], cta: [] };
  for (const a of items) (groups[a.atom_type] ?? (groups[a.atom_type] = [])).push(a);

  return (
    <div className="bg-white border rounded p-4 space-y-3">
      <h2 className="font-semibold">原子库（{items.length}）</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3">
        {(["hook", "pain", "trust", "cta"] as const).map((t) => (
          <div key={t}>
            <div className="text-xs font-mono uppercase text-zinc-500 mb-1">
              {t} ({groups[t]?.length || 0})
            </div>
            <div className="space-y-2">
              {(groups[t] || []).map((a) => (
                <div key={a.id} className="border rounded p-2 text-sm">
                  <ComplianceBadge grade={a.compliance_grade} />
                  <div className="mt-1">{a.content}</div>
                  {a.created_by_agent && a.created_by_agent !== "a2" && (
                    <div className="text-xs text-zinc-400 mt-1">
                      by {a.created_by_agent}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function ComplianceBadge({ grade }: { grade: string | null }) {
  if (!grade) return <span className="text-xs text-zinc-400">grade=?</span>;
  const cls =
    grade === "R"
      ? "bg-red-100 text-red-700"
      : grade === "Y"
        ? "bg-amber-100 text-amber-800"
        : "bg-emerald-100 text-emerald-700";
  return (
    <span className={`px-1.5 py-0.5 rounded text-xs font-mono ${cls}`}>{grade}</span>
  );
}
