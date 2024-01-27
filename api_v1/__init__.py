

from fastapi import APIRouter

from api_v1.resume.views import resume_router
from api_v1.users.views import user_router

main_router = APIRouter()


main_router.include_router(router=resume_router, prefix='/resume')
main_router.include_router(router=user_router, prefix='/users')

