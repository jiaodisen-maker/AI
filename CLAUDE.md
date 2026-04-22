## Skill routing

When the user's request matches an available skill, ALWAYS invoke it using the Skill
tool as your FIRST action. Do NOT answer directly, do NOT use other tools first.
The skill has specialized workflows that produce better results than ad-hoc answers.

Key routing rules:
- Product ideas, "is this worth building", brainstorming → invoke office-hours
- Bugs, errors, "why is this broken", 500 errors → invoke investigate
- Ship, deploy, push, create PR → invoke ship
- QA, test the site, find bugs → invoke qa
- Code review, check my diff → invoke review
- Update docs after shipping → invoke document-release
- Weekly retro → invoke retro
- Design system, brand → invoke design-consultation
- Visual audit, design polish → invoke design-review
- Architecture review → invoke plan-eng-review
- Save progress, checkpoint, resume → invoke checkpoint
- Code quality, health check → invoke health

## 保健品中台 (ecom-*) 冷启动守卫

任何 `ecom-*` skill (除 `ecom-bootstrap` / `ecom-shared` 自己) 被调用时，若
`~/.zhongtai/.initialized` 不存在，**必须先触发 `/ecom-bootstrap`** 做冷启动初始化。
bootstrap 跑完后再回到原来的 skill。

ecom 体系的架构：
- `ecom-bootstrap` — 首次用必跑；配平台登录 cookie / 品牌档案 / 飞书 webhook / ERP / 蓝帽子备案 / 竞品库
- `ecom-shared` — 共享 bash 库 (dataroot / credentials 自愈登录 / feishu 推送 / platform 常量); 不直接调
- `ecom-blue-cap-sync` — 自动抓本司所有蓝帽子备案入库
- `ecom-ps-competitor-seed` — 自动发现竞品并入库
- 其他 223 个业务 skill — 在 Step 1 source `ecom-shared/lib/*`，所有数据从 `~/.zhongtai/` 读写

中台数据根目录约定：`~/.zhongtai/` (可用 `ZHONGTAI_HOME` 环境变量覆盖)
- `credentials/platforms/*.json` — 各平台登录 cookie (chmod 600)
- `config.json` — 品牌 / 店铺 / ERP / webhook
- `data/products/blue-cap-registry.json` — 本司所有 SKU + 备案
- `data/competitors/seed.json` — 竞品清单
- `artifacts/{daily,weekly,monthly}/` — 报告产物 (按时间戳)
- `logs/` — 登录日志 / 爬虫日志 / 合规命中
