from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class User(Base):

    username: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))
