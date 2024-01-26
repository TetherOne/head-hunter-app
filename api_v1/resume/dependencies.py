from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import db_helper
from core.models import Resume
from . import crud


async def resume_by_id(
        resume_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Resume:

    resume = await crud.get_resume(session=session, resume_id=resume_id)

    if resume is not None:

        return resume

    raise HTTPException(

        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User {resume_id} not found',

    )