from typing import Optional
from sqlalchemy.orm import Session
from ..models.bean_recipient import BeanRecipient
from ..schemas.bean_recipient import BeanRecipientCreate, BeanRecipientUpdate  # 이 부분 추가
from .base import CRUDBase

class CRUDBeanRecipient(CRUDBase[BeanRecipient, BeanRecipientCreate, BeanRecipientUpdate]):
    # 특정 Bean과 특정 사용자를 기준으로 BeanRecipient를 조회
    def get_by_bean_and_user(self, db: Session, *, bean_id: int, user_id: int) -> Optional[BeanRecipient]:
        return db.query(self.model).filter(BeanRecipient.bean_id == bean_id, BeanRecipient.user_id == user_id).first()

bean_recipient = CRUDBeanRecipient(BeanRecipient)

# __all__ 리스트 추가
__all__ = ["bean_recipient"]
