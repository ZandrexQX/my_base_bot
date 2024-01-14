from sqlalchemy import BigInteger, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User_db(Base):
    __tablename__ = 'users_account'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column(INTEGER)
    reg_date: Mapped[str] = mapped_column()

    def __str__(self):
        return f"<User: {self.user_id}>"
