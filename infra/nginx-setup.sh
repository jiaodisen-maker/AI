#!/usr/bin/env bash
# 安装 Nginx + 配置反向代理
set -euo pipefail

APP_DIR=/opt/agentic-insight

if ! command -v nginx >/dev/null; then
    apt-get install -y nginx
fi

install -m 0644 "$APP_DIR/infra/nginx.conf" /etc/nginx/sites-available/agentic-insight
ln -sf /etc/nginx/sites-available/agentic-insight /etc/nginx/sites-enabled/agentic-insight
rm -f /etc/nginx/sites-enabled/default

nginx -t
systemctl enable --now nginx
systemctl reload nginx

echo "✅ Nginx 启动。访问 http://<ECS-公网IP>/"
echo "   API:    http://<ECS-公网IP>/api/health"
echo "   Web:    http://<ECS-公网IP>/"
echo "   Health: http://<ECS-公网IP>/health"
