from uuid import UUID

from fastapi import APIRouter

from schemas.classmates import ClassmateSchema
from services.classmates import ClassmatesService

router = APIRouter(tags=["Classmates"])


@router.get(
    "/",
    response_model=list[ClassmateSchema]
)
async def get_classmates(class_id: UUID):
    return await ClassmatesService.get_classmates(class_id)
