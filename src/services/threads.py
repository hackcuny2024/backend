from uuid import UUID

from sqlalchemy import select

from database.session import SessionScope
from database.tables.threads import Thread
from schemas.threads import CreateThreadSchema, ThreadSchema


class ThreadsService:

    @staticmethod
    async def create_thread(schema: CreateThreadSchema) -> ThreadSchema:
        new_thread = Thread(
            class_id=schema.class_id,
            name=schema.name,
            created_by=schema.creator_id
        )
        async with SessionScope.get_session() as session:
            session.add(new_thread)
            await session.commit()
            return ThreadSchema.model_validate(new_thread)

    @staticmethod
    async def get_threads(class_id: UUID) -> list[ThreadSchema]:
        async with SessionScope.get_session() as session:
            return [
                ThreadSchema.model_validate(thread)
                for thread in await session.scalars(
                    select(Thread).where(Thread.class_id == class_id)
                )
            ]
