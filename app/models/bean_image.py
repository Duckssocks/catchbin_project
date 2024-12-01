from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class BeanImage(Base):
    __tablename__ = "bean_images"

    image_id = Column(Integer, primary_key=True, index=True)
    bean_id = Column(Integer, ForeignKey("beans.bean_id"), nullable=False)
    image_url = Column(String(500), nullable=False)

    bean = relationship("Bean", back_populates="images")

# __all__ 리스트 추가
__all__ = ["BeanImage"]