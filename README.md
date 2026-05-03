# AI Platform - 治理层 v0.2

保健品企业 AI 中台的**治理层**，专为已有 20+ 个 Agent 的企业设计。

> **核心理念**：不重写现有 Agent，加一层治理让它们被统一管理。

---

## 完整架构

```
┌─────────────────────────────────────────────────────┐
│  飞书 Bot (lark-bot)                                 │
│  · 加密事件解密 + 签名验证                             │
│  · Slash 命令 (/clear /history /agents /help)        │
│  · 用户级私聊回复（绝不广播）                          │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP
┌──────────────────────▼──────────────────────────────┐
│  Agent Router (agent-router)                         │
│                                                      │
│  ┌────────────────────────────────────────────────┐│
│  │ 中间件链（洋葱模型）                              ││
│  │ Audit → PII → Compliance → RateLimit → Experience││
│  └────────────────────────────────────────────────┘│
│                       │                              │
│  ┌────────────────────▼──────────────────────────┐ │
│  │ 6 个稳定 Port（业务代码 0 框架依赖）            │ │
│  │ ├─ AgentRegistryPort  (注册/发现/调用)          │ │
│  │ ├─ LLMPort            (生成/流式)              │ │
│  │ ├─ SessionPort        (用户级隔离)             │ │
│  │ ├─ MemoryPort         (经验引擎)               │ │
│  │ ├─ SkillPort          (SKILL.md 加载)          │ │
│  │ └─ ToolPort           (工具执行)               │ │
│  └─────────────────────────────────────────────────┘│
└──────────────────────┬──────────────────────────────┘
                       │ 跨框架调用
   ┌──────────┬────────┼────────┬───────────┬─────────┐
   ▼          ▼        ▼        ▼           ▼         ▼
 Coze       Dify    扣子   LangGraph  AgentScope  自建HTTP
                                       1.x/2.0
                       │
                       ▼
   ┌─────────────────────────────────────────────────┐
   │  数据层：3 个 Redis 物理隔离                      │
   │  · agent-registry-redis    Agent 元数据         │
   │  · session-redis           用户会话              │
   │  · memory-redis            经验引擎              │
   └─────────────────────────────────────────────────┘
```

---

## 5 分钟快速开始

```bash
# 1. 复制配置
cp .env.example .env

# 2. 启动整个栈
docker compose up -d

# 3. 检查健康
curl http://localhost:8000/healthz
curl http://localhost:8001/healthz

# 4. 注册示例 Agent
python scripts/seed_agents.py

# 5. 模拟飞书消息（不需要真实飞书凭据）
curl -X POST http://localhost:8001/debug/message \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "alice", "text": "帮我写文案"}'
```

---

## 把现有 20+ Agent 接入

```bash
# 1. 编辑 scripts/agents.example.yaml，按格式填你公司的 Agent
cp scripts/agents.example.yaml scripts/agents.yaml
vim scripts/agents.yaml

# 2. 校验
python scripts/bulk_import_agents.py scripts/agents.yaml --dry-run

# 3. 实际导入
python scripts/bulk_import_agents.py scripts/agents.yaml

# 4. 生成库存报告
python scripts/inventory_report.py --format markdown > inventory.md
```

支持的 framework：`coze` / `dify` / `langgraph` / `agentscope_1x` / `custom_http` / `mock`

---

## API 总览（24 个端点）

### Agent 管理
- `POST /agents` 注册
- `GET /agents` 列表（按 framework/team/maturity 过滤）
- `GET /agents/{name}` 详情
- `PUT /agents/{name}` 更新
- `DELETE /agents/{name}` 注销
- `POST /agents/discover` 语义检索

### 调用
- `POST /agents/invoke` 统一调用（含完整中间件链）
- `POST /agents/stream` 流式调用

### Session
- `GET /sessions/{id}` 会话状态
- `GET /sessions/{id}/history` 消息历史
- `DELETE /sessions/{id}` 清空

### Memory（经验引擎）
- `POST /memory/patterns` 存储 pattern
- `POST /memory/search` 检索

### Skill
- `GET /skills` 列出 SKILL.md
- `GET /skills/{name}` 单个详情

### 统计 + 健康
- `GET /agents/{name}/stats` / `GET /stats`
- `GET /healthz` / `GET /readyz` / `GET /livez`

---

## 6 Port 框架隔离设计

业务代码**只 import**：
```python
from app.adapters.types import Message, Skill, AgentSpec, ...
from app.adapters.ports import LLMPort, SkillPort, AgentRegistryPort, ...
from app.adapters.factory import AdapterFactory
```

**永不 import**：`agentscope`, `langchain`, `langgraph`, `claude_sdk`

切换框架只改一行 env：
```bash
AGENT_FRAMEWORK=mock           # 测试
AGENT_FRAMEWORK=agentscope_1x  # 当下
AGENT_FRAMEWORK=langgraph      # 替代
AGENT_FRAMEWORK=agentscope_2x  # 未来
```

### 自检脚本
```bash
# 业务代码不能直接 import 框架（应输出空）
grep -rn "import agentscope\|import langgraph\|import langchain" \
  services/agent-router/app/ services/lark-bot/app/ \
  --include="*.py" | grep -v "/impls/" | grep -v "types.py"
```

---

## 中间件链（5 个内置）

按 use() 顺序洋葱式执行，可拦截、可修改：

| 中间件 | 作用 | 配置 |
|---|---|---|
| `audit_middleware` | 审计日志 | 总开 |
| `pii_middleware` | PII 脱敏（手机/邮箱/身份证/银行卡） | `ENABLE_PII` |
| `compliance_middleware` | 禁词扫描 | `ENABLE_COMPLIANCE` |
| `rate_limit_middleware` | 限流（用户/分钟+用户/天） | `RATE_LIMIT_PER_MIN/DAY` |
| `experience_middleware` | 经验注入 + 自动记录 | `ENABLE_EXPERIENCE` |

中间件全部框架无关，不依赖 AgentScope/LangGraph。

---

## 用户级隔离（解决多人共享 Agent 的隐私问题）

```
飞书用户 A          飞书用户 B
    │                  │
    ▼                  ▼
session_id=A       session_id=B   ← 物理隔离
    │                  │
    ▼                  ▼
独立会话历史       独立会话历史
独立中间件元数据   独立中间件元数据
独立限流计数      独立限流计数
```

A 和 B 的对话**互不可见**，对应前面分析里 HiClaw "多 Human 共享 Team" 的隐私 bug。

---

## 经验引擎 v1

每次成功调用自动记录为 pattern：
```python
{
  "skill_name": "compliant-copy",
  "input": "阿胶糕小红书文案",
  "output": "（经过审核的文案）",
  "feedback": {"rating": 5},  # 后续可加人工反馈
  "timestamp": 1714780800,
}
```

下次相似输入会自动检索 top-k 注入到 prompt（Jaccard 相似度 + 反馈加权）。

生产可换 embedding + 向量检索（Milvus/Qdrant）。

---

## 项目结构

```
.
├── pyproject.toml
├── docker-compose.yml
├── .env.example
├── .gitignore
│
├── services/
│   ├── agent-router/                # 治理层（24 个端点）
│   │   └── app/
│   │       ├── main.py
│   │       └── adapters/
│   │           ├── types.py         # 数据类（永不变）
│   │           ├── ports.py         # 6 Protocol（永不变）
│   │           ├── factory.py       # 工厂模式
│   │           ├── middleware.py    # 洋葱中间件链
│   │           ├── resilience.py    # retry/timeout/circuit-breaker
│   │           └── impls/
│   │               ├── invokers.py        # Coze/Dify/LangGraph/AS1x/HTTP/Mock
│   │               ├── local_registry.py  # Redis Agent 注册
│   │               ├── redis_session.py   # 生产 Session
│   │               ├── redis_memory.py    # 生产经验引擎
│   │               ├── skill_loader.py    # SKILL.md 加载器
│   │               ├── agentscope_1x.py   # AgentScope 1.x LLM
│   │               ├── langgraph_adapter.py # LangGraph LLM
│   │               └── mock_adapter.py    # 测试用
│   │
│   └── lark-bot/                    # 飞书入口（8 个端点）
│       └── app/
│           ├── main.py              # 事件订阅 + slash 命令
│           └── lark_security.py     # 签名验证 + 加密事件解密
│
├── scripts/
│   ├── seed_agents.py               # 注册 3 个示例
│   ├── bulk_import_agents.py        # 批量导入（YAML）
│   ├── agents.example.yaml          # 5 种 framework 示例
│   └── inventory_report.py          # 库存盘点（重复检测/Top成本）
│
└── tests/                           # 43 个测试，含用户隔离验证
```

---

## 4 周路线图

- **Week 1** ✅ 6 Port + LocalAgentRegistry + Lark Bot + Mock 端到端
- **Week 2** ✅ Redis Session/Memory + 5 中间件 + Skill Loader + 真 AgentScope/LangGraph adapter + 飞书签名/加密
- **Week 3** 把现有 20+ Agent 用 `bulk_import_agents.py` 导入 + 库存盘点 + 去重
- **Week 4** 用 LangGraph 重写第 1 个核心 Agent + 灰度上线

剩下的工作（可在前端/配置完成）：
- 添加新 Agent → 调 `POST /agents` 或填 yaml
- 修改 Agent 元数据 → 调 `PUT /agents/{name}`
- 调整中间件 → 改 env 变量
- 切换框架 → 改 `AGENT_FRAMEWORK`
- 配置权限 → 改 Agent 的 `allowed_users/teams`
- 调禁词 → 改环境变量或 yaml

---

## 测试

```bash
pip install pytest pytest-asyncio fastapi pydantic httpx pyyaml cryptography
python -m pytest tests/ -v
# 43 passed in 0.5s
```

包括：
- 类型稳定性测试
- Mock adapter 测试（含**用户隔离**验证）
- 中间件链测试（PII / 合规 / 洋葱顺序）
- SKILL.md 加载器测试（含 mtime 自动刷新）
- 弹性工具测试（retry / timeout / 熔断）
- 飞书安全测试（签名 / AES 加解密）
- 工厂模式测试

---

## 设计原则

1. **业务代码 0 框架依赖** — 业务层只 import `adapters/types.py` 和 `adapters/ports.py`
2. **SKILL.md 标准** — 对齐 Anthropic 开放标准，跨框架可移植
3. **用户级隔离** — `session_id = user_id`，物理隔离三个 Redis
4. **配置驱动切换** — 改一行 env 切换框架/中间件/数据源
5. **可观测优先** — 每次调用都记录统计 + 中间件元数据
6. **影子模式预留** — Adapter 层支持新框架并行验证

---

## 资源占用（参考）

100 用户场景，全栈：
- 5 个服务 Pod
- ~3 vCPU / ~6Gi 内存
- 月成本约 ¥1,500（阿里云）

对比：HiClaw 全栈同场景需 308 Pod / 32 vCPU / 80Gi，月成本 ¥15,000+。
