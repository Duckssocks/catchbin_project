from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BeanRecipientBase(BaseModel):
    bean_id: int
    user_id: int
    is_read: bool

class BeanRecipientCreate(BeanRecipientBase):
    pass

class BeanRecipientUpdate(BaseModel):
    is_read: Optional[bool] = None

class BeanRecipient(BeanRecipientBase):
    read_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# __all__ 리스트 추가
__all__ = ["BeanRecipient", "BeanRecipientCreate", "BeanRecipientUpdate"]
