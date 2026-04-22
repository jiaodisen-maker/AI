---
name: ecom-inv-inbound-receive
description: |
  保健品入库收货 SOP：扫描到货单 → 录入批号/生产日期/保质期 → 抽检合格率 →
  对应质检报告归档 → 上架到 ERP（旺店通/万里牛/聚水潭）。保健品每批次必录
  COA，绑定蓝帽子批号。Use when 收货 / 入库 / 到货 / 保健品入库.
allowed-tools: [Bash, Read, Write, AskUserQuestion]
triggers: [入库, 收货, 到货登记, 保健品入库]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: on-demand }
---

# 保健品入库收货

## Step 1: 收集到货信息
用 AskUserQuestion 拿: 供应商、PO 号、到货 SKU 清单、每个 SKU 的批号/生产日期/数量。若用户有到货单图片/PDF，用 Read 读出 OCR 结果。

## Step 2: 保健品专项校验
每个批号必录: `{生产日期, 保质期, 批号, COA 报告路径, 蓝帽子号}`。缺任何一项 → block + 要求补充。

## Step 3: 抽检比例计算
按批次大小算抽检样本（<1000: 5%, 1000-10000: 3%, >10000: 1%），生成抽检指令卡。

## Step 4: 录入 ERP
```bash
# 调 ERP API (旺店通/万里牛/聚水潭) 写入库单
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source "$(cred_path erp env)"
curl -X POST ... # 具体接口取决于 ERP
```
或导出 CSV 让用户手工导入。

## Step 5: COA 归档
质检报告 PDF 存 `~/.zhongtai/qc-reports/<批号>/<SKU>.pdf`，建索引。

## Step 6: 经验沉淀 + 飞书推送
```bash
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
exp_record ecom-inv-inbound-receive "..."
```

## 参考规范
详见 `/home/user/AI/skills/09-supply-chain/inv-inbound-receive/SKILL.md` (v0 spec)
