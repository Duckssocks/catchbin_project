from typing import List
from sqlalchemy.orm import Session
from ..models.bean_image import BeanImage
from ..schemas.bean_image import BeanImageCreate
from .base import CRUDBase

class CRUDBeanImage(CRUDBase[BeanImage, BeanImageCreate, BeanImageCreate]):
    def create_with_bean(self, db: Session, *, obj_in: BeanImageCreate) -> BeanImage:
        db_obj = BeanImage(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_by_bean(self, db: Session, *, bean_id: int) -> List[BeanImage]:
        return db.query(self.model).filter(BeanImage.bean_id == bean_id).all()

bean_image = CRUDBeanImage(BeanImage)

# __all__ 리스트 추가
__all__ = ["bean_image"]
