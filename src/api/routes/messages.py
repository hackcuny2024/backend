import datetime
from uuid import UUID, uuid4
import random

from fastapi import APIRouter, Query
from sqlalchemy.exc import IntegrityError

from api.exceptions import BadRequestException
from api.schemas import SendMessageRequesstSchema
from schemas.messages import MessageSchema, SendMessageSchema
from services.classes import ClassService
from services.classmates import ClassmatesService
from services.messages import MessagesService

router = APIRouter(tags=["Messages"])


@router.post(
    "/",
    response_model=MessageSchema
)
async def send_message(body: SendMessageRequesstSchema):
    classmate = await ClassmatesService.get_classmate(body.sender_id)
    if not classmate:
        raise BadRequestException("Invalid sender_id.")

    class_ = await ClassService.get_class(classmate.class_id)

    try:
        return await MessagesService.send_message(
            SendMessageSchema(
                class_id=class_.id,
                sender_id=classmate.id,
                thread_id=body.thread_id,
                text=body.text
            )
        )
    except IntegrityError:
        raise BadRequestException("Invalid thread_id.")


@router.get(
    "/",
    response_model=list[MessageSchema]
)
async def get_messages(
    class_id: UUID, thread_id: UUID | None = Query(None)
):
    return await MessagesService.get_messages(class_id, thread_id)
