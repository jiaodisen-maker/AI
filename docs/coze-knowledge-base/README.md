# Coze 知识库（内部参考）

> 整理自 2026-05 的公开信息。后续做方案时**优先引用本目录**，避免又去网上拍脑袋。

## 文件索引

| # | 文件 | 内容 |
|---|---|---|
| 01 | `01-platform-overview.md` | 平台架构（Eino / FlowGram / Hertz / VikingDB）|
| 02 | **`02-versions-and-pricing.md`** | **套餐对比 + 计费规则**（今天重点装的）|
| 03 | `03-coze-2.5-features.md` | Agent World / 云电脑 / 云手机 / 独立邮箱 / Skills / Plan |
| 04 | `04-enterprise-edition.md` | 企业版独有特性、SLA、安全、私有化选项 |
| 05 | `05-coze-loop.md` | 评测 + 观测 + 提示词管理（开源 Apache 2.0）|
| 06 | `06-knowledge-base-rag.md` | KB 切片策略、混合检索、命中率优化 |
| 07 | `07-comparison.md` | Coze Pro vs HiAgent vs Coze Studio 自部署 vs Dify/FastGPT |
| 08 | `_gaps.md` | **我搜不到、需要你复制粘贴给我的页面清单** |

## 信息来源说明

本目录的内容来自：
- 字节/火山公开发布稿（aitop100、chinaz、QQ News、Sohu 等）
- coze-dev/coze-studio 和 coze-dev/coze-loop 的 GitHub 仓库
- CloudWeGo 的 Eino 框架文档
- 第三方测评（53AI、cnblogs、developer.volcengine 文章）

**不来自**：
- ❌ docs.coze.cn 原始页（被沙箱防火墙 block，403）
- ❌ Volcengine 官方计费明细页（同上）
- ❌ CSDN/知乎/掘金深度文章（同上）

因此所有具体数字以官方文档为准。本目录里**任何数字 ± 10% 内可信**，但不应直接拿去签合同。

## 维护规约

- 看到新版本/新功能 → 在对应文件里加一节，**别开新文件**
- 数字过期了 → 划线保留 + 加新数字 + 注明日期，**别直接覆盖**（保留版本对比能力）
- 引用本目录时写 `docs/coze-knowledge-base/02-versions-and-pricing.md#企业版`，不要复制粘贴数字到处散
