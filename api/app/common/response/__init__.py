from enum import Enum
from typing import Dict, List, Union

from fastapi.responses import JSONResponse

from .formats import send_format


class APIResponse(JSONResponse):
    def __init__(
        self, code: Enum, data: Union[Dict, List, str] = None, **kwargs
    ):
        super().__init__(
            content=send_format(code.value[0], code.value[1], data), 
            status_code=code.value[2], 
            **kwargs,
        )
