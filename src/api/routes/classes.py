import datetime
from uuid import UUID

from fastapi import APIRouter

from schemas.classes import ClassSchema

router = APIRouter(tags=["Classes"])


@router.get(
    "/{class_id}",
    response_model=ClassSchema
)
async def get_class(class_id: UUID):
    return ClassSchema(
        id=class_id,
        name="Math class",
        info="This class is awesome",
        created_at=datetime.datetime.utcnow()
    )
