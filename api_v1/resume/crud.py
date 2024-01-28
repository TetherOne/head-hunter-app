from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ResumeUpdatePartial
from .schemas import ResumeCreate
from .schemas import ResumeUpdate

from sqlalchemy import Result
from sqlalchemy import select

from core.models import Resume



async def get_all_resume(session: AsyncSession) -> list[Resume]:
    """

    Функция для получения всех резюме

    """
    stmt = select(Resume).order_by(Resume.id)
    result: Result = await session.execute(stmt)
    all_resume = result.scalars().all()

    return list(all_resume)



async def get_resume(session: AsyncSession, resume_id: int) -> Resume | None:
    """

    Функция для получения резюме по id

    """
    return await session.get(Resume, resume_id)



async def create_resume(session: AsyncSession, resume_in: ResumeCreate) -> Resume:
    """

    Функция для создания резюме

    """
    resume = Resume(**resume_in.model_dump())
    session.add(resume)
    await session.commit()

    return resume



async def update_resume(
        session: AsyncSession,
        resume: Resume,
        resume_update: ResumeUpdate | ResumeUpdatePartial,
        partial: bool = False,
) -> Resume:
    """

    Функция для обновления резюме

    """

    for name, value in resume_update.model_dump(exclude_unset=partial).items():
        setattr(resume, name, value)

    await session.commit()

    return resume



async def delete_resume(session: AsyncSession, resume: Resume) -> None:
    """

    Функция для удаления резюме

    """
    await session.delete(resume)
    await session.commit()






















