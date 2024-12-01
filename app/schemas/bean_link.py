from pydantic import BaseModel

class BeanLinkBase(BaseModel):
    bean_id: int
    link_url: str

class BeanLinkCreate(BeanLinkBase):
    pass

class BeanLink(BeanLinkBase):
    link_id: int

    class Config:
        orm_mode = True

# __all__ 리스트 추가
__all__ = ["BeanLink", "BeanLinkCreate"]
