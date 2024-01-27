from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .resume import Resume
    from .profile import Profile



class User(Base):

    username: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))

    resume: Mapped[list['Resume']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')