---
name: testimonial-compliance-check
domain: 11-compliance
platform: all
role: 合规
frequency: on-demand
inputs:
  - testimonial: 用户见证/案例原文
  - media: 图文 / 视频 / 朋友圈 / 直播
outputs:
  - 合规修订版 + 风险评估
human_review_required: true
compliance_filter: false
data_sources:
  - 违禁词库
  - 广告法第 16/38 条
allowed-tools:
  - Read
  - Write
---

# 用户见证/案例合规 (`testimonial-compliance-check`)

## 何时调用
征集的用户证言/前后对比/打卡素材要公开传播前。

## 输入
- **testimonial** — 用户原话 + 图片/视频描述
- **media** — 使用媒介

## 输出
- `rewritten_testimonial` — 改写版
- `risk_assessment` — 风险点
- `permission_check` — 用户是否签授权书

## Workflow
1. 扫疗效词: 治好 / 根治 / 见效 / 瘦了 X 斤 / 等
2. 扫医生/机关/患者形象: 不得以"医生推荐""患者证言"表述
3. 扫医院/药品关联: 不得对比药品/医院
4. 前后对比图: 不得暗示疗效
5. 改写: 保留用户"使用感受", 去掉"疗效断言"
6. 要求用户签《授权书》: 肖像权 / 内容使用权 / 合规声明

## 改写示例
| 用户原话 | 合规改写 |
|---------|---------|
| 吃了三个月,血糖降下来了 | 坚持吃了三个月,饮食+运动配合下身体状态感觉轻松了 |
| 我老公高血压,吃这个好了 | 我家里人长期配合健康饮食 |
| 再也不用吃药了 | (删除,不可改写) |

## 授权书要点
- 用户知晓自己的案例会用于商业宣传
- 品牌不保证相同效果
- 用户保留随时撤回授权的权利
