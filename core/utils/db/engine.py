from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.engine import URL


def create_engine_db(url: URL|str) -> AsyncEngine:
    return create_async_engine(url=url, echo=True, pool_pre_ping=True)

async def proceed_schemas(engine: AsyncEngine, metadata):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

async def get_session_maker(engine: AsyncEngine) -> AsyncSession:
    return AsyncSession(engine)

async def get_session(url: URL):
    async_engine = create_engine_db(url)
    return await get_session_maker(async_engine)
