#!/usr/bin/env bash
# v6 Agentic Insight 阶段 1 一键 bootstrap（fresh Ubuntu 22.04 ECS）
#
# 用法：
#   curl -fsSL https://<your-host>/bootstrap.sh | sudo bash -s -- <repo_url>
# 或：
#   sudo bash infra/bootstrap.sh <repo_url>
#
# 假设：
# - root 或 sudo 执行
# - Ubuntu 22.04 LTS (其它发行版需调 apt)
# - 数据盘已挂载到 /data（500GB ESSD）
set -euo pipefail

REPO_URL="${1:-}"
APP_DIR=/opt/agentic-insight
DATA_DIR=/data/agentic-insight

if [[ -z "$REPO_URL" && ! -d "$APP_DIR/.git" ]]; then
  echo "Usage: bootstrap.sh <repo_url>" >&2
  exit 1
fi

echo "===> 1/9 系统更新 + 基础包"
apt-get update -y
# Python 3.11+ 兼容：Ubuntu 22.04 用 python3.11，24.04 默认 python3 (3.12) 已满足
PY_PKG="python3 python3-venv python3-dev python3-pip"
if command -v lsb_release >/dev/null && [[ "$(lsb_release -rs)" == "22.04" ]]; then
    add-apt-repository -y ppa:deadsnakes/ppa || true
    apt-get update -y
    PY_PKG="python3.11 python3.11-venv python3.11-dev python3-pip"
fi
apt-get install -y curl git ufw fail2ban $PY_PKG \
                   build-essential ffmpeg jq make ca-certificates gnupg lsb-release

echo "===> 2/9 Docker + compose plugin"
if ! command -v docker >/dev/null; then
  install -m 0755 -d /etc/apt/keyrings
  # 国内 ECS 优先走阿里云 Docker 镜像（download.docker.com 在中国网络不稳）
  DOCKER_REPO="${DOCKER_REPO:-https://mirrors.aliyun.com/docker-ce/linux/ubuntu}"
  rm -f /etc/apt/keyrings/docker.gpg
  curl -fsSL "${DOCKER_REPO}/gpg" | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  chmod a+r /etc/apt/keyrings/docker.gpg
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    ${DOCKER_REPO} $(lsb_release -cs) stable" \
    > /etc/apt/sources.list.d/docker.list
  apt-get update -y
  apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  systemctl enable --now docker
fi

echo "===> 3/9 Node 20 (Next.js)"
if ! command -v node >/dev/null; then
  # 国内 ECS 走阿里云 NodeSource 镜像
  if curl -fsS --max-time 5 https://deb.nodesource.com/setup_20.x -o /tmp/nodesetup.sh 2>/dev/null; then
    bash /tmp/nodesetup.sh && apt-get install -y nodejs
  else
    # fallback: 阿里云 Node 二进制（避免 nodesource 不可达）
    apt-get install -y nodejs npm || {
      echo "Node 安装失败，请手动装 Node 20+ 后重跑"
      exit 1
    }
  fi
fi

echo "===> 4/9 应用用户 + 目录"
id -u app >/dev/null 2>&1 || useradd -m -s /bin/bash app
usermod -aG docker app
mkdir -p "$APP_DIR" "$DATA_DIR"/{pgdata,miniodata,redisdata}
chown -R app:app "$APP_DIR" "$DATA_DIR"

echo "===> 5/9 拉取仓库"
if [[ -n "$REPO_URL" && ! -d "$APP_DIR/.git" ]]; then
  sudo -u app git clone "$REPO_URL" "$APP_DIR"
fi
cd "$APP_DIR"
sudo -u app git pull --ff-only || true

echo "===> 6/9 Python venv + 依赖"
PY_BIN="python3.11"
command -v python3.11 >/dev/null || PY_BIN="python3"

# 配 pip 国内镜像（app 用户级别）
sudo -u app mkdir -p /home/app/.pip
sudo -u app tee /home/app/.pip/pip.conf > /dev/null <<'EOF'
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
timeout = 120
EOF

sudo -u app PY_BIN="$PY_BIN" bash <<'EOSU'
cd /opt/agentic-insight
${PY_BIN} -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .
EOSU

echo "===> 7/9 Web build"
# 配 npm 国内镜像（app 用户级别）
sudo -u app npm config set registry https://registry.npmmirror.com 2>/dev/null || true
sudo -u app bash <<'EOSU'
cd /opt/agentic-insight/web
npm install --no-audit --no-fund
npm run build
EOSU

echo "===> 8/9 防火墙 + fail2ban"
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable
systemctl enable --now fail2ban

echo "===> 9/9 systemd units"
install -m 0644 "$APP_DIR/infra/agentic-api.service"     /etc/systemd/system/
install -m 0644 "$APP_DIR/infra/agentic-worker.service"  /etc/systemd/system/
install -m 0644 "$APP_DIR/infra/agentic-web.service"     /etc/systemd/system/
systemctl daemon-reload

cat <<EOF

✅ Bootstrap 完成。下一步（人工）：

1) 编辑 .env 填入 LLM keys：
   sudo -u app vim $APP_DIR/infra/.env

2) 起 docker stack：
   sudo -u app bash -c "cd $APP_DIR && make up && make migrate && make seed"

3) 起应用 systemd 服务：
   systemctl enable --now agentic-worker agentic-api agentic-web

4) 部署 Nginx 反向代理：
   bash $APP_DIR/infra/nginx-setup.sh

5) 跑端到端 demo：
   sudo -u app bash -c "cd $APP_DIR && make demo"

6) 健康检查：
   bash $APP_DIR/infra/health-check.sh

EOF
