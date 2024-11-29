from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(100))
    profile_picture = Column(String(200), nullable=True)
    status_message = Column(String(200), nullable=True)
    is_private = Column(Boolean, default=False)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())

__all__ = ["User"]
