# AI 中台 — 技术规格说明书（Spec）

> 自进化企业 AI 操作系统 | 保健品行业深度适配 | Skill-Centered Architecture

## 1. 项目概述

### 1.1 定位

以 **Skill 为中心**的企业 AI 中台，不是通用 AI 平台，而是保健品行业深度适配的自进化 AI 操作系统。所有模块（Agent、本体、经验引擎、护栏、渠道）均为 Skill 服务。

### 1.2 核心差异化

| 差异化能力 | 说明 |
|---|---|
| **经验引擎** | 每次 Skill 运行后记录人工修正，自动提取 pattern，Skill 越用越准 |
| **12 维企业本体** | 公司的组织/能力/流程/领域/目标/事件/策略全部结构化，Agent 查询零歧义 |
| **三层合规校验** | 禁词库 + 规则引擎 + LLM 审核，保健品广告法全覆盖 |
| **Skill 中心架构** | 一切能力都是 Skill，护栏/本体/经验自动注入 Skill 生命周期 |

### 1.3 验证状态

- 已通过扣子/Coze 验证 Skill 模式有效性
- 弃用扣子原因：数据安全、海外模型接入、复杂 Skill、信息合规（四堵墙）

## 2. 技术架构

### 2.1 10 层架构

```
Layer 10  接入层     飞书Bot · Web(AG-UI) · API · CLI · MCP Server
Layer 9   Agent层    AgentScope (多Agent编排，仅Tier3多步骤场景)
Layer 8   Harness层  权限门控 · 确定性/概率性混合执行
Layer 7   护栏层     SafetyGuard(注入/PII检测) + 合规引擎(行业)
Layer 6   本体层     12维YAML本体 · OntologyService · 管理API
Layer 5   记忆层     Redis短期会话 + ExperienceEngine长期pattern
Layer 4   Skill层    BaseSkill生命周期 · SkillDispatcher三档路由
Layer 3   网关层     LiteLLM路由 (本地Qwen / 海外Claude / 专用微调)
Layer 2   可观测层   结构化日志 (Langfuse待集成)
Layer 1   基础设施   SQLAlchemy + Redis + Docker Compose
```

### 2.2 Skill 中心原则

**一切请求都经过 BaseSkill.run() 生命周期，无例外。**

```
validate → 输入护栏 → 本体注入 → 经验注入 → execute
→ 输出护栏 → post_execute → 经验记录
```

Agent（AgentScope）不在 Skill 上面，而在 Skill 系统内部，仅负责 Tier 3 多步编排。

### 2.3 三档路由（SkillDispatcher）

```
Tier 1: 触发词匹配   0 token, 0 延迟   "写文案" → compliant-copy
Tier 2: LLM意图分类  少量 token        "上月胶原蛋白卖了多少" → data-query
Tier 3: Agent编排     多步推理          "查数据然后写报告" → 多Skill协作
```

## 3. 技术栈

| 层级 | 选型 | 版本 | 理由 |
|---|---|---|---|
| 语言 | Python | 3.11+ | 异步原生，AI 生态最成熟 |
| Web 框架 | FastAPI | 0.115+ | 异步、自动 OpenAPI 文档 |
| Agent 框架 | AgentScope | 1.0.18 | 中文原生、多 Agent 编排、阿里生态 |
| LLM 路由 | LiteLLM | 1.50+ | 100+ 模型统一接口 |
| 数据模型 | Pydantic | 2.10+ | 类型安全、Settings 管理 |
| ORM | SQLAlchemy | 2.0+ | 异步、成熟稳定 |
| 缓存/记忆 | Redis | 5.2+ | 会话状态、经验缓存 |
| 定时调度 | APScheduler | 3.10+ | 巡逻任务 cron 调度 |
| HTTP 客户端 | httpx | 0.28+ | 异步原生 |
| 认证 | PyJWT | 2.10+ | JWT token 管理 |
| 本体存储 | YAML + Git | - | 运营可读、版本化可追溯 |
| 部署 | Docker Compose | - | api + redis 一键启动 |

### 3.1 模型选型

```
主力本地:  Qwen2.5-72B-Instruct  (Tool Calling 国产最优, vLLM 部署)
辅助本地:  DeepSeek-V3            (MoE, 高并发批处理, 成本最低)
海外复杂:  Claude Sonnet 4.6      (复杂推理, 创意任务)
合规审核:  本地模型               (数据不出境)
```

## 4. 模块规格

### 4.1 Skill 系统 (`app/skills/`)

| 文件 | 职责 |
|---|---|
| `base.py` | BaseSkill 抽象基类，8 步生命周期（含护栏/本体/经验注入） |
| `registry.py` | SkillRegistry，注册/发现/触发词匹配 |
| `dispatcher.py` | SkillDispatcher，三档路由 |
| `models.py` | SkillMeta, SkillInput, SkillOutput, SkillExecutionRecord |
| `builtin/compliant_copy.py` | 合规文案生成 Skill（300+ 禁词，三层校验） |

**SkillMeta 规格:**

```python
id: str              # "compliant-copy"
name: str            # "合规文案生成"
description: str     # 用于意图路由匹配
category: SkillCategory  # content/data/operation/product/patrol
triggers: list[str]  # ["写文案", "生成文案", "合规文案"]
parameters: dict     # JSON Schema
model_preference: ModelPreference  # local/overseas/specialized/auto
```

### 4.2 企业本体 (`app/ontology/`)

**12 维本体模型:**

| 维度 | 文件 | 核心内容 |
|---|---|---|
| 组织 | `organization.yaml` | 部门、角色、权限、汇报线 |
| 能力 | `capabilities.yaml` | 人+Agent 能力、自动化状态、路线图 |
| 流程 | `workflows.yaml` | SOP 步骤、确定性/概率性标记、审批链 |
| 领域 | `domain/health_supplements.yaml` | 3 类产品、4 渠道、合规规则、竞品 |
| 目标 | `goals.yaml` | OKR、KR 巡逻规则 |
| 事件 | `events.yaml` | 触发条件、响应流程、SLA |
| 策略 | `policies.yaml` | 合规、安全分级、成本控制、审批 |
| 数据 | `data_definitions.yaml` | 指标定义、公式、口径、数据源 |
| 工具 | `tools.yaml` | Skill 目录、外部 API |
| 客户 | `customers.yaml` | 用户画像、分群、渠道偏好 |
| 时间 | `schedule.yaml` | 日/周/月节奏、大促时间 |
| 资源 | `resources.yaml` | 预算分配、库存预警规则 |

**查询接口:**

```
OntologyService.query_product(name)     → 成分/功效/禁止宣称
OntologyService.query_metric(name)      → 定义/公式/数据源
OntologyService.query_role(name)        → 权限/工具/汇报线
OntologyService.query_compliance(name)  → 批准功效/禁止宣称/免责声明
OntologyService.query_workflow(name)    → SOP 步骤/审批链
OntologyService.query_capability(name)  → 持有者/自动化率/缺口
```

### 4.3 经验引擎 (`app/experience/`)

**核心循环:**

```
用户输入 → Skill prompt + 经验库 → LLM → AI 输出
              ↑                              │
              │                              ▼
              └── 经验引擎提取差异 ←── 人工修改 pattern
```

**置信度机制:**

```
新 pattern 诞生       → 0.3
第二次验证            → 0.5
5 次以上一致          → 0.8（自动注入 prompt）
被用户否决            → -0.2
confidence < 0.1     → 自动归档
```

**相似度匹配:** 字符 bigram（支持中文，不依赖分词库）

### 4.4 合规引擎 (`app/skills/builtin/compliant_copy.py`)

**三层校验:**

| 层 | 方法 | 特点 |
|---|---|---|
| Layer 1 | 正则禁词扫描 | 300+ 禁词，确定性，0 误判 |
| Layer 2 | 规则引擎 | 断言检查、代言检查、免责声明检查 |
| Layer 3 | LLM 语义审核 | 审核原始文案（非修复后），异常返回不通过 |

**多平台适配:** 小红书（口语化）、抖音（3 秒抓注意力）、公众号（专业深度）、京东（卖点前置）

### 4.5 护栏层 (`app/guardrails/`)

**输入护栏（嵌入 BaseSkill 生命周期）:**

- Prompt 注入检测（7 个中英文模式）
- 不通过直接拦截，不到 execute 步

**输出护栏:**

- PII 检测：身份证、手机号、邮箱、银行卡
- 检测到标记 warning（不阻止，由业务决定）

### 4.6 记忆层 (`app/memory/`)

- **SessionMemory:** Redis-backed 多轮对话记忆，50 条上限，2h TTL
- 无 Redis 时自动 fallback 到内存

### 4.7 认证 (`app/auth/`)

- JWT Bearer token + API Key 双模式
- debug 模式自动跳过（开发便利）
- token 24h 过期

### 4.8 MCP Server (`app/mcp/`)

- 暴露 Skill 和本体查询为 MCP 工具
- 外部 Agent（Claude Code, Gemini CLI, 飞书 Aily）可发现和调用

### 4.9 CLI (`app/cli/`)

```bash
zhongtai health                    # 健康检查
zhongtai skill list                # 列出技能
zhongtai skill exec <id> <msg>     # 执行技能
zhongtai ontology list             # 列出本体维度
zhongtai ontology validate         # 验证本体文件
zhongtai patrol list               # 列出巡逻任务
zhongtai patrol run <id>           # 手动触发巡逻
```

### 4.10 渠道层 (`app/channels/`)

- **飞书 Bot:** Webhook 接收、challenge 验证、消息解析、回复发送
- **Token 管理:** 2 小时过期自动刷新（5 分钟缓冲）
- **消息去重:** 内存 set（生产需改 Redis SETNX）

### 4.11 巡逻系统 (`app/patrol/`)

- APScheduler cron 调度
- 4 级告警：P0 立即通知、P1 紧急、P2 日常、P3 静默
- 飞书主动推送

## 5. API 规格

### 5.1 端点列表

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/health` | 健康检查 |
| POST | `/api/chat` | 主对话接口（三档路由） |
| GET | `/api/skills/` | 列出所有技能 |
| GET | `/api/skills/{id}` | 技能详情 |
| POST | `/api/skills/{id}/execute` | 直接执行技能 |
| GET | `/api/skills/{id}/experience` | 技能经验统计 |
| GET | `/api/ontology/dimensions` | 列出 12 维本体 |
| GET | `/api/ontology/dimension/{name}` | 获取维度全量数据 |
| GET | `/api/ontology/product/{name}` | 查询产品信息 |
| GET | `/api/ontology/metric/{name}` | 查询指标定义 |
| GET | `/api/ontology/role/{name}` | 查询角色权限 |
| GET | `/api/ontology/compliance/{name}` | 查询合规规则 |
| GET | `/api/ontology/workflow/{name}` | 查询业务流程 |
| GET | `/api/ontology/capability/{name}` | 查询能力信息 |
| POST | `/api/ontology/reload` | 热重载本体文件 |
| POST | `/api/experience/corrections` | 提交人工修正 |
| GET | `/api/experience/patterns/{skill_id}` | 查看经验 pattern |
| POST | `/api/experience/patterns/{id}` | 确认/否决 pattern |
| POST | `/api/feishu/webhook` | 飞书事件回调 |
| GET | `/api/patrol/tasks` | 列出巡逻任务 |
| POST | `/api/patrol/tasks/{id}/run` | 手动触发巡逻 |
| GET | `/docs` | Swagger API 文档（自动生成） |

### 5.2 对话接口（核心）

**请求:**

```json
POST /api/chat
{
  "message": "帮我写一篇胶原蛋白的小红书文案",
  "user_id": "zhangsan",
  "session_id": "optional-session-id"
}
```

**响应:**

```json
{
  "content": "生成的文案内容...",
  "skill_id": "compliant-copy",
  "tier": 1,
  "execution_time_ms": 1234
}
```

## 6. 数据模型

### 6.1 ORM 表

| 表名 | 用途 |
|---|---|
| `skill_execution_logs` | Skill 执行日志（input/output/耗时） |
| `experience_patterns` | 经验 pattern（规则/置信度/使用次数） |
| `patrol_logs` | 巡逻执行日志（告警级别/建议动作） |

### 6.2 Redis Keys

```
session:{id}:history   → 对话历史 (List, TTL 2h)
exp:records:{skill_id} → 执行记录 (List)
exp:patterns:{skill_id} → 经验 pattern (Hash)
```

## 7. 部署

### 7.1 Docker Compose

```yaml
services:
  api:    # FastAPI 服务, port 8080
  redis:  # Redis 7, port 6379
```

### 7.2 启动

```bash
# 开发模式
pip install -e ".[dev]" && pip install agentscope pyyaml aiosqlite
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

# Docker 模式
cp .env.example .env  # 编辑配置
docker compose up -d
```

### 7.3 环境变量

见 `.env.example`，核心配置：
- `LOCAL_MODEL_BASE_URL` — 本地 vLLM 地址
- `ANTHROPIC_API_KEY` — Claude API
- `FEISHU_APP_ID/SECRET` — 飞书 Bot
- `REDIS_URL` — Redis 连接
- `DATABASE_URL` — 数据库连接

## 8. 测试

### 8.1 测试矩阵

| 类型 | 数量 | 覆盖 |
|---|---|---|
| 单元测试 | 53 | auth, skills, dispatcher, experience, ontology, guardrails, memory, mcp, compliance |
| API 端点测试 | 36 | 全部 22 个端点 + 边界测试 |
| **合计** | **89** | **全部通过** |

### 8.2 运行测试

```bash
python -m pytest tests/ -v    # 单元测试
ruff check app/ tests/        # Lint
```

## 9. 项目统计

```
源代码:     58 个 Python 文件, 4218 行
测试代码:    9 个测试文件, 632 行
本体 YAML:  12 个文件, 458 行
总文件数:    87
总代码行:    6000+
Git 提交:    7
```

## 10. 协议支持路线

| 协议 | 状态 | 优先级 |
|---|---|---|
| MCP | 骨架已实现 | P0 — 5800+ 工具生态互通 |
| AG-UI | 待实现 | P1 — Web 工作台流式交互 |
| A2A | 待实现 | P2 — 跨 Agent 协作 |
| A2UI | 跟踪 | P3 — 声明式 UI 生成 |

## 11. 后续演进

```
Phase 1 (当前): 单 Agent + 多 Skill + 12 维本体
Phase 2:        接通业务数据 + 更多 Skill (数据查询/报表)
Phase 3:        多角色 Agent + SOP 驱动 + Graphiti 时序记忆
Phase 4:        生产加固 (SSO/RBAC/Langfuse/Portkey/Celery)
Phase 5:        公司数字孪生 (组织本体驱动 Agent 自动生成)
```
