from __future__ import annotations

from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    app_name: str = "AI Business Dashboard"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./business_dashboard.db"
    sqlite_database_url: str = "sqlite:///./business_dashboard.db"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 120
    frontend_url: str = "http://localhost:5173"
    cors_origins: list[str] = ["http://localhost:5173"]
    openai_api_key: str | None = None

    @property
    def active_database_url(self) -> str:
        return self.database_url or self.sqlite_database_url


settings = Settings()
