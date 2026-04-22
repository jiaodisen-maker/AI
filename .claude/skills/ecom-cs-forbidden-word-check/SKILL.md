---
name: ecom-cs-forbidden-word-check
description: |
  客服外发话术违禁词检测。Wrapper of ecom-forbidden-word-scan for 实时客服
  对话监控 / 批量话术库审核。Use when 客服话术合规 / 客服违禁词.
allowed-tools: [Bash, Read, Write]
triggers: [客服话术合规, 客服违禁词]
ecom: { domain: 08-customer-service, role: 客服, frequency: on-demand }
---

# 客服话术违禁词

## Step 1: 输入
- 实时: 单条客服回复前扫
- 批量: FAQ 库全扫

## Step 2: 调用底层
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
scan_forbidden "$REPLY"
```

## Step 3: 命中阻断
critical → block 发送 + 提示客服改写.

## Step 4: 统计
每月统计各客服违禁词命中率, 纳入绩效.
