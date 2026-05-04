# 缺口清单（已基本关闭）

> 2026-05-04 更新：抓了 951 页之后，原来的 8 项缺口几乎都补上了。
> 仅剩 1 项需要走商务通道。

## 已补全的（在 `raw/` 里都能查到）

| # | 之前缺什么 | 现在在哪 |
|---|---|---|
| ① 计费总览 | ✅ `raw/coze_cn/coze_pro/billing_overview.md` |
| ② 模型费用 | ✅ `raw/coze_cn/coze_pro/model_fee.md` + `doubao_resource_pack.md` |
| ③ 内置集成费用 | ✅ `raw/coze_cn/coze_pro/internal_integrations_fee.md` |
| ④ 企业版管理员手册 | ✅ `raw/coze_cn/coze_pro/enterprise_plan.md` + `payer.md` + `member_fee.md` |
| ⑤ Open API 限流 | ✅ `raw/coze_cn/developer_guides/api_*.md`（195 页里有）|
| ⑥ Agent World 文档 | ✅ `raw/coze_cn/cozespace/*.md`（27 页全套）|
| ⑦ Coze Loop 接入指南 | ✅ `raw/coze_cn/cozeloop/*.md`（120 页全套）|

## 仍未补的（不影响落地决策）

| # | 缺什么 | 怎么办 |
|---|---|---|
| ⑧ Coze Pro **私有部署** vs HiAgent 详细对比 | 不在公开文档里——走商务通道。或者直接看 GitHub `coze-dev/coze-studio`（已抓 `raw/github_coze/`）做自部署评估 |

## 后续维护

发现新版本 / 新功能 / 新文档时：

```bash
python tools/scrape-coze-docs-rendered.py --site coze_cn --resume
git diff docs/coze-knowledge-base/raw/ | head -100
```

新增内容 → 更新 `PLAN.md` / `SALES-BOT.md` 的相关章节，带日期注释。
