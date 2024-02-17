from uuid import UUID

from pydantic import BaseModel, Field

from schemas.classes import ClassSchema
from schemas.classmates import ClassmateSchema


class JoinClassResponseSchema(BaseModel):
    new_class: ClassSchema
    joined_as: ClassmateSchema


class SendMessageRequesstSchema(BaseModel):
    sender_id: UUID
    thread_id: UUID | None = Field(None)
    text: str
