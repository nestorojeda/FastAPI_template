# FastAPI Template

A modern FastAPI template with user management, API key authentication, PostgreSQL database, and Docker support.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🔐 **API Key Authentication** - Secure endpoints with API keys
- 📦 **PostgreSQL** - Robust database with SQLAlchemy ORM
- 🐳 **Docker** - Containerized deployment with Docker Compose
- 📝 **Alembic** - Database migrations
- 📚 **OpenAPI Documentation** - Automatic API documentation
- ⚡ **Async Support** - Built with async/await
- 🔍 **Type Checking** - Leveraging Python type hints
- 🧪 **Testing Ready** - Prepared for pytest
- 🎯 **Postman Collection** - Ready-to-use API collection

## Requirements

- Python 3.12+
- Docker and Docker Compose
- PostgreSQL (if running locally)
- Postman (for using the API collection)

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-template
```

2. Start the services using Docker Compose:
```bash
make up
```

This will:
- Build the Docker images
- Start the PostgreSQL database
- Run database migrations
- Start the FastAPI application

The API will be available at: http://localhost:8000

## API Documentation

Once the application is running, you can access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Users

- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/me/` - Get current user info (requires authentication)
- `GET /api/v1/users/` - List all users (requires authentication)

## Authentication

Protected endpoints require an API key to be sent in the header:
```
X-API-Key: your-api-key
```

You'll receive an API key when creating a new user.

## Development

### Running Locally

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the PostgreSQL database:
```bash
make up db
```

4. Run migrations:
```bash
make migrate
```

5. Start the application:
```bash
uvicorn app.main:app --reload
```

### Available Make Commands

- `make build` - Build Docker images
- `make up` - Start all services
- `make down` - Stop all services
- `make logs` - View logs
- `make shell` - Open a shell in the API container
- `make migrate` - Run database migrations
- `make migrate-down` - Rollback last migration
- `make test` - Run tests
- `make lint` - Run linter
- `make format` - Format code

## Project Structure

```
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       └── endpoints/
│   │           └── users.py
│   ├── core/
│   │   ├── auth.py
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/
│   │   └── user.py
│   └── schemas/
│       └── user.py
├── scripts/
│   ├── init.sh
│   └── wait_for_db.py
├── alembic/
│   ├── env.py
│   └── versions/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Environment Variables

The following environment variables can be set in a `.env` file:

```env
POSTGRES_SERVER=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi_db
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Postman Collection

The project includes a Postman collection for easy API testing:

1. Import the following files into Postman:
   - `FastAPI_Template.postman_collection.json` - API endpoints collection
   - `FastAPI_Template.postman_environment.json` - Environment variables

2. Select the "FastAPI Template - Local" environment in Postman

3. The collection includes:
   - Create User endpoint (POST)
   - Get Current User endpoint (GET)
   - List Users endpoint (GET)

4. After creating a user, copy the returned API key and:
   - Open the "FastAPI Template - Local" environment
   - Update the `api_key` variable with your key
   - Save the environment

5. Now you can use all authenticated endpoints

## License

This project is licensed under the MIT License - see the LICENSE file for details. 