from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class IdentifiableSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class TimestampedSchema(BaseModel):
    created_at: datetime
