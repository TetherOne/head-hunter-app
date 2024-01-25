from pydantic import BaseModel
from pydantic import ConfigDict



class UserBase(BaseModel):

    name: str



class UserCreate(UserBase):
    pass



class UserUpdate(UserCreate):
    pass



class UserUpdatePartial(UserCreate):

    name: str | None = None



class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int