---
name: ecom-ad-copy-rewrite
description: |
  不合规文案自动改写。读 replacement-dict.json 对应命中词的合规替代，
  重构句子保留卖点，再过 forbidden-word-scan 验证。Use when 改文案 /
  合规改写 / 帮我改一下 / rewrite copy.
allowed-tools: [Bash, Read, Write]
triggers: [改文案, 合规改写, rewrite copy, 帮我改一下]
ecom: { domain: 11-compliance, role: 合规, frequency: on-demand }
---

# 合规改写

## Step 1: 接收原文 + 违规报告
若用户未提供报告，先跑 `ecom-forbidden-word-scan`。

## Step 2: 查替代词
```bash
DICT=/home/user/AI/.claude/skills/_ecom/data/replacement-dict.json
# 每个命中词 → 查替代
```

## Step 3: LLM 重写
保留卖点 + 语气，用替代词重构句子。谐音黑话类直接删除段落。

## Step 4: 二次过审
再跑 forbidden-word-scan 验证。若仍命中 critical → 放弃自动改写 + 返回人工。

## Step 5: 输出 diff
原 vs 改后 对比表。

## Step 6: 经验沉淀
若用户后续调整了改写版本，把 {auto_rewrite, human_final} 入 experience.jsonl。
