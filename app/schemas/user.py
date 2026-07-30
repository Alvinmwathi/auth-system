from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, Integer, String
from app.database.base import Base

class UserRegister(BaseModel):
    email: EmailStr
    password: str= Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    email: EmailStr


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)