.PHONY: help up down migrate api worker fmt lint test demo

help:
	@echo "  make up         — 启动 Postgres+pgvector / Temporal / MinIO / Redis"
	@echo "  make down       — 停止所有服务"
	@echo "  make migrate    — 跑 Alembic 升级到最新版本"
	@echo "  make seed       — 灌 microtype 50 个 seed 组合到表 (status='active')"
	@echo "  make api        — 启动 FastAPI (uvicorn, port 8000)"
	@echo "  make worker     — 启动 Temporal worker"
	@echo "  make test       — pytest"
	@echo "  make demo       — 端到端 demo (需先 up + migrate + worker + api)"
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

fmt:
	ruff format .

lint:
	ruff check api/ worker/ tests/
