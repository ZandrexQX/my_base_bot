from sqlalchemy import URL

users_url = URL.create(
        "postgresql+asyncpg",
        username='postgres',
        host='localhost',
        password='53792162_db',
        database='postgres',
        port=5432
    )