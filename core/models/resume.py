from sqlalchemy.orm import Mapped

from core.models.base import Base



class Resume(Base):
    __tablename__ = 'resume'

    job_name: Mapped[str]
    skills: Mapped[str]
    experience: Mapped[str]
    salary: Mapped[int]
    phone: Mapped[str]

