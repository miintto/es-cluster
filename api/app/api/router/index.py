from fastapi import APIRouter, Depends

from app.common.response import APIResponse
from app.common.response.codes import Http2XX
from app.config.settings import get_settings, Settings

router = APIRouter()


@router.get("/")
async def index(settings: Settings = Depends(get_settings)) -> APIResponse:
    data = {"fast": "API", "env": settings.APP_ENV}
    return APIResponse(Http2XX.SUCCESS, data=data)
