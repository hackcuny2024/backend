from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.tables.abstract import IdentifiableAbstractTable, TimestampedAbstractTable


class Message(IdentifiableAbstractTable, TimestampedAbstractTable):
    __tablename__ = "messages"

    class_id: Mapped[UUID] = mapped_column(ForeignKey("classes.id"), nullable=False)
    sender_id: Mapped[UUID] = mapped_column(ForeignKey("classmates.id"), nullable=False)
    thread_id: Mapped[UUID | None] = mapped_column(ForeignKey("threads.id"), nullable=True)

    text: Mapped[str] = mapped_column(nullable=False)
