from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base



class Resume(Base):
    __tablename__ = 'resume'

    job_name: Mapped[str]
    skills: Mapped[str]
    experience: Mapped[str]
    salary: Mapped[int]

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
    )
