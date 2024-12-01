from pydantic import BaseModel

class BeanImageBase(BaseModel):
    bean_id: int
    image_url: str

class BeanImageCreate(BeanImageBase):
    pass

class BeanImage(BeanImageBase):
    image_id: int

    class Config:
        orm_mode = True


# __all__ 리스트 추가
__all__ = ["BeanImage", "BeanImageCreate"]