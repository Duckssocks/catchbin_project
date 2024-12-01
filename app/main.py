from fastapi import FastAPI
from .core.config import settings
from .api.v1.api import api_router
from .core.database import Base, engine

# 서버를 실행하면서 Database를 생성한다!!!
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# main문에 api 엔드포인트를 정의하지 않고, 라우터로 관리한다.
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to CatchBin API"} 
