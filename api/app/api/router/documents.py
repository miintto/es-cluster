from fastapi import APIRouter, Depends

from app.common.response import APIResponse
from app.common.response.codes import Http2XX
from app.config.settings import Settings, get_settings
from app.api.schema.documents import DocumentSearchParams
from app.api.search.handler import DocumentSearchHandler

router = APIRouter()


@router.get("")
async def get_document(
    params: DocumentSearchParams = Depends(),
    settings: Settings = Depends(get_settings),
) -> APIResponse:
    handler = DocumentSearchHandler(host=settings.ELASTICSEARCH_HOST)
    return APIResponse(Http2XX.SUCCESS, data=handler.search(params.dict()))
