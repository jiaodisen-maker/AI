# 缺口清单 —— 需要你贴的内容

> 沙箱防火墙挡了 docs.coze.cn / coze.cn / volcengine.com / csdn.net 等所有相关域名（403）。
> 下面这几页你**复制粘贴**给我，我把对应文件补完。每页贴完都注明 `-- 已补于 2026-MM-DD`。

## ① 计费总览原文（最优先）

**URL**：https://docs.coze.cn/cozespace/coze_billing_overview

**我要从这页拿到**：
- 各版本完整对比表（避免我搜来的数字过期）
- 资源点的精确换算公式
- 7 大计费项的精确单价
- 资源包/续费的具体价格
- "超额"的处理策略（停服 / 自动扣费 / 通知）

**贴的方式**：直接全文粘贴到聊天，我会写进 `02-versions-and-pricing.md` 标注 `★官方源`。

---

## ② 模型费用页

**URL**：https://www.volcengine.com/docs/84458/1585097

**我要拿到**：
- Doubao 全系列单价（input/output/cache）
- DeepSeek 单价
- Claude 单价（如果支持）
- 微调模型单价
- 视频/视觉模型单价

---

## ③ 内置集成费用页

**URL**：https://www.volcengine.com/docs/84458/2123431

**我要拿到**：
- 插件调用单价
- 知识库存储 GB·月单价
- 音视频服务单价
- Trace 上报单价（超过套餐配额后）
- 记忆库存储单价
- 云电脑 / 云手机 / 邮箱使用费率（2.5 新加的）

---

## ④ 企业版管理员手册

**URL**：https://www.coze.cn/open/docs/tutorial/internal_enterprise_permission_management

**我要拿到**：
- 角色定义具体权限点（owner / admin / member 各能干什么不能干什么）
- 工作空间隔离机制（数据/资源/计费）
- 部门管理（多级组织树）
- 审计日志能查什么
- 月预算上限怎么设
- 外部用户管控具体规则

---

## ⑤ Open API 限流文档

**URL**：https://www.coze.cn/open/docs/api/...（具体路径未知）

**我要拿到**：
- 各端点的 RPM/RPS 限制
- 限流触发的 HTTP 状态码和重试建议
- 企业版 12,000 RPM 是怎么分摊的（per workspace / per bot / per PAT？）

---

## ⑥ Agent World 相关文档

**URL**：https://docs.coze.cn/cozespace/...（具体子目录未知）

**我要拿到**：
- 云电脑 / 云手机 / 邮箱的具体启用流程
- 这些资源的并发限制（一个 Agent 能开几台云电脑？）
- 数据持久化策略（重启会清吗？）
- 跨 Agent 通信协议

---

## ⑦ Coze Loop 接入指南

**URL**：https://github.com/coze-dev/coze-loop/wiki 部分能看，但企业版接入文档需要从 docs.coze.cn 拿

**我要拿到**：
- 企业版 SaaS 的 Loop 是单独开还是默认开？
- 200 万 Trace/月是按工作空间还是按企业整体？
- 评测集怎么导入 / 导出
- 跟自部署 Loop 的差异

---

## ⑧ 私有化部署官方说明

**URL**：未知，可能在 https://www.volcengine.com/product/coze-pro 或合作通道

**我要拿到**：
- Coze Pro 是否支持完全私有化（VPC 之上的私有部署）
- 私有化定价
- 私有化能不能用 Agent World

---

## 贴的时候请注明每页的「页面标题 + URL + 抓取日期」

格式建议：

```
### 页面：扣子计费总览
URL: https://docs.coze.cn/cozespace/coze_billing_overview
抓取日期: 2026-05-04

<这里粘正文>
```

我看到这个格式自动把内容写进对应的 .md 文件，加上 `★官方源` 标记和引用。

---

## 不需要你贴的（我已经搜到 90%）

- ✅ 套餐核心数字（02-versions-and-pricing.md 已写）
- ✅ Coze 2.5 Agent World 主要能力（03-coze-2.5-features.md 已写）
- ✅ 企业版主要特性（04-enterprise-edition.md 已写）
- ✅ Eino / FlowGram 架构（01-platform-overview.md 已写）
- ✅ vs HiAgent / Coze Studio（07-comparison.md 已写）
