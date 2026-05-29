from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置，通过环境变量或 .env 文件加载。"""

    # 应用
    APP_NAME: str = "Car Claim AI"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # 数据库
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/car_claim_ai"

    # JWT
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
