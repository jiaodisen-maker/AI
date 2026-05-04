---
name: feishu-realtime-setup
description: 部署 / 自检 / 重启飞书 → 记忆系统的实时数据通道
trigger:
  - 接入飞书 / 配飞书 / 飞书数据通
  - feishu setup / sync feishu
inputs:
  mode: webhook | long_connection（默认 webhook）
  action:
    - deploy        # 首次部署
    - healthcheck   # 检查链路是否通畅
    - restart       # 重启所有进程
    - backfill      # 临时回填
    - drain_dlq     # 处理死信队列
---

# Skill: feishu-realtime-setup

## 目标
保证飞书数据**实时、不丢**进 GBrain + Hindsight。

## action: deploy（首次部署）

### Webhook 模式
1. 飞书开放平台后台
   - 创建企业自建应用，拿到 `app_id` / `app_secret`
   - 事件订阅 → 配置 URL：`https://memory.your-domain.com/webhook/feishu`
   - 生成 `encrypt_key` + `verification_token`
   - 添加事件订阅（见 config.example.yaml `subscribed_events`）
   - 申请权限：`im:message`, `drive:drive`, `calendar:calendar`, `vc:meeting`,
     `contact:user.base:readonly`, `approval:instance.callback`
2. 服务端
   ```bash
   cp sources/feishu/config.example.yaml sources/feishu/config.yaml
   # 填好 4 个凭据
   echo 'FEISHU_APP_SECRET=...' >> .env
   echo 'FEISHU_ENCRYPT_KEY=...' >> .env
   echo 'FEISHU_VERIFICATION_TOKEN=...' >> .env
   docker-compose -f sources/feishu/docker-compose.yml up -d
   ```
3. 在飞书后台点"验证 URL"，应当返回 challenge → 配置完成

### 长连接模式（无公网）
- 飞书后台同上，但 URL 留空
- 启动 `python sources/feishu/long_connection.py &`
- 同时需要 `worker.py` / `token_refresher.py` / `backfill.py`

## action: healthcheck（必跑）

按顺序验证四件事：

| 检查项 | 命令 | 期望 |
|---|---|---|
| 1. Redis 在跑 | `redis-cli ping` | `PONG` |
| 2. token 续期成功 | `redis-cli get feishu:tenant_access_token` | 非空字符串 |
| 3. 队列有消费者 | `redis-cli xinfo groups feishu:events` | consumers ≥ 1, lag 不持续涨 |
| 4. 端到端 | 自己给机器人发一条 DM"健康检查" | 30 秒内 `memory_recall("健康检查")` 命中 |

**任一失败 → 给负责人推飞书告警**（不要静默修复，因为可能是凭据问题）。

## action: backfill

```bash
# 临时拉过去 72 小时
python -m sources.feishu.backfill --hours 72
```

什么时候用：
- 部署完发现历史数据没进
- DLQ 太满处理完想验证
- 飞书侧告知有事件投递异常

## action: drain_dlq

死信队列里的事件**不要自动重处理**——大概率是配置问题或飞书 API 变更。

```bash
# 看 DLQ 里有什么
redis-cli xrange feishu:events:dlq - +

# 决定后再回灌
redis-cli xrange feishu:events:dlq - + | python -m sources.feishu.requeue_dlq
```

要先排查 reason，**修好根因再 drain**。

## 边界 / 不要做的事

- ❌ 不要把 `app_secret` / `encrypt_key` 写进 git，必须走环境变量或 secret manager
- ❌ 不要在 webhook handler 里调记忆系统——会超时被飞书重投，**必须立即入队**
- ❌ DLQ 不自动 retry——那是给人审的
- ❌ token 不要在每个 worker 各拉各的——共享 Redis 一份，避免被飞书限流封 IP
- ❌ Backfill 时同事正在用别把队列挤满——`backfill` 用专门的 `priority=low` stream（生产建议拆）

## 排错速查

| 现象 | 原因 | 处理 |
|---|---|---|
| 飞书后台"URL 验证失败" | encrypt_key 或 verification_token 不对 | 重对一次 |
| Webhook 响应 401 | 签名校验失败 | 检查 `encrypt_key` 是否 base64 编码 |
| 队列堆积 | worker 太少 / memory MCP 慢 | 加 worker / 看 MCP 日志 |
| 同一条消息进了多次 | event_id 去重失效 | 检查 Redis idempotency 库是否被清 |
| token 一直 401 | app_secret 过期或权限改了 | 重发 secret，重启 token_refresher |
| 长连接频繁断 | 网络 / 飞书侧限流 | 看 lark-oapi 日志，必要时切 webhook |
