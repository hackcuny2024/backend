from typing import Any

from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    def __init__(self,
                 detail: Any,
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 headers: dict[str | Any] | None = None):
        super().__init__(status_code, detail, headers)


class NotFoundException(HTTPException):
    def __init__(self,
                 detail: Any,
                 status_code: int = status.HTTP_404_NOT_FOUND,
                 headers: dict[str | Any] | None = None):
        super().__init__(status_code, detail, headers)