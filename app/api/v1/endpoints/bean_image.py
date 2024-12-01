from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ....api.deps import get_db, get_current_user
from ....schemas.bean_image import BeanImageCreate, BeanImage
from ....models.user import User as UserModel
from ....crud.bean import bean as bean_crud
from ....crud.bean_image import bean_image as bean_image_crud

router = APIRouter()

# 6. Bean에 이미지 추가하기
@router.post("/bean/{bean_id}/image", response_model=BeanImage)
def add_bean_image(*, db: Session = Depends(get_db), bean_id: int, image_in: BeanImageCreate, current_user: UserModel = Depends(get_current_user)):
    # Bean이 존재하는지 확인해보고... 
    db_bean = bean_crud.get(db=db, id=bean_id)
    # 없으면 예외 발생
    if not db_bean:
        raise HTTPException(status_code=404, detail="그러한 bean은 없는데, bean 이름을 다시 확인해주시겠습니까?")
    
    return bean_image_crud.create_with_bean(db=db, obj_in=image_in)

# __all__ 리스트 추가
__all__ = ["router"]
