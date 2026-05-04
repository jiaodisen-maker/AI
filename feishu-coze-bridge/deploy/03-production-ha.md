# 生产高可用升级（Week 2）

> Day 1 单实例验证 OK 之后做。**不要跳过单实例直接上 HA**。
> 目标：双实例 + 火山 ALB + 火山 RDS + KMS + Redis 实例。

## 架构升级图

```
   [Day 1]                          [Week 2 升级后]
                                    
   1 台 ECS                          公网 → 火山 ALB
   ├ bridge                              │
   ├ workers ×3                          ▼
   ├ caddy           →   ┌──────────┬──────────┐
   ├ postgres            │ ECS-1    │ ECS-2    │
   └ redis               │ bridge   │ bridge   │
                         │ workers  │ workers  │
                         └────┬─────┴────┬─────┘
                              │          │
                         火山 RDS PG  火山 Redis
                         (内网访问)    (内网访问)
                              │
                         火山 KMS（密钥）
```

## 升级步骤

### Step 1：开火山 RDS PostgreSQL（30 分钟）

火山控制台 → 关系型数据库 RDS → 创建 PostgreSQL 实例：

| 项 | 值 |
|---|---|
| 版本 | PostgreSQL 16 |
| 规格 | rds.pg.1c2g（1 vCPU, 2 GB） |
| 存储 | 50 GB SSD |
| 网络 | **跟 ECS 同 VPC + 同子网** |
| 主备 | 主备版（高可用）|
| 备份 | 每日自动 + 7 天保留 |
| 加密 | TDE 透明数据加密 ✅ |

成本约 **¥350/月**。

创建后：
1. 控制台开"白名单"，加你 ECS 内网 IP
2. 拿到内网 endpoint：`rds-xxx.rds.ivolces.com:5432`
3. 创建 db `bridge` + 用户 `bridge`

迁移数据：

```bash
# 在 ECS 上 dump 单实例 postgres
docker compose exec postgres pg_dump -U bridge bridge > /tmp/bridge.sql

# 恢复到 RDS
PGPASSWORD=xxx psql -h rds-xxx.rds.ivolces.com -U bridge bridge < /tmp/bridge.sql
```

更新 `.env`:

```
DATABASE_URL=postgresql://bridge:xxx@rds-xxx.rds.ivolces.com:5432/bridge
```

从 docker-compose.yml 删掉 `postgres` 服务。

### Step 2：开火山 Redis 实例（20 分钟）

火山控制台 → 缓存数据库 Redis → 创建：

| 项 | 值 |
|---|---|
| 版本 | Redis 7 |
| 规格 | 1 GB 主从 |
| 网络 | 同 VPC |

成本约 **¥150/月**。

更新 `.env`:

```
REDIS_URL=redis://:xxx@redis-xxx.redis.ivolces.com:6379/0
```

从 docker-compose.yml 删掉 `redis` 服务。

### Step 3：火山 KMS 托管所有密钥（30 分钟）

参考 `docs/coze-knowledge-base/AI-GATEWAY-SETUP.md §4.4`：

```bash
# 在 ECS 上装火山 CLI
curl ... | bash
volcengine configure

# 把所有密钥放进 KMS
volcengine kms create-secret --name bridge/feishu-app-secret --value "$FEISHU_APP_SECRET"
volcengine kms create-secret --name bridge/feishu-encrypt-key --value "$FEISHU_ENCRYPT_KEY"
volcengine kms create-secret --name bridge/feishu-verification-token --value "$FEISHU_VERIFICATION_TOKEN"
volcengine kms create-secret --name bridge/coze-pat --value "$COZE_PAT"
volcengine kms create-secret --name bridge/feishu-alert-webhook --value "$FEISHU_ALERT_WEBHOOK"
```

写一个 `entrypoint.sh` 启动时拉密钥：

```bash
#!/bin/sh
set -e
export FEISHU_APP_SECRET=$(volcengine kms get-secret-value --name bridge/feishu-app-secret --query 'SecretValue' -o text)
export FEISHU_ENCRYPT_KEY=$(volcengine kms get-secret-value --name bridge/feishu-encrypt-key --query 'SecretValue' -o text)
export FEISHU_VERIFICATION_TOKEN=$(volcengine kms get-secret-value --name bridge/feishu-verification-token --query 'SecretValue' -o text)
export COZE_PAT=$(volcengine kms get-secret-value --name bridge/coze-pat --query 'SecretValue' -o text)
export FEISHU_ALERT_WEBHOOK=$(volcengine kms get-secret-value --name bridge/feishu-alert-webhook --query 'SecretValue' -o text)
exec "$@"
```

修改 `Dockerfile`：

```dockerfile
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "-m", "bridge.server"]
```

`.env` 里删掉敏感字段（保留非敏感的非业务配置）。

### Step 4：开第二台 ECS（15 分钟）

跟第一台**同规格 + 同 VPC**。

```bash
# 第二台同样初始化
ssh ubuntu@<ECS-2 IP>
sudo apt update && sudo apt install -y docker.io docker-compose-plugin git
git clone ... && cd feishu-coze-bridge
cp .env.example .env  # 跟第一台一致（或共享配置）
docker compose up -d
```

⚠️ **第二台不要跑 backfill 和 token-refresher**——单实例即可。
改 docker-compose.yml 把这俩 service 注释掉。

### Step 5：火山 ALB（30 分钟）

火山控制台 → 负载均衡 → 应用型 ALB → 创建：

| 项 | 值 |
|---|---|
| 类型 | 公网 ALB |
| 监听 | HTTPS 443（上传你的证书 / 用火山托管证书）|
| 后端服务 | 创建后端组 `bridge-backend`，加 ECS-1:8810 + ECS-2:8810 |
| 健康检查 | HTTP GET /healthz |

成本约 **¥200/月**。

DNS 改：把 `bridge.your-company.com` 从 ECS-1 IP 改到 **ALB 公网 IP**。

ECS 侧不再需要 Caddy（ALB 接管 HTTPS）—— 从 docker-compose.yml 删 caddy 服务。

但 bridge 要监听 `0.0.0.0:8810` 给 ALB 探测——已经是默认。

### Step 6：飞书后台改 webhook URL

`https://bridge.your-company.com/webhook/feishu` 不变（DNS 已切）。
飞书后台不用改。

### Step 7：验证

```bash
# 关一台 ECS 模拟故障
ssh ubuntu@<ECS-1 IP>
docker compose stop bridge

# 飞书发消息 → 应该 ECS-2 接管，无中断
# ALB 健康检查会标记 ECS-1 unhealthy
```

恢复：`docker compose start bridge`

## 升级后成本

| 项 | 月费 |
|---|---|
| ECS × 2（4C16G）| ¥700 |
| EIP × 2（1Mbps 各）| ¥120 |
| RDS PG 主备（1C2G）| ¥350 |
| Redis 主从（1G）| ¥150 |
| ALB | ¥200 |
| 域名 | ¥7（年摊月）|
| KMS（少量凭据）| ¥10 |
| **总计** | **≈ ¥1,540/月** |

跟 Day 1 单实例（¥800/月）比，多 ¥740 换来：
- ✅ 单实例宕机不影响业务
- ✅ Postgres + Redis 自动备份
- ✅ 密钥不在 .env 里
- ✅ 全流量进 ALB 有审计日志

## Week 2 验收清单

```
□ 关一台 ECS，5 秒内 ALB 切流量
□ /metrics 仍能从内网访问
□ 飞书 webhook 流量经过 ALB 日志能查到
□ KMS 密钥拉取每次启动正常
□ Postgres 主备切换演练（季度 1 次）
□ 月度成本对账
```

## 接下来

- 接监控告警（参考 `04-runbook.md`）
- 季度演练（拉一台 ECS 重启 / KMS 凭据轮换 / DLQ drain）
- 半年评估是否升 4C8G→8C16G（看 CPU 利用率）
