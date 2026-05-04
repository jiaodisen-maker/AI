---
name: memory-recall
description: 跨 GBrain + Hindsight 检索，RRF 融合，返回结果自带来源标签
trigger:
  - 之前 / 上次 / 翻一下 / 查一下
  - recall / find / lookup
inputs:
  query: 自然语言问题或关键词（必填）
  k: 返回条数，默认 5
  filter:
    source_only: 限定来源 KB | MEM | both（默认 both）
    subject_ref: 限定实体
---

# Skill: memory-recall

## 目标
回答"我之前/我们之间存过什么相关的"。

## 步骤

1. **调 MCP `memory_recall`**
   ```
   memory_recall(query="张三上次提的续约", k=5)
   ```

2. **接收返回**
   返回数组，每条包含：
   ```
   {
     "id": "...",
     "text": "...",
     "score": 0.87,
     "source": "KB" | "MEM",
     "ref": "brain/people/zhangsan.md" 或 "m_9011",
     "ts": "2026-04-30T10:00Z"
   }
   ```

3. **呈现给用户/上游 Agent**
   - **必须保留 `[KB]` / `[MEM]` 标签**——下游 LLM 要用它判断"客观档案 vs 主观印象"
   - 同一实体的 KB + MEM 命中归为一组，KB 在上、MEM 在下
   - 标注时间戳，让用户判断时效

4. **降级**
   - Hindsight 超时 → 仅返回 KB 结果，文末注明 `(working memory unavailable)`
   - GBrain 超时 → 仅返回 MEM 结果，文末注明 `(knowledge base unavailable)`

## 边界 / 不要做的事

- ❌ 不要把 `[MEM]` 当事实陈述给用户（它是 Agent 的主观记忆）
- ❌ 不要把检索结果直接重写回 GBrain（凝固走 reflect）
- ❌ 不要做"猜测式补全"——查不到就如实说没有

## 例子

> 用户："张三上次跟我聊续约说了啥"
>
> Skill 调用：`memory_recall("张三 续约", k=5)`
>
> 返回（节选）：
> ```
> [KB] brain/people/zhangsan.md  (2026-04-12)
>   合同到期日 2026-09-30，去年续约由 King 经手
> [MEM] m_9011                    (2026-04-30)
>   倾向于 Q3 续约，对价格敏感（置信度 0.78，3 次观察）
> ```
>
> 回复用户：原样保留标签，不要拼成一段去掉来源。
