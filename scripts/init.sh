#!/bin/sh

# Wait for the database to be ready
echo "Waiting for database to be ready..."
python scripts/wait_for_db.py

# Run migrations
echo "Running database migrations..."
alembic upgrade head

# Start the application
echo "Starting the application..."
exec "$@" 