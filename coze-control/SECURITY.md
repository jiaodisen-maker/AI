# SECURITY —— 凭据与数据规范

## 第一原则：PAT 永远不进 git

任何提交里不允许出现：
- `pat_*` 字符串（Coze PAT 前缀）
- `COZE_PAT=<值>` 直接写明
- `Authorization: Bearer ...` 的具体值

### 检查方式
```bash
# pre-commit 钩子（建议加）
git diff --cached | grep -E '(pat_[A-Za-z0-9]{20,}|COZE_PAT=[^$])' && {
    echo "BLOCKED: PAT-like string in commit"; exit 1; }
```

## 第二原则：只通过环境变量传递

`secrets.py` 故意只支持环境变量，**不读 yaml / json / 任何文件**。
要塞 secret 进 yaml？`secrets.py` 会主动拒绝并打日志。

```python
# 正确
pat = secrets.require("COZE_PAT")

# 错误（会抛 SecretInFileError）
pat = yaml.load(...)["coze"]["pat"]
```

## 第三原则：泄露即轮换

任何渠道（Slack / 飞书 / 邮件 / git / 工单 / AI 对话）出现过的 PAT 都视为泄露。

- 立即去 [coze.cn → 个人访问令牌](https://www.coze.cn/open/oauth/pats) 撤销
- 重新生成
- 新 token 只通过本地 `.env`（gitignored）或 secret manager

## 第四原则：最小权限

PAT 创建时只勾选实际需要的 scope：

| 任务 | scope |
|---|---|
| pull（只读快照）| Bot:Read, Workflow:Read, Knowledge:Read, Conversation:Read |
| eval（跑对话）| + Chat |
| push（写回）| + Bot:Write, Workflow:Write, Knowledge:Write |

平时用读权限的 PAT；要 push 时用一条单独的高权限 PAT 临时设置后立即撤销。

## 第五原则：数据脱敏

`pull.py` 拉下来的 yaml 里：
- 用户对话日志默认**只存哈希 + 元数据**，不存正文
- 系统 prompt 中如发现疑似密钥（PAT / API key / 私钥）→ 打 `[REDACTED]` 标记，写到 `bots/<id>.yaml.warnings`
- 想看正文走 `analyze.py --include-content`，单次操作不进 git

## 第六原则：审计

所有对 Coze 的写入（push / ab promote）必须：
- 经 PR review
- 触发器留证：commit hash + PR 号 + 操作人 → 写 `ops_audit.log`
- `lint.py` 不通过禁止 push
