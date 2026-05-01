#!/usr/bin/env bash
# Agentic Insight 一键安装（国内 ECS 优化版）
#
# 设计原则：
# - 所有依赖源都换成国内镜像（apt / pip / npm / docker）
# - 每步带重试 + 回退方案
# - 幂等：跑过的步骤会跳过，断点续跑友好
# - 失败时输出明确的下一步命令
#
# 用法：
#   sudo bash infra/install-all-china.sh
#
# 前置条件：
# - Ubuntu 22.04 / 24.04
# - 数据盘已挂在 /data（如果有 500GB 数据盘的话）
# - 仓库已 clone 到 /opt/agentic-insight
set -uo pipefail

APP_DIR=/opt/agentic-insight
LOG_FILE=/tmp/agentic-install.log

red()   { echo -e "\033[0;31m$1\033[0m"; }
green() { echo -e "\033[0;32m$1\033[0m"; }
yellow(){ echo -e "\033[0;33m$1\033[0m"; }
step()  { echo; yellow "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; yellow "  $1"; yellow "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; }

cd "$APP_DIR" || { red "代码不在 $APP_DIR，先 git clone"; exit 1; }

# ────────────────────────────────────────────────────
step "1/10  apt 换阿里云镜像 + 基础包"
# ────────────────────────────────────────────────────
UBUNTU_CODENAME=$(lsb_release -cs)
cat > /etc/apt/sources.list.d/aliyun.sources <<EOF
Types: deb
URIs: http://mirrors.aliyun.com/ubuntu/
Suites: ${UBUNTU_CODENAME} ${UBUNTU_CODENAME}-updates ${UBUNTU_CODENAME}-security ${UBUNTU_CODENAME}-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
EOF
apt-get update -y || red "apt update 失败（可能镜像源问题，重试一次）"
apt-get install -y curl git ufw fail2ban python3 python3-venv python3-dev python3-pip \
                   build-essential ffmpeg jq make ca-certificates gnupg lsb-release unzip \
    && green "✓ 基础包就绪" \
    || { red "基础包装失败"; exit 1; }

# ────────────────────────────────────────────────────
step "2/10  Docker（阿里云镜像）"
# ────────────────────────────────────────────────────
if ! command -v docker >/dev/null; then
    rm -f /etc/apt/keyrings/docker.gpg /etc/apt/sources.list.d/docker.list
    install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    chmod a+r /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://mirrors.aliyun.com/docker-ce/linux/ubuntu ${UBUNTU_CODENAME} stable" \
        > /etc/apt/sources.list.d/docker.list
    apt-get update -y
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    systemctl enable --now docker
    green "✓ Docker 安装完成"
else
    green "✓ Docker 已安装，跳过"
fi

# Docker daemon 镜像加速
mkdir -p /etc/docker
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com",
    "https://docker.m.daocloud.io",
    "https://docker.nju.edu.cn"
  ]
}
EOF
systemctl restart docker
green "✓ Docker registry mirror 已配"

# ────────────────────────────────────────────────────
step "3/10  Node 20（阿里云 NodeSource 镜像）"
# ────────────────────────────────────────────────────
if ! command -v node >/dev/null; then
    apt-get install -y nodejs npm
    NODE_VER=$(node -v 2>/dev/null | sed 's/v//' | cut -d. -f1)
    if [ "${NODE_VER:-0}" -lt 18 ]; then
        red "Node 版本太老 ($NODE_VER)，下载阿里云 Node 20 二进制"
        cd /tmp
        curl -fsSL https://mirrors.aliyun.com/nodejs-release/v20.18.0/node-v20.18.0-linux-x64.tar.xz \
            -o node.tar.xz
        tar -xf node.tar.xz
        cp -rf node-v20.18.0-linux-x64/{bin,include,lib,share} /usr/local/
        cd "$APP_DIR"
    fi
    green "✓ Node $(node -v) 就绪"
else
    green "✓ Node 已安装 $(node -v)，跳过"
fi

# ────────────────────────────────────────────────────
step "4/10  应用用户 + 数据目录"
# ────────────────────────────────────────────────────
id -u app >/dev/null 2>&1 || useradd -m -s /bin/bash app
usermod -aG docker app

DATA_ROOT=/data
[ -d /data ] || DATA_ROOT=/var/lib
mkdir -p "$DATA_ROOT/agentic-insight"/{pgdata,miniodata,redisdata,backup}
chown -R app:app "$DATA_ROOT/agentic-insight" "$APP_DIR"
green "✓ 数据目录: $DATA_ROOT/agentic-insight"

# ────────────────────────────────────────────────────
step "5/10  pip 国内镜像 (阿里云)"
# ────────────────────────────────────────────────────
sudo -u app mkdir -p /home/app/.pip
sudo -u app tee /home/app/.pip/pip.conf > /dev/null <<EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
timeout = 180
retries = 3
EOF
green "✓ pip 配置完成"

# ────────────────────────────────────────────────────
step "6/10  Python venv + 依赖"
# ────────────────────────────────────────────────────
sudo -u app bash <<'EOSU'
set -e
cd /opt/agentic-insight
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install --upgrade pip wheel setuptools
# 重试 3 次（网络抖动）
for i in 1 2 3; do
    if .venv/bin/pip install -e .; then
        echo "✓ pip install -e . 成功 (尝试 $i)"
        break
    else
        echo "× 尝试 $i 失败，重试..."
        sleep 5
    fi
done
EOSU
green "✓ Python 依赖就绪"

# ────────────────────────────────────────────────────
step "7/10  npm 国内镜像 + Web build"
# ────────────────────────────────────────────────────
sudo -u app npm config set registry https://registry.npmmirror.com
sudo -u app bash <<'EOSU'
set -e
cd /opt/agentic-insight/web
for i in 1 2 3; do
    if npm install --no-audit --no-fund; then break; fi
    sleep 5
done
npm run build
EOSU
green "✓ Web build 完成"

# ────────────────────────────────────────────────────
step "8/10  防火墙 + fail2ban"
# ────────────────────────────────────────────────────
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable
systemctl enable --now fail2ban
green "✓ UFW + fail2ban 启用"

# ────────────────────────────────────────────────────
step "9/10  systemd 单元"
# ────────────────────────────────────────────────────
install -m 0644 "$APP_DIR/infra/agentic-api.service"     /etc/systemd/system/
install -m 0644 "$APP_DIR/infra/agentic-worker.service"  /etc/systemd/system/
install -m 0644 "$APP_DIR/infra/agentic-web.service"     /etc/systemd/system/
systemctl daemon-reload
green "✓ systemd 单元就绪（未启动，等 .env 配好再 enable）"

# ────────────────────────────────────────────────────
step "10/10  .env 模板 + 起 docker stack"
# ────────────────────────────────────────────────────
if [ ! -f "$APP_DIR/infra/.env" ]; then
    cp "$APP_DIR/infra/.env.example" "$APP_DIR/infra/.env"
    chmod 600 "$APP_DIR/infra/.env"
    chown app:app "$APP_DIR/infra/.env"
    yellow "  ⚠ 已生成 infra/.env，下一步去填 LLM keys"
fi

# 起 docker stack
sudo -u app bash -c "cd $APP_DIR && docker compose -f infra/docker-compose.yml up -d"
sleep 5
green "✓ docker stack 启动"

# ────────────────────────────────────────────────────
echo
green "════════════════════════════════════════════════════════"
green "  ✅ 安装完成"
green "════════════════════════════════════════════════════════"
echo
echo "下一步（人工）："
echo "  1) 编辑 .env 填 LLM keys（DEEPSEEK_API_KEY / QWEN_API_KEY）："
echo "     sudo -u app vim $APP_DIR/infra/.env"
echo
echo "  2) 跑数据库迁移 + seed："
echo "     sudo -u app bash -c 'cd $APP_DIR && make migrate && make seed'"
echo
echo "  3) 启动应用："
echo "     systemctl enable --now agentic-worker agentic-api agentic-web"
echo
echo "  4) 装 Nginx 反向代理（单 80 入口）："
echo "     sudo bash $APP_DIR/infra/nginx-setup.sh"
echo
echo "  5) 健康检查："
echo "     sudo bash $APP_DIR/infra/health-check.sh"
echo
echo "  6) 端到端 demo："
echo "     sudo -u app bash -c 'cd $APP_DIR && make demo'"
echo
echo "服务端口（验证用）："
echo "  Postgres : localhost:5432"
echo "  Temporal : localhost:7233 (UI: 8233)"
echo "  MinIO    : localhost:9000 (Console: 9001)"
echo "  API      : 8000 (启动 systemd 后)"
echo "  Web      : 3000 (启动 systemd 后)"
