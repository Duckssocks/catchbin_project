from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ....api.deps import get_db, get_current_user
from ....schemas.bean_link import BeanLinkCreate, BeanLink
from ....models.user import User as UserModel
from ....crud.bean import bean as bean_crud
from ....crud.bean_link import bean_link as bean_link_crud

router = APIRouter()

# 7. Bean에 링크 추가하기
@router.post("/bean/{bean_id}/link", response_model=BeanLink)
def add_bean_link(*, db: Session = Depends(get_db), bean_id: int, link_in: BeanLinkCreate, current_user: UserModel = Depends(get_current_user)):
    # Bean이 존재하는지 확인해보고 ...
    db_bean = bean_crud.get(db=db, id=bean_id)
    # 없으면 예외 처리
    if not db_bean:
        raise HTTPException(status_code=404, detail="그러한 bean은 없는데, bean 이름을 다시 확인해주시겠습니까?")
    
    return bean_link_crud.create_with_bean(db=db, obj_in=link_in)
    
# __all__ 리스트 추가
__all__ = ["router"]
