from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from typing import TYPE_CHECKING, AsyncGenerator

from sqlalchemy import String

from core.models import Base
from ..config import async_session_maker

if TYPE_CHECKING:
    from .resume import Resume
    from .profile import Profile



class User(SQLAlchemyBaseUserTable[int], Base):

    __tablename__ = 'users'


    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))


    resume: Mapped[list['Resume']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    session = None
    try:
        async with async_session_maker() as s:
            session = s
            yield session
    except GeneratorExit:
        if session:
            await session.close()
        raise



async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)