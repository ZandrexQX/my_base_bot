from sqlalchemy import URL

users_url = URL.create(
        "postgresql+asyncpg",
        username='postgres',
        host='localhost',
        password='1',
        database='postgres',
        port=5432
    )