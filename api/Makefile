help:
	@echo "Targets:"
	@echo "    make start"
	@echo "    make down"
	@echo "    make pull"
	@echo "    make build"
	@echo "    make migration"

restart:
	docker-compose down
	docker-compose up -d

start:
	docker-compose up -d

down:
	docker-compose down

pull:
	docker-compose pulldocker

build:
	docker-compose build

migration:
	alembic upgrade heads

uvicorn:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 9000