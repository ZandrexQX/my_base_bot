import datetime
from asyncio import run

from sqlalchemy.ext.asyncio import AsyncSession

from core.utils.db import User, connection, Base
from sqlalchemy import select, update


# add
@connection()
async def add_query(session: AsyncSession, model: Base, **kwargs):
    model_db = model(**kwargs)
    session.add(model_db)
    return model_db

# res = run(add_query(user_id=342343213, username="Dima", age=21))
# print(res)

# select one
@connection(commit=False)
async def select_user_id(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.user_id == user_id))
    return result.scalar_one_or_none()

# res = run(select_id(user_id=375230092))
# print(res.to_dict())

# select multi
@connection(commit=False)
async def select_by_age(session: AsyncSession, value: int):
    res = await session.execute(select(User_db).where(User_db.age == value))
    return res.scalars().all()

# res = run(select_by_age(value=21))
# for r in res: print(r.to_dict())

@connection()
async def update_query(session: AsyncSession, user_id: int, key: str, value: int | str):
    await session.execute(update(User_db).where(User_db.user_id == user_id), {key: value})

# res = run(update_query(user_id=342412313, key="username", value="Bob"))
# res = run(update_query(user_id=342412313, key="reg_date", value='01.01.2023'))
