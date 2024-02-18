from uuid import UUID

from sqlalchemy import select, desc

from database.session import SessionScope
from database.tables.classmates import Classmate
from database.tables.messages import Message
from schemas.messages import SendMessageSchema, MessageSchema


class MessagesService:

    @staticmethod
    async def send_message(schema: SendMessageSchema) -> MessageSchema:
        message = Message(**schema.model_dump())
        async with SessionScope.get_session() as session:
            session.add(message)
            await session.commit()
            return MessageSchema.model_validate(message)

    @staticmethod
    async def get_messages(class_id: UUID, thread_id: UUID | None = None) -> list[MessageSchema]:
        stmt = select(Message, Classmate.name).where(
            Message.class_id == class_id,
            Message.thread_id == thread_id
        ).join(
            Classmate,
            Message.sender_id == Classmate.id
        )

        async with SessionScope.get_session() as session:
            return [
                MessageSchema(
                    **entry[0].__dict__,
                    sender_name=entry[1]
                )
                for entry in (await session.execute(stmt)).all()
            ]
