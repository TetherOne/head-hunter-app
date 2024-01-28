from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from .mixins import UserRelationMixin

from sqlalchemy import String

from core.models import Base



class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = 'profile'


    city: Mapped[str | None] = mapped_column(String(30))
    bio: Mapped[str | None]


