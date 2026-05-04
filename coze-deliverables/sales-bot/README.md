# 销售助手 · 8 个交付物

> 配合 `docs/coze-knowledge-base/SALES-BOT.md` 食用。
> 这些是**可直接执行/粘贴**的工程资产，按 4 周冲刺顺序产出。

## 清单

| # | 文件 | 谁用 | Week |
|---|---|---|---|
| 1 | `01-system-prompts.md` | 工程师 4（粘到 Coze）| 1 |
| 2 | `02-workflow-templates/`（3 个 YAML）| 工程师 4 | 2 |
| 3 | `03-crm-plugin-openapi.yaml` | 工程师 2 | 1 |
| 4 | `04-database-schema.sql` + 同步脚本 | 工程师 3 | 1 |
| 5 | `05-eval-golden-set.jsonl` + 评测器 | 工程师 6 + 你 | 2 |
| 6 | `06-compliance-guardrails.md` | 法务 + 工程师 4 | 1 |
| 7 | `07-feishu-entrypoint.md` | 工程师 7 | 1 |
| 8 | `08-coze-loop-setup.md` | 工程师 6 | 2 |

## 顺序建议

并行做：**1, 3, 4, 6, 7**（Week 1 全部启动）
串行做：**2 依赖 3+4+6**；**5 依赖 1+2**；**8 在 1+2 跑通后**

## 如何使用

每个文件都自带"如何粘到 Coze / 如何部署"说明。看 `01-system-prompts.md` 起步。
