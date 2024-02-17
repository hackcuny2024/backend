from pydantic import BaseModel, Field

from .common import IdentifiableSchema, TimestampedSchema


class ClassSchema(IdentifiableSchema, TimestampedSchema):
    name: str
    info: str | None = Field(None)

    sunday: str | None = Field(None)
    monday: str | None = Field(None)
    tuesday: str | None = Field(None)
    wednesday: str | None = Field(None)
    thursday: str | None = Field(None)
    friday: str | None = Field(None)
    saturday: str | None = Field(None)


class JoinClassSchema(BaseModel):
    username: str = Field(max_length=100)
