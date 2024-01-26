from sqlalchemy import select
from sqlalchemy import Result

from sqlalchemy.ext.asyncio import AsyncSession


from core.models import Resume

from .schemas import ResumeCreate, ResumeUpdate, ResumeUpdatePartial


async def get_all_resume(session: AsyncSession) -> list[Resume]:
    """

    Функция для получения всех пользователей

    """
    stmt = select(Resume).order_by(Resume.id)
    result: Result = await session.execute(stmt)
    all_resume = result.scalars().all()

    return list(all_resume)



async def get_resume(session: AsyncSession, resume_id: int) -> Resume | None:
    """

    Функция для получения пользователя по id

    """
    return await session.get(Resume, resume_id)



async def create_resume(session: AsyncSession, resume_in: ResumeCreate) -> Resume:
    """

    Функция для создания пользователя

    """
    resume = Resume(**resume_in.model_dump())
    session.add(resume)
    await session.commit()

    return resume



async def update_resume(session: AsyncSession, resume: Resume, resume_update: ResumeUpdate | ResumeUpdatePartial,) -> Resume:
    """

    Функция для обновления пользователя

    """

    for name, value in resume_update.model_dump().items():
        setattr(resume, name, value)

    await session.commit()

    return resume



async def delete_resume(session: AsyncSession, resume: Resume) -> None:
    """

    Функция для удаления пользователя

    """
    await session.delete(resume)
    await session.commit()






















