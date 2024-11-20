from functools import wraps

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from my_base.core.utils.db import Base
from my_base.core.utils.db.url_db import users_url


DEBUG_MODE = False

engine = create_async_engine(url=users_url, echo=DEBUG_MODE)
get_session = async_sessionmaker(engine, expire_on_commit=False)

async def db_connect():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def connection(commit: bool = True):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with get_session() as session:
                try:
                    result = await func(*args, session=session,  **kwargs)
                    if commit:
                        await session.commit()
                    return result
                except Exception as e:
                    await session.rollback()
                    raise e
                finally:
                    await session.close()
        return wrapper
    return decorator