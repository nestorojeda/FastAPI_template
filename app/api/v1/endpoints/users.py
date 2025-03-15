from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core import auth
from app.models.user import User
from app.schemas.user import User as UserSchema, UserCreate
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
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

@router.get("/me/", response_model=UserSchema)
def read_user_me(current_user: User = Depends(auth.get_api_key)):
    return current_user

@router.get("/", response_model=List[UserSchema])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(auth.get_api_key)
):
    users = db.query(User).offset(skip).limit(limit).all()
    return users 