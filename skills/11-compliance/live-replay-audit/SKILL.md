---
name: live-replay-audit
domain: 11-compliance
platform: douyin | kuaishou | shipinghao | xiaohongshu | tmall | jd
role: 合规
frequency: post-live
inputs:
  - live_session_id
  - replay_url
outputs:
  - 违规时间戳清单 + 截图
  - 合规评分 + 改进建议
human_review_required: true
compliance_filter: false
data_sources:
  - 直播平台回放接口 / 录屏
  - 违禁词库
allowed-tools:
  - Bash
  - Read
  - Write
  - WebFetch
---

# 直播回放抽审 (`live-replay-audit`)

## 何时调用
每场直播下播后 2 小时内自动抽审；随机抽 20-30% 场次做深度审；全量做机审。

## 输入
- **live_session_id** — 直播场次 ID
- **replay_url** — 录播地址

## 输出
- `violation_log.md` — 时间戳 + 违规内容 + 截图
- `compliance_score` — 0-100
- `improvement_list` — 下次开播前主播/脚本改进项
- `archive_path` — 录播 + 违规取证文件 ≥ 90 天保存

## Workflow
1. 下载录播 (或流式抽帧)
2. ASR 语音转文字 (分片 30s)
3. 每片跑 `forbidden-word-scan` + `27-function-validator`
4. 画面识别: 识别"对比药品""医院场景""医生形象"违规镜头
5. 悬浮挂件检查: 资质挂件是否全程在线
6. 必带声明频次: 每 30 分钟是否口播"本品不能代替药物"
7. 生成违规时间戳 + 对应截图
8. 归档到合规留存库 (保存 ≥ 90 天, 建议 2 年)

## 违规等级
- 🔴 critical: 疗效断言、替代药品、明星背书 → 触发下播/限流/起诉准备
- 🟠 high: 绝对化用语、缺必带声明 → 次日整改 + 扣罚主播
- 🟡 medium: 语境擦边 → 脚本修订
