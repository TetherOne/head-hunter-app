from .schemas import ResumeUpdatePartial
from .schemas import ResumeCreate
from .schemas import ResumeUpdate
from .schemas import Resume

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import resume_by_id

from core.models import db_helper

from . import crud



resume_router = APIRouter(tags=['Resume'])



@resume_router.get('/', response_model=list[Resume])
async def get_all_resume(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_all_resume(session=session)



@resume_router.post(
    '/',
    response_model=Resume,
    status_code=status.HTTP_201_CREATED,
)
async def create_resume(
        resume_in: ResumeCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_resume(session=session, resume_in=resume_in)



@resume_router.get('/{resume_id}', response_model=Resume)
async def get_resume(
    resume: Resume = Depends(resume_by_id),
):
    return resume



@resume_router.put('/{resume_id}')
async def update_resume(
    resume_update: ResumeUpdate,
    resume: Resume = Depends(resume_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_resume(
        resume=resume,
        session=session,
        resume_update=resume_update,
    )



@resume_router.patch('/{resume_id}')
async def update_resume_partial(
    resume_update: ResumeUpdatePartial,
    resume: Resume = Depends(resume_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_resume(
        session=session,
        resume=resume,
        resume_update=resume_update,
        partial=True
    )



@resume_router.delete("/{resume_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_resume(
    resume: Resume = Depends(resume_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:

    await crud.delete_resume(session=session, resume=resume)































