"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";

export function ActivateButton({ microtypeId }: { microtypeId: string }) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  async function onClick() {
    if (!window.confirm("Activate this candidate microtype?")) return;
    setLoading(true);
    try {
      await api.activateMicrotype(microtypeId);
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
      className="text-xs bg-emerald-600 text-white px-2 py-1 rounded hover:bg-emerald-700 disabled:opacity-50"
    >
      {loading ? "…" : "Activate"}
    </button>
  );
}
