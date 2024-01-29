from pydantic import ConfigDict
from pydantic import BaseModel



class UserBase(BaseModel):

    username: str
    password: str



class UserCreate(UserBase):
    pass



class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int