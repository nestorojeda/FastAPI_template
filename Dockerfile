# Build stage
FROM python:3.11-slim-bullseye as build

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Development stage
FROM build as development

WORKDIR /app

# Copy application code
COPY . .

# Make the initialization script executable
RUN chmod +x scripts/init.sh

# Production stage
FROM build as production

WORKDIR /app

# Copy application code
COPY . .

# Make the initialization script executable
RUN chmod +x scripts/init.sh

# Use the initialization script as entrypoint
ENTRYPOINT ["./scripts/init.sh"]

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
