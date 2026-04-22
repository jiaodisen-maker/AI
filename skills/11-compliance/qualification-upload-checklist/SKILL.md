---
name: qualification-upload-checklist
domain: 11-compliance
platform: all
role: 合规
frequency: on-store-open | on-product-launch
inputs:
  - platform
  - product_sku
outputs:
  - 资质清单 + 各平台上传路径 + 是否齐全
human_review_required: false
compliance_filter: false
data_sources:
  - 内部资质库
allowed-tools:
  - Read
  - Bash
---

# 资质上传清单 (`qualification-upload-checklist`)

## 何时调用
新店铺开通 / 新品上架 / 类目报白 / 达人合作前。

## 输入
- **platform** — tmall | jd | pdd | douyin | kuaishou | shipinghao | xiaohongshu | wechat
- **product_sku** (选填)

## 输出
- 需上传资质清单 (markdown 表格)
- 各平台对应上传位置
- 资质有效期 + 到期提醒

## 必备资质 (保健品)
| 资质 | 必备 | 备注 |
|------|------|------|
| 营业执照 | ✅ | 食品经营/保健食品经营 范围 |
| 食品生产许可证 (SC) | ✅ | 保健食品类 |
| 保健食品注册证书 / 备案凭证 | ✅ | 蓝帽子 |
| 广告批文 (国食健广审字) | 建议 | 做广告投放必备 |
| 产品质检报告 / COA | ✅ | 按批次 |
| 法人身份证 | ✅ | |
| 商标注册证 | 建议 | 品牌方必备 |
| 授权书 | 代理商需 | 品牌方出具 |
| 进口保健食品: 进口商备案 | 跨境必备 | |

## 平台上传位置 (示例)
- 天猫: 商家中心 → 店铺 → 资质管理
- 抖店: 资质中心 → 行业资质
- 小红书: 千帆 → 店铺设置 → 资质管理
- 京东: 商家后台 → 店铺 → 资质
- 拼多多: 商家后台 → 资质信息
- 视频号: 小店后台 → 资质

## Workflow
1. 查询平台最新资质要求 (用 [platform-health-rule-monitor](../platform-health-rule-monitor/))
2. 对比内部资质库
3. 输出缺失资质清单
4. 对每个资质生成"上传 SOP"卡片
5. 标记到期 ≤ 90 天的资质
