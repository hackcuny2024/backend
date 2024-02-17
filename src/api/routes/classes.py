import datetime
from uuid import UUID, uuid4

from fastapi import APIRouter, status

from api.exceptions import NotFoundException
from schemas.classes import ClassSchema, CreateClassSchema
from schemas.classmates import ClassmateSchema

router = APIRouter(tags=["Classes"])


TEMPORARY_CLASSES: list[ClassSchema] = []

TEMPORARY_CLASSMATES: list[ClassmateSchema] = []


@router.post(
    "/",
    response_model=ClassSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_class(body: CreateClassSchema):
    new_class = ClassSchema(
        id=uuid4(),
        name=body.name,
        info=body.info,
        created_at=datetime.datetime.utcnow()
    )
    TEMPORARY_CLASSES.append(new_class)
    return new_class


@router.get(
    "/{class_id}",
    response_model=ClassSchema
)
async def get_class(class_id: UUID):
    for class_entry in TEMPORARY_CLASSES:
        if class_entry.id == class_id:
            return class_entry
    raise NotFoundException("Class not found.")
