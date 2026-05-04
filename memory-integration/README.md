# memory-integration

OpenClaw 用的"双层记忆"Skill 包：把 **GBrain**（语义/长期）和 **Hindsight**（情景/工作）拼成一个统一的记忆系统。

OpenClaw 通过 `RESOLVER.md` 路由意图到对应 Skill，每个 Skill 调底层 `scripts/` 里的 router / 守护进程 / MCP server。

## 目录

```
memory-integration/
├── README.md              # 本文件
├── RESOLVER.md            # OpenClaw 意图路由表（必读）
├── config.yaml            # 路由规则 + 阈值
├── skills/                # OpenClaw 可执行的 Skill
│   ├── memory-write.md
│   ├── memory-recall.md
│   ├── memory-reflect.md
│   └── memory-bootstrap.md
├── scripts/               # 底层实现
│   ├── router.py          # MemoryRouter（写入路由 + 检索融合）
│   ├── auto_dream.py      # 守护进程（Hindsight → GBrain 凝固）
│   └── mcp_server.py      # 对外的统一 MCP（3 个工具）
└── brain/                 # GBrain Brain Repo 入口（软链或子模块）
```

## 三步上手

```bash
# 1. 安装依赖
bun install -g @garrytan/gbrain
pip install hindsight-memory pyyaml httpx

# 2. 初始化（OpenClaw 调 memory-bootstrap.md）
python scripts/mcp_server.py --setup

# 3. 启动
python scripts/mcp_server.py &        # 暴露 3 个 MCP 工具给 OpenClaw
python scripts/auto_dream.py --cron   # 后台凝固守护
```

## OpenClaw 看到的接口（仅 3 个）

| MCP 工具 | 作用 |
|---|---|
| `memory_write(content, hints)` | 写记忆，自动路由到 GBrain 或 Hindsight |
| `memory_recall(query, k)` | 跨两边检索，RRF 融合，结果带 `[KB]`/`[MEM]` 标签 |
| `memory_reflect(scope)` | 触发反思 + 凝固稳定 belief 进 GBrain |

## 哲学（一句话）

> Hindsight 是海马体，GBrain 是大脑皮层。autoDream 在两者之间做"睡眠时的记忆固化"。
