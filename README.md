# AI — Agentic Insight Platform

v6 内容洞察系统：9 Agent 协同流水线，把 1 个抖音 URL 全自动跑成"拆解 → 4 路交叉 → microtype 归类 → 反向生成 → 多 LLM 自盲评 → DSPy prompt 自优化"。

## 文档

- [`v6-agentic-insight-plan.md`](./v6-agentic-insight-plan.md) — 完整方案（架构 / 排期 / 决策门）
- [`docs/v6-architecture.md`](./docs/v6-architecture.md) — 架构索引
- [`docs/poc-research-memorandum-template.md`](./docs/poc-research-memorandum-template.md) — PoC 法务备忘录模板（W4 PoC 通道开启前必签）
- [`research-synthesis.md`](./research-synthesis.md) — 历史研究合成
- [`action-plan-3-layers.md`](./action-plan-3-layers.md) — 历史 3 层行动方案
- [`review-synthesis-v2.md`](./review-synthesis-v2.md) — 三方评审报告

## 快速启动

```bash
cp infra/.env.example infra/.env

make up                    # 启动 PG+pgvector / Temporal / MinIO / Redis
make migrate               # 建 10 表 + pgvector + PoC 隔离 trigger
make api                   # 启动 FastAPI （:8000）
make worker                # 启动 Temporal worker（另一个终端）
```

服务地址：
- API: http://localhost:8000/health
- Temporal UI: http://localhost:8233
- MinIO Console: http://localhost:9001

## 仓库结构

```
api/        FastAPI 薄层（routes + models）
worker/     Temporal worker（workflows + 9 agents）
dspy/       Prompt 自优化模块
web/        Next.js UI (W3)
db/         Alembic 迁移（10 表 + PoC trigger）
infra/      Docker Compose
rules/      banned_terms_14categories.yaml + microtype_schema.yaml
docs/       架构索引 + PoC 法务备忘录模板
```

## 排期

- W0 系统初始化（Day 1-3）— **当前阶段（已完成 repo 骨架）**
- W1 A2/A3 + Temporal 骨架（Day 4-10）
- W2 A4/A5/A6/A7（Day 11-17）
- W3 A8/A9 + DSPy 闭环 + UI（Day 18-24）
- W4 buffer + A1 Discovery + 决策门（Day 25-28）
