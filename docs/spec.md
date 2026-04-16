# AI 中台 — 完整技术规格说明书 (Spec v0.5.0)

> 自进化企业 AI 操作系统 · 保健品行业深度适配 · Skill-Centered Architecture
>
> 11 个 Phase 全量交付 · 174 测试通过 · 11,000+ 行代码 · 99 个 Python 文件 · 17 次 git commit

---

## 目录

1. [项目概述](#1-项目概述)
2. [11 层架构总览](#2-11-层架构总览)
3. [11 Phase 路线图](#3-11-phase-路线图)
4. [模块详细规格](#4-模块详细规格)
5. [Skill 系统](#5-skill-系统)
6. [12 维企业本体](#6-12-维企业本体)
7. [Brain & Agent 系统](#7-brain--agent-系统)
8. [API 端点完整列表](#8-api-端点完整列表)
9. [前端规格](#9-前端规格)
10. [测试体系](#10-测试体系)
11. [部署架构](#11-部署架构)
12. [开发指南](#12-开发指南)

---

## 1. 项目概述

### 1.1 定位

**Skill 中心架构的企业 AI 中台**，为保健品行业深度适配。

不是通用 AI 平台，核心差异在于：
- 把行业经验沉淀为可执行 Skill
- 让 Agent 调用 Skill 完成任务
- 用本体提供领域语义
- 用经验引擎让 Skill 越用越准

### 1.2 核心差异化

| 差异化能力 | 说明 |
|---|---|
| **Skill 中心** | Skill 是价值核心，所有模块为 Skill 服务 |
| **经验引擎** | 人工修正自动学习为可复用 pattern，置信度自适应 |
| **12 维企业本体** | 组织/能力/流程/领域/目标/事件/策略/数据/工具/客户/时间/资源 |
| **三层合规** | 禁词正则 + 规则引擎 + LLM 语义审核 |
| **多 Agent 编排** | AgentScope MsgHub + SequentialPipeline + 角色 Agent |
| **自进化能力** | AutoML + RLHF + 自愈检测 + 元学习 |
| **私有部署** | 数据安全、海外模型接入、复杂 Skill、信息合规 |

### 1.3 技术栈

| 层级 | 选型 | 版本 |
|---|---|---|
| 语言 | Python | 3.11+ |
| Web 框架 | FastAPI | 0.135+ |
| Agent 框架 | AgentScope | 1.0.18 |
| Deep Agent | LangChain + LangGraph | 1.2 + 1.1 |
| LLM 路由 | LiteLLM Router | 1.83 |
| 数据模型 | Pydantic | 2.12 |
| ORM | SQLAlchemy (async) | 2.0 |
| 缓存/会话 | Redis | 7 |
| 业务数据库 | MySQL | 8.0 |
| 知识图谱 | Neo4j Community | 5 |
| 可观测 | Langfuse | 2.x |
| 任务队列 | Celery + Redis broker | 5.x |
| 前端 | Alpine.js + Tailwind CSS | CDN |
| 部署 | Docker Compose | v2.20+ |
| 认证 | PyJWT | 2.12 |


---

## 2. 11 层架构总览

```
Layer 11  接入层      飞书Bot · Web(Claude Code 风格 SPA) · API · CLI · MCP · A2A
Layer 10  Agent层     AgentScope (ReActAgent + 角色 Agent + MsgHub + Pipeline)
Layer 9   Deep层      LangChain Deep Agent (开放式深度推理, /deep 命令)
Layer 8   Harness层   护栏门控 · 上下文管理 · 确定性/概率混合执行
Layer 7   护栏层      SafetyGuard (Prompt 注入 + PII) + Cost Control + 循环检测
Layer 6   本体层      12 维 YAML 本体 + 查询服务 + MCP 暴露
Layer 5   记忆层      SessionMemory(Redis) + ExperienceEngine + ExperienceGraph
Layer 4   Skill层     BaseSkill 8 步生命周期 · Dispatcher · 6 内置 + 1 多模态
Layer 3   网关层      LiteLLM Router · Cost Control · 重试/Fallback
Layer 2   可观测层    Langfuse + 审计中间件 + 结构化日志
Layer 1   基础设施    MySQL + Redis + Neo4j + Langfuse-DB + Celery + Docker
```

### 关键设计原则

**Skill 中心**：一切请求都经过 BaseSkill.run() 生命周期，没有任何旁路。

**Agent 不替代 Skill**：Agent 决定调哪个 Skill，Skill 才是真正的执行者和价值中心。Agent 来来去去，Skill 的经验沉淀下来不会丢。

**确定性 + 概率性混合**：合规检查是确定性的（禁词正则、规则引擎），文案生成是概率性的（LLM）。两者通过 Skill 生命周期串起来。

**本体驱动一切**：12 维企业本体定义了组织、能力、流程、领域知识、目标、事件、策略、数据、工具、客户、时间、资源。所有 Agent 和 Skill 从本体获取上下文。

---

## 3. 11 Phase 路线图

| Phase | 主题 | 核心交付 |
|---|---|---|
| **Phase 0** | 原型骨架 | Skill系统 + LLM路由 + 经验引擎 + 巡逻系统 |
| **Phase 1** | AgentScope替换 | Brain层重构 + Skill中心架构 + 12维本体 |
| **Phase 2** | 接通业务 | 6 个内置 Skill + Docker 全栈 + 数据库 |
| **Phase 3** | 多角色 Agent | AgentFactory + WorkflowEngine + MsgHub |
| **Phase 4** | 生产加固 | SSO + RBAC + Langfuse + 预算 + Celery + 审计 |
| **Phase 5** | 数字孪生 | 插件发现 + YAMLSkill + A2A + 经验图谱 |
| **Phase 6** | 自服务生态 | SkillFactory + EvalSet + A/B 测试 |
| **Phase 7** | 智能涌现 | MetaAnalyzer + SkillOptimizer + HealingDetector |
| **Phase 8** | 多模态扩展 | 图像/音频/视频/文档 + Visual QA Skill |
| **Phase 9** | 联邦协作 | 多租户 + 跨组织 MCP 联邦 |
| **Phase 10** | 自主进化 | AutoML + RLHF + 自我改进循环 |

---

## 4. 模块详细规格

`app/` 下每个子模块的职责、关键类、入口函数。按依赖顺序（基础设施 → 核心 → 接入）。

### 4.1 `app/config.py` — 全局配置

`Settings` 继承 `pydantic_settings.BaseSettings`，从 `.env` 读取。单例 `settings` 被全项目 import。

| 字段组 | 关键字段 |
|---|---|
| 应用 | `app_name` / `app_env` / `debug` / `secret_key` |
| 本地 LLM | `local_model_base_url` / `local_model_name` / `local_model_api_key` |
| 海外 LLM | `anthropic_api_key` / `openai_api_key` / `model_routing_strategy` |
| 存储 | `database_url` / `redis_url` / `milvus_host` / `clickhouse_host` |
| 飞书 | `feishu_app_id` / `feishu_app_secret` / `feishu_verification_token` |
| 巡逻 | `patrol_enabled` / `patrol_timezone` / `use_celery` |
| 可观测 | `langfuse_public_key` / `langfuse_secret_key` / `langfuse_host` |
| 成本控制 | `per_task_max_tokens` / `per_task_max_calls` / `per_user_daily_tokens` |

### 4.2 `app/main.py` — 应用装配入口

- `AppState` dataclass 持有所有运行期组件实例
- `lifespan(app)` 在 FastAPI 启动时按顺序装配：Data → Experience → LLM → Ontology → Memory → Skill Runtime → Skills → Brain → RoleAgents → Workflow → Dispatcher → MCP → Channels → Patrol
- `create_app()` 构造 FastAPI 实例，挂载 `CORSMiddleware` + `AuditMiddleware`，`include_router` 八个 API 路由（`health` / `auth` / `chat` / `skills` / `experience` / `feishu` / `patrol` / `ontology`），并挂载 `app/static/` 作为前端
- `get_app_state()` 供各路由取全局状态

> 注：`app/api/a2a.py` 已实现 Agent Card + task 生命周期，但当前未在 `create_app()` 中 `include_router`，属于已写好但未启用。

### 4.3 `app/llm/` — LLM 网关层

| 文件 | 职责 |
|---|---|
| `router.py` | `ModelRouter` 封装 LiteLLM 内置 `Router`，本地/海外两组 `model_name`，自动 retry/fallback/cooldown |
| `models.py` | `ChatRequest` / `ChatResponse` / `ChatMessage` / `Role` Pydantic 数据模型 |
| `cost_control.py` | `CostController` + `BudgetConfig` + `TaskBudget`：per-task/per-user token & call 上限 + 循环检测（滑动窗口） |

### 4.4 `app/skills/` — Skill 层（架构中心）

| 文件 | 职责 |
|---|---|
| `base.py` | `BaseSkill` 抽象基类 + 8 步 `run()` 生命周期 + `configure_skill_runtime()` 注入全局 guardrail/ontology/experience |
| `models.py` | `SkillMeta` / `SkillInput` / `SkillOutput` / `SkillExecutionRecord` / `SkillCategory` / `ModelPreference` |
| `registry.py` | `SkillRegistry`：按 id 注册、trigger 词反查、按 category 过滤 |
| `dispatcher.py` | `SkillDispatcher`：Fast track + Agent loop + `/deep` + `/workflow` + `/discuss` 路由 |
| `factory.py` | `SkillFactory`：`from_template` / `from_yaml` / `from_examples` 三种创建方式 + `SKILL_TEMPLATES` 三个内置模板 |
| `yaml_skill.py` | `YAMLSkill`：用 YAML 定义 Skill 不写 Python，支持 `prompt_template` / `ontology_needs` / `model_preference` |
| `discovery.py` | `PluginDiscovery`：扫描 `builtin/` / `plugins/` / `~/.zhongtai/skills/` / `yaml_skills/` 四个来源 |
| `builtin/` | 6 个内置 Skill：`CompliantCopySkill` / `DataQuerySkill` / `ReportGenSkill` / `WebSearchSkill` / `CompetitorWatchSkill` / `ContentAdaptSkill`，外加 `VisualQASkill`（多模态） |

详见 [§5 Skill 系统](#5-skill-系统)。

### 4.5 `app/brain/` — Brain 层

| 文件 | 关键类 |
|---|---|
| `agent.py` | `AgentFactory`（创建 coordinator / role agent / MsgHub / SequentialPipeline / FanoutPipeline）+ `BrainAgent`（`chat` / `multi_agent_discuss` / `sequential_workflow`）|
| `workflow.py` | `WorkflowEngine`：从 `workflows.yaml` 读 SOP，逐步执行（deterministic / probabilistic / human_approval），支持条件与门控 |
| `deep.py` | `run_deep_agent()`：用 LangGraph `create_react_agent` + LangChain `StructuredTool` 包裹 Skills |
| `tools.py` | `register_skills_as_tools()`：把 Skill 转成 AgentScope `Toolkit` 工具函数，注入 experience prompt |

详见 [§7 Brain & Agent 系统](#7-brain--agent-系统)。

### 4.6 `app/ontology/` — 12 维企业本体

| 文件 | 职责 |
|---|---|
| `loader.py` | `OntologyLoader`：从 `definitions/` 递归加载所有 `*.yaml`，按文件 stem 作为维度名缓存，支持 `reload()` 热重载 |
| `service.py` | `OntologyService`：`query_product` / `query_metric` / `query_role` / `query_compliance` / `query_workflow` / `query_capability` / `list_dimensions` |
| `models.py` | Pydantic 模型：`RoleDefinition` / `CapabilityDefinition` / `WorkflowStep` / `MetricDefinition` / `ProductInfo` / `BusinessEvent` |
| `mcp_server.py` | `expose_ontology_via_mcp()`：把 6 个查询方法注册为 MCP 工具 |
| `definitions/*.yaml` | 11 个顶层维度 YAML + `definitions/domain/` 领域维度 |

详见 [§6 12 维企业本体](#6-12-维企业本体)。

### 4.7 `app/experience/` — 经验引擎

| 文件 | 关键类 | 职责 |
|---|---|---|
| `engine.py` | `ExperienceEngine` | 核心差异化：`record_execution` / `learn_from_correction` / `get_experience_prompt` / 置信度管理 |
| `store.py` | `ExperienceStore` | 持久化层：内存 + Redis + SQLAlchemy 三态，capped 10K 防泄漏 |
| `models.py` | `ExperienceRecord` / `ExperiencePattern` | 单次执行记录 + 被学习出的规则 |
| `graph.py` | `ExperienceGraph` / `ExperienceNode` / `ExperienceEdge` | 时序经验图谱（Phase 5 交付） |

### 4.8 `app/memory/` — 记忆层

- `session.py` — `SessionMemory`：Redis backed 多轮对话记忆，50 条上限，2h TTL，Redis 不可用时降级到 in-memory
- `experience.py` — 经验引擎到记忆层的适配器

### 4.9 `app/guardrails/` — 护栏层

- `safety.py` — `SafetyGuard` + `GuardResult`
  - `check_input()`：7 条 prompt 注入正则（中英文），如 "ignore all previous instructions" / "你现在是"
  - `check_output()`：4 类 PII 模式（身份证、手机号、邮箱、银行卡）

### 4.10 `app/auth/` — 认证授权层（Phase 4）

| 文件 | 关键类/函数 | 职责 |
|---|---|---|
| `jwt.py` | `create_token()` / `decode_token()` | PyJWT 签发/校验，含过期处理 |
| `middleware.py` | `require_auth()` | FastAPI 依赖：Bearer JWT 或 `X-API-Key` 头，`debug=true` 时 bypass |
| `feishu_sso.py` | `FeishuSSO` | OAuth2 授权码流 → 换飞书 access token → 签发本地 JWT |
| `rbac.py` | `RBACEngine` | 读 `organization.yaml` 的 role → tools 映射做 Skill 权限校验 |
| `audit.py` | `AuditMiddleware` | 记录每一次 API 请求（user / path / method / status / duration） |

### 4.11 `app/api/` — HTTP 接口层

9 个路由文件对应 9 个模块；详见 [§8 API 端点完整列表](#8-api-端点完整列表)。

### 4.12 `app/channels/` — 渠道接入层

- `feishu.py` — `FeishuBot`：webhook 验签、主动发消息、token 2h 刷新
- `message.py` — `MessageRouter`：把渠道原始消息转成 `SkillDispatcher.dispatch()` 调用，Redis SETNX 去重 5min TTL
- `models.py` — 消息 Pydantic 模型

### 4.13 `app/patrol/` — 巡逻系统

- `base.py` — `BasePatrolTask`：巡逻任务抽象，`config()` 返回 cron 表达式
- `scheduler.py` — `PatrolScheduler`：APScheduler `AsyncIOScheduler` + `CronTrigger.from_crontab`
- `celery_app.py` / `tasks.py` — Celery 版本（`settings.use_celery=true` 时启用）
- `notifier.py` — `PatrolNotifier`：通过 `FeishuBot` 主动推送告警卡片
- `models.py` — 告警级别（P0–P3）、巡逻任务配置模型

### 4.14 `app/mcp/` — MCP 服务器

- `server.py` — `MCPServerManager`：`register_skill_tool` / `register_ontology_tools` / `list_tools` / `call_tool`
- `skill_tools.py` — 把 Skill 注册为 MCP 工具的适配函数
- `ontology_tools.py` — 把本体查询注册为 MCP 工具（6 个：product / metric / role / compliance / workflow / capability）

### 4.15 `app/cli/` — zhongtai CLI

- `main.py` — `zhongtai` 命令行（httpx → `http://localhost:8080/api`）
- 子命令：`health` / `skill list|exec` / `ontology list|validate` / `patrol list|run`

### 4.16 `app/observability/` — 可观测（Phase 4）

- `client.py` — `ObservabilityClient`：Langfuse SDK 封装，未配置环境变量时退化为 no-op

### 4.17 `app/multimodal/` — 多模态处理（Phase 8）

- `processors.py` — `ImageProcessor` / `AudioProcessor` / `VideoProcessor` / `DocumentProcessor`

### 4.18 `app/evals/` — 评估框架（Phase 6）

- `eval_set.py` — `EvalCase` / `EvalResult` / `EvalSet` / `EvalRunner`

### 4.19 `app/experiments/` — A/B 测试（Phase 6）

- `ab_test.py` — `ABTest` / `Variant` / `ABTestResult`：粘性分配（按 user_id 哈希）

### 4.20 `app/meta/` — 元学习（Phase 7）

- `analyzer.py` — `MetaAnalyzer`：跨 Skill 模式分析、Skill 序列挖掘
- `optimizer.py` — `SkillOptimizer`：Skill 健康评分 + prompt 自动优化
- `healing.py` — `HealingDetector` / `HealthSignal` / `HealthState`：异常检测 + 自愈

### 4.21 `app/federation/` — 联邦协作（Phase 9）

- `tenant.py` — `Tenant` / `TenantManager`：多租户数据隔离
- `mcp_federation.py` — `MCPFederation` / `FederatedPeer`：跨组织 MCP 联邦

### 4.22 `app/evolution/` — 自主进化（Phase 10）

- `automl.py` — `PromptAutoML` / `PromptCandidate`：DSPy 风格的 prompt 自动优化
- `rl_feedback.py` — `RLFeedback` / `FeedbackRecord`：从人工修正做 RLHF-lite
- `self_improve.py` — `SelfImproveLoop` / `ImprovementReport`：编排 AutoML + RL + healing

---

## 5. Skill 系统

### 5.1 核心原则：Skill 即价值中心

所有请求（无论来自 `/chat`、`/skills/{id}/execute`、飞书 webhook、巡逻任务、A2A、MCP 调用）最终都必须经过 `BaseSkill.run()`。没有旁路。

### 5.2 BaseSkill 8 步生命周期

`app/skills/base.py` 的 `BaseSkill.run()`：

```
SkillInput
    │
    ▼
┌─────────────────────┐
│ 1. validate         │ ← 子类可重写，返回 error 字符串或 None
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 2. guardrail_input  │ ← SafetyGuard.check_input()
│                     │   Prompt 注入检测（7 条正则）
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 3. inject_ontology  │ ← 读 skill.ontology_needs() 声明的维度
│                     │   把 OntologyService.loader.get(dim) 写入
│                     │   skill_input.context["ontology"]
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 4. inject_experience│ ← ExperienceEngine.get_experience_prompt(skill_id)
│                     │   写入 context["experience_prompt"]
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 5. execute          │ ← 子类必须实现，核心业务逻辑
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 6. guardrail_output │ ← SafetyGuard.check_output()
│                     │   PII 检测（身份证/手机/邮箱/银行卡）
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 7. post_execute     │ ← 子类可重写，Skill-specific 后处理
│                     │   （如合规文案的三层校验）
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│ 8. record           │ ← ExperienceEngine.record_execution()
│                     │   为未来的 pattern 学习留痕
└─────────┬───────────┘
          │
          ▼
  SkillExecutionRecord（id / input / output / execution_time_ms）
```

子类只需要实现 `meta()` + `execute()`，其余 7 步由框架自动执行。

### 5.3 SkillMeta 元数据

`app/skills/models.py` 定义的 `SkillMeta`：

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | `str` | 唯一标识，如 `compliant-copy` |
| `name` | `str` | 显示名 |
| `description` | `str` | 意图路由用的描述 |
| `category` | `SkillCategory` | `content` / `data` / `operation` / `product` / `patrol` |
| `version` | `str` | 语义化版本，默认 `1.0.0` |
| `author` | `str` | |
| `triggers` | `list[str]` | 触发词，Fast track 关键词匹配 |
| `parameters` | `dict` | JSON Schema 风格参数定义 |
| `permissions` | `list[str]` | RBAC 所需权限 |
| `model_preference` | `ModelPreference` | `local` / `overseas` / `specialized` / `auto` |

### 5.4 SkillRegistry

`app/skills/registry.py`：

- `register(skill)` — 记录 id → skill，同时把每个 trigger 词写进反向索引
- `get(skill_id)` — 按 id 取
- `find_by_trigger(text)` — 遍历 trigger 索引，子串匹配（lowercase），返回第一个命中
- `list_all()` / `list_by_category(cat)` — 列出 `SkillMeta`
- `count` — 注册数量

### 5.5 SkillDispatcher — 1+1+Deep 路由

`app/skills/dispatcher.py` 的 `dispatch()`：

```
用户消息 msg
    │
    ▼
┌─────────────────────────────────────────┐
│ 命令前缀判断                              │
│   /deep …    → run_deep_agent()          │
│   /workflow …→ workflow_engine.execute() │
│   /discuss … → brain.multi_agent_discuss │
└─────────┬───────────────────────────────┘
          │ 无命令前缀
          ▼
┌─────────────────────────────────────────┐
│ Fast track                               │
│   registry.find_by_trigger(msg)          │
│   命中 → skill.run()（0 tokens, instant）│
└─────────┬───────────────────────────────┘
          │ 未命中
          ▼
┌─────────────────────────────────────────┐
│ Main path: Agent loop                    │
│   BrainAgent.chat() (AgentScope ReAct)   │
│   模型自己决定调哪些 Skill                │
└─────────┬───────────────────────────────┘
          │ Agent 失败
          ▼
   fallback 再试一次 trigger 匹配
```

所有路径都通过 `SessionMemory.add_message()` 记录对话。

### 5.6 SkillDispatcher 支持的命令

| 命令 | 路由方式 | 说明 |
|---|---|---|
| `/deep <query>` | LangGraph ReAct Agent | 开放式研究，多步推理 |
| `/workflow <name>` | `WorkflowEngine.execute_workflow` | 从 `workflows.yaml` 执行 SOP |
| `/discuss <topic>` | `BrainAgent.multi_agent_discuss` | MsgHub 多 Agent 群聊 |
| （无前缀，触发词命中） | Fast track | 直接 Skill |
| （无前缀，未命中） | AgentScope coordinator | 由模型决定工具调用 |

### 5.7 六个内置 Skill

`app/skills/builtin/`（构造参数均为 `ModelRouter`）：

| Skill ID | 类名 | 类别 | 触发词示例 | 说明 |
|---|---|---|---|---|
| `compliant-copy` | `CompliantCopySkill` | `content` | 写文案 / 合规文案 / 小红书 | 保健品广告法合规，三层校验（禁词正则 → 规则引擎 → LLM 语义审核），`post_execute` 做最终合规 gate |
| `data-query` | `DataQuerySkill` | `data` | 查数据 / GMV / ROI | 自然语言 → SQL，注入 `data_definitions` 本体 |
| `report-gen` | `ReportGenSkill` | `data` | 日报 / 周报 / 月报 | 自动生成报表，注入 `goals` 本体 |
| `web-search` | `WebSearchSkill` | `operation` | 联网搜索 / 行业动态 | 外部信息检索 |
| `competitor-watch` | `CompetitorWatchSkill` | `operation` | 竞品分析 / 对比 | 注入 `health_supplements` 本体的 competitor 信息 |
| `content-adapt` | `ContentAdaptSkill` | `content` | 适配 / 多平台 | 一稿多平台改写（XHS/Douyin/WeChat/JD） |

多模态额外 Skill（Phase 8）：

| `visual-qa` | `VisualQASkill` | `operation` | 看图 / 包装照 / 截图分析 | 调用 `MultimodalProcessor.ImageProcessor` |

### 5.8 SkillFactory — 程序化创建

`app/skills/factory.py`：

- `from_template(skill_id, name, description, template, params, triggers)`：用 `SKILL_TEMPLATES` 中三个模板之一（`content_writer` / `data_analyst` / `compliance_checker`）
- `from_yaml(yaml_content)`：从 YAML 字符串构造 `YAMLSkill`
- `from_examples(skill_id, name, description, examples, triggers)`：few-shot，给 I/O pair 自动生成 prompt

### 5.9 YAMLSkill — 不写 Python 定义 Skill

`app/skills/yaml_skill.py`：

```yaml
id: weekly-summary
name: 周报摘要
description: 总结本周亮点
category: content
triggers: [周报摘要, 总结亮点]
model_preference: local
ontology_needs: [data_definitions, goals]
temperature: 0.7
max_tokens: 2048
prompt_template: |
  你是周报摘要专家。基于以下指标，写一段简短的周报摘要。
  {ontology_context}
  用户输入: {user_message}
```

`YAMLSkill.execute()` 会把 `ontology_context` / `experience_prompt` / `user_message` / 以及 `skill_input.parameters.*` 全部 format 到 `prompt_template`。

### 5.10 PluginDiscovery — 四源自动发现

`app/skills/discovery.py` 的 `PluginDiscovery.discover_all()`：

| 来源 | 路径 | 格式 |
|---|---|---|
| Built-in | `app/skills/builtin/` | Python（`main.py` 手动注册） |
| Plugins | `app/skills/plugins/` | Python `BaseSkill` 子类 |
| External | `~/.zhongtai/skills/` | Python `BaseSkill` 子类 |
| YAML | `app/skills/yaml_skills/` | YAML 文件 |

---

## 6. 12 维企业本体

### 6.1 维度清单

本体是 YAML 文件，按文件名作为维度标识，存放在 `app/ontology/definitions/`：

| 维度 | 文件 | 说明 |
|---|---|---|
| **组织** | `organization.yaml` | 部门、角色、权限、汇报关系、协作关系 |
| **能力** | `capabilities.yaml` | 人 + Agent 能力，自动化状态（none / partial / full），自动化覆盖率 |
| **流程** | `workflows.yaml` | SOP 定义，每步有 `role` / `type` / `skill` / `condition` / `gate` |
| **数据** | `data_definitions.yaml` | 指标定义，含中文名、公式、数据源、维度 |
| **目标** | `goals.yaml` | OKR + 巡逻规则（自动监控触发条件） |
| **事件** | `events.yaml` | 业务事件，`trigger_condition` / `severity` / `response_workflow` / `sla` |
| **策略** | `policies.yaml` | 合规、安全、成本、审批策略 |
| **工具** | `tools.yaml` | Skill 注册表 + 外部工具目录 |
| **客户** | `customers.yaml` | 客户分群，渠道/内容偏好 |
| **时间** | `schedule.yaml` | 周期任务 + 关键业务日期 |
| **资源** | `resources.yaml` | 预算 + 库存告警规则 |
| **领域** | `domain/health_supplements.yaml` + `domain/prohibited_words.yaml` | 保健品领域本体（3 个产品品类 + 4 个渠道 + 合规规则 + 竞品 + 80+ 禁词 6 个分类） |

### 6.2 OntologyLoader — 加载与热重载

`app/ontology/loader.py`：

- `DEFINITIONS_DIR = Path(__file__).parent / "definitions"`
- `load_all()` — `rglob("*.yaml")` 递归加载；`yaml.safe_load` + 按 stem 作为 key 缓存到 `self._cache`
- `get(dimension)` — 懒加载，首次访问触发 `load_all()`
- `reload()` — 清缓存重新加载（`/api/ontology/reload` 调用）
- `dimensions` property — 列出当前缓存的全部维度名

### 6.3 OntologyService — 查询接口

`app/ontology/service.py`，封装在 `OntologyLoader` 之上的 6 个查询方法：

| 方法 | 返回 | 说明 |
|---|---|---|
| `query_product(name)` | `{category, subcategories, approved_claims, prohibited_claims, competitors, ...}` | 从 `health_supplements` 产品品类匹配 |
| `query_metric(name)` | `{metric, chinese_name, formula, data_source, dimensions}` | 精确匹配 + 中文模糊匹配 |
| `query_role(name)` | `{role, permissions, tools, data_scope, reports_to}` | 从 `organization` roles 查 |
| `query_compliance(product_name)` | `{product, approved_claims, prohibited_claims, required_disclaimers}` | 基于 `query_product` 构造 |
| `query_workflow(name)` | `{workflow, steps, ...}` | 从 `workflows.yaml` 查 SOP |
| `query_capability(name)` | `{id, name, holders, automation_status, gaps, priority}` | 跨 `capability_domains` 遍历 |
| `list_dimensions()` | `list[str]` | 已加载的维度名 |

### 6.4 Pydantic 模型

`app/ontology/models.py` 定义强类型的本体数据结构，供 RBAC / Agent / Skill 使用：

- `RoleDefinition(name, permissions, tools, data_scope, reports_to, collaborates_with)`
- `CapabilityDefinition(id, name, holders, automation_status, automation_coverage, gaps, priority)`
- `WorkflowStep(id, role, action, skill, type, condition, gate, timeout)` — `type ∈ {deterministic, probabilistic, human_approval}`
- `MetricDefinition(chinese_name, definition, formula, data_source, dimensions, warning)`
- `ProductInfo(category, subcategories, key_ingredients, approved_claims, prohibited_claims, required_disclaimers, competitors)`
- `BusinessEvent(trigger_condition, severity, response_workflow, auto_actions, sla, escalation)`

### 6.5 MCP 暴露

`app/mcp/server.py` 的 `MCPServerManager.register_ontology_tools(ontology_service)` 会把 6 个查询方法注册为 MCP 工具，外部 Agent（Claude Code / Gemini CLI / Feishu Aily）可直接调用。

### 6.6 在 Skill 中声明依赖

Skill 在 `ontology_needs()` 中返回它依赖的维度列表，框架会在第 3 步自动注入：

```python
class CompliantCopySkill(BaseSkill):
    def ontology_needs(self) -> list[str]:
        return ["health_supplements", "prohibited_words", "policies"]
```

注入结果写到 `skill_input.context["ontology"]`，Skill 在 `execute()` 里直接读。

---

## 7. Brain & Agent 系统

### 7.1 Brain 层的定位

Brain **不替代** Skill。Brain 决定"调哪个 Skill"，Skill 才是真正的执行者和价值中心。Agent 来来去去，Skill 的经验沉淀下来不会丢。

### 7.2 AgentFactory — 从本体创建 Agent

`app/brain/agent.py` 的 `AgentFactory`：

| 方法 | 说明 |
|---|---|
| `initialize(model_config)` | `agentscope.init()`，默认构造 `litellm_chat` 模型配置指向本地 Qwen |
| `create_coordinator(toolkit, experience_prompt)` | 创建总调度 `ReActAgent`，挂载 `Toolkit`，`max_iters=10` |
| `create_role_agent(role_name, role_def, toolkit)` | 从 `organization.yaml` 的 role 定义创建角色 Agent，`max_iters=5`，system prompt 注入 `permissions` / `tools` / `data_scope` |
| `_create_memory()` | 优先 `RedisMemory`，失败退化 `InMemoryMemory` |
| `create_sequential_pipeline(agents)` | `SequentialPipeline` |
| `create_parallel_pipeline(agents)` | `FanoutPipeline` |
| `create_msg_hub(agents, announcement)` | `MsgHub` 多 Agent 群聊 |

System prompt 模板：`COORDINATOR_PROMPT` + `ROLE_PROMPT_TEMPLATE`（见源码）。

### 7.3 BrainAgent — 高层接口

`app/brain/agent.py` 的 `BrainAgent`：SkillDispatcher 只调它的几个方法。

| 方法 | 说明 |
|---|---|
| `initialize(model_config)` | 调 `factory.initialize` + `create_coordinator` |
| `register_tool(func)` | 把一个 Python 函数注册到 `Toolkit`，供 coordinator 调用 |
| `create_role_agent(role_name, role_def)` | 创建并缓存角色 Agent 到 `_role_agents` |
| `chat(message, user_id, session_id, experience_prompt)` | 总调度入口，注入经验 prompt，调用 `coordinator(user_msg)` |
| `multi_agent_discuss(topic, role_names, rounds=3)` | `MsgHub` 群聊，多轮讨论，聚合结论 |
| `sequential_workflow(task, role_names)` | `SequentialPipeline` 依次执行 |
| `role_agent_names` | 已创建的角色 Agent 列表 |

### 7.4 Skills-as-Tools Bridge

`app/brain/tools.py` 的 `register_skills_as_tools(brain, registry, experience_engine)`：

遍历 `SkillRegistry`，对每个 Skill 生成一个 tool 函数，签名统一为 `(user_message: str, platform: str = "", product_name: str = "") -> str`，函数内部：

1. 从 `ExperienceEngine.get_experience_prompt` 读经验 prompt
2. 构造 `SkillInput`
3. `ThreadPoolExecutor` 中 `asyncio.run(skill.run(skill_input))` 跑完整生命周期
4. 把 output content 加上合规警告后返回字符串
5. 设置 `func.__name__ = meta.id.replace("-", "_")` + `__doc__` 以供 AgentScope 生成 schema

这样任何 Skill 都能被 `ReActAgent` 自主调用。

### 7.5 WorkflowEngine — SOP 执行

`app/brain/workflow.py` 的 `WorkflowEngine.execute_workflow(workflow_name, initial_context)`：

1. 从 `OntologyService.query_workflow(name)` 读 `workflows.yaml` 中的 SOP
2. 逐步执行 `steps`：
   - 计算 `condition`（若有），不满足则 `skipped`
   - `type == human_approval` → 立即 `blocked`，返回 `pending_approval`
   - 有 `skill` 字段 → `registry.get(skill).run(SkillInput(...))`，走完整生命周期
   - 有 `gate` 字段 → `skill.run` 失败时阻塞
3. 每步输出写回 `context[f"step_{id}_output"]`，供后续步骤引用
4. 返回 `{workflow, steps_total, steps_completed, blocked, results[]}`

### 7.6 Deep Agent — LangGraph 开放研究

`app/brain/deep.py` 的 `run_deep_agent(query, skill_registry, user_id, session_id)`：

- 用 LangChain 的 `ChatOpenAI` 指向 LiteLLM 本地 endpoint
- `create_react_agent(llm, tools)` 创建 LangGraph ReAct Agent
- `_build_tools_from_skills(registry)` 把每个 Skill 包成 `StructuredTool`
- 每个 tool 执行时在 `ThreadPoolExecutor` 里 `asyncio.run(skill.run(...))`，完整生命周期
- 异步 `agent.ainvoke({"messages": [...]})` 获取结果

依赖 `[deep]` 可选 extras（`langchain` / `langgraph` / `langchain-openai`）。未安装时 `ImportError` 被 `SkillDispatcher._deep_agent` 捕获，降级到普通 Agent loop。

### 7.7 启动时角色 Agent 自动创建

`app/main.py` 的 `_create_role_agents(state)`：

```python
org = state.ontology_service.loader.get("organization")
roles = org.get("roles", {})
for role_name, role_def in roles.items():
    state.brain.create_role_agent(role_name, role_def)
```

新增角色 = 编辑 `organization.yaml`，重启服务；无需改代码。

---

## 8. API 端点完整列表

所有路由统一前缀 `/api`（在 `create_app()` 中 `include_router(..., prefix="/api")`）。鉴权统一走 `app/auth/middleware.py::require_auth`（Bearer JWT 或 `X-API-Key` 头；`settings.debug=true` 时自动放行）。

### 8.1 `health` — 健康检查

`app/api/health.py`

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| GET | `/api/health` | 否 | 返回 `{status, version}` |

### 8.2 `auth` — 认证（Phase 4）

`app/api/auth.py`

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| GET  | `/api/auth/feishu/url` | 否 | 获取飞书 OAuth 授权 URL |
| POST | `/api/auth/feishu/callback` | 否 | 用 code 换飞书 access token，签发本地 JWT |
| POST | `/api/auth/login` | 否 | 本地开发 login |
| GET  | `/api/auth/me` | ✓ | 当前用户信息 |
| GET  | `/api/auth/permissions` | ✓ | 当前角色的 RBAC 权限 |

### 8.3 `chat` — 对话入口

`app/api/chat.py`

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| POST | `/api/chat` | ✓ | 主对话接口，经 `SkillDispatcher.dispatch` 路由 |

请求体：
```json
{"message": "帮我写一篇胶原蛋白的小红书文案", "user_id": "", "session_id": ""}
```

响应体：
```json
{"content": "...", "skill_id": "compliant-copy", "mode": "fast|agent|deep|workflow|discuss", "execution_time_ms": 1234}
```

### 8.4 `skills` — Skill 管理

`app/api/skills.py`（自带 `prefix="/skills"`）

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| GET  | `/api/skills/` | 否 | 列出所有 `SkillMeta` |
| GET  | `/api/skills/{skill_id}` | 否 | 单个 Skill 元数据 |
| POST | `/api/skills/{skill_id}/execute` | ✓ | 直接执行（跳过意图路由，仍走完整生命周期） |
| GET  | `/api/skills/{skill_id}/experience` | 否 | 该 Skill 的经验 pattern 列表 + 统计 |

### 8.5 `experience` — 经验管理

`app/api/experience.py`（自带 `prefix="/experience"`）

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| POST | `/api/experience/corrections` | ✓ | 提交人工修正 → 触发经验学习 |
| GET  | `/api/experience/patterns/{skill_id}` | 否 | 列出某 Skill 的全部经验 pattern |
| POST | `/api/experience/patterns/{pattern_id}` | ✓ | 确认 / 否决 pattern（`action: "confirm" | "reject"`） |

### 8.6 `feishu` — 飞书 Webhook

`app/api/feishu.py`

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| POST | `/api/webhook` | 否（飞书自带签名） | 飞书 Bot 事件回调，验签 + 去重 + 调 `MessageRouter` |

### 8.7 `ontology` — 本体查询与管理

`app/api/ontology.py`

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| GET  | `/api/dimensions` | 否 | 列出全部已加载维度名 |
| GET  | `/api/dimension/{name}` | 否 | 返回单维度的完整 YAML 数据 |
| GET  | `/api/product/{name}` | 否 | 产品查询（`query_product`） |
| GET  | `/api/metric/{name}` | 否 | 指标查询（`query_metric`） |
| GET  | `/api/role/{name}` | 否 | 角色查询（`query_role`） |
| GET  | `/api/compliance/{product_name}` | 否 | 合规规则查询 |
| GET  | `/api/workflow/{name}` | 否 | SOP 查询 |
| GET  | `/api/capability/{name}` | 否 | 能力查询 |
| POST | `/api/reload` | ✓ | 热重载全部本体 YAML |

### 8.8 `patrol` — 巡逻任务

`app/api/patrol.py`

| 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|
| GET  | `/api/tasks` | 否 | 列出已注册巡逻任务 |
| POST | `/api/tasks/{task_id}/run` | 否 | 手动触发某巡逻任务（用于调试） |

### 8.9 `a2a` — Agent-to-Agent 协议（已实现，未启用）

`app/api/a2a.py`（**当前未在 `create_app()` 中 include**，需手动挂载后生效）

| 方法 | 路径 | 说明 |
|---|---|---|
| GET  | `/.well-known/agent-card.json` | A2A Agent Card |
| POST | `/api/a2a/tasks` | 创建 task 执行 Skill |
| GET  | `/api/a2a/tasks/{task_id}` | 查询 task 状态 |

---

## 9. 前端规格

### 9.1 技术栈与文件

- 单文件 SPA：`app/static/index.html`
- 无构建过程，FastAPI 直接 `FileResponse` 返回
- CDN 依赖：`tailwindcss` + `alpinejs@3`
- 风格：Claude Code 风格暗色主题，对话为主，面板为辅

### 9.2 布局

```
┌────────────────────────────────────────────┬──────────────┐
│ Header                                     │              │
│  AI 中台  v0.1.0  ●  N skills  M 维本体    │              │
├────────────────────────────────────────────┤              │
│                                            │  右侧面板     │
│                                            │  ┌────────┐  │
│            对话区                           │  │技能    │  │
│  (Welcome / messages / loading)            │  │本体    │  │
│                                            │  │合规    │  │
│                                            │  │经验    │  │
│                                            │  └────────┘  │
│                                            │              │
├────────────────────────────────────────────┤              │
│ 输入栏                                      │              │
│  [说你想做什么...]                  [发送] │              │
└────────────────────────────────────────────┴──────────────┘
```

### 9.3 主界面：对话中心

- 空状态提示："说你想做什么"
- 6 个 Quick action chips：写合规文案 / 查数据 / 写报告 / 竞品分析 / 联网搜索 / 多平台适配
- 3 个命令 chips：`/workflow` / `/deep` / `/discuss`
- 消息气泡：用户右对齐蓝色，Assistant 左对齐暗灰
- Assistant 消息下方显示：`⚡skill_id` / `mode` / `Nms` 标签

### 9.4 右侧面板（可折叠）

| Tab | 内容 |
|---|---|
| **技能** | `GET /api/skills/` 列表，显示 name + description + triggers 标签（点击即触发对话） |
| **本体** | `GET /api/dimensions` 12 维列表 + 点击加载 `GET /api/dimension/{name}` |
| **合规** | 输入产品名 → `GET /api/compliance/{name}` → 批准/禁止声明对比 |
| **经验** | 按 skill 列经验 pattern + 置信度 + 确认/否决按钮（调 `POST /api/experience/patterns/{id}`） |

### 9.5 前端状态管理

Alpine `x-data="app()"` 持有：
- `messages[]` / `input` / `loading` — 对话状态
- `skills[]` / `ontologyDims[]` / `health` — 后端元数据
- `showPanel` / `pt` — 面板显示 / 当前 tab
- `selDim` / `dimD` / `cQ` / `cR` / `pats` — 面板子状态

---

## 10. 测试体系

### 10.1 覆盖清单

16 个测试文件在 `tests/` 下，通过 `pyproject.toml` 中 `pytest.ini_options.asyncio_mode = "auto"` 自动识别异步测试。

| 文件 | 测试数 | 覆盖范围 |
|---|---|---|
| `test_auth.py` | 4 | JWT 创建 / 校验 / 过期 / middleware |
| `test_skills.py` | 5 | `SkillRegistry` / trigger 反查 / `SkillMeta` / 生命周期骨架 |
| `test_experience.py` | 7 | `ExperienceStore` CRUD / Chinese bigram similarity / confidence 管理 |
| `test_ontology.py` | 11 | `OntologyLoader` / 6 查询方法 / 12 维存在性 / hot reload |
| `test_guardrails.py` | 7 | Prompt 注入（中英文）/ PII 检测（身份证、手机、邮箱、银行卡） |
| `test_memory.py` | 4 | `SessionMemory` 多轮会话 / session 隔离 / TTL |
| `test_compliance.py` | 7 | 禁词匹配 / 规则引擎 / auto-fix / platform 检测 |
| `test_compliance_evals.py` | — | 112 case `EvalSet`：21 违规 / 14 clean / 5 规则 / 9 平台 / 6 auto-fix |
| `test_mcp.py` | 4 | 工具注册 / 调用 / ontology tools |
| `test_agent.py` | 3 | `AgentFactory` 配置 / `BrainAgent` 创建 / tool 注册 |
| `test_workflow.py` | 4 | 已知/未知 workflow / human approval / 缺 ontology 降级 |
| `test_dispatcher.py` | 8 | Fast track / Agent loop / `/workflow` / `/discuss` / `/deep` |
| `test_deep_agent.py` | 3 | LangChain 导入 / Skill wrapper / 模块 import |
| `test_new_skills.py` | 10 | 5 个新 Skill 的 meta / ontology_needs / registry 集成 / trigger 路由 |
| `test_phase4.py` | 15 | SSO / RBAC / Langfuse / Cost Control / Celery / Audit |
| `test_phase5_10.py` | 24 | 数字孪生 / SkillFactory / EvalSet / A/B / MetaAnalyzer / Healing / 多模态 / 联邦 / 进化 |

### 10.2 运行测试

```bash
# 全部测试
pytest

# 单文件
pytest tests/test_skills.py -v

# 只跑某 phase
pytest tests/test_phase4.py tests/test_phase5_10.py -v
```

### 10.3 Lint

```bash
ruff check app/ tests/
```

配置见 `pyproject.toml` `[tool.ruff]`：`target-version=py311`、`line-length=100`、启用 `E F I N W`。

---

## 11. 部署架构

### 11.1 Docker Compose 全栈

`docker-compose.yaml` 定义 7 个服务：

| 服务 | 镜像 | 端口 | 职责 |
|---|---|---|---|
| `api` | 本地 `build: .` | 8080 | FastAPI 主服务（`uvicorn app.main:app`） |
| `mysql` | `mysql:8.0` | 3306 | 业务数据库（Skill 执行日志、经验 pattern），UTF-8 配置 |
| `redis` | `redis:7-alpine` | 6379 | 会话记忆、经验缓存、飞书去重、限流 |
| `neo4j` | `neo4j:5-community` | 7474 / 7687 | 知识图谱（本体关系、经验时序图谱），含 APOC 插件 |
| `langfuse-db` | `postgres:15-alpine` | — | Langfuse 元数据 |
| `langfuse` | `langfuse/langfuse:latest` | 3000 | LLM 可观测性 Web UI |
| `celery-worker` | 本地 `build: .` | — | Celery 分布式任务执行 |
| `celery-beat` | 本地 `build: .` | — | Celery 定时调度（代替 APScheduler） |

全部服务配置了 `healthcheck`、`restart: unless-stopped`、命名卷（`mysql_data` / `redis_data` / `neo4j_data` / `langfuse_db`）。

### 11.2 Dockerfile

`FROM python:3.11-slim`：
1. 装系统依赖：`build-essential` / `default-libmysqlclient-dev` / `pkg-config`
2. `pip install -e ".[dev]"` + 额外的 `agentscope` / `pyyaml` / `aiosqlite` / `asyncmy`
3. `EXPOSE 8080`
4. `CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]`

### 11.3 `.env.example` 关键变量

| 组 | 变量 |
|---|---|
| 基础 | `APP_ENV` / `DEBUG` / `SECRET_KEY` |
| 本地 LLM | `LOCAL_MODEL_BASE_URL` / `LOCAL_MODEL_NAME` / `LOCAL_MODEL_API_KEY` |
| 海外 LLM | `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `MODEL_ROUTING_STRATEGY` |
| 数据库 | `DATABASE_URL` / `REDIS_URL` |
| 向量 / 分析 | `MILVUS_HOST:PORT` / `CLICKHOUSE_HOST:PORT` |
| 飞书 | `FEISHU_APP_ID` / `FEISHU_APP_SECRET` / `FEISHU_VERIFICATION_TOKEN` / `FEISHU_ENCRYPT_KEY` |
| OSS | `OSS_ENDPOINT` / `OSS_ACCESS_KEY_ID` / `OSS_ACCESS_KEY_SECRET` / `OSS_BUCKET` |
| 巡逻 | `PATROL_ENABLED` / `PATROL_TIMEZONE` |

完整清单见 [.env.example](../.env.example)。

### 11.4 启动顺序（推荐）

```bash
cp .env.example .env
# 填入真实的 LLM / 飞书 / LANGFUSE 凭证

# 全栈启动
docker compose up -d mysql redis neo4j
docker compose up -d langfuse-db langfuse
docker compose up -d api celery-worker celery-beat

# 查看日志
docker compose logs -f api
```

### 11.5 部署指南引用

完整部署手册见 [`docs/deployment.md`](./deployment.md)，涵盖：Docker / 本地 dev 模式 / 3 种 LLM 配置（DataEyes / vLLM / DeepSeek）/ 飞书机器人申请流程 / CLI 使用 / 验证清单 / 生产加固。

---

## 12. 开发指南

### 12.1 新增一个 Skill（Python 方式）

1. 在 `app/skills/builtin/my_skill.py` 建文件：

```python
from app.llm.router import ModelRouter
from app.skills.base import BaseSkill
from app.skills.models import (
    SkillCategory, SkillInput, SkillMeta, SkillOutput
)

class MySkill(BaseSkill):
    def __init__(self, model_router: ModelRouter) -> None:
        self.router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="my-skill",
            name="我的技能",
            description="做 XX 事情",
            category=SkillCategory.CONTENT,
            triggers=["做XX", "XX一下"],
        )

    def ontology_needs(self) -> list[str]:
        # 声明依赖的本体维度，框架会自动注入
        return ["health_supplements"]

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        # 读取注入的本体
        ontology = skill_input.context.get("ontology", {})
        # 读取注入的经验
        experience = skill_input.context.get("experience_prompt", "")
        # 调 LLM
        # ...
        return SkillOutput(success=True, content="结果")
```

2. 在 `app/skills/builtin/__init__.py` 导出 `MySkill`
3. 在 `app/main.py::_register_builtin_skills` 中 `state.skill_registry.register(MySkill(router))`
4. 写测试：`tests/test_my_skill.py`

### 12.2 新增一个 Skill（YAML 方式，不写 Python）

1. 在 `app/skills/yaml_skills/weekly_summary.yaml` 建文件：

```yaml
id: weekly-summary
name: 周报摘要
description: 总结本周亮点
category: content
triggers: [周报摘要, 本周总结]
model_preference: local
ontology_needs: [data_definitions, goals]
prompt_template: |
  你是周报摘要专家。基于以下指标和目标：
  {ontology_context}
  历史经验: {experience_prompt}
  请为用户写一段周报摘要。
  用户输入: {user_message}
```

2. 启动时 `PluginDiscovery.discover_yaml_skills()` 会自动注册

### 12.3 扩展本体

新增维度：
1. 在 `app/ontology/definitions/` 放一个 `my_dimension.yaml`
2. 重启服务（或调 `POST /api/reload`）热重载
3. 若需要强类型，在 `app/ontology/models.py` 加 Pydantic 模型
4. 若需要暴露查询接口，在 `app/ontology/service.py` 加 `query_my_dimension()`
5. 若要暴露为 MCP 工具，在 `app/mcp/server.py::register_ontology_tools` 的 `tool_mappings` 中加一行

修改现有维度：编辑对应 YAML → 调 `POST /api/reload` 生效。

### 12.4 新增 MCP 工具

```python
# app/main.py lifespan 中
state.mcp_server.register_skill_tool(
    skill_id="my-tool",
    name="工具显示名",
    description="工具描述（供外部 Agent 意图匹配）",
    handler=my_async_handler,
    parameters={"type": "object", "properties": {...}},
)
```

### 12.5 调试 LLM Router

```python
from app.llm.router import ModelRouter
from app.llm.models import ChatRequest, ChatMessage, Role

router = ModelRouter()
resp = await router.chat(ChatRequest(
    messages=[ChatMessage(role=Role.USER, content="你好")],
    model_preference="local",   # local / overseas / specialized / auto
    temperature=0.7,
    max_tokens=2048,
))
print(resp.content)
```

`ModelRouter` 内部用 LiteLLM 的 `Router`，内置 retry / fallback / cooldown。本地模型通过 `LOCAL_MODEL_BASE_URL` 指向 vLLM；海外模型通过 `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` 启用。

### 12.6 飞书 Bot 接入

1. 在 [飞书开放平台](https://open.feishu.cn) 创建企业自建应用
2. 配置事件订阅，回调 URL 指向 `https://<your-host>/api/webhook`
3. 获取 App ID / App Secret / Verification Token / Encrypt Key
4. 填到 `.env` 的 `FEISHU_*` 变量
5. `FeishuBot` 启动时自动刷新 tenant access token（2h 过期）
6. 消息会走 `MessageRouter` → `SkillDispatcher.dispatch` → Skill 生命周期

### 12.7 跑测试

```bash
pip install -e ".[dev]"
pytest                              # 全部
pytest tests/test_skills.py -v      # 单文件
pytest -k "test_dispatcher"         # 关键字过滤
ruff check app/ tests/              # lint
```

### 12.8 生产部署前检查清单

- [ ] `.env` 中所有 `change-me-*` 已替换
- [ ] `DEBUG=false`，生产环境 `require_auth` 必须生效
- [ ] `SECRET_KEY` / `NEXTAUTH_SECRET` 已换
- [ ] `LOCAL_MODEL_BASE_URL` 指向真实 vLLM 服务
- [ ] `FEISHU_*` 已填真实凭证
- [ ] `LANGFUSE_*` 已填
- [ ] `POST /api/reload` 能成功热重载本体
- [ ] `pytest` 全绿、`ruff check` 无错
- [ ] Docker compose 所有服务 `healthcheck` 通过

---

