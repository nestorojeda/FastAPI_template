from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.base import Base
from app.db.session import engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Template",
    version="1.0.0",
    description="A FastAPI template with user management and API key authentication"
)

app.include_router(api_router, prefix="/api/v1")
