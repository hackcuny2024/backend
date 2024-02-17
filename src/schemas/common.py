from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class IdentifiableSchema(BaseModel):
    id: UUID


class TimestampedSchema(BaseModel):
    created_at: datetime
