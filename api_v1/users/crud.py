from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import Result
from sqlalchemy import select

from core.models import User



async def get_users(session: AsyncSession) -> list[User]:

    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()

    return list(users)



async def get_user(session: AsyncSession, user_id: int) -> User | None:

    return await session.get(User, user_id)
