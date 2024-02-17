from uuid import UUID

from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.tables.abstract import IdentifiableAbstractTable, TimestampedAbstractTable


class Classmate(IdentifiableAbstractTable, TimestampedAbstractTable):
    __tablename__ = "classmates"
    __table_args__ = (UniqueConstraint("class_id", "name"),)

    class_id: Mapped[UUID] = mapped_column(ForeignKey("classes.id"), unique=False, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
