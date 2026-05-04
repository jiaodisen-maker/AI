---
name: memory-reflect
description: 触发反思 + 凝固——把 Hindsight 中稳定的 belief/entity 写出为 GBrain markdown，并把 GBrain 新文档反向索引为 World Facts
trigger:
  - 整理一下 / 总结最近 / 凝固 / dream
  - reflect / consolidate
inputs:
  scope:
    - recent     # 最近 24h（默认，便宜）
    - all        # 全量（贵，建议每周一次）
    - entity:<ref>  # 仅针对某个实体
  dry_run: 默认 false；true 时只报告会做什么但不写
---

# Skill: memory-reflect

## 目标
执行睡眠时的"记忆固化"：

- ✅ 稳定的 Hindsight Entity Summaries → 写入/更新 GBrain markdown
- ✅ 高置信度 Beliefs → 追加到对应 GBrain 档案的 `## 观察` 段
- ✅ GBrain 新增/修改的文档 → 摘要回灌进 Hindsight `world_facts` 网络
- ✅ 冲突（新 belief 与旧档案矛盾）→ 不自动改，转给人审

## 步骤

1. **调 MCP `memory_reflect`**
   ```
   memory_reflect(scope="recent", dry_run=False)
   ```
   底层执行 `scripts/auto_dream.consolidate(scope)`。

2. **接收报告**
   ```
   {
     "consolidated_entities": 7,       # 凝固成 markdown 的实体数
     "appended_beliefs": 12,            # 追加到档案的 belief 数
     "indexed_docs": 23,                # 反向灌进 Hindsight 的新文档
     "conflicts": [                     # 不自动改的冲突
       {"path": "brain/people/zhangsan.md",
        "old": "...", "new": "...", "ticket": "T_5521"}
     ],
     "duration_ms": 18234
   }
   ```

3. **处理冲突**
   - 每个 `conflict` → 通过飞书 Bot 推一条审核消息给负责人
   - 审核通过 → 调 `memory_write(..., hints={"override": True})` 走正式更新

4. **告诉用户**
   - 简报形式：`今晨整合：7 个档案更新，12 条新观察，23 篇文档入库，2 条冲突待审`

## 调度建议

- **守护进程模式**（推荐）：`scripts/auto_dream.py --cron` 每小时跑一次 `scope=recent`
- **OpenClaw 主动调用**：用户明确说"整理一下"或"总结最近"才调
- **每周日凌晨**：跑一次 `scope=all` 做完整对账

## 边界 / 不要做的事

- ❌ 凝固时**绝不**自动覆盖 GBrain 已有内容——冲突一律走 human_review
- ❌ 不要把低置信度（< 0.80）或新生（< 24h）的 belief 写进 GBrain
- ❌ 凝固后 Hindsight 那条记忆**保留**（标记 archived），不要删，给审计用
