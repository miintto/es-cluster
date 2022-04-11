import logging

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request

from app.common.exceptions import APIException
from app.common.response import APIResponse
from app.common.response.codes import Http4XX, Http5XX

logger = logging.getLogger(__name__)


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> APIResponse:
    logger.error(repr(exc))
    return APIResponse(Http4XX.VALIDATE_ERROR)


async def api_exception_handler(
    request: Request, exc: APIException
) -> APIResponse:
    logger.error(repr(exc))
    return APIResponse(exc.error)


async def default_exception_handler(
    request: Request, exc: Exception
) -> APIResponse:
    logger.error(repr(exc))
    return APIResponse(Http5XX.SERVER_ERROR)


exception_handlers = {
    RequestValidationError: request_validation_exception_handler,
    APIException: api_exception_handler,
    Exception: default_exception_handler,
}
