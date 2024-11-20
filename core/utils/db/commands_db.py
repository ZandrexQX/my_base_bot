import datetime
from asyncio import run

from sqlalchemy.ext.asyncio import AsyncSession

from my_base.core.utils.db import User_db, connection
from sqlalchemy import select, update


# add
@connection()
async def add_query(session: AsyncSession, user_id: int, username: str, age: int):
    """
    Adds a new user to the database.

    Args:
        session: The database session.
        user_id: The Telegram user ID.
        username: The username of the user.
        age: The age of the user.

    Returns:
        The newly created User_db object.
    """
    user_db = User_db(
        user_id=user_id,
        username=username,
        age=age,
        reg_date=datetime.date.today().strftime('%d.%m.%Y')
    )
    session.add(user_db)
    return user_db

# res = run(add_query(user_id=342343213, username="Dima", age=21))
# print(res)

# select one
@connection(commit=False)
async def select_id(session: AsyncSession, user_id: int):
    """
    Select a user by user_id.

    Args:
        session: The database session.
        user_id: The Telegram user ID.

    Returns:
        The User_db object if found, otherwise None.
    """
    result = await session.execute(select(User_db).where(User_db.user_id == user_id))
    return result.scalar_one_or_none()

# res = run(select_id(user_id=375230092))
# print(res.to_dict())

# select multi
@connection(commit=False)
async def select_by_age(session: AsyncSession, value: int):
    """
    Select multiple users by age.

    Args:
        session: The database session.
        value: The age to select users by.

    Returns:
        A list of User_db objects that match the specified age.
    """
    res = await session.execute(select(User_db).where(User_db.age == value))
    return res.scalars().all()

# res = run(select_by_age(value=21))
# for r in res: print(r.to_dict())

@connection()
async def update_query(session: AsyncSession, user_id: int, key: str, value: int | str):
    """
    Update a user by user_id.

    Args:
        session: The database session.
        user_id: The Telegram user ID.
        key: The column name to update.
        value: The value to update the column with.

    Returns:
        None.
    """
    await session.execute(update(User_db).where(User_db.user_id == user_id), {key: value})

# res = run(update_query(user_id=342412313, key="username", value="Bob"))
# res = run(update_query(user_id=342412313, key="reg_date", value='01.01.2023'))
