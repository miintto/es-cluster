from functools import lru_cache
import os

from pydantic import BaseSettings

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


class Settings(BaseSettings):
    PROJECT_NAME: str =  "FastAPI Application"
    BASE_DIR: str = BASE_DIR
    APP_ENV: str
    DEBUG: bool = False
    SECRET_KEY: str

    class Config:
        env_file = BASE_DIR + "/.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
