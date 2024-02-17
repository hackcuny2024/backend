from sqlalchemy.orm import Mapped, mapped_column

from database.tables.abstract import IdentifiableAbstractTable, TimestampedAbstractTable


class Class(IdentifiableAbstractTable, TimestampedAbstractTable):
    __tablename__ = "classes"

    name: Mapped[str] = mapped_column(nullable=False, unique=False)
    info: Mapped[str | None] = mapped_column(nullable=True, unique=False)

    admin_username: Mapped[str] = mapped_column(nullable=False, unique=False)

    sunday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
    monday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
    tuesday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
    wednesday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
    thursday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
    friday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
    saturday: Mapped[str | None] = mapped_column(nullable=True, unique=False)
