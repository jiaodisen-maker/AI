---
name: memory-bootstrap
description: 第一次部署时初始化两套记忆系统并冷启动索引
trigger:
  - bootstrap / init / 初始化 / 第一次
inputs:
  brain_repo_path: GBrain markdown 仓库路径（必填）
  postgres_url: GBrain 用的 Postgres 连接串（必填）
  hindsight_storage: Hindsight 数据目录（默认 ./hindsight_data）
---

# Skill: memory-bootstrap

## 目标
**只在第一次或灾难恢复时跑一次**。把空环境变成可用的双层记忆系统。

## 步骤

1. **预检**
   - `bun --version` ≥ 1.0
   - `python --version` ≥ 3.11
   - Postgres 可连，且 `pgvector` 扩展已安装
   - `brain_repo_path` 是 git 仓库

2. **初始化 GBrain**
   ```bash
   cd $brain_repo_path
   gbrain init
   gbrain index --full     # 把所有 markdown 灌进 Postgres
   gbrain mcp serve --port 7801 &
   ```

3. **初始化 Hindsight**
   ```bash
   python -c "from hindsight import init; init(storage='$hindsight_storage')"
   ```

4. **冷启动跨灌注**
   把 GBrain 中的核心实体作为 World Facts 灌进 Hindsight，让它有底子可参考：
   ```
   memory_reflect(scope="all", dry_run=False)
   ```

5. **启动守护**
   ```bash
   python scripts/auto_dream.py --cron &
   python scripts/mcp_server.py &
   ```

6. **健康检查**
   - `memory_write(content="test", hints={"type":"test"})` → 期望返回 ok
   - `memory_recall(query="test")` → 期望命中刚才写入的
   - 两个进程都还在跑

7. **报告**
   返回部署摘要：GBrain 索引页数、Hindsight 初始记忆数、两个 MCP endpoint。

## 边界

- ❌ 已有数据时**不要**跑 `gbrain index --full --reset`，会清库
- ❌ 不要把 `hindsight_data/` 目录提交进 git（数据非源）
- ❌ 不要在生产上跑 `dry_run=False` 的全量 reflect 在白天——锁库时间长，挑凌晨
