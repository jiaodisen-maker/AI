.PHONY: help up down migrate seed api worker fmt lint test demo discover purge monitoring health logs

help:
	@echo "  make up         — 启动 Postgres+pgvector / Temporal / MinIO / Redis"
	@echo "  make down       — 停止所有服务"
	@echo "  make migrate    — 跑 Alembic 升级到最新版本"
	@echo "  make seed       — 灌 microtype 50 个 seed 组合到表 (status='active')"
	@echo "  make api        — 启动 FastAPI (uvicorn, port 8000)"
	@echo "  make worker     — 启动 Temporal worker"
	@echo "  make test       — pytest"
	@echo "  make demo       — 端到端 demo (需先 up + migrate + worker + api)"
	@echo "  make discover CHANNEL=poc QUERY=氨糖 N=5  — A1 批量发现 + 起 workflow"
	@echo "  make purge      — 跑 PoC TTL 清理（删 30 天前 poc_crawled 数据 + MinIO 对象）"
	@echo "  make monitoring — 启动 Prometheus + Grafana + Alertmanager 监控栈"
	@echo "  make health     — 检查 stack 服务可达性"
	@echo "  make logs       — tail Temporal worker 日志"
	@echo "  make fmt        — ruff format"
	@echo "  make lint       — ruff check"

up:
	docker compose -f infra/docker-compose.yml --env-file infra/.env up -d

down:
	docker compose -f infra/docker-compose.yml down

migrate:
	cd db && alembic upgrade head

seed:
	python scripts/seed_microtypes.py

api:
	uvicorn api.main:app --reload --port 8000

worker:
	python -m worker.run_worker

test:
	pytest tests/

demo:
	python scripts/demo_ingest.py

discover:
	python scripts/discovery_run.py --channel $(CHANNEL) --query $(QUERY) --n $(N)

purge:
	python scripts/poc_purge.py

monitoring:
	docker compose -f infra/monitoring/docker-compose.yml up -d
	@echo "Prometheus: http://localhost:9090"
	@echo "Grafana:    http://localhost:3001 (admin/admin)"
	@echo "Alertmgr:   http://localhost:9093"

health:
	@echo "API:" && curl -s http://localhost:8000/health || echo "  ✗ down"
	@echo "Temporal UI:" && curl -sI http://localhost:8233 | head -1 || echo "  ✗ down"
	@echo "Postgres:" && pg_isready -h localhost -p 5432 || echo "  ✗ down"
	@echo "MinIO:" && curl -sI http://localhost:9000/minio/health/live | head -1 || echo "  ✗ down"

logs:
	docker compose -f infra/docker-compose.yml logs -f --tail=100

fmt:
	ruff format .

lint:
	ruff check api/ worker/ tests/
