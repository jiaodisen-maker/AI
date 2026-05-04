# sources/feishu —— 实时数据通道

把飞书所有产生信息的入口实时灌进 `MemoryRouter`，由 router 自动路由到 GBrain / Hindsight。

## 架构

```
                 飞书开放平台
                  │
   ┌──────────────┼─────────────────────────────┐
   │              │                             │
   │ Webhook 模式  │ 长连接模式                   │
   ▼              ▼                             │
┌─────────┐  ┌──────────────┐                   │
│server.py│  │long_connection│  ← 二选一          │
│FastAPI  │  │.py            │                  │
│/webhook │  │WebSocket      │                  │
└────┬────┘  └──────┬────────┘                  │
     │              │                           │
     │ 验签解密      │ 直接拿到 event              │
     │ 去重 (event_id)│                          │
     │ 立即 ACK      │                           │
     └──────┬───────┘                           │
            ▼                                   │
       ┌──────────────────┐                     │
       │ Queue (Redis     │                     │
       │ Streams)         │ ──→ DLQ            │
       └──────┬───────────┘     (重试超 N 次)    │
              │                                 │
              ▼                                 │
       ┌─────────────────┐                      │
       │ worker.py       │                      │
       │ - translator    │                      │
       │ - 调 MCP 工具    │                      │
       │   memory_write  │                      │
       └──────┬──────────┘                      │
              │                                 │
              ▼                                 │
        MemoryRouter (上一层)                    │
              │                                 │
       ┌──────┴──────┐                          │
       ▼             ▼                          │
    GBrain      Hindsight                       │
                                                │
   ─────────────────────────────────────────────┘
   守护进程：
     token_refresher.py    tenant_access_token 自动续期
     backfill.py           启动 / 灾难恢复时拉历史数据
```

## 文件清单

```
sources/feishu/
├── README.md                  本文件
├── config.example.yaml        飞书凭据 + 订阅事件清单
├── server.py                  Webhook 接收（FastAPI）
├── long_connection.py         WebSocket 长连接（无公网时用）
├── worker.py                  队列消费者：event → memory_write
├── translator.py              event 类型 → memory hints 映射
├── backfill.py                冷启动 / 灾难恢复回填
├── token_refresher.py         tenant_access_token 守护进程
├── idempotency.py             event_id 去重
└── docker-compose.yml         一键启全套
```

## 事件 → 记忆路由表（translator.py 实现）

| 飞书事件 | 内容提取 | 路由 |
|---|---|---|
| `im.message.receive_v1` (DM) | 对话片段 + sender | Hindsight (`type=experience`) |
| `im.message.receive_v1` (群 @bot) | 指令 + 上下文 | Hindsight (`type=interaction`) |
| `drive.file.edit_v1` | 文档摘要 + url | GBrain (`type=document`) |
| `calendar.calendar.event.changed_v4` | 标题/时间/参与人 | GBrain (`type=meeting`) |
| `bitable.record.changed_v1` | 记录快照 + 表名 | GBrain (`type=record`) |
| `approval.instance.changed` | 决定 + 理由 | both（事实→KB，判断→MEM）|
| `vc.meeting.recording.ended_v1` | 拉转写 → 摘要 | both |
| `contact.user.updated_v3` | 人员变更 | GBrain (`type=person_profile`) |

## 实时性 SLO

| 指标 | 目标 |
|---|---|
| Webhook 入口 → ACK | < 200ms |
| Webhook → 进入 Hindsight | p99 < 3s |
| 入 GBrain（向量化）| p99 < 10s |
| 失败重试间隔 | 1s, 2s, 4s, 8s, 16s（5 次后 DLQ）|
| Backfill 频率 | 启动 1 次 + 每天凌晨 1 次对账 |
| token 提前续期 | 过期前 10 分钟 |

## 二选一：Webhook vs 长连接

|  | Webhook | 长连接 |
|---|---|---|
| 公网入口要求 | 必须 HTTPS 域名 | ❌ 不需要 |
| 部署 | FastAPI + 反代 | 一个 Python 进程 |
| 可靠性 | 飞书重试 3 次 | 心跳掉线就重连 |
| 性能 | 高（无单点）| 单点，QPS 受限 |
| **推荐场景** | 公司有公网 K8s | 内网 / 本地开发 |

两者**用同一个 worker / translator / queue**，只是入口换了。配置切换即可。

## 启动

```bash
cp sources/feishu/config.example.yaml sources/feishu/config.yaml
# 填 app_id / app_secret / encrypt_key / verification_token

# Webhook 模式
docker-compose -f sources/feishu/docker-compose.yml up -d

# 或长连接模式（无公网）
python sources/feishu/long_connection.py &
python sources/feishu/worker.py &
python sources/feishu/token_refresher.py --cron &
python sources/feishu/backfill.py --once
```
