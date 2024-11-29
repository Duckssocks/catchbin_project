from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ....core.config import settings
from ....core.security import create_access_token
from ....crud.user import user as user_crud
from ....schemas.user import Token
from ....api.deps import get_db

router = APIRouter()

# 로그인 인증 및 현재 사용자인지 아닌지 알기 위한 라우터 코드.
@router.post("/login", response_model=Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):

    # 1. 사용자 인증을 진행함. 입력받은 email, password에 대하여 
    user = user_crud.authenticate(db, email=form_data.username, password=form_data.password)
    # 2. 만약 로그인을 하려고 하는데 그런 유저가 없다? 예외 발생시킴.
    if not user:
        raise HTTPException(
            status_code=401,
            detail="이메일 또는 비밀번호가 올바르지 않습니다."
        )
    
    # 3. 만약 로그인 성공하면, JWT 토큰 발급해서 로그인 상태로..
    access_token = create_access_token(
        data={"sub": str(user.user_id)}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "로그인이 성공하였습니다!"
    }

__all__ = ["router"]
