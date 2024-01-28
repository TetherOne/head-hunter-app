from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Resume(UserRelationMixin, Base):
    __tablename__ = 'resume'
    _user_back_populates = 'resume'


    job_name: Mapped[str]
    skills: Mapped[str]
    experience: Mapped[str]
    salary: Mapped[int]

