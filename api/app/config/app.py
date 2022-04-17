import logging.config

from fastapi import FastAPI

from app.api.router import api_router
from app.common.exceptions.handlers import exception_handlers
from app.common.middlewares.logging import LoggingMiddlewareI
from app.common.response import APIResponse
from app.config.settings import get_settings

settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        default_response_class=APIResponse,
        exception_handlers=exception_handlers,
    )

    logging.config.dictConfig(config=settings.LOGGING_CONFIG)

    app.add_middleware(LoggingMiddlewareI)
    app.include_router(api_router)
    return app
