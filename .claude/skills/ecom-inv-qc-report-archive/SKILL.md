---
name: ecom-inv-qc-report-archive
description: |
  保健品质检报告 (COA) 按批次归档。上传 PDF → OCR 提取关键指标 (重金属/菌落/
  主成分含量) → 对比批准标准 → 入库 + 飞书归档索引。Use when 归档质检 /
  COA 存档 / 质检报告入库.
allowed-tools: [Bash, Read, Write]
triggers: [归档质检, COA 存档, 质检报告入库]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: on-demand }
---

# 质检报告归档

## Step 1: 拿到 PDF + 对应批号
用 AskUserQuestion 拿: 批号、SKU、PDF 路径、出报告机构。

## Step 2: OCR 提取关键指标
用 Bash + pdftotext (或 Python pdfplumber)：
- 重金属: 铅/砷/汞 mg/kg
- 菌落总数: cfu/g
- 主成分含量 (如胶原蛋白肽 g/100g)
- 感官/水分/灰分

## Step 3: 对比批准标准
读 `~/.zhongtai/qc-standards/<sku>.json` 的上下限，任一超标 → 🔴 block + 不入库 + 飞书告警品控部。

## Step 4: 归档
移 PDF 到 `~/.zhongtai/qc-reports/<批号>/<sku>_YYYYMMDD.pdf`，建索引条目：
```json
{"batch":"...","sku":"...","report_path":"...","pass":true,"indicators":{...}}
```
追加到 `~/.zhongtai/qc-reports/index.jsonl`。
