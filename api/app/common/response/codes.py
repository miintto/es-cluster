from xmlrpc.client import SERVER_ERROR
from starlette import status
from enum import Enum


class Http2XX(Enum):
    SUCCESS = ("S000", "성공", status.HTTP_200_OK)
    CREATED = ("S001", "생성 완료", status.HTTP_201_CREATED)


class Http4XX(Enum):
    BAD_REQUEST = ("F000", "잘못된 요청", status.HTTP_400_BAD_REQUEST)
    VALIDATE_ERROR = (
        "F001", "유효하지 않은 파라미터입니다.", status.HTTP_422_UNPROCESSABLE_ENTITY
    )
    INVALID_DATE_RANGE = (
        "F002",
        "시작 날짜가 종료 날짜보다 큽니다.",
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


class Http5XX(Enum):
    SERVER_ERROR = (
        "E000", "알 수 없는 에러", status.HTTP_500_INTERNAL_SERVER_ERROR
    )
