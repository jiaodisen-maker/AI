---
name: ecom-platform-health-rule-monitor
description: |
  各平台保健品规则更新监控。每周扫天猫/京东/抖店/小红书/拼多多/视频号
  规则中心近 7 天公告，对比本地规则快照，识别变动 + 影响分析。
  Use when 平台规则更新 / 合规规则监控 / 行业规则.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [平台规则更新, 合规规则监控, 行业规则]
ecom: { domain: 11-compliance, role: 合规, frequency: weekly }
---

# 平台规则监控

## Step 1: 用 gstack browse 抓规则中心
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
for URL in \
  "https://rules.tmall.com" \
  "https://rule.jd.com" \
  "https://school.jinritemai.com" \
  "https://help.xiaohongshu.com" \
  "https://rule.pinduoduo.com"; do
  $B goto "$URL"; $B wait --networkidle
  $B text >> /tmp/rules-$(date +%Y%m%d).txt
done
```

## Step 2: 过滤关键词
grep "保健食品|滋补|健康|医疗|广告|类目"。

## Step 3: diff 本地快照
```bash
SNAP=~/.zhongtai/rule-snapshots/latest.txt
diff $SNAP /tmp/rules-$(date +%Y%m%d).txt > /tmp/rules-diff.txt
```

## Step 4: LLM 生成影响摘要
哪些 skill 需更新，哪些素材要重审。

## Step 5: 飞书推送 + 更新快照
