from uuid import UUID

from fastapi import APIRouter, status

from api.exceptions import NotFoundException
from schemas.classes import ClassSchema, CreateClassSchema
from services.classes import ClassService

router = APIRouter(tags=["Classes"])


@router.post(
    "/",
    response_model=ClassSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_class(body: CreateClassSchema):
    return await ClassService.create_class(body)


@router.get(
    "/{class_id}",
    response_model=ClassSchema
)
async def get_class(class_id: UUID):
    fetched_class = await ClassService.get_class(class_id)
    if not fetched_class:
        raise NotFoundException("Class not found.")
    return fetched_class
