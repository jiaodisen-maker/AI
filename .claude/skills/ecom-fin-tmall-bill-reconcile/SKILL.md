---
name: ecom-fin-tmall-bill-reconcile
description: |
  tmall 平台货款/佣金/扣点月度对账。自动拉平台账单 + 推广消耗 + ERP 成交退款，
  三表对账，差异 > 1元标红，生成报告推送财务主管。Use when tmall 对账 /
  tmall 账单 / 月度对账 / 财务对账.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [tmall 对账, tmall 账单, 月度对账]
ecom: { domain: 10-finance, platform: tmall, role: 财务, frequency: monthly }
---

# tmall 月度对账

## Step 1: 登录后台
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
ensure_login tmall
$B cookie-import "$(cred_path tmall)"
```

## Step 2: 拉平台账单 + 推广消耗
导出 CSV 到 /tmp/tmall-bill-$(date +%Y%m).csv

## Step 3: 拉 ERP 成交 + 退款
从 ~/.zhongtai/scrm 或 ERP API。

## Step 4: Python 三表对账
```python
# 货款 = 成交 - 扣点 - 营销 - 退款
# 差异 > 1元 标红
```

## Step 5: 生成对账报告
Write 到 ~/.zhongtai/artifacts/ecom-fin-tmall-bill-reconcile/YYYYMM/report.md

## Step 6: 推送财务
```bash
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
feishu_card "tmall 月度对账" "$SUMMARY"
```

## 参考
v0 规范: /home/user/AI/skills/10-finance/fin-tmall-bill-reconcile/SKILL.md
