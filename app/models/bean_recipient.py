from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class BeanRecipient(Base):
    __tablename__ = "bean_recipients"

    bean_id = Column(Integer, ForeignKey("beans.bean_id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    received_at = Column(DateTime(timezone=True), server_default=func.now())
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime(timezone=True), nullable=True)

    bean = relationship("Bean", back_populates="recipients")
    user = relationship("User", back_populates="received_beans")

# __all__ 리스트 추가
__all__ = ["BeanLink"]