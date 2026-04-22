---
name: ecom-cs-presale-consult-reply
description: |
  售前咨询应答。合规口径回答成分/功效/适用人群/服用方法，敏感问题 (有病能不能吃)
  模板回答 + 建议咨询医生。出答前过违禁词。Use when 售前回复 / 客服答疑.
allowed-tools: [Bash, Read, Write]
triggers: [售前回复, 客服答疑, 咨询回复]
ecom: { domain: 08-customer-service, role: 客服, frequency: on-demand }
---

# 售前咨询回复

## Step 1: 识别问题类别
成分 / 功效 / 适用人群 / 服用方法 / 有效期 / 运输 / 对比其他 / 敏感 (疗效)

## Step 2: 查 FAQ 库
~/.zhongtai/faq/<category>.md 拿标准答案。

## Step 3: 合规改写
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
scan_forbidden "$REPLY"
```

## Step 4: 敏感问答
"XX 病能不能吃" → 不回答具体病症, 回 "建议咨询医生, 本品不能代替药物"。

## Step 5: 必带
全部回复含 "本品不能代替药物治疗疾病" 或等效表述。
