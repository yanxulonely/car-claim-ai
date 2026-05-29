from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check():
    """健康检查接口。"""
    return {"status": "ok"}
