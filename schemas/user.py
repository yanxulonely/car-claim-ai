from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """注册请求体。"""

    email: EmailStr
    password: str


class UserOut(BaseModel):
    """用户响应体（不含密码）。"""

    id: int
    email: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class Token(BaseModel):
    """JWT token 响应体。"""

    access_token: str
    token_type: str = "bearer"
