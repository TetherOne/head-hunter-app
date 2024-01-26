from pydantic import BaseModel
from pydantic import ConfigDict



class ResumeBase(BaseModel):

    job_name: str
    skills: str
    experience: str
    salary: int
    phone: str


class ResumeCreate(ResumeBase):
    pass



class ResumeUpdate(ResumeCreate):
    pass



class ResumeUpdatePartial(ResumeCreate):

    job_name: str | None = None
    skills: str | None = None
    experience: str | None = None
    salary: int | None = None
    phone: str | None = None


class Resume(ResumeBase):

    model_config = ConfigDict(from_attributes=True)

    id: int