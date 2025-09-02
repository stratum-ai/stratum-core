.PHONY: help venv-unix venv-win run-unix run-win compose-up compose-down compose-rebuild compose-logs clean setup

# Auto-detect Python binary on Unix-like systems (covers WSL)
PYTHON_BIN := $(shell if command -v python >/dev/null 2>&1; then echo python; else echo python3; fi)

help:
	@echo "Available targets:"
	@echo "  venv-unix        Create venv and install deps (macOS/Linux/WSL)"
	@echo "  venv-win         Create venv and install deps (Windows PowerShell/CMD)"
	@echo "  run-unix         Run API with uvicorn from venv (macOS/Linux/WSL)"
	@echo "  run-win          Run API with uvicorn from venv (Windows)"
	@echo "  compose-up       Start Postgres, Qdrant, Trino, API"
	@echo "  compose-down     Stop all services"
	@echo "  compose-rebuild  Rebuild API image and restart API"
	@echo "  compose-logs     Tail compose logs"
	@echo "  clean            Remove venv and build caches"
	@echo "  setup            Install Docker (apt), add user to docker group, create venv"
	@echo "  smoke            Run compose smoke tests"
	@echo "  wait             Wait for services (Trino/Qdrant/API)"

venv-unix:
	$(PYTHON_BIN) -m venv .venv
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
smoke:
	bash scripts/smoke/01_health.sh
	bash scripts/smoke/02_index.sh
	bash scripts/smoke/03_find.sh

wait:
	bash scripts/wait-for.sh localhost 8080 60 trino
	bash scripts/wait-for.sh localhost 6333 60 qdrant
	bash scripts/wait-for.sh localhost 8000 60 api

clean:
	rm -rf .venv __pycache__ .pytest_cache .mypy_cache

setup:
	@echo "[setup] Installing Docker (apt) and creating venv"
	@if command -v apt-get >/dev/null 2>&1; then \
		sudo apt-get update -y && \
		sudo apt-get install -y ca-certificates curl gnupg lsb-release && \
		sudo install -m 0755 -d /etc/apt/keyrings && \
		if [ ! -f /etc/apt/keyrings/docker.gpg ]; then curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg; fi && \
		if [ ! -f /etc/apt/sources.list.d/docker.list ]; then echo "deb [arch=$$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $$(. /etc/os-release && echo $$VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null; fi && \
		sudo apt-get update -y && \
		sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin; \
	else \
		echo "[setup] apt-get not available; please install Docker manually."; \
	fi
	@sudo groupadd -f docker || true
	@sudo usermod -aG docker $$USER || true
	@echo "[setup] Creating Python venv and installing requirements"
	$(PYTHON_BIN) -m venv .venv || python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "[setup] Verify docker version (may require re-login for group to take effect)"
	@docker --version || true
	@echo "[setup] Removing problematic Docker credential helpers in WSL if present"
	@mkdir -p $$HOME/.docker ; \
	 if [ -f $$HOME/.docker/config.json ]; then cp $$HOME/.docker/config.json $$HOME/.docker/config.json.bak; fi ; \
	 echo '{ "auths": {} }' > $$HOME/.docker/config.json
	@sudo bash -lc 'mkdir -p /root/.docker ; if [ -f /root/.docker/config.json ]; then cp /root/.docker/config.json /root/.docker/config.json.bak; fi ; echo "{ \"auths\": {} }" > /root/.docker/config.json'
	@echo "[setup] Enabling and starting Docker service"
	@sudo systemctl enable --now docker 2>/dev/null || sudo service docker start || true
