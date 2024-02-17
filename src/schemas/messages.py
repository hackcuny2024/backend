from uuid import UUID

from pydantic import Field, BaseModel

from config import USERNAME_MAX_LENGTH
from .common import IdentifiableSchema, TimestampedSchema


class MessageSchema(IdentifiableSchema, TimestampedSchema):
    class_id: UUID
    sender_id: UUID
    sender_name: str | None = Field(None, max_length=USERNAME_MAX_LENGTH)
    thread_id: UUID | None = Field(None)
    text: str


class SendMessageSchema(BaseModel):
    class_id: UUID
    sender_id: UUID
    thread_id: UUID | None = Field(None)
    text: str
