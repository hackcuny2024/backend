from uuid import UUID

from pydantic import BaseModel

from schemas.common import IdentifiableSchema, TimestampedSchema


class ThreadSchema(IdentifiableSchema, TimestampedSchema):
    class_id: UUID
    name: str
    created_by: UUID


class CreateThreadSchema(BaseModel):
    class_id: UUID
    name: str
    creator_id: UUID
