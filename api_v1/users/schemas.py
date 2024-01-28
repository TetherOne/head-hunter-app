from pydantic import ConfigDict
from pydantic import BaseModel



class UserBase(BaseModel):

    username: str
    surname: str



class UserCreate(UserBase):
    pass



class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int