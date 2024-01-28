from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import UserCreate

from core.models import User

from crud import create_user_profile

from sqlalchemy import Result
from sqlalchemy import select



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



async def create_user_and_profile(session: AsyncSession, user_in: UserCreate) -> User:
    """

    Функция для создания пользователя и его профиля

    """
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()

    user_id = user.id

    await create_user_profile(session, user_id)

    return user

