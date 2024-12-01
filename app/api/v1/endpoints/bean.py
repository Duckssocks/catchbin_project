 
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ....api.deps import get_db, get_current_user
from ....schemas.bean import Bean, BeanCreate
from ....models.user import User as UserModel
from ....crud.bean import bean as bean_crud
from ....crud.bean_recipient import bean_recipient as bean_recipient_crud
from ....schemas.bean_image import BeanImageCreate, BeanImage  
from ....schemas.bean_link import BeanLinkCreate, BeanLink  
from typing import List

router = APIRouter()

# 1. 모든 Bean을 조회한다. (시스템에서 받았든, 자기가 만들어서 친구한테 보냈든 간에 상관없이)
@router.get("/beans", response_model=List[Bean])
def get_beans(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    beans = bean_crud.get_multi(db, skip=skip, limit=limit)
    return beans

# 2. 빈 생성하기 -> 특정 사용자가 시스템으로부터 받거나, 친구에게 보내기 위해 만들거나 등등 모든 부분을 다 포괄한다.
@router.post("/bean", response_model=Bean)
def create_bean(*, db: Session = Depends(get_db), bean_in: BeanCreate, current_user: UserModel = Depends(get_current_user)):
    # 현재 로그인한 사용자에게만 적용..
    return bean_crud.create_with_creator(db=db, obj_in=bean_in, creator_id = current_user.user_id)

# 3. 특정 사용자가 만든 Bean 조회 
@router.get("/bean-user", response_model=List[Bean])
def get_user_beans(user_id: int, db: Session = Depends(get_db), skip: int=0, limit: int = 100):
    beans = bean_crud.get_by_creator(db=db, creator_id=user_id, skip=skip, limit=limit)
    return beans

# 4. 특정 Bean 삭제! (빈 생성자 또는 수신자(친구로부터 빈을 받는 사람)가 삭제 가능)
@router.delete("/bean/{bean_id}", response_model=Bean)
def delete_bean(*, db: Session = Depends(get_db), bean_id: int, current_user: UserModel = Depends(get_current_user)):
    db_bean = bean_crud.get(db=db, id=bean_id)
    if not db_bean:
        raise HTTPException(status_code=404, detail="그런 Bean은 존재하지 않습니다! Bean id를 잘 확인해주세요.")
    
    # 사용자가 생성자이거나 수신자인지 확인해보고.. 아니라면 ? -> 삭제할 권한이 없다.
    if db_bean.creator_id != current_user.user_id:
        recipient = bean_recipient_crud.get_by_bean_and_user(db=db, bean_id=bean_id, user_id=current_user.user_id)
        if not recipient:
            raise HTTPException(status_code=403, detail="당신은 이 Bean과 관련된 사람이 아니므로, 삭제할 권한이 없습니다!")
    
    return bean_crud.remove(db=db, id=bean_id)

# 5. 특정 카테고리의 Bean 조회하기
@router.get("/bean-category", response_model=List[Bean])
def get_category_beans(category_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    beans = bean_crud.get_by_category(db=db, category_id=category_id, skip=skip, limit=limit)
    return beans

