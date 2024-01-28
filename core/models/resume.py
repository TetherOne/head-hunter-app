from .mixins import UserRelationMixin

from sqlalchemy.orm import Mapped

from core.models.base import Base



class Resume(UserRelationMixin, Base):
    __tablename__ = 'resume'
    _user_back_populates = 'resume'


    job_name: Mapped[str]
    skills: Mapped[str]
    experience: Mapped[str]
    salary: Mapped[int]

