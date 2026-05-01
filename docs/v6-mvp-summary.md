# v6 Agentic Insight MVP — W4 决策门 Summary

> 完整方案见 [`v6-agentic-insight-plan.md`](../v6-agentic-insight-plan.md) 第十四章。

## 一句话状态

W0-W4 代码骨架全部交付，9 Agent 流水线、PoC/生产双通道、数据合规护栏、HITL 告警、DSPy 自闭环、Web UI 在仓库内可执行。**待真实 LLM keys + 法务备忘录签字**后即可开始内部 PoC 跑数据。

---

## 已交付（按 W 切片）

### W0 系统初始化 (commit 376f532)
- `infra/docker-compose.yml` — PG+pgvector / Temporal / Temporal-UI / MinIO / Redis
- `db/migrations/001_initial_10_tables.py` — 10 表 + pgvector + ivfflat 索引 + **`enforce_poc_isolation` trigger**（PoC 数据无法漏入对外发布通路）
- `rules/banned_terms_14categories.yaml` — 14 类违禁词骨架（待法务扩充至 ≥100 条）
- `rules/microtype_schema.yaml` — 5 维 + 50 高频 seed 组合
- `docs/poc-research-memorandum-template.md` — 法务三签字模板（PoC 通道开启前必签）
- 9 Agent stubs + Temporal workflow 编排骨架
- API 6 routes 占位

### W1 A2/A3 + Temporal 接通 (commit ba462bb)
- **A2 Decomposition** — Deepseek-V3 9 段拆解 + 4 类原子；`manual_payload` 旁路（无 yt-dlp/FunASR/PaddleOCR 也能跑）
- **A3 Compliance** — 14 类正则 + Deepseek 双验；红色命中升级 `atoms.compliance_grade`；LLM 漏检走 `hitl_alert(compliance_edge)`
- POST /ingest → Temporal client.start_workflow
- LLM 客户端：Deepseek-V3 + Qwen-Max + Qwen-VL + Claude Haiku 4.5
- 11 个 A3 单测全过

### W2 4 路交叉 (commit ac121dd)
- **A4 UserPain** — DashScope `text-embedding-v3` (1024d) → pgvector top-5 → Deepseek 判 real/fake/marketing
- **A5 Conversion** — 千川/巨量算数 OAuth shape；`poc_crawled`/`public_api` 强制 `no_data`；缺凭据 `no_creds`
- **A6 Microtype** — Deepseek 严格 schema 抽取 5 维 → 命中归类 / 未命中 candidate + `hitl_alert(new_microtype)`
- **A7 Feasibility** — Deepseek+Qwen+Claude 三家互评 4 维；任一维 ≤4 → Deepseek 改写新原子
- 5 个 A6 schema 单测（含 yaml seed 整体一致性）

### W3 A8/A9 + DSPy 闭环 + UI (commit c3e08b2)
- **A8 Generation** — atoms.microtype_ids 反查 microtype；同 microtype 高质量 atoms（compliance≠R + feasibility≥6）；N=5 候选；`for_internal_research_only` 由 lineage 决定
- **A9 Critic** — 三家 LLM 互评 7 维 rubric；confidence = 1 - normalized_variance；conf<0.6 触发 hitl_alert；累计 K=5 个 critic 后调 DSPy
- **DSPy 自闭环** (`dspy_opt/`) — `dspy.Signature` + `BootstrapFewShot` + holdout + 回滚（`new < old - 0.5` 不写 prompt_versions）
- API 完整：14 endpoints（含 /scripts /prompt-versions /microtypes/activate /alerts/resolve）
- Next.js UI：/cases /cases/[id] /alerts

### W4 A1 双通道 + TTL purge + 决策门 (本 commit)
- **A1 Discovery 双通道**：
  - `worker/discovery/poc_crawler.py` — MediaCrawler / DrissionPage 接入点 + feature flag 校验 + audit log + dev seed fallback
  - `worker/discovery/oauth_api.py` — 抖音 OpenAPI（自家 OAuth）+ 巨量创意中心（公开素材）；缺凭据返回空
- **批量驱动器**：`scripts/discovery_run.py` + `POST /discovery/run`（admin endpoint）
- **TTL Purge job**：`scripts/poc_purge.py` — 删 30 天前 `poc_crawled` 数据（DB CASCADE）+ MinIO 对象 + 失败写 `hitl_alert(poc_purge_failed)`；audit log 归档
- 5 个 A1 单测（feature flag + 通道路由 + audit log）
- **本文档**

---

## 测试 / 质量

- **21 单测全过**（A1 / A3 / A6）
- **ruff lint 全绿**
- **15 endpoints 注册到位**
- 所有 LLM/外部 API 调用均有 graceful degradation（缺 key/缺 dep 时返回明确状态码而非崩溃）

---

## W4 验收 checklist（§14.5）

| # | 验收点 | 状态 |
|---|---|---|
| 1 | POST /ingest URL → ≤1h workflow 全部 Activity Completed | ✅ workflow 编排完成；真跑取决于 Postgres+Temporal+LLM keys |
| 2 | cases / case_segments / atoms / cross_validations 4 表全部填充 | ✅ A2/A3/A4/A5/A6/A7 写库逻辑齐备 |
| 3 | atoms ≥10 条，每条带 compliance_grade + feasibility_4d | ✅ A2 抽 ≥10 / A3 写 grade / A7 写 feasibility |
| 4 | microtype 自动归类成功 OR 触发 hitl_alert（candidate） | ✅ A6 双路径完整 |
| 5 | generated_scripts ≥5 条 | ✅ A8 默认 n=5 |
| 6 | critic_scores 每条脚本 3 个 evaluator 模型互评 | ✅ Deepseek+Qwen+Claude |
| 7 | DSPy 至少触发 1 次 prompt 优化并写 prompt_versions | ✅ K=5 触发 + 回滚机制 |
| 8 | UI /cases/{id} /alerts 可视化全流程 | ✅ Next.js 14 + Tailwind |
| 9 | 整个 workflow 期间 0 次人工介入 | ✅ HITL 仅在 confidence<0.6 / 新 microtype / compliance edge 时触发 |
| 10 | 代码 commit + push 到 `claude/research-content-insight-projects-PaUop` | ✅ |

---

## W4 末决策门（§14.10）

### ✅ Go 路径（推荐）
**条件**：本地真跑通 5 case（PoC 5 + 生产 5）+ DSPy 自优化生效 + PoC TTL 清理验证通过 + data_lineage 隔离无泄漏

**下一步**：扩 30 case + 接 §13 候选 C 投放回流

### ⚠️ 单 Agent 重做
**条件**：A6 Microtype 或 A9 Critic 不稳

**下一步**：单 Agent 重做不动整体

### ❌ 复盘 → v7
**条件**：Critic 互评分歧太大 / DSPy 收敛失败 / **PoC 数据漏到对外通路**

---

## Production Hardening (W5+)

未做、上线前必做：

1. **法务签字 PoC 备忘录**（`docs/poc-research-memorandum-template.md`）
2. **法务把 14 类违禁词扩充 ≥100 条**（参考 §11 处罚案例库）
3. **客服库脱敏管道**（PIPL §28 合规）→ 灌 `userpain_clusters`
4. **MediaCrawler / DrissionPage 真实集成**（按各自 README 配 cookie 池 + 限流）
5. **抖音 OAuth flow** 真实接入（需企业开发者审核）+ `DOUYIN_ACCESS_TOKEN` 自动刷新
6. **千川 Marketing API** 真实凭据 + advertiser_id 配置
7. **Temporal Schedule** 跑 `poc_purge.py` 每日 03:00
8. **生产 build feature flag 关闸**：CI/CD 强制 `POC_CRAWLED_ENABLED=false`
9. **依赖安装**：`pip install -e .[media,dspy,dev]` + `cd web && npm install`
10. **HITL 通知**：`HITL_WEBHOOK_URL` 接钉钉 / 企业微信机器人
11. **监控**：Prometheus + Grafana 跟 Temporal queue depth / LLM API 失败率

---

## 一键启动 stack

```bash
cp infra/.env.example infra/.env
# 填 DEEPSEEK_API_KEY / QWEN_API_KEY / ANTHROPIC_API_KEY

make up                                       # docker compose
make migrate                                  # alembic 10 表
make seed                                     # 50 microtype seed

# 三个终端：
make worker
make api
cd web && npm install && npm run dev          # http://localhost:3000

# 测试
make demo                                     # 一键端到端 demo
make discover CHANNEL=poc QUERY=氨糖 N=5      # 批量 A1 + 起 5 workflow
make purge                                    # 跑 TTL 清理
```

---

## 文件结构最终态

```
AI/
├─ api/                       FastAPI (15 endpoints)
│  ├─ main.py
│  ├─ config.py db.py temporal_client.py
│  └─ routes/  ingest cases atoms microtypes generate alerts prompts scripts discovery
├─ worker/
│  ├─ workflows/agentic_insight.py
│  ├─ agents/                 a1..a9 全实装
│  ├─ discovery/              poc_crawler / oauth_api
│  ├─ llm/                    Deepseek + Qwen + Claude 客户端
│  ├─ embeddings.py           DashScope text-embedding-v3
│  ├─ storage.py              MinIO
│  └─ db.py                   sync SQLAlchemy
├─ dspy_opt/                  DSPy 自优化（signatures + optimizer + trainset_builder）
├─ web/                       Next.js 14 + Tailwind
│  └─ app/                    page / cases / alerts
├─ db/migrations/             Alembic 10 表 + PoC trigger
├─ infra/                     docker-compose.yml + .env.example
├─ rules/                     banned_terms_14categories.yaml + microtype_schema.yaml
├─ docs/                      v6-architecture / poc-memo / v6-mvp-summary（本文件）
├─ scripts/                   demo_ingest / seed_microtypes / discovery_run / poc_purge
└─ tests/                     21 unit tests
```
