import datetime

from ..db import User_db, get_session, url_db
from sqlalchemy import select, update

# async def query(session: AsyncSession):
#     async with session as conn:
#         user_1 = User(
#         user_id=342412351,
#         username="Alex"
#         )
#         conn.add(user_1)
#         await conn.commit()

async def insert_query(user_id: int, username: str, age: int):
    session = await get_session(url_db.users_url)
    async with session as conn:
        current_date = datetime.date.today()
        user_db = User_db(
            user_id=user_id,
            username=username,
            age=age,
            reg_date=current_date.strftime('%d.%m.%Y')
        )
        conn.add(user_db)
        await conn.commit()
        await session.close()


async def select_id(user_id: int):
    session = await get_session(url_db.users_url)
    async with session as conn:
        stmt = select(User_db).where(User_db.user_id == user_id)
        res = await conn.execute(stmt)
        await session.close()
        return res.scalar_one_or_none()

async def update_query(user_id: int, key: str, value: int|str):
    session = await get_session(url_db.users_url)
    async with session as conn:
        await conn.execute(
            update(User_db).where(User_db.user_id == user_id), {key: value}
        )
        await conn.commit()
        await session.close()
