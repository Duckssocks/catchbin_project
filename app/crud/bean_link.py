from typing import List
from sqlalchemy.orm import Session
from ..models.bean_link import BeanLink
from ..schemas.bean_link import BeanLinkCreate
from .base import CRUDBase

class CRUDBeanLink(CRUDBase[BeanLink, BeanLinkCreate, BeanLinkCreate]):
    def create_with_bean(self, db: Session, *, obj_in: BeanLinkCreate) -> BeanLink:
        db_obj = BeanLink(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_by_bean(self, db: Session, *, bean_id: int) -> List[BeanLink]:
        return db.query(self.model).filter(BeanLink.bean_id == bean_id).all()

bean_link = CRUDBeanLink(BeanLink)

# __all__ 리스트 추가
__all__ = ["bean_link"]
