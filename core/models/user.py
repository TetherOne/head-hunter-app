from sqlalchemy.orm import Mapped

from core.models.base import Base


class User(Base):
    __tablename__ = 'user'

    name: Mapped[str]

