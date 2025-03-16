# FastAPI Template

A modern FastAPI template with user management, API key authentication, PostgreSQL database, and Nuxt.js frontend.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🎨 **Nuxt 3** - Vue.js framework for building modern web applications
- 🔐 **API Key Authentication** - Secure endpoints with API keys
- 📦 **PostgreSQL** - Robust database with SQLAlchemy ORM
- 🐳 **Docker** - Containerized deployment with Docker Compose
- 📝 **Alembic** - Database migrations
- 📚 **OpenAPI Documentation** - Automatic API documentation
- ⚡ **Async Support** - Built with async/await
- 🔍 **Type Checking** - Leveraging Python and TypeScript
- 🧪 **Testing Ready** - Prepared for pytest
- 🎯 **Postman Collection** - Ready-to-use API collection

## Requirements

- Python 3.12+
- Node.js 20+
- Docker and Docker Compose
- PostgreSQL (if running locally)
- Postman (for using the API collection)

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-template
```

2. Start all services using Docker Compose:
```bash
make up
```

This will:
- Build the Docker images
- Start the PostgreSQL database
- Run database migrations
- Start the FastAPI backend
- Start the Nuxt frontend

The services will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Development

### Running Backend Locally

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

5. Start the backend:
```bash
uvicorn app.main:app --reload
```

### Running Frontend Locally

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

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
├── app/                  # Backend application
│   ├── api/             # API endpoints
│   ├── core/            # Core functionality
│   ├── db/              # Database configuration
│   ├── models/          # SQLAlchemy models
│   └── schemas/         # Pydantic schemas
├── frontend/            # Nuxt.js frontend
│   ├── components/      # Vue components
│   ├── composables/     # Vue composables
│   ├── pages/           # Vue pages
│   ├── stores/          # Pinia stores
│   └── types/           # TypeScript types
├── scripts/             # Utility scripts
├── alembic/             # Database migrations
├── docker-compose.yml   # Docker services configuration
├── Dockerfile           # Backend Dockerfile
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