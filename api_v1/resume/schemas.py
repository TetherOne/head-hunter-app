from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict



class ResumeBase(BaseModel):

    user_id: int
    job_name: str
    skills: str
    experience: str
    salary: int



class ResumeCreate(ResumeBase):
    pass



class ResumeUpdate(ResumeCreate):
    pass



class ResumeUpdatePartial(ResumeCreate):

    user_id: int = None
    job_name: Optional[str] = None
    skills: Optional[str] = None
    experience: Optional[str] = None
    salary: Optional[int] = None



class Resume(ResumeBase):

    model_config = ConfigDict(from_attributes=True)

    id: int