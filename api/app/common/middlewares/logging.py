import logging
import uuid

from starlette.middleware.base import (
    BaseHTTPMiddleware, 
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("fastapi.request")


class LoggingMiddlewareI(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        key = str(uuid.uuid4())[-12:]
        log_msg = f"[{key}] {request.method} {request.url.path}"
        logger.info(log_msg)
        resp = await call_next(request)
        logger.info(f"{log_msg} - {resp.status_code}")
        print("여기 실행됨?")
        return resp
