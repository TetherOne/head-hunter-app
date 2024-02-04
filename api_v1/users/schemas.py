from pydantic import ConfigDict
from pydantic import BaseModel
from pydantic import EmailStr



class UserBase(BaseModel):

    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool


class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int