import { api, type Alert } from "@/lib/api";
import { ResolveButton } from "./ResolveButton";

export default async function AlertsPage({
  searchParams,
}: {
  searchParams: { status?: string };
}) {
  const status: "open" | "resolved" =
    searchParams.status === "resolved" ? "resolved" : "open";

  let alerts: Alert[] = [];
  let error: string | null = null;
  try {
    alerts = await api.listAlerts(status);
  } catch (e) {
    error = (e as Error).message;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold">HITL Alerts</h1>
        <div className="text-sm space-x-3">
          <a
            href="/alerts?status=open"
            className={status === "open" ? "font-semibold" : "text-blue-600"}
          >
            Open
          </a>
          <a
            href="/alerts?status=resolved"
            className={status === "resolved" ? "font-semibold" : "text-blue-600"}
          >
            Resolved
          </a>
        </div>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded text-sm">
          API error: {error}
        </div>
      )}

      <div className="space-y-3">
        {alerts.length === 0 && !error && (
          <div className="text-zinc-500 text-sm">no {status} alerts</div>
        )}
        {alerts.map((a) => (
          <div key={a.id} className="bg-white border rounded p-4">
            <div className="flex items-start justify-between">
              <div className="space-y-1">
                <AlertTypeBadge type={a.alert_type} />
                <div className="text-xs text-zinc-500">
                  {new Date(a.created_at).toLocaleString("zh-CN")}
                </div>
              </div>
              {status === "open" && <ResolveButton alertId={a.id} />}
              {status === "resolved" && (
                <div className="text-xs text-zinc-500">
                  resolved by {a.resolved_by} at{" "}
                  {a.resolved_at && new Date(a.resolved_at).toLocaleString("zh-CN")}
                </div>
              )}
            </div>
            <pre className="mt-3 bg-zinc-50 border rounded p-2 text-xs overflow-x-auto">
              {JSON.stringify(a.payload, null, 2)}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
}

function AlertTypeBadge({ type }: { type: string }) {
  const cls =
    type === "compliance_edge"
      ? "bg-red-100 text-red-800"
      : type === "low_confidence"
        ? "bg-amber-100 text-amber-800"
        : type === "new_microtype"
          ? "bg-sky-100 text-sky-800"
          : type === "poc_purge_failed"
            ? "bg-purple-100 text-purple-800"
            : "bg-zinc-100 text-zinc-700";
  return (
    <span className={`px-2 py-1 rounded text-xs font-mono ${cls}`}>{type}</span>
  );
}
