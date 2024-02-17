from uuid import UUID

from fastapi import APIRouter, status

from api.exceptions import BadRequestException
from schemas.threads import ThreadSchema, CreateThreadSchema
from services.classmates import ClassmatesService
from services.threads import ThreadsService

router = APIRouter(tags=["Threads"])


@router.post(
    "/",
    response_model=ThreadSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_thread(body: CreateThreadSchema):
    proof_of_belonging = await ClassmatesService.get_classmate(body.creator_id)
    if not proof_of_belonging or proof_of_belonging.class_id != body.class_id:
        raise BadRequestException("You don't belong to the class specified.")

    return await ThreadsService.create_thread(body)


@router.get(
    "/",
    response_model=list[ThreadSchema]
)
async def get_threads(class_id: UUID):
    return await ThreadsService.get_threads(class_id)
