from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from typing import TYPE_CHECKING

from sqlalchemy import String

from core.models import Base



if TYPE_CHECKING:
    from .resume import Resume
    from .profile import Profile



class User(Base):

    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(40))

    resume: Mapped[list['Resume']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')