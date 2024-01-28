from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from .dependencies import user_by_id
from core.models import db_helper

from .schemas import UserCreate
from .schemas import User

from . import crud



user_router = APIRouter(tags=['Users'])



@user_router.get('/', response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_users(session=session)



@user_router.post(
    '/',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
        user_in: UserCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_user_and_profile(session=session, user_in=user_in)



@user_router.get('/{user_id}', response_model=User)
async def get_user(
    user: User = Depends(user_by_id),
):
    return user