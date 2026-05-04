# 部署指南

## 30 秒决策

| 选项 | 推荐度 | 理由 |
|---|---|---|
| **火山引擎 ECS（杭州 / 北京）** | ⭐⭐⭐⭐⭐ | 跟 Coze 企业版同账户，KMS 共用，内网到 Coze 后端低延迟，账单合并 |
| 阿里云 / 腾讯云 ECS | ⭐⭐⭐⭐ | 团队熟悉，可选；缺点：跨云走公网到 Coze |
| 公司自有机房 | ⭐⭐⭐ | 数据全可控；缺点：公网入口 + HTTPS 自己搞 |
| 火山 VKE (K8s) | ⭐⭐ | 800 人量级用不上，复杂 |
| Cloudflare Tunnel + 任意 | ⭐⭐⭐ | 不用买公网 IP，但生产用要小心 |

**推荐路径**：起步 1 台火山 ECS + Docker Compose；2 个月后升级到 2 台 + ALB + RDS。

## 文件

| 文件 | 内容 |
|---|---|
| `01-volcengine-ecs.md` | 火山 ECS 最小部署（4 小时完成）|
| `02-go-live-checklist.md` | 上线前/后必跑检查清单 |
| `03-production-ha.md` | 生产高可用升级（双实例 + ALB + RDS + KMS）|
| `04-runbook.md` | 故障排查 SOP |

## 起步路径

```
Day 1   01-volcengine-ecs.md      最小部署上线（4 小时）
Day 2   02-go-live-checklist.md    跑完所有验收
Week 2  03-production-ha.md        生产化加固
持续    04-runbook.md              出问题查这个
```
