from fastapi_users import schemas

from pydantic import EmailStr



class UserRead(schemas.BaseUser[int]):

    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool


    class Config:
        orm_mode = True



class UserCreate(schemas.BaseUserCreate):

    username: str
    password: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool



class UserUpdate(schemas.BaseUserUpdate):
    pass