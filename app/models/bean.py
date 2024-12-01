from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base 

class Bean(Base):
    __tablename__ = "beans"

    bean_id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    # category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
    title = Column(String(200), nullable=False)
    content_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_personal = Column(Boolean, default=False)

    creator = relationship("User", back_populates="beans")
    # category = relationship("Category", back_populates="beans")
    recipients = relationship("BeanRecipient", back_populates="bean", cascade="all, delete-orphan")
    images = relationship("BeanImage", back_populates="bean", cascade="all, delete-orphan")
    links = relationship("BeanLink", back_populates="bean", cascade="all, delete-orphan")


# __all__ 리스트 추가
__all__ = ["Bean"]


