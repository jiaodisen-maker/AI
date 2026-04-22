---
name: ecom-live-script-precheck
description: |
  直播脚本开播前合规预审。分段 (开场/讲品/demo/价格/催单/承接/下播)，
  每段扫违禁词 + 27项校验 + 必带声明频次 + demo 内容合规。
  Use when 直播脚本审核 / 开播前过合规 / 主播培训卡.
allowed-tools: [Bash, Read, Write]
triggers: [直播脚本审核, 开播前过合规, 主播培训卡]
ecom: { domain: 11-compliance, role: 合规, frequency: per-live-session }
---

# 直播脚本预审

## Step 1: 分段
按主播动作分 7 段。

## Step 2: 每段跑合规
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
for SEG in ...; do scan_forbidden "$SEG"; done
```

## Step 3: 校验必带
全场「本品不能代替药物」≥ 每 30 分钟一次 + 悬浮挂件资质。

## Step 4: 校验 demo
不得「对比药品」「当场治病」「前后对比展示疗效」。

## Step 5: 主播资质 vs 声明权限
普通主播不可做医学建议；营养师/药师需挂证。

## Step 6: 输出
- compliance_report.md
- anchor_training_card.md (口播禁语清单)
