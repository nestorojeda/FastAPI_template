from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    api_key: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
 