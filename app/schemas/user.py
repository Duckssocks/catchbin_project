from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    profile_picture: Optional[str] = None
    status_message: Optional[str] = None
    is_private: bool = False

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    user_id: int
    date_joined: datetime

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str
    message: str = "로그인에 성공하였습니다!"

__all__ = ["User", "UserCreate", "UserUpdate", "Token"] 
