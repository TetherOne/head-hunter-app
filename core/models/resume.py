from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from .mixins import UserRelationMixin

from core.models.base import Base

from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from .user import User



class Resume(UserRelationMixin, Base):

    __tablename__ = 'resume'
    _user_back_populates = 'resume'

    id: Mapped[int] = mapped_column(primary_key=True)
    job_name: Mapped[str]
    skills: Mapped[str]
    experience: Mapped[str]
    salary: Mapped[int]

