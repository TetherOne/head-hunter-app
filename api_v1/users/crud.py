from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User



async def get_users(session: AsyncSession) -> list[User]:
    """

    Функция для получения всех резюме

    """
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()

    return list(users)