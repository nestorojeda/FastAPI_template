# Makefile for managing Docker Compose commands

.PHONY: build up down logs shell migrate migrate-down test lint format destroy dev prod

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

# Open a shell in the backend container
shell-api:
	docker-compose exec api /bin/bash

# Run migrations
migrate:
	docker-compose exec api alembic upgrade head

# Rollback migrations
migrate-down:
	docker-compose exec api alembic downgrade -1

# Destroy all containers, volumes, and networks
destroy:
	docker-compose down -v --remove-orphans

# Start the application in development mode with HMR
dev:
	@echo "Starting application in development mode..."
	docker-compose -f docker-compose.dev.yml down || true
	docker-compose -f docker-compose.dev.yml build
	docker-compose -f docker-compose.dev.yml up -d
	@echo "Application is running in development mode. Use 'make logs' to view logs."

# Start the application in production mode
prod:
	@echo "Starting application in production mode..."
	docker-compose -f docker-compose.prod.yml down || true
	docker-compose -f docker-compose.prod.yml build
	docker-compose -f docker-compose.prod.yml up -d
	@echo "Application is running in production mode. Use 'make logs' to view logs."
