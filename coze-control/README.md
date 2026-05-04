# coze-control —— 把 Coze 变成 GitOps 化的可治理资产

把 coze.cn（企业版）上的所有 bot / workflow / knowledge 拉成 git，做评测、分析、优化、回写、A/B、规约校验。

> **安全前置**：所有凭据只走环境变量。任何把 PAT 写进 yaml/json/源码的尝试都会被 `secrets.py` 拒绝。详见 `SECURITY.md`。

## 解决的 4 个问题

| 问题 | 模块 | 频率 | 输出 |
|---|---|---|---|
| **a. prompt 飘** | `eval.py` + `optimize.py` | 每次提交 + 每天 | 黄金题分数 + 时间序列 + 改写建议 PR |
| **b. KB 召回差** | `kb_analyze.py` | 每周 | 哪些 chunk 从没被命中 / 哪些 query 没好答案 / 重切建议 |
| **c. 不知道哪里坏** | `analyze.py` | 每天 | 失败模式聚类（兜底/重复提问/突然结束/👎），Top10 → 喂给 optimize |
| **d. 多 bot 治理** | `pull.py` + `push.py` + `lint.py` + `ab.py` | pull 每日；push/lint 每次 PR；ab 持续 | bot/workflow/KB 全部 git 化、可 diff、可 review、可回滚 |

## 一句话流程

```
   Coze 工作空间
       │ pull.py (每日)            ↑ push.py (PR 合并 + 回归通过)
       ▼                            │
   git: coze-control/bots/*.yaml ← 人 / Agent 改这里 ← optimize.py 提议
       │                            │
       │ lint.py 校验                │
       │ eval.py 跑黄金题            │
       │ analyze.py 挖日志           │
       │ kb_analyze.py 测召回        │
       └────────────────────────────┘
```

## 目录

```
coze-control/
├── README.md                  本文件
├── SECURITY.md                ★ 凭据 / 数据安全规范（必读）
├── .env.example               哪些环境变量要设
├── .gitignore                 排除 .env / secrets / 任何 *.token
├── config.yaml                非敏感配置（API base、超时、并发等）
├── secrets.py                 安全的 secret 读取（拒绝任何非 env 来源）
├── client.py                  Coze Open API 封装（所有调用走它）
├── pull.py                    Coze → git mirror
├── push.py                    git → Coze（带 lint + eval 守门）
├── lint.py                    bot/workflow 规约校验
├── eval.py                    黄金题回归（每天 + push 守门）
├── analyze.py                 对话日志失败模式聚类
├── kb_analyze.py              KB 召回质量分析
├── optimize.py                LLM 优化建议生成（只提议，不直推）
├── ab.py                      A/B 变体管理与流量切分
├── bots/                      <bot_id>.yaml（pull 写入）
├── workflows/                 <workflow_id>.yaml
├── knowledge/                 <kb_id>/ + recall_report.md
├── evals/
│   ├── golden.jsonl           黄金问题集（人工维护）
│   ├── history.jsonl          每次 eval 的得分时序
│   └── reports/               每次的详细报告
└── plugins/
    └── memory/                把 memory-integration 暴露给 Coze 当插件
        ├── manifest.json      Coze 插件元数据
        ├── openapi.yaml       OpenAPI 规范
        └── server.py          HTTP 服务（封装 memory_write/recall/reflect）
```

## 三步上手

```bash
# 1. 设环境变量（只在你机器上）
cp coze-control/.env.example coze-control/.env
# 编辑 .env，填 COZE_PAT 等

# 2. 安全自检
python -m coze_control.secrets --selftest

# 3. 第一次 pull（只读，不改 Coze 任何东西）
python -m coze_control.pull --workspace $COZE_WORKSPACE_ID
git add coze-control/bots coze-control/workflows coze-control/knowledge
git commit -m "snapshot: initial coze pull"
```

## OpenClaw 入口
`skills/coze-control.md` —— actions：
`pull / lint / eval / analyze / kb_analyze / optimize / push / ab`
