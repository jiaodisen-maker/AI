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
