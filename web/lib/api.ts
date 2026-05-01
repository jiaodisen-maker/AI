const BASE = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`, { cache: "no-store" });
  if (!res.ok) throw new Error(`${res.status} ${path}`);
  return res.json();
}

async function post<T>(path: string, body?: unknown): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) throw new Error(`${res.status} ${path}`);
  return res.json();
}

export type CaseListItem = {
  id: string;
  url: string;
  platform: string | null;
  brand: string | null;
  sku: string | null;
  category: string | null;
  data_lineage: string;
  ingested_at: string;
};

export type Segment = {
  id: string;
  segment_type: string;
  start_sec: number | null;
  end_sec: number | null;
  asr_text: string | null;
  ocr_text: string | null;
  visual_desc: string | null;
  llm_analysis: Record<string, unknown> | null;
};

export type Atom = {
  id: string;
  atom_type: string;
  content: string;
  compliance_grade: string | null;
  feasibility_4d: Record<string, unknown> | null;
  source_segment_id: string | null;
  created_by_agent: string | null;
};

export type CrossValidation = {
  id: string;
  agent: string;
  verdict: string | null;
  confidence: number | null;
  raw_data: Record<string, unknown> | null;
  validated_at: string;
};

export type CaseDetail = {
  case: CaseListItem & { duration_sec: number | null; raw_meta: unknown };
  segments: Segment[];
  atoms: Atom[];
  cross_validations: CrossValidation[];
};

export type Alert = {
  id: string;
  alert_type: string;
  payload: Record<string, unknown>;
  status: "open" | "resolved";
  resolved_by: string | null;
  resolved_at: string | null;
  created_at: string;
};

export type Microtype = {
  id: string;
  scene: string;
  audience: string;
  ingredient: string;
  emotion: string;
  restriction: string;
  status: "active" | "candidate" | "deprecated";
  proposed_by_agent: boolean;
};

export type ScriptListItem = {
  id: string;
  microtype_id: string;
  prompt_version: string;
  output: string;
  llm_model: string;
  for_internal_research_only: boolean;
  generated_at: string;
};

export type ScriptDetail = {
  script: ScriptListItem & { atom_ids: string[] };
  critic_scores: {
    id: string;
    evaluator_model: string;
    scores: Record<string, number>;
    reasoning: string | null;
    confidence: number | null;
    scored_at: string;
  }[];
};

export type PromptVersion = {
  id: string;
  agent: string;
  version: string;
  metric: Record<string, unknown> | null;
  created_at: string;
  trigger_critic_id: string | null;
};

export const api = {
  listCases: () => get<CaseListItem[]>("/cases?limit=50"),
  getCase: (id: string) => get<CaseDetail>(`/cases/${id}`),
  listAlerts: (status: "open" | "resolved" = "open") =>
    get<Alert[]>(`/alerts?status=${status}`),
  resolveAlert: (id: string, by: string) =>
    post<{ id: string; status: string }>(
      `/alerts/${id}/resolve?resolved_by=${encodeURIComponent(by)}`,
    ),
  searchAtoms: (params: {
    q?: string;
    atom_type?: string;
    grade?: string;
    microtype_id?: string;
  } = {}) => {
    const qs = new URLSearchParams(
      Object.entries(params).filter(([, v]) => v) as [string, string][],
    );
    return get<Atom[]>(`/atoms?${qs}`);
  },
  listMicrotypes: (status?: string) =>
    get<Microtype[]>(`/microtypes${status ? `?status=${status}` : ""}`),
  activateMicrotype: (id: string) =>
    post<{ id: string; status: string }>(`/microtypes/${id}/activate`),
  listScripts: () => get<ScriptListItem[]>("/scripts?limit=50"),
  getScript: (id: string) => get<ScriptDetail>(`/scripts/${id}`),
  listPromptVersions: () => get<PromptVersion[]>("/prompt-versions"),
  getPromptVersion: (id: string) =>
    get<PromptVersion & { prompt_text: string }>(`/prompt-versions/${id}`),
};
