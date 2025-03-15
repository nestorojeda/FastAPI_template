from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session
from app.models.user import User
from app.db.session import get_db
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def generate_api_key() -> str:
    return secrets.token_urlsafe(32)

async def get_api_key(
    api_key_header: str = Security(api_key_header),
    db: Session = Depends(get_db)
) -> User:
    user = db.query(User).filter(
        User.api_key == api_key_header,
        User.is_active == True
    ).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
    return user 