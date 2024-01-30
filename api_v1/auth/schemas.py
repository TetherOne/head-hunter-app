from typing import Optional

from fastapi_users import schemas

from pydantic import EmailStr



class UserRead(schemas.BaseUser[int]):

    id: int
    username: str
    email: EmailStr
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]



class UserCreate(schemas.BaseUserCreate):

    username: str
    password: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False