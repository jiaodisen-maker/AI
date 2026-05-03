# AI Platform - 治理层

保健品企业 AI 中台的**治理层**，专为已有 20+ 个 Agent 的企业设计。

## 核心设计

```
┌────────────────────────────────────────────────┐
│  飞书 Bot (lark-bot)                            │
│  · 用户消息接收                                  │
│  · 用户级隔离（session_id = user_id）            │
└────────────────┬───────────────────────────────┘
                 │ HTTP
┌────────────────▼───────────────────────────────┐
│  Agent Router (agent-router)                    │
│  · 6 个稳定 Port（业务代码 0 框架依赖）           │
│  · LocalAgentRegistry（Redis 存元数据）          │
│  · Invoker 路由（Coze/Dify/LangGraph/HTTP）     │
└────────────────┬───────────────────────────────┘
                 │ 跨框架调用
   ┌─────────────┼──────────────┬─────────────┐
   ▼             ▼              ▼             ▼
 Coze         Dify          LangGraph     自建 Agent
 (5 个)       (8 个)         (新建 3-5)    (4 个)
```

## 快速开始

### 1. 启动服务（5 分钟）

```bash
# 复制配置（飞书凭据可暂时空着）
cp .env.example .env

# 启动所有服务
docker compose up -d

# 检查健康
curl http://localhost:8000/healthz
curl http://localhost:8001/healthz
```

### 2. 注册示例 Agent

```bash
# 使用宿主 Python 跑（也可在容器内）
pip install httpx
python scripts/seed_agents.py
```

输出：
```
✓ Registered: compliant-copywriter
✓ Registered: data-analyst
✓ Registered: compliance-reviewer

总计 3 个 Agent 已注册：
  - compliant-copywriter           [mock] [production]
  - data-analyst                   [mock] [production]
  - compliance-reviewer            [mock] [beta]
```

### 3. 测试发现 + 调用

```bash
# 列出所有 Agent
curl http://localhost:8000/agents | jq

# 语义检索
curl -X POST http://localhost:8000/agents/discover \
  -H 'Content-Type: application/json' \
  -d '{"query": "帮我写小红书文案"}' | jq

# 直接调用
curl -X POST http://localhost:8000/agents/invoke \
  -H 'Content-Type: application/json' \
  -d '{
    "agent_name": "compliant-copywriter",
    "input": "写一篇阿胶糕小红书文案",
    "session_id": "user_001",
    "user_id": "user_001"
  }' | jq

# 查看统计
curl http://localhost:8000/agents/compliant-copywriter/stats | jq
```

### 4. 模拟飞书消息（开发）

```bash
# 不用飞书凭据，直接通过 debug 接口测端到端
curl -X POST http://localhost:8001/debug/message \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "alice", "text": "帮我写文案"}' | jq
```

## 项目结构

```
.
├── pyproject.toml
├── docker-compose.yml
├── .env.example
├── services/
│   ├── agent-router/                # 治理层核心
│   │   ├── Dockerfile
│   │   └── app/
│   │       ├── main.py              # FastAPI 入口
│   │       └── adapters/            # 框架隔离层（核心资产）
│   │           ├── types.py         # 数据类（永不变）
│   │           ├── ports.py         # 6 个 Protocol（永不变）
│   │           ├── factory.py       # 工厂模式
│   │           └── impls/           # 各框架实现
│   │               ├── invokers.py        # Coze/Dify/LangGraph 调用器
│   │               ├── local_registry.py  # Redis 注册表
│   │               └── mock_adapter.py    # 测试用
│   └── lark-bot/                    # 飞书入口
│       ├── Dockerfile
│       └── app/main.py
├── scripts/
│   └── seed_agents.py               # 注册示例 Agent
└── tests/
```

## 6 个 Port 架构

业务代码只依赖这 6 个抽象，永不依赖任何框架：

| Port | 用途 |
|---|---|
| `LLMPort` | LLM 文本生成（屏蔽 AgentScope/LangGraph 差异） |
| `SkillPort` | Skill 加载和路由（对齐 Anthropic SKILL.md 标准） |
| `SessionPort` | 用户级会话隔离（关键：解决多用户隐私） |
| `ToolPort` | 工具执行（流式，对齐 2.0 ToolChunk） |
| `MemoryPort` | 经验/知识检索（业务护城河） |
| `AgentRegistryPort` | **跨框架 Agent 注册、发现、调用**（治理层核心） |

## 切换框架（架构主权）

通过环境变量切换底层框架，业务代码 0 改动：

```bash
# 当前默认：Mock（测试用）
AGENT_FRAMEWORK=mock

# 切到 AgentScope 1.x
AGENT_FRAMEWORK=agentscope_1x

# 切到 LangGraph
AGENT_FRAMEWORK=langgraph

# 未来切到 AgentScope 2.0
AGENT_FRAMEWORK=agentscope_2x
```

## 4 周路线图

- **Week 1（当前）**：Registry + Lark Bot + Mock 跑通端到端 ✅
- **Week 2**：迁移现有 20+ Agent 进 Registry
- **Week 3**：去重 + SKILL.md 标准化 + 经验引擎 v1
- **Week 4**：用 LangGraph 重写第 1 个核心 Agent + 灰度上线

## 设计原则

1. **业务代码 0 框架依赖** — 业务层只 import `adapters/types.py` 和 `adapters/ports.py`
2. **SKILL.md 标准** — 对齐 Anthropic 开放标准，跨框架可移植
3. **用户级隔离** — `session_id = user_id`，避免多人 Team 共享的隐私泄露
4. **影子模式预留** — 新框架并行验证再切换
5. **可观测优先** — 每次调用都记录统计

## 自检脚本

确保业务代码没有意外引入框架依赖：

```bash
# 应该输出空（业务层只能 import adapters）
grep -rn "import agentscope\|import langgraph\|import langchain" \
  services/agent-router/app/ \
  --exclude-dir=adapters
```
