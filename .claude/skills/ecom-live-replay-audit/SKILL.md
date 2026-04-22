---
name: ecom-live-replay-audit
description: |
  直播回放抽审。下播后 2 小时内自动机审 100%，随机抽 20-30% 做深度审。
  ASR 转文字 + 分片违禁词扫 + 画面识别违规镜头 + 归档 ≥ 90 天。
  Use when 直播回放审 / 直播合规审 / 违规取证.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [直播回放审, 直播合规审, 违规取证]
ecom: { domain: 11-compliance, role: 合规, frequency: post-live }
---

# 直播回放审

## Step 1: 下载/流式拿到录播
```bash
# 平台 API 拿回放 URL 或录屏
```

## Step 2: ASR 分片转文字 (30s/片)
调 Whisper / 讯飞 / 阿里云 ASR。

## Step 3: 每片合规扫
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
for SEG in segments; do scan_forbidden "$SEG"; done
```

## Step 4: 画面识别
找「对比药品/医院/医生形象」镜头 (用多模态 LLM 或 CV)。

## Step 5: 必带声明频次校验
全程至少每 30 分钟口播一次「本品不能代替药物」。

## Step 6: 悬浮挂件全程校验
抽 10 帧图看是否挂齐资质。

## Step 7: 归档
存 ≥ 90 天 (建议 2 年，市监局可能查)。
