---
name: ecom-miniprogram-product-publish
description: |
  小程序商城商品上架。SKU + 主图/详情 + 资质合规 + SEO 标题。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [小程序上架, 小程序商品]
ecom: { domain: 03-private-domain, role: 运营, frequency: on-demand }
---

# miniprogram-product-publish

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
# Write to ~/.zhongtai/artifacts/ecom-miniprogram-product-publish/YYYYMMDD/
feishu_card "miniprogram-product-publish" "$REPORT"
exp_record "ecom-miniprogram-product-publish" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/miniprogram-product-publish/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
