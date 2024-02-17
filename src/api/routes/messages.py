import datetime
from uuid import UUID, uuid4
import random

from fastapi import APIRouter

from schemas.messages import MessageSchema

router = APIRouter(tags=["Messages"])


@router.get(
    "/",
    response_model=list[MessageSchema]
)
async def get_messages(class_id: UUID):
    messages = [
        MessageSchema(
            id=uuid4(),
            class_id=class_id,
            sender_name=f"Classmate #{i % 5}",
            text=f"hello {i}",
            created_at=datetime.datetime.utcnow()
        )
        for i in range(random.randrange(0, 30))
    ]
    random.shuffle(messages)
    return messages
