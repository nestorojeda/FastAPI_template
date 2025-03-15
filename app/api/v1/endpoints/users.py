from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core import auth
from app.models.user import User
from app.schemas.user import User as UserSchema, UserCreate, UserResponse
from app.db.session import get_db

router = APIRouter()

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    tags=["users"],
    responses={
        201: {
            "description": "User created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "username": "johndoe",
                        "email": "john@example.com",
                        "id": 1,
                        "is_active": True,
                        "api_key": "your-api-key-here"
                    }
                }
            }
        },
        400: {
            "description": "Email already registered",
            "content": {
                "application/json": {
                    "example": {"detail": "Email already registered"}
                }
            }
        }
    }
)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user with the following information:

    - **username**: required, must be unique
    - **email**: required, must be unique and valid email format
    - **password**: required, will be hashed
    
    Returns the created user information including the API key.
    """
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = auth.get_password_hash(user.password)
    api_key = auth.generate_api_key()
    
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        api_key=api_key
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get(
    "/me/",
    response_model=UserSchema,
    summary="Get current user",
    tags=["users"],
    responses={
        200: {
            "description": "Current user information",
            "content": {
                "application/json": {
                    "example": {
                        "username": "johndoe",
                        "email": "john@example.com",
                        "id": 1,
                        "is_active": True
                    }
                }
            }
        },
        401: {
            "description": "Invalid API Key",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid API Key"}
                }
            }
        }
    }
)
async def read_user_me(current_user: User = Depends(auth.get_api_key)):
    """
    Get information about the currently authenticated user.
    
    Requires API key authentication via the X-API-Key header.
    """
    return current_user

@router.get(
    "/",
    response_model=List[UserSchema],
    summary="List all users",
    tags=["users"],
    responses={
        200: {
            "description": "List of users",
            "content": {
                "application/json": {
                    "example": [{
                        "username": "johndoe",
                        "email": "john@example.com",
                        "id": 1,
                        "is_active": True
                    }]
                }
            }
        },
        401: {
            "description": "Invalid API Key",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid API Key"}
                }
            }
        }
    }
)
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(auth.get_api_key)
):
    """
    Retrieve a list of all users.
    
    Parameters:
    - **skip**: Number of users to skip (pagination)
    - **limit**: Maximum number of users to return
    
    Requires API key authentication via the X-API-Key header.
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return users 