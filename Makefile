.PHONY: help venv-unix venv-win run-unix run-win compose-up compose-down compose-rebuild compose-logs clean

help:
	@echo "Available targets:"
	@echo "  venv-unix        Create venv and install deps (macOS/Linux)"
	@echo "  venv-win         Create venv and install deps (Windows PowerShell/CMD)"
	@echo "  run-unix         Run API with uvicorn from venv (macOS/Linux)"
	@echo "  run-win          Run API with uvicorn from venv (Windows)"
	@echo "  compose-up       Start Postgres, Qdrant, Trino, API"
	@echo "  compose-down     Stop all services"
	@echo "  compose-rebuild  Rebuild API image and restart API"
	@echo "  compose-logs     Tail compose logs"
	@echo "  clean            Remove venv and build caches"

venv-unix:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

venv-win:
	py -m venv .venv
	.\.venv\Scripts\python.exe -m pip install --upgrade pip
	.\.venv\Scripts\python.exe -m pip install -r requirements.txt

run-unix:
	. .venv/bin/activate && uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

run-win:
	.\.venv\Scripts\uvicorn.exe api.main:app --reload --host 0.0.0.0 --port 8000

compose-up:
	docker compose up -d

compose-down:
	docker compose down

compose-rebuild:
	docker compose build api && docker compose up -d api

compose-logs:
	docker compose logs -f --tail=200

clean:
	rm -rf .venv __pycache__ .pytest_cache .mypy_cache
