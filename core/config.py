from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Ticket Assistant API"
    seeding_enabled: bool = False

    db_user: str = "DB_USER"
    db_password: str = "DB_PASSWORD"
    db_host: str = "DB_HOST", "localhost"
    db_port: str = "DB_PORT", "5432"
    db_name: str = "DB_NAME"


@lru_cache
def get_settings() -> Settings:
    return Settings()
