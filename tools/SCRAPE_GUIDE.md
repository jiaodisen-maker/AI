# 把 Coze 全站文档喂给 Claude 的操作手册

> 沙箱屏蔽 `docs.coze.cn` / `coze.cn` / `volcengine.com`，Claude 自己抓不到。
> 你**在自己电脑上**跑爬虫 → 推到 git → Claude 从 git 读。**不需要任何 PAT，全是公开文档。**

## 60 秒上手

```bash
git pull origin claude/compare-gbrain-hindsight-ROzjg
pip install httpx beautifulsoup4 html2text lxml
python tools/scrape-coze-docs.py
git add docs/coze-knowledge-base/raw/
git commit -m "scrape: coze docs"
git push
```

完事。告诉 Claude "已 push"。

## 爬什么

`scrape-coze-docs.py` 默认爬 4 个站点：

| 站点 | 内容 | 预估页数 |
|---|---|---|
| `coze_cn` | docs.coze.cn + coze.cn/open/docs | 100-300 |
| `volcengine_coze` | volcengine.com 上跟 Coze/Coze Pro 相关 | 30-80 |
| `cloudwego_eino` | Eino 框架（Coze 的编排引擎）| 30-50 |
| `github_coze` | coze-studio + coze-loop 仓库 wiki/README | 20-40 |

**总共 200-500 页 markdown，预计 30-60 分钟跑完，输出 5-30 MB**。

## 输出结构

```
docs/coze-knowledge-base/raw/
├── _index.json            url → 文件路径 + 标题 + 哈希（重要！Claude 用这个导航）
├── _failures.json         抓失败的 URL + 原因
├── coze_cn/
│   ├── cozespace/coze_billing_overview.md
│   ├── guides/teams.md
│   ├── api/open/docs/...
│   └── ...
├── volcengine_coze/
├── cloudwego_eino/
└── github_coze/
```

每个 .md 文件顶部有 frontmatter：
```yaml
---
source_url: https://docs.coze.cn/...
title: 'xxx'
site: coze_cn
scraped_at: 2026-05-04T08:00:00Z
---
```

## 常见问题

### Q1：跑一半中断了？
```bash
python tools/scrape-coze-docs.py --resume    # 接着之前的来
```

### Q2：只想爬某个站？
```bash
python tools/scrape-coze-docs.py --site coze_cn
python tools/scrape-coze-docs.py --site coze_cn --site cloudwego_eino
```

### Q3：抓下来的 .md 内容**几乎是空的**？
说明那个站点是 JS 渲染（SPA）的，`requests` 抓到的 HTML 里没有正文。
解决：换 Playwright 渲染版（告诉 Claude "docs.coze.cn 是 SPA"，他会写 `scrape-rendered.py`）。

### Q4：被对方反爬封 IP 了？
极少。`scrape-coze-docs.py` 已经：
- 间隔 300ms 一页（很慢很礼貌）
- 设置 User-Agent 标识来源
- 单站点 800 页上限

如真被封，挂个公司 VPN 或换网络重试。

### Q5：`_failures.json` 里有几十条失败？
正常。常见原因：
- 登录墙（部分企业管理页要登录才能看）
- 重定向到首页（已下线的旧页）
- 内容是 JS 渲染（见 Q3）

把 `_failures.json` 也提交，Claude 会按失败清单决定要不要单独处理。

## 备用方案（爬虫失败时）

### B1. wget 镜像
```bash
wget --recursive --no-parent --page-requisites --convert-links \
     --domains=docs.coze.cn \
     --user-agent="Mozilla/5.0" \
     --wait=0.5 \
     https://docs.coze.cn/
```
拿到 HTML 后再跑 `python tools/html-to-md.py`（如需要告诉 Claude 写）。

### B2. 浏览器扩展批量保存
- **MarkDownload** (Chrome/Firefox) — 一键当前页存 markdown
- **SingleFile** — 存为单 HTML 然后跑转换器
- 把保存的文件丢进 `docs/coze-knowledge-base/raw/manual/`

### B3. 复制粘贴（≤ 20 页核心内容）
按 `docs/coze-knowledge-base/_gaps.md` 列的 8 个优先页，逐个 Ctrl+A → 粘聊天。

## 增量更新

Coze 在迭代，文档每周都改。建议：
```bash
# 每两周跑一次（resume 模式只抓新页）
python tools/scrape-coze-docs.py --resume
git diff docs/coze-knowledge-base/raw/ | head -100   # 看变更
git add . && git commit -m "scrape: weekly update" && git push
```

Claude 看 git diff 就知道新版本改了什么。

## 之后 Claude 会怎么用

1. 读 `_index.json` 拿到全部 URL → 文件映射
2. 按主题归类（计费、工作流、Agent World、API、企业管理...）
3. 重写 `docs/coze-knowledge-base/01..07-*.md` 的每个章节，**全部基于原文引用** + 标 ★官方源
4. 更新 `_gaps.md`（应该全部勾掉）
5. 给你**真正基于完整数据**的能力盘点 + 落地方案 + 风险评估

## 隐私

爬虫抓的全部是 docs.coze.cn / coze.cn 的**公开文档**。
不需要 PAT，不抓你的 bot 数据，不抓客户对话。
你可以跑完前先 `cat docs/coze-knowledge-base/raw/_index.json` 看看抓了哪些 URL，确认没问题再 push。
