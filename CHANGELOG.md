# Changelog

## W7 — 全栈集成实装

**真实管道实装**：
- **媒体管道完整** (`worker/agents/a2_media.py`)：yt-dlp 下载 → MinIO 存储 → ffmpeg 抽音/抽帧 → FunASR 转写 → PaddleOCR 字幕 → Qwen-VL 视觉理解；A2 decomposition 直接调用，缺 manual_payload 时走真管道
- **抖音 OAuth 完整 flow** (`worker/discovery/oauth_tokens.py`)：DB 表 `oauth_tokens` (迁移 002) 持久化 access/refresh tokens；自动刷新（剩余 ≤5min 触发）；exchange_code 接 OAuth 回调
- **千川 Marketing API 完整 client** (`worker/discovery/qianchuan_client.py`)：v3.0 报表（CPM/CTR/CVR/GMV）+ 视频信息接口；通过 oauth_tokens 表读取 advertiser_id；A5 改用此 client
- **DSPy compiled prompt 真正喂回 A8**：`dspy_opt.optimizer` 把 BootstrapFewShot 学到的 demos 序列化成 LLM-friendly system prompt（DEFAULT + 高分示例）写入 `prompt_versions.prompt_text`；A8 启动时拉最新版本作为系统提示

**生产监控栈**：
- `infra/monitoring/docker-compose.yml`：Prometheus + Grafana + Alertmanager
- `prometheus.yml` 抓 API `/metrics`；`alerts.yml` 5 条规则（HITL 堆积/PoC purge 失败/合规边界/新 microtype 候选）
- Grafana dashboard JSON：8 panels（open alerts/PoC pending/cases/DSPy/lineage/atoms/alerts trend/microtypes）+ datasource 自动 provision
- `make monitoring` 一键启动

**集成测试**：
- `tests/integration/test_workflow_mocked.py` — mock LLM 跑 A2→A3 全链 + 验 PoC isolation trigger 真实 RAISE EXCEPTION
- 自动 skip if no DATABASE_URL；CI 用 GitHub Actions Postgres service container 真跑

**Quality of Life**：
- structured logging + correlation IDs（worker `setup_structured_logging`）
- 违禁词补到 100+ patterns（年龄/性别歧视、医疗机构、特殊人群类目扩充）
- /discovery Web UI 页（批量 A1 触发表单）
- Makefile 加 monitoring / health / logs 三命令
- CI 拆双 job（lint+unit + integration-test with PG service）+ production-build feature flag 守卫

**40/40 单测 pass + 集成测试就绪 + ruff 全绿。**

## W6 — UI 完整 6 页 + 违禁词全 14 类 v0.2

- **Web UI 4 个新页面**：
  - `/atoms` 文本/类型/合规等级搜索
  - `/microtypes` 列表 + status filter + candidate Activate 按钮
  - `/scripts` 列表 + `/scripts/[id]` 详情（7 维 critic 平均分 grid + 三家 evaluator 表）
  - `/prompts` DSPy prompt 历史
- 违禁词类目 04-14 全部扩到 v0.2 水平（每类 +5-10 patterns）
- **8 个 v0.2 命中单测**（同行贬损/医疗器械/极限词/中医经络/数据造假/伪科学/酸碱体质/能量场）
- API client 类型补完（`web/lib/api.ts` 新增 Microtype/ScriptListItem/ScriptDetail/PromptVersion 类型）
- 导航栏补全 6 个页面链接

**40/40 pytest pass，ruff 全绿，UI 6 页齐备。**

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
