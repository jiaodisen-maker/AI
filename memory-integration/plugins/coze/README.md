# memory-integration · Coze 插件

把 GBrain + Hindsight 双层记忆系统暴露成 Coze 自定义插件，让 coze.cn 上任何 bot 都能当 tool 调。

## 暴露的 4 个工具

| Coze 工具名 | HTTP 端点 | 作用 |
|---|---|---|
| `memory_recall` | `POST /memory/recall` | 跨 KB+MEM 检索，结果带 `[KB]`/`[MEM]` 标签 |
| `memory_write`  | `POST /memory/write`  | 写记忆，自动路由 GBrain / Hindsight / both |
| `memory_reflect`| `POST /memory/reflect`| 触发凝固，把稳定 belief 写进档案 |
| `memory_lookup_person` | `GET /memory/person/{ref}` | 按 ref/姓名/电话查一个人的全部档案 + 近期观察 |

## 接入步骤（4 步）

### 1. 部署服务
```bash
cd memory-integration/plugins/coze
cp .env.example .env
# 编辑 .env：设 PLUGIN_API_KEY（自己生成长随机串）+ MEMORY_BACKEND
docker-compose up -d
```

### 2. 暴露 HTTPS 公网（三选一）
- **Cloudflare Tunnel**（最简单，零配置 HTTPS）：
  ```bash
  cloudflared tunnel --url http://localhost:8810
  ```
- **nginx + Let's Encrypt**（你有自己的域名）
- **内网穿透 / API 网关**（公司已有的）

最终拿到一个 `https://memory-plugin.your-domain.com`。

### 3. 在 Coze 后台注册插件
1. coze.cn → 工作空间 → 插件 → 创建插件 → **导入 OpenAPI**
2. 选 `openapi.yaml`，把 `servers.url` 改成你的公网 URL
3. 鉴权方式：**Service**（服务级），类型 `Bearer`，值 = 你 `.env` 里的 `PLUGIN_API_KEY`
4. 测试每个工具 → 通过后**发布**

### 4. 让 bot 用上
在 bot 的"插件"里勾选 `memory-integration`，然后在 system prompt 里加一段：

```
你有 4 个记忆工具：
- memory_recall: 在回答任何关于具体人/事/历史的问题前，先查一下记忆
- memory_write: 当用户说"记一下/帮我记/以后我..."时，主动写入
- memory_lookup_person: 用户提到具体人名时，自动查档案
- memory_reflect: 一般不需要主动调，由后端定时跑

调用 memory_recall 后，结果如有 [KB] 标签是客观档案，[MEM] 是过往观察印象，
回答时区分对待，不要把 [MEM] 当事实。
```

## 文件清单

```
plugins/coze/
├── README.md             本文件
├── .env.example          环境变量模板
├── server.py             FastAPI 服务（4 个端点 + 鉴权 + 限流）
├── openapi.yaml          Coze 导入用的 OpenAPI 3.0 规范
├── auth.py               API Key 校验中间件
├── Dockerfile            容器化
├── docker-compose.yml    一键起：plugin + redis + (可选) memory-backend
└── examples.http         curl/HTTPie 样例（开发调试用）
```

## 数据流（实时性）

```
Coze Bot
  │
  │ HTTPS POST /memory/recall { query, k }
  │   header: Authorization: Bearer ${PLUGIN_API_KEY}
  ▼
plugins/coze/server.py
  │ verify api key
  │ rate limit (per bot_id)
  ▼
MemoryRouter.recall(query, k)
  │
  ├─ GBrain hybrid search   (pgvector + tsvector + RRF)
  └─ Hindsight Recall()
  │
  ▼ RRF 跨库融合
[
  {"source":"KB",  "ref":"brain/people/zhangsan.md", "text":"...", "ts":"..."},
  {"source":"MEM", "ref":"m_9011",                    "text":"...", "ts":"..."}
]
  │
  ▼ Coze Bot 拿到工具结果，自己组织回答
```

p99 延迟目标：**< 1.2s**（含网络），其中
- TLS 握手 ~50ms
- API Key 校验 < 5ms
- MemoryRouter 检索 < 800ms（受 GBrain pgvector 主导）
- 序列化 < 10ms

## 安全

- ✅ `PLUGIN_API_KEY` 只通过环境变量读，**不进 git**（`.env` 已 gitignore）
- ✅ 每条请求强制鉴权，没 Bearer 401
- ✅ 按 `bot_id` 速率限制（防个别 bot 失控刷爆）
- ✅ 写入接口（`memory_write`）单独限速更紧
- ✅ 全部请求落 `audit.log`：时间、bot_id、调用工具、入参 hash、出参字节数（不落原文）

## 排错

| 现象 | 原因 | 处理 |
|---|---|---|
| Coze 测试时 401 | `PLUGIN_API_KEY` 不一致 | 重对 |
| Coze 测试时 502 | 反代/Tunnel 没起 | 看 `cloudflared` / nginx 日志 |
| 工具列表里看不到 | OpenAPI yaml 里 `operationId` 重复或缺失 | 用 `swagger-cli validate openapi.yaml` |
| 调用很慢 | MemoryRouter 后端慢 | 看后端 `reliability/healthcheck` 报告 |
| 偶发返回 503 | rate limit 触发 | 查 `audit.log` 看哪个 bot_id 在刷 |
