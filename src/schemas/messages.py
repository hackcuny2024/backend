from uuid import UUID

from pydantic import Field

from config import USERNAME_MAX_LENGTH
from .common import IdentifiableSchema, TimestampedSchema


class MessageSchema(IdentifiableSchema, TimestampedSchema):
    class_id: UUID
    sender_name: str = Field(max_length=USERNAME_MAX_LENGTH)
    text: str
