from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base


class User(Base):
    user_id: Mapped[int]
    username: Mapped[str]

    def __str__(self):
        return f"<User: {self.user_id}>"
    