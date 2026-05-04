# RESOLVER (memory-integration)

OpenClaw 在处理任何带"记/查/想/反思/学习"语义的请求时，先来这里查路由。

## 意图 → Skill 映射

| 用户意图（中文示例） | 触发关键词 | Skill |
|---|---|---|
| "记一下 / 帮我记住 / 把这个存起来" | 记、存、写入、备忘、save | `skills/memory-write.md` |
| "之前 X 是什么 / 我跟他聊过什么 / 翻一下记录" | 找、查、回忆、recall、之前、上次 | `skills/memory-recall.md` |
| "整理一下记忆 / 你怎么看 X / 总结最近" | 整理、反思、总结、凝固、reflect、dream | `skills/memory-reflect.md` |
| "重新初始化 / 第一次部署" | bootstrap、init、初始化、部署 | `skills/memory-bootstrap.md` |

## 兜底规则

- 用户消息里同时出现"记"和"问题/疑惑" → `memory-recall.md`（先查再说）
- 模糊请求（"你帮我处理一下"）→ 不要碰记忆系统，转给业务 Skill
- 任何对 GBrain 文件的**直接编辑请求** → 先 `memory-recall.md` 找到现有档案，再走 `memory-write.md` 的 update 路径，**禁止绕过 router**

## 数据来源 → 存储位置（提前固化的路由规则）

| 来源 | 类型 | 路由 |
|---|---|---|
| Gmail / Calendar / Wiki / Docs | 客观文档 | GBrain |
| 飞书 DM / 多轮对话 | 用户偏好、经验 | Hindsight |
| 会议纪要 | 文档主体 → GBrain；个人观察 → Hindsight | both |
| 巡逻发现的合规风险 | 事实 → GBrain；判断 → Hindsight | both |

详见 `config.yaml` 的 `routing_rules`。
