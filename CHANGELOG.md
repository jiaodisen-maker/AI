# Changelog

## W5 — Production Hardening

- **客服库 PIPL 脱敏 + 导入** (`scripts/import_userpain.py`)：手机/邮箱/身份证/订单号/IP/银行卡/中文姓名 7 类 PII 替换为 token，启发式聚类后嵌入入库
- **Temporal Schedule 编排**：`scripts/setup_purge_schedule.py` + `worker/workflows/poc_purge.py`，每 24h 自动跑 PoC TTL purge
- **HITL Webhook 通知** (`worker/hitl_notify.py`)：钉钉 / 企业微信 markdown 卡片；fail-soft；数据不在 IM 持久化
- **Prometheus /metrics**：6 类 gauges（open_alerts / cases by lineage / poc_pending_purge / atoms by type+grade / microtypes by status / dspy_prompt_versions）
- **GitHub Actions CI**（.github/workflows/ci.yml）：lint + test + production-build feature flag 守卫（main/release 分支强制 POC_CRAWLED_ENABLED=false）+ web build
- **违禁词扩充至 v0.2**：14 类各 +5-10 patterns；修复 v0.1 "第一" 误命中"第一件事"误报（加 negative lookahead）
- **PII 脱敏单测 9 条** + A3 v0.2 扩展 patterns 单测 3 条
- **`.env.example` 默认 POC_CRAWLED_ENABLED=false**（生产姿态正确，dev 自己 override）

**33/33 单测全过，ruff 全绿。**

## W4 — A1 双通道 + TTL purge + 决策门 (e441aa5)

- A1 Discovery 双通道：MediaCrawler/DrissionPage（PoC）+ 抖音 OpenAPI/巨量创意中心（生产）
- 批量驱动器：CLI + `POST /discovery/run`
- TTL Purge：30 天清理 + MinIO 对象 + audit log
- `docs/v6-mvp-summary.md` 决策门 summary

## W3 — A8/A9 + DSPy 闭环 + UI (c3e08b2)

- A8 Generation：N=5 候选脚本反向生成；data_lineage→for_internal_research_only
- A9 Critic：Deepseek+Qwen+Claude 三家互评 7 维 rubric；confidence = 1 − normalized_variance
- DSPy 自闭环（dspy_opt/）：BootstrapFewShot 编译 + holdout 校验 + 回滚机制
- Next.js 14 + Tailwind UI：/cases /cases/[id] /alerts

## W2 — 4 路交叉 (ac121dd)

- A4 UserPain：DashScope embedding + pgvector top-5 + Deepseek 真伪判定
- A5 Conversion：千川/巨量算数 OAuth shape；data_lineage 安全降级
- A6 Microtype：5 维 schema 抽取 + candidate 提案
- A7 Feasibility：3 家互评 4 维 + 不及格原子改写

## W1 — A2/A3 + Temporal (ba462bb)

- A2 Decomposition：Deepseek 9 段 + 4 类原子 + manual_payload 旁路
- A3 Compliance：14 类正则 + LLM 双验
- LLM 客户端：Deepseek-V3 + Qwen-Max + Qwen-VL + Claude Haiku 4.5
- Temporal client + POST /ingest 接通

## W0 — Monorepo 骨架 (376f532)

- 10 表 Alembic 迁移 + pgvector + `enforce_poc_isolation` trigger
- 14 类违禁词 yaml + microtype 5 维 + 50 seed
- 法务 PoC 备忘录模板
- 9 Agent stubs + Temporal workflow 骨架

## W—1 — v6 Plan (37902a1)

- v6 Agentic 内容洞察系统设计文档：9 Agent 流水线 + DSPy 自闭环 + PoC/生产双通道隔离
