---
name: ecom-27-function-validator
description: |
  保健品蓝帽子 27 项功能校验。核对宣传文案的功效声明是否 (1) 在 27 项之内
  (2) 与本产品蓝帽子备案一致 (3) 未扩大宣传。broader/unrelated 必改。
  Use when 校验功效声明 / 27项功能 / 蓝帽子校验 / 功效是否符合备案.
allowed-tools: [Bash, Read, Write]
triggers: [校验功效, 27项功能, 蓝帽子校验, 功效符合备案]
ecom: { domain: 11-compliance, role: 合规, frequency: on-demand }
---

# 蓝帽子 27 项功能校验

## Step 1: 拿输入
文案文本 + 蓝帽子号 (`国食健字G20xxxxxx`)。缺了问一次。

## Step 2: 执行校验
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
validate_27_function "$CLAIM" "$BLUE_CAP_NUMBER"
```

## Step 3: 处置
- `exact` → pass
- `narrower` → pass + 提示「可用但过保守」
- `broader_or_unrelated` → **block 必改**
- `no_27_function_claim` → 文案未涉功效，跳过

## Step 4: 联动
若命中 broader，自动触发 `ecom-ad-copy-rewrite` 给改写建议。
