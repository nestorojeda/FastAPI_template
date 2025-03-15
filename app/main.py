from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.base import Base
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

description = """
# FastAPI Template API

This is a **modern FastAPI template** that includes:

* **User Management**: Create and manage users
* **API Key Authentication**: Secure endpoints with API key authentication
* **PostgreSQL Database**: Robust data storage with migrations
* **Docker Support**: Easy deployment with Docker and Docker Compose

## Authentication

All protected endpoints require an API key to be sent in the header:
```
X-API-Key: your-api-key
```

## Users

You can:
* Create new users
* Get current user information
* List all users (requires authentication)
"""

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=description,
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Your Name",
        "url": "http://example.com/contact/",
        "email": "your@email.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations with users. Create users and manage them.",
        },
    ],
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)
