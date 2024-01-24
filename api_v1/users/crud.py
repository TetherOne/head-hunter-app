from sqlalchemy import select
from sqlalchemy import Result

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User

from .schemas import UserCreate



async def get_users(session: AsyncSession) -> list[User]:
    """

    Функция для получения всех пользователей

    """
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()

    return list(users)



async def get_user(session: AsyncSession, user_id: int) -> User | None:
    """

    Функция для получения пользователя по id

    """
    return await session.get(User, user_id)



async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    """

    Функция для создания пользователя

    """
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()

    return user
