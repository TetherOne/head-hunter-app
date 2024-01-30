from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ResumeUpdatePartial
from .schemas import ResumeCreate
from .schemas import ResumeUpdate

from core.models import Resume

from sqlalchemy import Result
from sqlalchemy import select



async def get_all_resume(session: AsyncSession) -> list[Resume]:

    stmt = select(Resume).order_by(Resume.id)
    result: Result = await session.execute(stmt)
    all_resume = result.scalars().all()

    return list(all_resume)



async def get_resume(session: AsyncSession, resume_id: int) -> Resume | None:

    return await session.get(Resume, resume_id)



async def create_resume(session: AsyncSession, resume_in: ResumeCreate) -> Resume:

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

    for name, value in resume_update.model_dump(exclude_unset=partial).items():
        setattr(resume, name, value)

    await session.commit()

    return resume



async def delete_resume(session: AsyncSession, resume: Resume) -> None:

    await session.delete(resume)
    await session.commit()






















