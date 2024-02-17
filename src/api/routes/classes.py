from uuid import UUID

from fastapi import APIRouter, status
from sqlalchemy.exc import IntegrityError

from api.exceptions import NotFoundException, BadRequestException
from api.schemas import JoinClassResponseSchema
from schemas.classes import ClassSchema, CreateClassSchema, JoinClassSchema
from services.classes import ClassService
from services.classmates import ClassmatesService

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


@router.post(
    "/join",
    response_model=JoinClassResponseSchema
)
async def join_class(body: JoinClassSchema):
    fetched_class = await ClassService.get_class(body.class_id)
    if not fetched_class:
        raise NotFoundException("Class not found.")

    try:
        classmate = await ClassmatesService.join_class(body)
    except IntegrityError:
        raise BadRequestException("Classmate with the username specified already exists in the class.")

    return JoinClassResponseSchema(
        new_class=fetched_class,
        joined_as=classmate
    )
