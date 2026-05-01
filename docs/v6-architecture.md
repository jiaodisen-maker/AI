# v6 Agentic 内容洞察系统 — 架构索引

完整架构 / 数据模型 / 排期 / 决策门见 [`v6-agentic-insight-plan.md`](../v6-agentic-insight-plan.md) 第十四章。

## 一句话定义

9 个 Agent 协同流水线，把 1 个抖音 URL 全自动跑成"拆解 → 4 路交叉 → microtype 归类 → 反向生成 → 多 LLM 自盲评 → DSPy prompt 自优化"，整个流程 0 人介入。

## 关键架构特性

- 全 Agent 跑在 Temporal Activity 里，可重试 / 可观察 / 可回放
- A2 / A8 prompt 用 DSPy 维护，A9 Critic 反馈触发自动 prompt 重训
- A1 Discovery 双通道：PoC（MediaCrawler 内部研究）/ 生产（OAuth + 公开 API），schema 级隔离
- A9 Critic ≥3 个不同家族 LLM 互评 + confidence 计算

## 仓库结构

```
AI/                            (jiaodisen-maker/AI repo root)
├─ api/                       FastAPI（薄层）
│  ├─ main.py
│  ├─ routes/                 ingest cases atoms microtypes generate alerts
│  └─ models/                 SQLAlchemy ORM
├─ worker/                    Temporal worker
│  ├─ workflows/agentic_insight.py
│  ├─ agents/                 a1..a9
│  └─ run_worker.py
├─ dspy/                      Prompt 自优化模块
├─ web/                       Next.js 14 (W3 实装)
├─ db/migrations/             Alembic 10 表
├─ infra/docker-compose.yml   PG+pgvector + Temporal + MinIO + Redis
├─ rules/
│  ├─ banned_terms_14categories.yaml   (W0 法务)
│  └─ microtype_schema.yaml             (W0 架构师)
└─ docs/
   ├─ v6-architecture.md                (本文件)
   ├─ poc-research-memorandum-template.md
   └─ v6-agentic-insight-plan.md → 顶层
```

## W0 启动流程

```bash
cp infra/.env.example infra/.env
docker compose -f infra/docker-compose.yml up -d
cd db && alembic upgrade head
```

启动后访问：
- Postgres: localhost:5432
- Temporal UI: http://localhost:8233
- MinIO Console: http://localhost:9001
