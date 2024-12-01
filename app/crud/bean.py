from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.bean import Bean
from ..models.bean_recipient import BeanRecipient
from ..schemas.bean import BeanCreate, BeanUpdate
from .base import CRUDBase

class CRUDBean(CRUDBase[Bean, BeanCreate, BeanUpdate]):
    def create_with_creator(self, db: Session, *, obj_in: BeanCreate, creator_id: int) -> Bean:
        db_obj = Bean(
            **obj_in.dict(),
            creator_id=creator_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_creator(self, db: Session, *, creator_id: int, skip: int = 0, limit: int = 100) -> List[Bean]:
        return db.query(self.model).filter(Bean.creator_id == creator_id).offset(skip).limit(limit).all()

    # def get_by_category(self, db: Session, *, category_id: int, skip: int = 0, limit: int = 100) -> List[Bean]:
    #    return db.query(self.model).filter(Bean.category_id == category_id).offset(skip).limit(limit).all()

    # 특정 Bean과 특정 수신자(user_id)를 기준으로 BeanRecipient 조회
    def get_recipient_by_bean_and_user(self, db: Session, *, bean_id: int, user_id: int) -> Optional[BeanRecipient]:
        return db.query(BeanRecipient).filter(BeanRecipient.bean_id == bean_id, BeanRecipient.user_id == user_id).first()

bean = CRUDBean(Bean)
# __all__ 리스트 추가
__all__ = ["bean"]