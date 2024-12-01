 
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BeanBase(BaseModel):
    title: str
    content_text: str
    # category_id: Optional[int] = None
    is_personal: bool = False

class BeanCreate(BeanBase):
    pass

class BeanUpdate(BeanBase):
    pass

class BeanInDBBase(BeanBase):
    bean_id: int
    creator_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Bean(BeanInDBBase):
    pass

# __all__ 리스트 추가
__all__ = ["Bean", "BeanCreate", "BeanUpdate"]