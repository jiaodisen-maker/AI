# AI 中台 — 自进化企业 AI 操作系统

以 Skill 为中心的企业 AI 中台。不是通用 AI 平台，而是深度适配保健品行业的自进化 AI 操作系统。

## 核心差异化

- **经验引擎**：每次 Skill 运行后记录人工修正，自动提取 pattern，Skill 越用越准
- **巡逻系统**：不等命令，主动扫描数据异常、竞品变化，飞书推送告警 + 建议动作
- **三层合规**：禁词库 + 规则引擎 + LLM 审核，保健品广告法全覆盖
- **私有部署**：解决扣子/Coze 的四堵墙（数据安全、海外模型、复杂 skill、信息合规）

## 架构

```
渠道层    飞书 Bot · Web 工作台 · API
            │
大脑层    意图识别 → Skill 路由 → 任务规划
            │
          ┌─┴─ 经验引擎 ─┐
          │ 记录 → 学习 → 注入 │
          └───────────────┘
            │
Skill层   内容系 · 数据系 · 运营系 · 产品系 · 巡逻系
            │
模型层    本地(Qwen) · 海外(Claude/GPT) · 专用(微调)
            │
数据层    MySQL · Redis · Milvus · ClickHouse
```

## 快速开始

```bash
# 1. 安装依赖
pip install -e ".[dev]"

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 填入实际配置

# 3. 启动服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

## API 端点

| 方法 | 路径 | 说明 |
|---|---|---|
| POST | `/api/chat` | 主对话接口 |
| GET | `/api/skills` | 列出所有技能 |
| POST | `/api/skills/{id}/execute` | 直接执行指定技能 |
| POST | `/api/experience/corrections` | 提交人工修正（触发经验学习） |
| GET | `/api/experience/patterns/{skill_id}` | 查看技能的经验规则 |
| POST | `/api/feishu/webhook` | 飞书 Bot 事件回调 |
| GET | `/api/patrol/tasks` | 列出巡逻任务 |
| POST | `/api/patrol/tasks/{id}/run` | 手动触发巡逻 |
| GET | `/api/health` | 健康检查 |

## 项目结构

```
app/
├── main.py                 # FastAPI 入口，组装所有组件
├── config.py               # 配置中心
├── api/                    # API 路由
│   ├── chat.py             # 对话接口
│   ├── skills.py           # 技能管理
│   ├── experience.py       # 经验管理
│   ├── feishu.py           # 飞书 webhook
│   ├── patrol.py           # 巡逻系统
│   └── health.py           # 健康检查
├── brain/                  # 大脑层
│   ├── intent.py           # 意图识别
│   ├── router.py           # 技能路由
│   └── planner.py          # 任务规划（多步编排）
├── skills/                 # 技能系统
│   ├── base.py             # BaseSkill 抽象基类
│   ├── registry.py         # 技能注册中心
│   ├── models.py           # 技能数据模型
│   └── builtin/
│       └── compliant_copy.py  # 合规文案生成（第一个 Skill）
├── experience/             # 经验引擎（核心差异化）
│   ├── engine.py           # 经验学习核心
│   ├── store.py            # 经验存储（内存 + Redis）
│   └── models.py           # 经验数据模型
├── patrol/                 # 巡逻系统（主动监控）
│   ├── scheduler.py        # 定时调度
│   ├── base.py             # 巡逻任务基类
│   ├── notifier.py         # 告警通知
│   └── models.py           # 巡逻数据模型
├── channels/               # 渠道层
│   ├── feishu.py           # 飞书 Bot
│   ├── message.py          # 消息路由（核心管道）
│   └── models.py           # 消息模型
├── llm/                    # 模型层
│   ├── router.py           # 智能路由（本地/海外/专用）
│   └── models.py           # LLM 数据模型
└── data/                   # 数据层
    ├── database.py         # SQLAlchemy 异步管理
    ├── redis.py            # Redis 管理
    └── models.py           # ORM 模型
```

## 技术栈

- **框架**: FastAPI (async)
- **LLM 路由**: LiteLLM (100+ 模型统一接口)
- **本地模型**: vLLM + Qwen-72B
- **海外模型**: Claude / GPT-4o
- **数据库**: SQLAlchemy + MySQL/SQLite
- **缓存**: Redis
- **向量库**: Milvus (RAG)
- **分析**: ClickHouse
- **调度**: APScheduler
- **渠道**: 飞书开放平台

## 设计文档

详细架构设计见 [docs/design.md](docs/design.md)
