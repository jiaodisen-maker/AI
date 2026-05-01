"use client";

import { useState } from "react";

const BASE = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";

type Result = {
  discovered: number;
  started_workflows: { workflow_id: string; url: string }[];
};

export function DiscoveryForm() {
  const [channel, setChannel] = useState<"poc" | "prod">("prod");
  const [query, setQuery] = useState("氨糖");
  const [n, setN] = useState(5);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const r = await fetch(`${BASE}/discovery/run`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ channel, query, n }),
      });
      if (!r.ok) {
        setError(`${r.status} ${await r.text()}`);
        return;
      }
      setResult(await r.json());
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="bg-white border rounded p-4 space-y-3 text-sm">
      <div className="flex gap-3 items-center">
        <label className="font-medium w-24">Channel</label>
        <select
          value={channel}
          onChange={(e) => setChannel(e.target.value as "poc" | "prod")}
          className="border rounded px-2 py-1"
        >
          <option value="prod">prod (OAuth + 巨量创意中心)</option>
          <option value="poc">poc (MediaCrawler — 内部研究 only)</option>
        </select>
      </div>
      <div className="flex gap-3 items-center">
        <label className="font-medium w-24">Query</label>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="border rounded px-2 py-1 flex-1"
        />
      </div>
      <div className="flex gap-3 items-center">
        <label className="font-medium w-24">N</label>
        <input
          type="number"
          min={1}
          max={50}
          value={n}
          onChange={(e) => setN(Number(e.target.value))}
          className="border rounded px-2 py-1 w-24"
        />
      </div>
      <button
        type="submit"
        disabled={loading}
        className="bg-zinc-800 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {loading ? "Running…" : "Run"}
      </button>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-2 rounded text-xs">
          {error}
        </div>
      )}

      {result && (
        <div className="bg-emerald-50 border border-emerald-200 p-3 rounded space-y-2">
          <div>Discovered {result.discovered} cases. Started {result.started_workflows.length} workflows.</div>
          <ul className="text-xs space-y-1">
            {result.started_workflows.map((w) => (
              <li key={w.workflow_id} className="font-mono">
                {w.workflow_id}  ←  {w.url}
              </li>
            ))}
          </ul>
        </div>
      )}
    </form>
  );
}
