from fastapi import APIRouter

from . import index
from . import documents


api_router = APIRouter()
api_router.include_router(index.router, prefix="", tags=["index"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
