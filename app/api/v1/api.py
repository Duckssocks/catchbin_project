from fastapi import APIRouter
from .endpoints import auth, user, bean, bean_image, bean_link

# API 라우터 생성
api_router = APIRouter()

# 기존의 엔드포인트 라우터 포함
api_router.include_router(auth, prefix="/auth", tags=["authentication"])
api_router.include_router(user, prefix="/users", tags=["users"])
api_router.include_router(bean, prefix="/beans", tags=["beans"])

# 새로운 엔드포인트 라우터 포함 (bean_image, bean_link)
api_router.include_router(bean_image, prefix="/bean-images", tags=["bean-images"])
api_router.include_router(bean_link, prefix="/bean-links", tags=["bean-links"])

__all__ = ["api_router"]
