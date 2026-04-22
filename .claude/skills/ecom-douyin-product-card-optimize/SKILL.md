---
name: ecom-douyin-product-card-optimize
description: |
  抖音商品卡 SEO 优化 (2026 货架场重点)。标题关键词 + 属性 + 详情页 + 价格力标签。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [商品卡优化, 抖音搜索, 商品卡 SEO]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# douyin-product-card-optimize

## Step 1: 基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
```

## Step 2: 核心动作
自主登录对应平台, 执行 description 所述动作. 内容类必过 `scan_forbidden` 违禁词 + `validate_27_function` 蓝帽子校验.

## Step 3: 输出 + 飞书推送
```bash
# Write to ~/.zhongtai/artifacts/ecom-douyin-product-card-optimize/YYYYMMDD/
feishu_card "douyin-product-card-optimize" "$REPORT"
exp_record "ecom-douyin-product-card-optimize" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/douyin-product-card-optimize/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
