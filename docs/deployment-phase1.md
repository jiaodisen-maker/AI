# 阶段 1 部署 Playbook —— 阿里云单机 MVP

预计耗时：**2-3 小时**（不含 ICP 备案，备案另算 7-15 天但阶段 1 不需要域名）

---

## Step 0 法务前置（不可跳，5 分钟人工 + 1-2 周内部走签）

- [ ] `docs/poc-research-memorandum-template.md` 走完法务+CTO+法定代表人三签字
- [ ] PDF 上传公司私有归档（OSS 私有 bucket / 内部 wiki）
- [ ] 法务部门接受 `rules/banned_terms_14categories.yaml v0.2` 作为 source of truth

> 没签前 `POC_CRAWLED_ENABLED` 必须留 `false`（默认就是）。

---

## Step 1 阿里云开通资源（30 分钟）

### 1.1 VPC + vSwitch
- 控制台 → VPC → 创建 VPC `agentic-insight-vpc`（10.0.0.0/16）
- 在 VPC 下建 vSwitch `mvp-vsw`（10.0.1.0/24，可用区 H 或 K）
- 阶段 1 不需要 PoC 沙箱 vSwitch（PoC 通道默认关）

### 1.2 ECS
- 实例：通用计算型 g7 / **ecs.g7.2xlarge**（8 vCPU / 32GB）or **ecs.g7.xlarge**（4 vCPU / 16GB，省钱）
- 镜像：Ubuntu 22.04 LTS 64 位
- 系统盘：100GB ESSD PL1
- 数据盘：500GB ESSD PL1（挂载到 `/data`，开"释放实例时同时释放"=否）
- 公网：按使用流量 5Mbps + 100GB 月包
- 安全组：暂只放 22 / 80（443 等域名+证书后再开）
- 登录：SSH 密钥对（不用密码）

预算确认：实例 ¥600 + 数据盘 ¥250 + 公网 ¥130 ≈ **¥1000/月**

### 1.3 数据盘挂载
SSH 进 ECS 后：
```bash
fdisk -l                              # 看到 /dev/vdb（500GB 数据盘）
mkfs.ext4 /dev/vdb
mkdir -p /data
echo "/dev/vdb /data ext4 defaults 0 0" >> /etc/fstab
mount -a
df -h /data                           # 确认挂载
```

---

## Step 2 一键 Bootstrap（10 分钟）

```bash
# 把仓库 URL 替换成你公司 GitLab/GitHub 内网仓库
curl -fsSL https://your-internal-host/bootstrap.sh \
    | sudo bash -s -- git@gitlab.your-corp.com:your/agentic-insight.git
```

或者先 git clone 再跑：
```bash
git clone <repo> /opt/agentic-insight
sudo bash /opt/agentic-insight/infra/bootstrap.sh
```

bootstrap 会装：Docker + Node 20 + Python 3.11 + ffmpeg + UFW + fail2ban + 应用 venv + Web build + systemd 单元。

---

## Step 3 配置 .env（5 分钟）

```bash
sudo -u app vim /opt/agentic-insight/infra/.env
```

必填：
```ini
DATABASE_URL=postgresql+psycopg://platform:platform@localhost:5432/platform
TEMPORAL_ADDRESS=localhost:7233
MINIO_ENDPOINT=localhost:9000
REDIS_URL=redis://localhost:6379/0

# 用阿里云 KMS 凭证（生产）或临时填明文（PoC）
DEEPSEEK_API_KEY=sk-...
QWEN_API_KEY=sk-...                   # DashScope key
ANTHROPIC_API_KEY=sk-ant-...

# v6 feature flag — 阶段 1 默认 false
POC_CRAWLED_ENABLED=false
POC_DATA_TTL_DAYS=30
HITL_WEBHOOK_URL=                     # 钉钉机器人 webhook
```

LLM key 申请：
- Deepseek: https://platform.deepseek.com/
- Qwen (DashScope): https://dashscope.console.aliyun.com/
- Anthropic: https://console.anthropic.com/

> KMS 集成（生产前）见 `docs/kms-integration.md`（待写）。阶段 1 明文 .env 可接受，但文件权限须 600。

```bash
chmod 600 /opt/agentic-insight/infra/.env
```

---

## Step 4 起 stack（10 分钟）

```bash
sudo -u app bash -c "cd /opt/agentic-insight && \
    make up && \
    make migrate && \
    make seed"
```

预期：`docker ps` 看到 5 个 container（postgres / temporal / temporal-ui / minio / redis），`microtypes` 表 50 行。

---

## Step 5 起应用（5 分钟）

```bash
sudo systemctl enable --now agentic-worker agentic-api agentic-web
sudo journalctl -fu agentic-worker        # 看 worker 注册到 Temporal
```

worker 应该输出：`{"level":"INFO","msg":"Worker started"}`

---

## Step 6 反向代理（5 分钟）

```bash
sudo bash /opt/agentic-insight/infra/nginx-setup.sh
```

完成后访问 `http://<ECS 公网IP>/`：
- `/` → Next.js 首页
- `/cases` → cases 列表
- `/api/health` → `{"status":"ok",...}`

---

## Step 7 端到端 demo（5 分钟）

```bash
sudo -u app bash -c "cd /opt/agentic-insight && make demo"
```

预期：cases 表新增 1 行；segments 9 行；atoms ≥10 条；cross_validations 至少 a3_compliance 一行。

打开 `http://<ECS 公网IP>/cases/{id}` 看 9 段拆解 + 原子卡片。

---

## Step 8 健康检查 + 监控（10 分钟）

```bash
sudo bash /opt/agentic-insight/infra/health-check.sh
```

期待：12 项全 ✅。

可选起监控栈：
```bash
sudo -u app bash -c "cd /opt/agentic-insight && make monitoring"
# Grafana http://<ECS-IP>:3001（先在安全组开 3001 + 9090）
```

---

## Step 9 PoC TTL 自动化（5 分钟，仅当 POC_CRAWLED_ENABLED=true）

```bash
sudo -u app bash -c "cd /opt/agentic-insight && python scripts/setup_purge_schedule.py"
```

阿里云 ECS 上 Temporal Schedule 会每天 03:00 自动跑 PocPurgeWorkflow。

---

## 可视化访问

阶段 1 默认全开 80（团队 5-10 人用）。**生产姿态前必须收紧**：
1. 安全组只放团队办公 IP
2. 或 Nginx `team_ips.conf` 加白名单
3. 或上 Aliyun SLB + IP 白名单 + ICP 备案 + HTTPS 证书

---

## 故障排查

| 现象 | 排查 |
|---|---|
| `make up` 失败 | `docker logs <container>` 看 PG 启动日志，多见数据盘没挂 |
| API 502 | `journalctl -u agentic-api` 看异常；常见 LLM key 没填 / DATABASE_URL 错 |
| Temporal worker 不注册 | `journalctl -u agentic-worker`；check `TEMPORAL_ADDRESS=localhost:7233` |
| `make demo` 报 LLM 错 | 检查 `.env` LLM key + 网络出口（华东节点 → Deepseek API 一般 <100ms）|
| 前端 404 | `npm run build` 是否成功；`agentic-web` systemd 是否启动 |

## 备份策略（阶段 1 最低限度）

```bash
# crontab 加每天 02:00 自动 dump
0 2 * * * docker exec $(docker ps -qf name=postgres) \
    pg_dump -U platform platform | gzip > /data/backup/pg_$(date +\%Y\%m\%d).sql.gz

# 保留 30 天
0 3 * * * find /data/backup -name 'pg_*.sql.gz' -mtime +30 -delete
```

升阶段 2 时这些 dump 直接 `pg_restore` 到 RDS。

---

## 阶段 1 限制（明确边界）

- ❌ 不能对外发布脚本 / 投放
- ❌ ECS 重启 = 短暂中断（docker volume 数据保留）
- ❌ 单点故障（盘坏 = 数据丢，靠 pg_dump 兜底）
- ❌ 无 KMS 密钥托管（明文 .env）
- ❌ 无 WAF / DDoS 防护
- ✅ 可内部 5-10 人研究使用
- ✅ 可跑 PoC 通道（备忘录签字后开 flag）
- ✅ 可累计 50-100 case 验证流水线

> 触发任意一个升阶 → 走 `docs/deployment.md` 阶段 1→3 直跳路径。
