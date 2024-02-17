from uuid import UUID

from pydantic import BaseModel, Field

from config import USERNAME_MAX_LENGTH, CLASSNAME_MAX_LENGTH
from .common import IdentifiableSchema, TimestampedSchema


class ClassSchema(IdentifiableSchema, TimestampedSchema):
    name: str
    info: str | None = Field(None)
    admin_username: str

    sunday: str | None = Field(None)
    monday: str | None = Field(None)
    tuesday: str | None = Field(None)
    wednesday: str | None = Field(None)
    thursday: str | None = Field(None)
    friday: str | None = Field(None)
    saturday: str | None = Field(None)


class CreateClassSchema(BaseModel):
    name: str = Field(max_length=CLASSNAME_MAX_LENGTH)
    info: str | None = Field(None)
    admin_username: str = Field(max_length=USERNAME_MAX_LENGTH)


class JoinClassSchema(BaseModel):
    class_id: UUID
    name: str = Field(max_length=USERNAME_MAX_LENGTH)
