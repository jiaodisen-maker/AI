.PHONY: help up down migrate api worker fmt lint

help:
	@echo "  make up         — 启动 Postgres+pgvector / Temporal / MinIO / Redis"
	@echo "  make down       — 停止所有服务"
	@echo "  make migrate    — 跑 Alembic 升级到最新版本"
	@echo "  make api        — 启动 FastAPI (uvicorn, port 8000)"
	@echo "  make worker     — 启动 Temporal worker"
	@echo "  make fmt        — ruff format"
	@echo "  make lint       — ruff check"

up:
	docker compose -f infra/docker-compose.yml --env-file infra/.env up -d

down:
	docker compose -f infra/docker-compose.yml down

migrate:
	cd db && alembic upgrade head

api:
	uvicorn api.main:app --reload --port 8000

worker:
	python -m worker.run_worker

fmt:
	ruff format .

lint:
	ruff check .
