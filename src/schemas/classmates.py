from uuid import UUID

from .common import IdentifiableSchema, TimestampedSchema


class ClassmateSchema(IdentifiableSchema, TimestampedSchema):
    class_id: UUID
    name: str
