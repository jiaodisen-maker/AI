---
name: ecom-qualification-upload-checklist
description: |
  保健品多平台资质上传清单。按平台 (tmall/jd/pdd/douyin/kuaishou/
  shipinghao/xiaohongshu/wechat) 生成各自缺失资质 + 上传位置路径 + 有效期追踪。
  Use when 平台开店资质 / 新品上架资质 / 类目报白.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [平台开店资质, 新品上架资质, 类目报白, 蓝帽子上传]
ecom: { domain: 11-compliance, role: 合规, frequency: on-store-open }
---

# 资质上传清单

## Step 1: 拉目标平台最新要求
用 WebFetch 抓各平台规则中心 (见 ecom-platform-health-rule-monitor)。

## Step 2: 对比内部资质库 `~/.zhongtai/qualifications/`
必备: 营业执照, SC 生产许可 (保健食品), 保健食品注册/备案证书, 广告批文, 质检报告。

## Step 3: 输出缺失清单 + 上传路径
- 天猫: 商家中心 → 店铺 → 资质管理
- 抖店: 资质中心 → 行业资质
- 其他平台类似

## Step 4: 到期追踪 (调 ecom-qualification-expiry-tracker)
