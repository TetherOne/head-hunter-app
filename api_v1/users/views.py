from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .dependencies import user_by_id

from .schemas import User, UserCreate, UserUpdate, UserUpdatePartial

from . import crud



router = APIRouter(tags=['Users'])



@router.get('/', response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_users(session=session)



@router.post('/', response_model=User)
async def create_user(
        user_in: UserCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_user(session=session, user_in=user_in)



@router.get('/{user_id}', response_model=User)
async def get_user(
    user: User = Depends(user_by_id),
):
    return user



@router.put('/{user_id}')
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_user(
        user=user,
        session=session,
        user_update=user_update,
    )



@router.patch('/{user_id}')
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_user(
        user=user,
        session=session,
        user_update=user_update,
    )































