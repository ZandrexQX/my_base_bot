from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession
from .db.url_db import users_url

from .db import Base, create_engine_db, proceed_schemas, get_session_maker, User_db


async def db_connect():
    async_engine = create_engine_db(users_url)
    await proceed_schemas(async_engine, Base.metadata)