from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from .mixins import UserRelationMixin

from typing import TYPE_CHECKING

from sqlalchemy import String

from core.models import Base



if TYPE_CHECKING:
    from .user import User



class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = 'profile'


    city: Mapped[str | None] = mapped_column(String(30))
    bio: Mapped[str | None]


