from pydantic import BaseModel

from schemas.classes import ClassSchema
from schemas.classmates import ClassmateSchema


class JoinClassResponseSchema(BaseModel):
    new_class: ClassSchema
    joined_as: ClassmateSchema
