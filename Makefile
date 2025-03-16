# Makefile for managing Docker Compose commands

.PHONY: build up down logs shell migrate migrate-down test lint format destroy

# Build the Docker images using docker-compose
build:
	docker-compose build

# Start the containers in detached mode
up:
	docker-compose up -d

# Follow container logs
logs:
	docker-compose logs -f

# Stop the running containers
down:
	docker-compose down

# Open a shell in a container
shell:
	docker-compose exec api /bin/bash

# Run migrations
migrate:
	docker-compose exec api alembic upgrade head

# Rollback migrations
migrate-down:
	docker-compose exec api alembic downgrade -1

# Run tests
test:
	docker-compose exec api pytest

# Run linting
lint:
	docker-compose exec api flake8 .

# Format code
format:
	docker-compose exec api black .

# Destroy all containers, volumes, and networks
destroy:
	docker-compose down -v --remove-orphans
