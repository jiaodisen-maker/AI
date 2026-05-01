#!/usr/bin/env bash
# 阶段 1 完整健康检查 — 一眼看清 stack 状态
set -uo pipefail

PASS=0
FAIL=0
ok()   { echo "  ✅ $1"; PASS=$((PASS+1)); }
fail() { echo "  ❌ $1"; FAIL=$((FAIL+1)); }

echo "==> Docker services"
for svc in postgres temporal temporal-ui minio redis; do
    if docker ps --format '{{.Names}}' | grep -q "${svc}"; then
        ok "$svc running"
    else
        fail "$svc NOT running"
    fi
done

echo "==> Postgres"
if docker exec $(docker ps -qf "name=postgres") pg_isready -U platform >/dev/null 2>&1; then
    ok "Postgres ready"
else
    fail "Postgres not ready"
fi

echo "==> Application services"
for unit in agentic-worker agentic-api agentic-web; do
    if systemctl is-active --quiet "$unit"; then
        ok "systemd $unit active"
    else
        fail "systemd $unit not active"
    fi
done

echo "==> HTTP endpoints"
api_status=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8000/health 2>/dev/null || echo "000")
[[ "$api_status" == "200" ]] && ok "API /health 200" || fail "API /health = $api_status"

metrics_status=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8000/metrics 2>/dev/null || echo "000")
[[ "$metrics_status" == "200" ]] && ok "API /metrics 200" || fail "API /metrics = $metrics_status"

web_status=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:3000 2>/dev/null || echo "000")
[[ "$web_status" == "200" ]] && ok "Web :3000 200" || fail "Web :3000 = $web_status"

temporal_ui=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8233 2>/dev/null || echo "000")
[[ "$temporal_ui" == "200" ]] && ok "Temporal UI :8233 200" || fail "Temporal UI = $temporal_ui"

echo "==> DB schema"
table_count=$(docker exec $(docker ps -qf "name=postgres") \
    psql -U platform -d platform -tAc \
    "SELECT count(*) FROM information_schema.tables WHERE table_schema='public'" 2>/dev/null || echo "0")
[[ "$table_count" -ge 10 ]] && ok "tables = $table_count (≥10)" || fail "tables = $table_count (expected ≥10)"

mt_count=$(docker exec $(docker ps -qf "name=postgres") \
    psql -U platform -d platform -tAc \
    "SELECT count(*) FROM microtypes WHERE status='active'" 2>/dev/null || echo "0")
[[ "$mt_count" -ge 50 ]] && ok "active microtypes = $mt_count (≥50)" || fail "microtypes = $mt_count (run make seed)"

echo "==> Feature flag posture"
if grep -q "POC_CRAWLED_ENABLED=true" /opt/agentic-insight/infra/.env 2>/dev/null; then
    fail "POC_CRAWLED_ENABLED=true — 法务备忘录是否签字归档？"
else
    ok "POC_CRAWLED_ENABLED=false (生产安全姿态)"
fi

echo
echo "================================="
echo "  $PASS passed, $FAIL failed"
echo "================================="
exit $((FAIL > 0 ? 1 : 0))
