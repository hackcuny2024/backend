from uuid import UUID

from sqlalchemy import select

from database.session import SessionScope
from database.tables.classmates import Classmate
from schemas.classes import JoinClassSchema
from schemas.classmates import ClassmateSchema


class ClassmatesService:

    @staticmethod
    async def join_class(schema: JoinClassSchema) -> ClassmateSchema:
        new_classmate = Classmate(**schema.model_dump())
        async with SessionScope.get_session() as session:
            session.add(new_classmate)
            await session.commit()
            return ClassmateSchema.model_validate(new_classmate)

    @staticmethod
    async def get_classmates(class_id: UUID) -> list[ClassmateSchema]:
        async with SessionScope.get_session() as session:
            return [
                ClassmateSchema.model_validate(classmate)
                for classmate in await session.scalars(
                    select(Classmate).where(Classmate.class_id == class_id)
                )
            ]

    @staticmethod
    async def get_classmate(classmate_id: UUID) -> ClassmateSchema | None:
        async with SessionScope.get_session() as session:
            fetched_classmate = await session.scalar(
                select(Classmate).where(Classmate.id == classmate_id)
            )
            if fetched_classmate:
                return ClassmateSchema.model_validate(fetched_classmate)
