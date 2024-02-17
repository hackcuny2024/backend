from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker

from . import tables

from database.base import Base
from database.engine import create_async_engine, init_tables
from database.session import SessionScope as __SessionScope


async def init_db(url: URL | str):
    async_engine = create_async_engine(url)
    __SessionScope.init(async_sessionmaker(async_engine, expire_on_commit=False))
    await init_tables(async_engine, Base.metadata)
