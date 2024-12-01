from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class BeanLink(Base):
    __tablename__ = "bean_links"

    link_id = Column(Integer, primary_key=True, index=True)
    bean_id = Column(Integer, ForeignKey("beans.bean_id"), nullable=False)
    link_url = Column(String(500), nullable=False)

    bean = relationship("Bean", back_populates="links")

# __all__ 리스트 추가
__all__ = ["BeanLink"]