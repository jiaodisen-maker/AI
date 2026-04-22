---
name: ecom-kol-script-precheck
description: |
  KOL/达人稿预审。包含: 达人粉丝量核对（保健食品禁"具有一定影响力"达人代言）、
  违禁词、报备标识、广告标、必带声明、demo 合规、合同违约条款建议。
  Use when 达人稿审核 / KOL 稿合规 / 蒲公英报备前检查.
allowed-tools: [Bash, Read, Write]
triggers: [达人稿审核, KOL 稿合规, 蒲公英报备前检查]
ecom: { domain: 11-compliance, role: 合规, frequency: per-cooperation }
---

# KOL 稿预审

## Step 1: 核对达人粉丝量
保健品: 粉丝 > 100万 视为"具有一定影响力"，受限。

## Step 2: 跑合规
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
scan_forbidden "$KOL_DRAFT"
validate_27_function "$KOL_DRAFT" "$BLUE_CAP"
```

## Step 3: 必带元素检查
蒲公英 / 星图 报备标识 + 广告标 + "本品不能代替药物"。

## Step 4: 输出
- review_comments.md
- final_script.md
- contract_clauses.md (违规罚则金额建议)
