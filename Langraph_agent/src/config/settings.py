from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from datetime import datetime, timezone
from typing import Optional

class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    ENVIRONMENT: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    def get_current_time(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    @property
    def is_api_key_valid(self) -> bool:
        return bool(self.GOOGLE_API_KEY and len(self.GOOGLE_API_KEY) > 0)

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    if not settings.is_api_key_valid:
        raise ValueError("GOOGLE_API_KEY is not set or invalid. Please set a valid API key in your .env file.")
    return settings