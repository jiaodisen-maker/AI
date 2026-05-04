# feishu-coze-bridge

> 飞书全量数据 → Coze 企业旗舰版的实时同步桥梁。
> 跑在你公司 ECS（火山/阿里云），通过 Coze OpenAPI 写入。
> 配套文档：`docs/coze-knowledge-base/FEISHU-SYNC-BRIDGE.md`（架构）+ `SAAS-VS-SELFBUILD.md`（边界）。

## 30 秒上手（开发环境）

```bash
git clone <repo>
cd feishu-coze-bridge
cp .env.example .env
# 编辑 .env：填飞书 app_id/secret，Coze PAT，Redis URL
docker compose up -d
docker compose logs -f bridge worker
```

3 分钟之内你应该看到：
```
[bridge] FastAPI listening on 0.0.0.0:8810
[worker:w1] consuming feishu:events
[token-refresher] refreshed Feishu tenant_access_token, ttl=7200s
```

## 目录

```
feishu-coze-bridge/
├── README.md                        本文件
├── .env.example                     环境变量模板
├── docker-compose.yml               一键部署
├── Caddyfile                        HTTPS 反代
├── Dockerfile                       容器化
├── requirements.txt
├── bridge/                          ★ 主代码
│   ├── config.py                    配置加载
│   ├── server.py                    Webhook 接收（FastAPI）
│   ├── long_connection.py           长连接备选
│   ├── queue.py                     Redis Streams 队列
│   ├── idempotency.py               event_id 去重
│   ├── coze_client.py               ★ Coze OpenAPI 客户端
│   ├── feishu_client.py             飞书 OpenAPI 客户端
│   ├── translator.py                ★ 事件→Coze 动作翻译器
│   ├── worker.py                    队列消费者 + 重试
│   ├── safety.py                    PII 拦截
│   ├── audit.py                     审计日志
│   ├── token_refresher.py           飞书/Coze token 续期
│   └── backfill.py                  日常回填
├── tests/                           单测（PII / translator）
└── deploy/                          k8s manifest（可选）
```

## 数据流（一图看懂）

```
飞书事件订阅
  ↓ HTTPS POST
server.py（FastAPI, 验签+解密+去重）
  ↓ 立即 ACK <200ms
queue.py（Redis Streams）
  ↓ 多 worker 并发消费
worker.py
  ├─ translator.py 把飞书事件 → Coze 动作 dict
  ├─ safety.py 检查 PII（含 L4 数据 → 拦截不发）
  └─ coze_client.py 调 Coze OpenAPI 写入
  ↓
Coze 企业旗舰版（KB / chat / 成员 / workflow）
```

## 同步覆盖的 15 类飞书事件

见 `bridge/translator.py` 里的 `EVENT_HANDLERS`。每类事件都有 unit test 在 `tests/`。

## 部署到生产

参考 `docs/coze-knowledge-base/FEISHU-SYNC-BRIDGE.md §10`：双实例 + 火山 ALB + RDS + KMS。

## 排错

```bash
# 看 webhook 是否收到
docker compose logs bridge | grep "webhook received"

# 看队列堆积
docker compose exec redis redis-cli xinfo stream feishu:events

# 看 DLQ
docker compose exec redis redis-cli xrange feishu:events:dlq - +

# 看哪个 worker 慢
docker compose logs worker | grep ELAPSED
```

详细见 `docs/coze-knowledge-base/FEISHU-SYNC-BRIDGE.md §11`。

## 许可

公司内部代码，未经允许不外传。
PAT / 飞书 secret / API key 全走火山 KMS，**严禁**写在配置文件里。
