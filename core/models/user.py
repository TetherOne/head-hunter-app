from sqlalchemy.orm import Mapped

from core.models.base import Base


class User(Base):

    name: Mapped[str]

