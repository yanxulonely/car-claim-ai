from fastapi import FastAPI

from config import settings
from database import Base, engine
from routers import auth, health, users

# 创建数据库表（开发用，生产建议用 Alembic 迁移）
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

# 注册路由
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"app": settings.APP_NAME, "version": settings.APP_VERSION}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)
