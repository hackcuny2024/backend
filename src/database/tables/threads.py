from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from database.tables.abstract import IdentifiableAbstractTable, TimestampedAbstractTable


class Thread(IdentifiableAbstractTable, TimestampedAbstractTable):
    __tablename__ = "threads"
    __table_args__ = (UniqueConstraint("class_id", "name"),)

    class_id: Mapped[UUID] = mapped_column(ForeignKey("classes.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False, unique=False)

    created_by: Mapped[UUID] = mapped_column(ForeignKey("classmates.id"), nullable=False)
