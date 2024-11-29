from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....api.deps import get_db, get_current_user
from ....crud.user import user as user_crud
from ....schemas.user import User, UserCreate, UserUpdate
from ....models.user import User as UserModel
from typing import List

# 라우터는 모든 api 엔드포인트를 Main문에 다 작성할 수 없으니, 따로따로 나누어서 엔드포인트를 작성하기 위해 존재하는 것.
# 라우터를 사용함으로 인해, 유지보수가 쉬워짐.
router = APIRouter()

# get으로 /에 접근하면 모든 사용자 리스트를 반환함
@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    # 모든 사용자 목록을 반환함.
    users = user_crud.get_multi(db, skip=skip, limit=limit)
    return users

# post로 /user에 접근하면 새로운 사용자를 생성함.
@router.post("/user", response_model=User)
def create_user(*, db: Session = Depends(get_db), user_in:UserCreate,):
    # 새로운 사용자를 생성하기 전에,사용자가 기존에 있는지 점검해보기 !
    user = user_crud.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, 
                            detail="입력하신 이메일이 이미 존재합니다.")
    user = user_crud.create(db, obj_in=user_in)
    return user
