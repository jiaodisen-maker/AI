# 上线检查清单

> Day 1 部署完成后跑这 30 项。任一不过 → 修。

## 网络
```
□ https://bridge.your-company.com/healthz 返回 200
□ Caddy 证书是 Let's Encrypt（不是 self-signed）
□ ECS 安全组只开 22/80/443
□ /metrics 端口（9100）只能内网访问
□ 飞书后台事件订阅"测试通过"
```

## 飞书侧
```
□ 应用权限审批通过（不是"待审批"）
□ 13 类事件全部勾选
□ 应用已发布到企业（不是测试版）
□ Bot 头像、名字配好
```

## Coze 侧
```
□ PAT 有效期 ≥ 90 天
□ 至少有 1 个 bot 配好（销售助手）
□ 至少有 1 个 KB 配好（kb_sop）
□ Coze 企业旗舰版状态正常（不是欠费/到期警告）
□ Coze 工作空间外部集成已开启飞书相关
```

## Bridge 服务
```
□ docker compose ps 全 Up + Healthy
□ 8 个容器：postgres/redis/bridge/3×worker/token-refresher/backfill/caddy
□ token-refresher 1 小时内续过一次（看日志）
□ backfill 跑过启动时回填（看日志）
□ Postgres 能连接（docker exec）
□ Redis Streams 已建 consumer group
```

## 端到端测试（必须实测）
```
□ 飞书发消息 → 5 秒内 worker 日志能看到
□ 飞书新建 docx → 60 秒内 Coze KB 出现
□ 飞书改通讯录 → 1 小时内 Coze 成员变化
□ 飞书会议结束 → 5 分钟内 transcript 进 KB
□ 含手机号的消息 → safety.py 拦截（看 audit/pii_block.log）
□ 同一事件触发 2 次 → 第二次返回 dedup（idempotency 工作）
```

## 监控
```
□ Prometheus /metrics 能 curl
□ bridge_webhook_total 有数据
□ bridge_worker_total 有数据
□ Grafana（如已部署）展示曲线
□ 飞书告警机器人收到测试消息
```

## 安全
```
□ .env 不在 git 里（git status 检查）
□ .env 文件权限 chmod 600
□ ECS root 密码已改 / 禁用 root SSH
□ 火山安全组日志已开
□ EIP 流量监控已启用
```

## 文档 + 流程
```
□ Bridge URL / 凭据写进公司 wiki（受限访问）
□ 工程师 5 + 7 + 1 都能 SSH 到 ECS
□ 出值班排班（PoC 期工程师 5 主值班）
□ 故障联系人：飞书超管 / 法务 / 你
```

## 发现问题怎么办

任何一项 ❌ 都不要让飞书全员事件订阅生效。
先把订阅改回开发模式（仅自己测试账号）→ 修问题 → 再切生产。

## 跑完后

进入 `03-production-ha.md` 升级到双实例。
