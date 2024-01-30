from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from sqlalchemy import ForeignKey

from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from .user import User



class UserRelationMixin:

    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None


    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey('users.id'),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )


    @declared_attr
    def user(cls) -> Mapped['User']:
        return relationship(
            'User',
            back_populates=cls._user_back_populates,
        )
