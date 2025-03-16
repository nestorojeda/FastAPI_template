from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    """
    Base User Schema with common attributes
    """
    username: str = Field(
        ...,
        example="johndoe",
        description="Username for the user, must be unique"
    )
    email: EmailStr = Field(
        ...,
        example="john@example.com",
        description="Email address for the user, must be unique"
    )


class UserCreate(UserBase):
    """
    Schema for creating a new user
    """
    password: str = Field(
        ...,
        min_length=8,
        example="strongpassword123",
        description="Password for the user account, minimum 8 characters"
    )


class User(UserBase):
    """
    Schema for user information returned by the API
    """
    id: int = Field(
        ...,
        example=1,
        description="Unique identifier for the user"
    )
    is_active: bool = Field(
        default=True,
        example=True,
        description="Whether the user account is active"
    )

    class Config:
        from_attributes = True


class UserResponse(User):
    """
    Schema for user response that includes the API key
    """
    api_key: str = Field(
        ...,
        example="abcdef123456",
        description="API key for authenticating requests"
    )


class Token(BaseModel):
    """
    Schema for authentication tokens
    """
    access_token: str = Field(
        ...,
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        description="JWT access token"
    )
    token_type: str = Field(
        default="bearer",
        example="bearer",
        description="Type of the token"
    )
