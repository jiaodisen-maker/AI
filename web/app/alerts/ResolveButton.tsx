"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";

export function ResolveButton({ alertId }: { alertId: string }) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  async function onClick() {
    const by = window.prompt("Resolved by (your name)?");
    if (!by) return;
    setLoading(true);
    try {
      await api.resolveAlert(alertId, by);
      router.refresh();
    } catch (e) {
      window.alert("Failed: " + (e as Error).message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <button
      type="button"
      onClick={onClick}
      disabled={loading}
      className="text-sm bg-emerald-600 text-white px-3 py-1 rounded hover:bg-emerald-700 disabled:opacity-50"
    >
      {loading ? "…" : "Resolve"}
    </button>
  );
}
