from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import BaseModel



class UserBase(BaseModel):

    username: str
    hashed_password: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool



class UserCreate(UserBase):
    pass



class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int