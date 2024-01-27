from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import User
from . import crud

user_router = APIRouter(tags=['Users'])



@user_router.get('/', response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_users(session=session)