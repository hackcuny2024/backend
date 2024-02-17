from uuid import UUID

from sqlalchemy import select

from database.session import SessionScope
from database.tables.classes import Class
from schemas.classes import CreateClassSchema, ClassSchema


class ClassService:

    @staticmethod
    async def create_class(schema: CreateClassSchema) -> ClassSchema:
        new_class = Class(**schema.model_dump())
        async with SessionScope.get_session() as session:
            session.add(new_class)
            await session.commit()
            return ClassSchema.model_validate(new_class)

    @staticmethod
    async def get_class(class_id: UUID) -> ClassSchema | None:
        async with SessionScope.get_session() as session:
            fetched_class = await session.scalar(select(Class).where(Class.id == class_id))
            if fetched_class:
                return ClassSchema.model_validate(fetched_class)
