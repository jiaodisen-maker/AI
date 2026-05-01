# v6 Agentic Insight — 云部署手册

## TL;DR

- **首选**：阿里云华东 1（杭州）或华东 2（上海）
- **备选**：火山引擎（字节自家云，千川/巨量延迟最低）
- **不推荐**：AWS/GCP/Azure 海外（PIPL §38 + 抖音 OAuth 限制大陆 IP）

## 三阶段配置

### 阶段 1：MVP/PoC 内部研究 · 单机 · ¥1000-1300/月

ECS g7 通用计算 8 vCPU / 16GB RAM / 100GB SSD + 500GB ESSD 数据盘 + 5Mbps 公网。

所有 service 跑在一台机器：`docker compose -f infra/docker-compose.yml up -d` 起 PG+pgvector / Temporal / MinIO / Redis；API/worker/Next.js 直接 host 跑。

### 阶段 2：内部团队 30 case 扩量 · 拆 DB + OSS · ¥2700-3500/月

| 角色 | 配置 |
|---|---|
| ECS g7 | 8 vCPU / 16GB（worker + api + web）|
| RDS PostgreSQL 16 | 4 vCPU / 8GB / 200GB（pgvector 原生支持）|
| OSS 标准存储 | 500GB（替代 MinIO）|
| ARMS 监控 | Prometheus/Grafana 托管 |

### 阶段 3：对外发布 · HA 集群 · ¥8500-10000/月

ECS 集群 3× g7 + SLB；RDS HA 主备 + 30 天自动备份；Temporal Cluster 3 节点；WAF + SLS 长期日志。

## 网络与合规护栏（强制）

```
                [Internet]
                    │
              [WAF + SLB]
                    │
        ┌───────────┴───────────┐
        │   生产 VPC             │  Worker / API / Web / RDS / OSS
        │   oauth + public_api   │
        └───────────┬───────────┘
                    │ (peering 禁止 — 防 PoC 数据漏到生产)
        ┌───────────┴───────────┐
        │   PoC 沙箱 VPC         │  MediaCrawler / DrissionPage
        │   独立 NAT + 出网日志  │  日志留 ≥1 年
        └───────────────────────┘
```

**硬规则**：
1. 两 VPC 之间禁止 VPC peering / Transit Gateway 互通
2. API + RDS 默认不暴露公网；团队走 SLB+IP 白名单或 SAG/VPN
3. OSS bucket 默认 private，前端通过 STS 签时效 URL
4. PoC 沙箱 VPC 出网日志记 ≥1 年（合规审计）
5. PoC purge 销毁日志 → OSS 归档存储 ≥3 年

## 一键部署 checklist（阶段 1 · MVP）

### 0. 法务前置（不可跳过）
- [ ] `docs/poc-research-memorandum-template.md` 走完法务+CTO+法定代表人三签字
- [ ] 备忘录 PDF 上传 OSS 私有 bucket 归档
- [ ] 法务团队接受 14 类违禁词 yaml v0.2 作为 source of truth

### 1. 阿里云资源开通
- [ ] 创建 VPC（10.0.0.0/16）+ 2 个 vSwitch（生产 10.0.1.0/24 + PoC 沙箱 10.0.2.0/24）
- [ ] 安全组：API 8000 / Web 3000 / Temporal-UI 8233 / MinIO 9001 仅对团队 IP 开放
- [ ] **PoC 沙箱 vSwitch 不挂 EIP**，走独立 NAT 网关；NAT 流日志开启
- [ ] 购买 ECS g7 8C16G + ESSD 数据盘
- [ ] 公网带宽按量付费 5Mbps（够内部团队用）

### 2. 系统初始化
```bash
ssh root@<ecs-ip>
# 安装 Docker + docker compose plugin
curl -fsSL https://get.docker.com | bash
# 克隆仓库
git clone <repo> /opt/agentic-insight
cd /opt/agentic-insight
# 准备 env
cp infra/.env.example infra/.env
# 编辑 infra/.env：填 LLM keys（DEEPSEEK / QWEN / ANTHROPIC）
# POC_CRAWLED_ENABLED 仅在内部研究环境置 true（备忘录签字后）
vim infra/.env
```

### 3. 起 stack
```bash
make up           # PG + Temporal + MinIO + Redis
make migrate      # Alembic 10 表 + PoC trigger + oauth_tokens
make seed         # 50 microtype seed
# 启动 worker（systemd 单元）
sudo cp infra/agentic-worker.service /etc/systemd/system/
sudo systemctl enable --now agentic-worker
# 启动 API
sudo cp infra/agentic-api.service /etc/systemd/system/
sudo systemctl enable --now agentic-api
# Web
cd web && npm install && npm run build
sudo cp ../infra/agentic-web.service /etc/systemd/system/
sudo systemctl enable --now agentic-web
```

### 4. Temporal Schedule（PoC TTL 自动 purge）
```bash
python scripts/setup_purge_schedule.py
```

### 5. 监控（可选，建议起）
```bash
make monitoring   # Prometheus + Grafana + Alertmanager
# Grafana http://<ecs-ip>:3001 (admin/admin) 自动加载 agentic-insight dashboard
```

### 6. 健康检查
```bash
make health
```

预期输出：API 200 / Temporal UI 200 / Postgres ready / MinIO live。

### 7. 端到端 demo
```bash
make demo        # POST /ingest 喂虚构爆款，全流程跑通
```

打开 http://<ecs-ip>:3000 看 cases/atoms/scripts/alerts。

## 阶段 2 升级路径（30 case 扩量后）

1. RDS PostgreSQL 16 实例创建 → `pg_dump` 把现有 docker PG 数据迁过去 → 改 `DATABASE_URL` 重启
2. OSS bucket 创建 → MinIO `mc mirror` 全量同步 → 改 `MINIO_ENDPOINT` + STS 配置
3. 把 ECS 上的 PG/MinIO docker container stop（保 Temporal/Redis）

## 阶段 3 升级路径（对外发布前）

1. **生产 build feature flag 关闸**（CI 已守卫，再人工复核一次）
2. 全量清理 `data_lineage='poc_crawled'` 数据（DB + OSS）
3. 法务复审签字
4. ECS 集群 + SLB
5. RDS 升 HA 主备
6. WAF + SLS + ARMS 全链路监控接入
7. 域名 + ICP 备案 + HTTPS 证书

## 成本估算（月）

| 阶段 | 用户量 | ECS | DB | OSS | 监控 | 总计 |
|---|---|---|---|---|---|---|
| MVP/PoC | 4-5 内部 | ¥800 | docker | docker | docker | **¥1000-1300** |
| 团队 30 case | 5-10 内部 | ¥800 | ¥1200 | ¥120 | ¥300 | **¥2700-3500** |
| 对外发布 | 50+ | ¥3000 | ¥2500 | ¥250 | ¥1500 | **¥8500-10000** |

LLM API 成本另算（Deepseek + Qwen + Claude），按月 1000 case × 5 agent calls × ¥0.01-0.05/call ≈ **¥500-2500/月**。

## 故障 runbook

| 现象 | 排查 | 修复 |
|---|---|---|
| API 502 | `make health` 看 service 状态 | `systemctl restart agentic-api` |
| Workflow 卡住 | Temporal UI 看 activity 失败原因 | 多见 LLM API rate limit / OAuth token 过期 |
| `agentic_poc_pending_purge > 0` | TTL job 是否在跑？ | `python scripts/poc_purge.py` 手动跑 |
| `compliance_edge` 告警增多 | 词库需更新？ | 法务复审 `rules/banned_terms_14categories.yaml` |
| `poc_purge_failed` 告警 | **法律风险，立即排查** | 检查 OSS 权限 / MinIO 连接；手动清理后归档证据 |

## 安全基线

- ECS 系统：禁 root SSH，密钥登录，fail2ban
- DB：禁公网，仅 ECS 内网 IP 白名单
- OSS：bucket 默认 private + STS 签时效 URL
- 应用：API 不裸跑，Nginx + IP 白名单 + 简单 token；生产用 OAuth/SSO
- 密钥：阿里云 KMS 托管 LLM keys 与 OAuth secrets，不写 .env 明文
- 备份：RDS 自动备份 30 天 + OSS 跨区复制（PoC 不复制）
- 审计：ActionTrail 记 OSS / RDS / ECS 所有操作 ≥6 月
