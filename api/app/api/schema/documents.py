from datetime import date
from typing import Optional

from pydantic import BaseModel


class DocumentSearchParams(BaseModel):
    keyword: Optional[str] = None
    contents: bool = False
    start_dtm: Optional[date] = None
    end_dtm: Optional[date] = None
    author: Optional[str] = None
    size: int = 20
    index: int = 0
