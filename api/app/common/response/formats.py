from typing import Dict, List, Union

from fastapi.encoders import jsonable_encoder


def send_format(code: str, message: str, data: Union[Dict, List, str]) -> Dict:
    return {
        "code": code or "S000",
        "message": message,
        "data": jsonable_encoder(data),
    }
