from functools import lru_cache
import os

from pydantic import BaseSettings

_BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
_LOG_DIR = os.path.join(_BASE_DIR, "logs/")
if not os.path.exists(_LOG_DIR):
    os.makedirs(_LOG_DIR, exist_ok=True)


class Settings(BaseSettings):
    PROJECT_NAME: str =  "FastAPI Application"
    BASE_DIR: str = _BASE_DIR
    APP_ENV: str
    DEBUG: bool = False
    SECRET_KEY: str

    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] - %(name)s - [%(levelname)s] - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'default',
                'filename': f'{_LOG_DIR}/api.log',
            }
        },
        'loggers': {
            'fastapi.request': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }

    class Config:
        env_file = _BASE_DIR + "/.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
