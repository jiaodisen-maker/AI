# reliability —— 记忆层稳定性与优化

让 GBrain + Hindsight + Feishu 通道这一整套**自己监控自己、自己修自己、修不了报警**。

## 四个组件

```
   ┌─────────────────────────────────────────────────┐
   │              reliability/                        │
   │                                                  │
   │  healthcheck.py  ── 1 min cron ──→ alerts.py    │
   │  audit.py        ── 1 day cron ──→ alerts.py    │
   │  optimizer.py    ── 1 week    ──→ reporter.py   │
   │  reporter.py     ── 1 day cron ──→ 飞书 webhook │
   │                                                  │
   └─────────────────────────────────────────────────┘
                       │
                       ▼
        飞书机器人 / Prometheus / SLO 仪表盘
```

## 各组件职责

### `healthcheck.py` —— 它还活着吗
**频率：1 分钟**

8 项端到端探针，按依赖顺序往上检查（任一红 → 立即告警）：

| # | 检查 | 期望 | 失败影响 |
|---|---|---|---|
| 1 | Redis ping | `PONG` | 全瘫 |
| 2 | tenant_access_token TTL > 60s | 是 | 飞书侧拉不到数据 |
| 3 | Queue stream 存在且 consumers ≥ 1 | 是 | 数据进不来 |
| 4 | Queue lag < 阈值 | < 200 | 实时性退化 |
| 5 | DLQ 增量 < 阈值 | 1h 内 < 10 | 数据丢失风险 |
| 6 | `memory_write("__probe__")` 成功 | 200ms | 写入路径坏 |
| 7 | `memory_recall("__probe__")` 命中 | < 1s | 读取/索引坏 |
| 8 | autoDream 上次跑 < 25h | 是 | 凝固停滞 |

红即告警，连续 3 次红 → 升级（飞书群 → 电话）。

### `audit.py` —— 数据还对得上吗
**频率：1 天**

数据完整性审计，**只报告，不删数据**：

- 孤儿引用：GBrain 文件 frontmatter 里写的 `hindsight_ids` 是否还在 Hindsight 里？反向亦同
- 重复实体：同一个人是否在多个 markdown 里出现（按 `email` / `phone` / `feishu_open_id` 比对）
- 冲突积压：审核中的 conflict 多于 N 条 / 最老超过 M 天
- frontmatter schema：是否所有 `brain/people/*.md` 都有 `type: person` 和 `name`
- 索引一致性：GBrain Postgres 里的文档数 vs git ls-files 数
- Hindsight 归档残留：`mark_archived` 但 30 天前的还没被压缩

### `optimizer.py` —— 它还快吗
**频率：1 周**

性能优化，**有 dry-run 模式**：

- pgvector 索引重建：检测 Recall@5 是否低于基线，是 → `REINDEX INDEX CONCURRENTLY`
- Postgres VACUUM ANALYZE
- Hindsight 已归档记忆压缩
- 慢查询识别：top 10 检索耗时 > 500ms 的 query → 建议加 metadata 过滤
- 检索基线测试：跑一组金标问题，对比上周得分
- 阈值自适应建议：如果凝固冲突率 > 20%，建议把 `min_confidence` 从 0.80 调到 0.85（建议不自动改）

### `reporter.py` —— 给人看的日报
**频率：1 天，08:00**

推一条飞书卡片：

```
📊 记忆系统 · 2026-05-04 日报
─────────────────────
入库:    msg 234 · doc 12 · meeting 5
写入:    KB 142 · MEM 89 · both 23
检索:    p50=120ms  p99=480ms  (-15ms vs 昨日)
凝固:    实体 7 · 信念 12 · 冲突待审 2 ⚠️
DLQ:     0 (good)
SLO:     ✅ all green (24h)
建议:    pgvector recall@5 已降至 0.91，建议运行 optimize（点 [详情]）
```

## 文件清单

```
reliability/
├── README.md
├── config.yaml          阈值 + cron + 告警渠道
├── healthcheck.py       8 项探针 + 多档告警
├── audit.py             6 项数据完整性
├── optimizer.py         性能优化 + dry-run
├── reporter.py          日报生成与推送
├── alerts.py            告警分发（飞书 / 邮件 / 电话）
├── slo.py               SLO 计算（错误预算）
└── __init__.py
```

## 启动

```bash
# 开守护
python -m memory_integration.reliability.healthcheck --cron &
python -m memory_integration.reliability.audit       --cron &
python -m memory_integration.reliability.optimizer   --cron --dry-run &
python -m memory_integration.reliability.reporter    --cron &

# 或一次性
python -m memory_integration.reliability.healthcheck --once
```

## OpenClaw 入口
`skills/memory-reliability.md` —— 5 个 action：
`check / audit / optimize / report / triage`

## 告警分级

| 级别 | 触发条件 | 通道 |
|---|---|---|
| INFO | 周报、优化建议 | 飞书群消息 |
| WARN | DLQ 累积、凝固延迟、recall 性能下滑 | 飞书 @负责人 |
| CRITICAL | 探针 1/2/6/7 任一红 | 飞书电话 + 邮件 |
| FATAL | 连续 3 次 CRITICAL | 升级到第二联系人 |
