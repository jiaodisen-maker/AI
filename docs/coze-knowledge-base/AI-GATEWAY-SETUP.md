# 架 AI Gateway 完整指南

> 配合 `MODELS.md` 食用——`MODELS.md` 讲为什么，本文讲怎么做。
> 读者：工程师 2（主）+ 工程师 1（架构 review）。
> 目标：1 周内把生产可用的 AI Gateway 跑起来，让扣子能调它。

## 0. TL;DR · 30 秒决策

| 项 | 决策 |
|---|---|
| 网关软件 | **LiteLLM Proxy**（Apache 2.0，Python，BerriAI 出品）|
| 部署 | Docker Compose 在 1 台 4C8G ECS（火山引擎）|
| 数据库 | Postgres（自部署或火山 RDS）|
| HTTPS | Caddy（自动 Let's Encrypt）|
| 密钥 | 火山引擎 KMS 托管 |
| 监控 | Prometheus + Grafana |
| 时间 | **第 1 天单实例 PoC，第 1 周生产可用** |
| 成本 | ECS ¥300/月 + RDS ¥200/月 + 域名 ¥80/年 ≈ **¥600/月**（不含模型 API 费）|

---

## 1. 选型理由（5 分钟看完）

| 方案 | 中国可用 | OpenAI 兼容 | 模型支持 | UI | 中国本土 | 推荐 |
|---|---|---|---|---|---|---|
| **LiteLLM Proxy** | ✅ | ✅ 100% | **200+** | 有 admin UI | ❌ | ⭐⭐⭐⭐⭐ |
| One-API | ✅ | ✅ | 100+ | UI 漂亮 | ✅ | ⭐⭐⭐⭐ |
| Higress AI Gateway | ✅ | ✅ | 50+ | 阿里出 | ✅ | ⭐⭐⭐⭐ |
| OpenRouter（SaaS）| 不稳定 | ✅ | 200+ | 已有 | ❌ | ⭐⭐⭐（不自建场景）|
| 自研（FastAPI 转发）| - | 自己写 | 自己加 | 自己做 | - | ⭐（除非有特殊需求）|

**为什么选 LiteLLM**：
1. 模型支持最广（OpenAI/Claude/Gemini/Bedrock/Ollama/Azure/DeepSeek/通义/豆包... 200+）
2. OpenAI 协议 100% 兼容（扣子无缝接）
3. 内置：fallback / 限流 / 预算 / per-user key / 审计 / Trace
4. 活跃维护（每周更新）
5. 兼容 LangChain / LlamaIndex（未来扩展）

**One-API 是合理 plan B**：UI 更适合非技术人员看。如果你团队有人不爱命令行，可以选这个。

---

## 2. 部署前清单（半天准备）

### 2.1 资源准备

```
□ 1 台火山引擎 ECS 4C8G CentOS/Ubuntu  (PoC 阶段；生产建议 2 台 + ALB)
□ 1 个域名（例 ai-gw.your-company.com）
□ 域名解析到 ECS 公网 IP
□ ECS 安全组开 80 / 443
□ 1 个火山 RDS PostgreSQL 16 (1C2G) — 或先在 ECS 上自部署
□ 1 个火山引擎 KMS 凭据存储已开通
```

### 2.2 拿到所有 API Keys

```
□ OpenAI API key（有出境合规要求，先确认）
□ Anthropic Claude API key
□ DeepSeek 官方 API key（国内直连，推荐）
□ 月之暗面 Kimi API key
□ 火山方舟 API key（已经有就直接用）
□ 智谱 GLM API key
□ 自部署 Qwen / Llama 的 API endpoint + key（如有）
```

### 2.3 决策：单实例还是高可用？

| 阶段 | 配置 |
|---|---|
| Week 1 PoC | **单实例**（1 台 ECS + 自部署 Postgres）|
| Week 2-4 生产 | **双实例 + ALB + 火山 RDS**（高可用）|
| 推广全员后 | 加 Redis 缓存 + 监控告警全套 |

下面先讲单实例 PoC，后面给高可用升级路径。

---

## 3. 第 1 天：单实例 PoC（4 小时）

### 3.1 服务器准备

SSH 到 ECS：

```bash
# 装 Docker + Docker Compose
sudo apt update && sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
# 重新登录生效

# 建工作目录
mkdir -p ~/litellm && cd ~/litellm
```

### 3.2 准备配置文件

#### `~/litellm/.env`（**不要进 git**）

```bash
# 数据库（Postgres）
DATABASE_URL=postgresql://litellm:CHANGE_ME@postgres:5432/litellm

# Master Key（扣子调网关时用，给的就是这个）
LITELLM_MASTER_KEY=sk-master-CHANGE_ME_USE_openssl_rand_hex_32
LITELLM_SALT_KEY=sk-salt-CHANGE_ME_USE_openssl_rand_hex_32

# 模型 API Keys（生产请用 KMS，PoC 暂时明文）
OPENAI_API_KEY=sk-CHANGE_ME
ANTHROPIC_API_KEY=sk-ant-CHANGE_ME
DEEPSEEK_API_KEY=sk-CHANGE_ME
KIMI_API_KEY=sk-CHANGE_ME
GLM_API_KEY=CHANGE_ME
ARK_API_KEY=CHANGE_ME

# 自部署模型
QWEN_BASE_URL=http://internal-qwen.your-company.com/v1
QWEN_API_KEY=CHANGE_ME

# Postgres
POSTGRES_DB=litellm
POSTGRES_USER=litellm
POSTGRES_PASSWORD=CHANGE_ME
```

生成密钥：
```bash
echo "MASTER: $(openssl rand -hex 32)"
echo "SALT:   $(openssl rand -hex 32)"
echo "PG:     $(openssl rand -base64 24)"
```

#### `~/litellm/config.yaml`

```yaml
model_list:
  # ===== 国内模型（敏感数据可用）=====
  - model_name: deepseek-v3                         # ← 扣子里看到的名字
    litellm_params:
      model: deepseek/deepseek-chat                  # LiteLLM 内部映射
      api_key: os.environ/DEEPSEEK_API_KEY
      api_base: https://api.deepseek.com/v1

  - model_name: deepseek-r1
    litellm_params:
      model: deepseek/deepseek-reasoner
      api_key: os.environ/DEEPSEEK_API_KEY
      api_base: https://api.deepseek.com/v1

  - model_name: kimi-128k
    litellm_params:
      model: openai/moonshot-v1-128k                 # OpenAI 协议 + 自定义 base
      api_key: os.environ/KIMI_API_KEY
      api_base: https://api.moonshot.cn/v1

  - model_name: glm-4.7
    litellm_params:
      model: zhipu/glm-4
      api_key: os.environ/GLM_API_KEY

  - model_name: doubao-1.6
    litellm_params:
      model: openai/doubao-1-6-251015
      api_key: os.environ/ARK_API_KEY
      api_base: https://ark.cn-beijing.volces.com/api/v3

  - model_name: qwen-72b-internal                    # 自部署 Qwen
    litellm_params:
      model: openai/qwen-72b
      api_key: os.environ/QWEN_API_KEY
      api_base: os.environ/QWEN_BASE_URL

  # ===== 海外模型（仅通用任务，PII 拦截后才用）=====
  - model_name: gpt-4o
    litellm_params:
      model: openai/gpt-4o
      api_key: os.environ/OPENAI_API_KEY

  - model_name: gpt-4o-mini
    litellm_params:
      model: openai/gpt-4o-mini
      api_key: os.environ/OPENAI_API_KEY

  - model_name: claude-3-5-sonnet
    litellm_params:
      model: anthropic/claude-3-5-sonnet-20240620
      api_key: os.environ/ANTHROPIC_API_KEY

# ===== 路由 + Fallback =====
router_settings:
  routing_strategy: simple-shuffle
  fallbacks:
    - gpt-4o: ["claude-3-5-sonnet", "doubao-1.6"]    # GPT 挂了切 Claude，再挂切豆包
    - claude-3-5-sonnet: ["gpt-4o", "doubao-1.6"]
    - deepseek-v3: ["doubao-1.6"]                      # 国内之间互 fallback
  timeout: 30
  num_retries: 2

# ===== 全局设置 =====
general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/DATABASE_URL
  store_model_in_db: true                              # 模型配置也存 DB，admin UI 可改
  alerting: ["webhook"]                                # 告警走 webhook
  alerting_threshold: 30                               # 30 秒响应阈值

# ===== 安全 =====
litellm_settings:
  drop_params: true                                    # 模型不支持的参数自动丢弃
  set_verbose: false
  json_logs: true                                      # JSON 格式日志（喂 Loki/ES 用）
  cache: true                                          # 启用响应缓存（同 prompt 复用结果）
  request_timeout: 60
  max_budget: 1500                                     # 月预算上限 $1500
  budget_duration: 30d
  success_callback: ["langfuse"]                       # 可选：Langfuse 做 trace
  failure_callback: ["webhook"]                        # 失败推 webhook

# ===== 用户/团队预算（按部门发 Key 用）=====
team_budget:
  - team_id: sales                                     # 销售部
    max_budget: 300                                     # $300/月
    models: ["deepseek-v3", "doubao-1.6", "qwen-72b-internal"]   # 仅国内
  - team_id: marketing
    max_budget: 500
    models: ["deepseek-v3", "doubao-1.6", "gpt-4o", "claude-3-5-sonnet"]   # 可用海外
  - team_id: hr
    max_budget: 100
    models: ["deepseek-v3", "doubao-1.6"]               # 仅国内
  - team_id: legal
    max_budget: 200
    models: ["deepseek-v3", "doubao-1.6", "claude-3-5-sonnet"]
  - team_id: dev_sandbox                                # 工程师沙箱
    max_budget: 100
    models: ["*"]                                       # 全部
```

#### `~/litellm/docker-compose.yml`

```yaml
version: "3.9"

services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "${POSTGRES_USER}"]
      interval: 5s
      retries: 5

  litellm:
    image: ghcr.io/berriai/litellm:main-stable
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
    env_file: .env
    volumes:
      - ./config.yaml:/app/config.yaml:ro
    command:
      - "--config"
      - "/app/config.yaml"
      - "--port"
      - "4000"
      - "--num_workers"
      - "4"
    ports:
      - "127.0.0.1:4000:4000"               # 不直接暴露公网
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:4000/health/liveliness"]
      interval: 10s
      retries: 5

  caddy:
    image: caddy:2-alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data
      - caddy_config:/config

volumes:
  pg_data:
  caddy_data:
  caddy_config:
```

#### `~/litellm/Caddyfile`

```
ai-gw.your-company.com {
    encode gzip
    
    # 限速：每 IP 每秒 100 请求
    rate_limit {
        zone dynamic_ip {
            key {remote_host}
            events 100
            window 1s
        }
    }
    
    reverse_proxy localhost:4000 {
        header_up X-Real-IP {remote_host}
        header_up X-Forwarded-For {remote_host}
        # 流式响应必须 disable buffering
        flush_interval -1
    }
    
    # admin UI 加 IP 白名单（仅公司 VPN 内可访问）
    @admin path /ui /sso/* /admin/*
    handle @admin {
        @blocked not remote_ip 10.0.0.0/8 192.168.0.0/16
        respond @blocked "Forbidden" 403
        reverse_proxy localhost:4000
    }
}
```

> **替换 `your-company.com`** 为你真实域名。
> Caddy 会自动申请 Let's Encrypt 证书，1-3 分钟拿到。

### 3.3 起服务

```bash
cd ~/litellm
docker compose up -d
docker compose ps              # 应看到 3 个服务全 Up + Healthy
docker compose logs -f litellm # 看 LiteLLM 启动日志
```

### 3.4 自检

```bash
# 1. 健康
curl https://ai-gw.your-company.com/health/liveliness
# {"status":"healthy"}

# 2. 列出可用模型
curl -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  https://ai-gw.your-company.com/v1/models
# 应返回 deepseek-v3, kimi-128k, doubao-1.6, gpt-4o, claude-3-5-sonnet 等

# 3. 实测一次国内模型
curl -X POST https://ai-gw.your-company.com/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3",
    "messages": [{"role":"user","content":"你好"}],
    "stream": false
  }'

# 4. 测海外模型
curl -X POST https://ai-gw.your-company.com/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o","messages":[{"role":"user","content":"hello"}]}'

# 5. 测流式（扣子要用）
curl -X POST https://ai-gw.your-company.com/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v3","messages":[{"role":"user","content":"数到 5"}],"stream":true}'
# 应看到 SSE 流：data: {...} 一行行返回
```

### 3.5 PoC 验收清单

```
□ /health 返回 healthy
□ /v1/models 列出所有模型
□ 国内模型能调通（DeepSeek + Doubao）
□ 海外模型能调通（GPT + Claude）
□ 流式响应正常（必须！扣子依赖）
□ admin UI（https://your-domain/ui）能登录
□ 触发一次失败，看到 fallback 自动切换
□ 数据库里能看到调用记录（psql 进去查 spend_logs 表）
```

PoC 通过 → 进入第 2 周生产化。

---

## 4. 第 2 周：生产化（高可用 + 安全加固）

### 4.1 高可用架构

```
              ┌────────────────────┐
              │  火山 ALB 公网 LB   │
              └──────┬─────────────┘
                     │  HTTPS
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌────────┐  ┌────────┐    ┌────────┐
   │ LiteLLM│  │ LiteLLM│    │ Caddy   │
   │ inst 1 │  │ inst 2 │... │（admin） │
   └────┬───┘  └────┬───┘    └────────┘
        │           │
        └─────┬─────┘
              ▼
     ┌──────────────────┐
     │  火山 RDS Postgres│
     │  主备 + 自动备份  │
     └──────────────────┘
              │
              ▼
     ┌──────────────────┐
     │  火山 Redis（缓存）│
     └──────────────────┘
```

### 4.2 把数据库迁移到火山 RDS

1. 火山引擎控制台 → RDS PostgreSQL → 创建实例（**最低 1C2G + 100G SSD**）
2. 创建 db `litellm` + 用户 `litellm`
3. 配置内网安全组（仅 ECS 能访问）
4. 修改 `.env`：`DATABASE_URL=postgresql://litellm:xxx@rds-internal.volces.com:5432/litellm`
5. 重启服务，迁移数据

### 4.3 双实例部署

```yaml
# 在 2 台 ECS 上分别起
# ECS-1, ECS-2: 都跑 docker-compose（去掉 Caddy 段）
# 火山 ALB 配 backend 指向两台 ECS:4000
```

### 4.4 接入火山 KMS（替代明文 API Key）

#### Step 1：在火山 KMS 创建凭据

```bash
# 用火山 CLI 或控制台
volcengine kms create-secret \
  --secret-name litellm/openai \
  --secret-string "sk-xxx"

volcengine kms create-secret \
  --secret-name litellm/anthropic \
  --secret-string "sk-ant-xxx"

# ... 每个模型 key 一个凭据
```

#### Step 2：写一个 KMS sidecar 或启动脚本拉密钥

```bash
# entrypoint.sh
#!/bin/sh
set -e

# 从 KMS 拿密钥并设环境变量
export OPENAI_API_KEY=$(volcengine kms get-secret-value --secret-name litellm/openai --query 'SecretValue' -o text)
export ANTHROPIC_API_KEY=$(volcengine kms get-secret-value --secret-name litellm/anthropic --query 'SecretValue' -o text)
# ...

exec "$@"
```

```yaml
# docker-compose.yml 加
litellm:
  ...
  entrypoint: ["/entrypoint.sh"]
  command: ["litellm", "--config", "/app/config.yaml", "--port", "4000"]
```

> 更优方案：自定义 LiteLLM Docker image 启动时拉密钥，不暴露在容器 env 里。

### 4.5 PII 拦截（保健品合规命脉）

写一个 LiteLLM 自定义 callback，拦截海外模型的 PII：

#### `~/litellm/custom_callbacks/pii_blocker.py`

```python
"""阻止包含 PII 的请求发往海外模型。

放在 ~/litellm/custom_callbacks/pii_blocker.py
config.yaml 加：
  litellm_settings:
    callbacks: custom_callbacks.pii_blocker.PIIBlocker
"""
import re
from typing import Literal
from litellm.integrations.custom_logger import CustomLogger
from litellm.proxy.proxy_server import UserAPIKeyAuth

# 海外模型清单（在这清单里的会被 PII 检测拦截）
OVERSEAS_MODELS = {
    "gpt-4o", "gpt-4o-mini", "gpt-5", "o1", "o1-mini",
    "claude-3-5-sonnet", "claude-3-opus", "claude-3-haiku",
    "gemini-1.5-pro", "gemini-2.0",
}

# PII 正则（中国本地化）
PATTERNS = {
    "phone_cn":   re.compile(r"1[3-9]\d{9}"),                              # 手机
    "id_cn":      re.compile(r"[1-9]\d{5}(?:19|20)\d{2}\d{2}\d{2}\d{3}[\dXx]"),  # 身份证
    "bank_card":  re.compile(r"\d{16,19}"),                                # 银行卡
    "email":      re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"),
}

# 医疗/健康关键词（保健品行业敏感）
MEDICAL_KEYWORDS = [
    "处方", "病历", "就诊", "确诊", "症状", "疾病",
    "病理", "化验", "诊断", "病史", "手术",
]


class PIIBlocker(CustomLogger):
    async def async_pre_call_hook(
        self, user_api_key_dict: UserAPIKeyAuth,
        cache, data, call_type: Literal["completion", "embeddings", "image_generation"]
    ):
        model = data.get("model", "")
        if model not in OVERSEAS_MODELS:
            return data       # 国内模型放行

        # 拼所有 messages 内容
        text = " ".join(
            m.get("content", "") if isinstance(m.get("content"), str)
            else "" for m in data.get("messages", [])
        )

        # PII 正则
        violations = []
        for name, pat in PATTERNS.items():
            if pat.search(text):
                violations.append(name)

        # 医疗关键词
        med_hits = [kw for kw in MEDICAL_KEYWORDS if kw in text]
        if med_hits:
            violations.append(f"medical:{','.join(med_hits)}")

        if violations:
            from fastapi import HTTPException
            raise HTTPException(
                status_code=403,
                detail={
                    "error": "PII detected, overseas model call blocked",
                    "violations": violations,
                    "model": model,
                    "advice": "请使用国内模型（如 deepseek-v3、doubao-1.6）",
                }
            )
        return data

    async def async_log_failure_event(self, kwargs, response_obj,
                                       start_time, end_time):
        # 拦截事件单独写到日志
        pass
```

启用：

```yaml
# config.yaml 加
litellm_settings:
  callbacks: ["custom_callbacks.pii_blocker.PIIBlocker"]
```

挂载 callback 目录：

```yaml
# docker-compose.yml
litellm:
  volumes:
    - ./config.yaml:/app/config.yaml:ro
    - ./custom_callbacks:/app/custom_callbacks:ro
```

测试：

```bash
# 应被拦截（手机号 + 海外模型）
curl -X POST https://ai-gw.your-company.com/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role":"user","content":"客户王总 13800138000 想买产品"}]
  }'
# 期望：HTTP 403 + violations: ["phone_cn"]

# 同样的内容发国内模型应放行
curl -X POST https://ai-gw.your-company.com/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3",
    "messages": [{"role":"user","content":"客户王总 13800138000 想买产品"}]
  }'
# 期望：正常返回
```

### 4.6 按部门发独立 Key（虚拟 Key）

```bash
# 用 admin API 创建按部门 key（master key 操作）
curl -X POST https://ai-gw.your-company.com/key/generate \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "team_id": "sales",
    "key_alias": "sales-coze-prod",
    "models": ["deepseek-v3", "doubao-1.6", "qwen-72b-internal"],
    "max_budget": 300,
    "duration": "30d",
    "rpm_limit": 100,
    "tpm_limit": 100000
  }'
# 返回：{"key": "sk-team-sales-xxx", ...}

# 销售部用这个 key 调，受限：只能用 3 个国内模型，每月 $300，100 RPM
```

把 `sk-team-sales-xxx` 给销售对应的扣子工作空间用。

---

## 5. 接到扣子（终于到了）

### 5.1 在扣子里接 1 个"主网关模型" + N 个"路由别名"

按 `MODELS.md §2.5`：

扣子里**接 5-10 个自定义模型**，每个对应网关里 1 个 `model_name`。每个填：

| 字段 | 值 |
|---|---|
| 模型展示名称 | DeepSeek-V3（公司）|
| 模型唯一标识 | `deepseek-v3` ← LiteLLM 里的 model_name |
| API URL | `https://ai-gw.your-company.com/v1` |
| 鉴权方式 | Authorization |
| 鉴权密钥 | 火山 KMS 凭据：`coze-litellm-team-key`（每部门一份）|
| 模型能力 | 工具调用 ✅ 深度思考 ✅ |
| 上下文长度 | 64000（DeepSeek 真实值）|

**销售空间用销售 key**、**市场空间用市场 key**——这样按部门统计成本和限流。

### 5.2 扣子工作空间授权

按 `MODELS.md §3.5`：

```
销售空间：开放 deepseek-v3, doubao-1.6, qwen-72b-internal
市场空间：开放 全部
HR 空间：开放 deepseek-v3, doubao-1.6
法务空间：开放 deepseek-v3, doubao-1.6, claude-3-5-sonnet
沙箱空间：开放 全部
```

---

## 6. 监控 + 告警

### 6.1 LiteLLM Admin UI（开箱即用）

访问 `https://ai-gw.your-company.com/ui`，用 master key 登录。能看到：

- 所有模型列表 + 实时调用量
- 每个 key/team 消耗（按月、按模型）
- 失败请求 + 错误明细
- 缓存命中率
- 成本仪表盘

### 6.2 接 Prometheus + Grafana

```yaml
# config.yaml
litellm_settings:
  callbacks: ["prometheus", "custom_callbacks.pii_blocker.PIIBlocker"]
```

```yaml
# docker-compose.yml 加
prometheus:
  image: prom/prometheus
  volumes:
    - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
    - prom_data:/prometheus
  ports:
    - "127.0.0.1:9090:9090"

grafana:
  image: grafana/grafana
  ports:
    - "127.0.0.1:3000:3000"
  volumes:
    - grafana_data:/var/lib/grafana
```

```yaml
# prometheus.yml
scrape_configs:
  - job_name: litellm
    static_configs:
      - targets: ['litellm:4000']
    metrics_path: /metrics
```

关键指标：
- `litellm_requests_total{model, team_id, status}` —— 调用次数
- `litellm_request_duration_seconds{model}` —— 延迟
- `litellm_total_tokens{model}` —— Token 消耗
- `litellm_spend_metric{model, team_id}` —— 花费

### 6.3 飞书告警

写一个 LiteLLM webhook callback 推飞书：

#### `~/litellm/custom_callbacks/feishu_alert.py`

```python
import os
import httpx
from litellm.integrations.custom_logger import CustomLogger

WEBHOOK = os.environ["FEISHU_ALERT_WEBHOOK"]


class FeishuAlerter(CustomLogger):
    async def async_log_failure_event(self, kwargs, response_obj,
                                       start_time, end_time):
        model = kwargs.get("model", "?")
        error = str(response_obj)[:200] if response_obj else "unknown"
        team = kwargs.get("metadata", {}).get("team_id", "?")
        async with httpx.AsyncClient(timeout=5) as cli:
            await cli.post(WEBHOOK, json={
                "msg_type": "text",
                "content": {"text": f"⚠️ AI Gateway 失败\n模型: {model}\n团队: {team}\n错误: {error}"}
            })
```

```yaml
# config.yaml
litellm_settings:
  failure_callback: ["custom_callbacks.feishu_alert.FeishuAlerter"]
```

告警规则：
- 单模型 5 分钟错误率 > 10% → 告警
- 单模型 P99 延迟 > 30s → 告警
- 月预算消耗 > 80% → 告警
- 任意 PII 拦截事件 → 告警（重要！合规事件留痕）

---

## 7. 运维 SOP

### 7.1 模型上下线

```bash
# 加新模型（不重启）
# 1. 改 config.yaml
# 2. 重新加载（admin UI → Settings → Reload）
# 或 docker compose restart litellm（5 秒下线 + 重启）

# 下线某模型
# 1. 先在扣子里把模型改成"灰度"，新 bot 用替代模型
# 2. 等老 bot 全切完
# 3. 再从 config.yaml 删
```

### 7.2 密钥轮换（每季度）

```bash
# 1. 生成新 key（OpenAI 控制台）
# 2. 在 KMS 创建新版本
# 3. 重启 litellm，自动从 KMS 拉新 key
# 4. 用 admin UI 撤销旧 key
```

### 7.3 容量规划

| 量级 | 资源 |
|---|---|
| 每天 1 万次调用 | 单实例 4C8G 够 |
| 每天 10 万次调用 | 双实例 + RDS 4C8G + Redis 2C4G |
| 每天 100 万次调用 | 4 实例 + RDS 8C16G + Redis 4C8G + 缓存层 |

监控指标：
- CPU 利用率 > 70% → 加实例
- Postgres 慢查询 > 100ms → 调 schema
- 月 API 调用费 > 预算 80% → 评估

### 7.4 故障演练（建议每月 1 次）

```
□ 演练 1：杀掉 1 个 litellm 实例 → 验证 ALB 切流量到健康实例
□ 演练 2：屏蔽 OpenAI API → 验证 fallback 自动切 Claude
□ 演练 3：填满 Postgres → 验证服务降级到只读
□ 演练 4：发起 PII 攻击 → 验证拦截 + 飞书告警
□ 演练 5：master key 泄露 → 演练 1 小时内换新 + 撤销旧
```

---

## 8. 故障排查速查表

| 现象 | 可能原因 | 处理 |
|---|---|---|
| 扣子调网关 401 | API Key 不对 / KMS 凭据错 | 用 curl 直接验 master key |
| 扣子调网关 502 | LiteLLM 容器挂 / 反代配置错 | docker logs litellm |
| 流式响应不工作 | Caddy buffering | Caddyfile 加 `flush_interval -1` |
| OpenAI 偶发超时 | 国内→海外网络 | LiteLLM 加重试 + fallback |
| 某模型一直失败 | 模型 API 变更 / Key 失效 | admin UI Settings → Test 模型 |
| 数据库连接池满 | 高并发 | 升 RDS 配置 / 加连接池 |
| PII 拦截误报 | 正则太严 | 调整 PATTERNS / 加 allowlist |
| 月底突然大账单 | 某 bot 失控刷 | LiteLLM team_budget + 单次 max_tokens |

---

## 9. 完整部署清单（**工程师 2 按这个干**）

### Week 1（PoC，4-5 天）

```
Day 1
□ 申请 ECS 4C8G + 域名 + 安全组
□ 装 Docker + Docker Compose
□ 写 config.yaml + .env + docker-compose.yml + Caddyfile
□ docker compose up -d
□ 自检：5 个 curl 命令全过

Day 2
□ 接所有模型 API Key 到 .env
□ 测每个模型 chat/completions 通
□ 测流式响应通
□ admin UI 能登录

Day 3
□ 写 PII Blocker callback
□ 测 PII 拦截规则
□ 接到扣子 1 个工作空间（沙箱）
□ 在扣子里测 1 个 bot 通

Day 4-5
□ 文档 + 给团队培训
□ 跑 24 小时，看错误率
```

### Week 2（生产化，5 天）

```
Day 1
□ 申请火山 RDS PostgreSQL
□ 数据迁移到 RDS

Day 2
□ 第 2 台 ECS 起 LiteLLM
□ 配火山 ALB 健康检查

Day 3
□ KMS 接入：所有 API Key 走 KMS
□ 写 entrypoint.sh 启动时拉密钥

Day 4
□ Prometheus + Grafana 接入
□ 飞书告警 callback

Day 5
□ 按部门发虚拟 key
□ 在扣子各部门空间接入
□ 跑故障演练
```

### Week 3-4（推广 + 优化）

```
□ 业务方培训
□ Coze Loop 接入（看哪个模型在哪个 bot 慢/贵）
□ 缓存命中率优化（开启 Redis 缓存）
□ 成本周报机制
□ 季度密钥轮换演练
```

---

## 10. 验收清单（你 review 工程师 2 的工作时用）

```
功能
□ 能调通所有列表里的模型（10+）
□ 流式响应能在扣子里看到逐字输出
□ 触发失败时 fallback 自动切换
□ admin UI 能创建虚拟 key + 设预算

合规
□ PII 拦截规则覆盖手机/身份证/银行卡/医疗关键词
□ 海外模型只对 marketing/legal/training 空间开放
□ 拦截事件能被告警 + 留痕

可靠性
□ 双实例 + ALB
□ 单实例宕机 30 秒内自动切流量
□ Postgres 自动备份每天 1 次
□ 月预算硬上限设了
□ 扣子里有 1-2 个直连官方模型作 fallback（万一网关全挂）

可观测
□ Grafana 看每个模型 / 每个团队的实时调用量
□ 月成本能按部门拆账
□ 有失败告警飞书机器人
□ Coze Loop 看到 trace

成本
□ 月预算上限 ≤ ¥10,000
□ 国内模型占调用量 ≥ 70%
□ 缓存命中率 ≥ 20%
□ 至少 1 个 fallback 真触发过

运维
□ 模型上下线 SOP 文档
□ 密钥轮换 SOP 文档
□ 故障排查速查表（本文 §8）
□ 工程师 1 + 2 + 6 都能独立操作
```

---

## 11. 参考链接

- LiteLLM Proxy 文档：https://docs.litellm.ai/docs/proxy/quick_start
- LiteLLM 配置参考：https://docs.litellm.ai/docs/proxy/configs
- LiteLLM custom callbacks：https://docs.litellm.ai/docs/observability/custom_callback
- LiteLLM 虚拟 key：https://docs.litellm.ai/docs/proxy/virtual_keys
- Caddy 配置：https://caddyserver.com/docs/caddyfile
- 火山 KMS 凭据：火山引擎控制台 → 密钥管理服务

---

## 12. 这套做完，你拿到了什么

```
✅ 一个公网 HTTPS endpoint：https://ai-gw.your-company.com/v1
✅ 10+ 模型可用（豆包/DeepSeek/Kimi/GLM/Qwen/GPT/Claude...）
✅ 加新模型 5 分钟（改 yaml + 重启）
✅ 按部门控成本（月预算硬上限）
✅ 海外模型 PII 自动拦截（合规护栏）
✅ 全链路审计（每次调用都有 trace）
✅ 自动 fallback（OpenAI 挂了切 Claude）
✅ 飞书告警（异常 30 秒内你知道）
✅ 月成本可分摊（每个部门一份账单）
```

接到扣子之后，**你 800 人公司任何 bot 都能用任意模型，且统一管控**。
新模型上线只用 2 步：网关加配置 → 扣子接 1 个自定义模型。
