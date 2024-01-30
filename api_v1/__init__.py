from api_v1.auth.manager import get_user_manager

from api_v1.resume.views import resume_router

from api_v1.auth.schemas import UserCreate
from api_v1.auth.schemas import UserRead

from api_v1.users.views import user_router

from api_v1.auth.auth import auth_backend

from fastapi_users import FastAPIUsers

from fastapi import APIRouter

from core.models import User



main_router = APIRouter()



main_router.include_router(router=resume_router, prefix='/resume')
main_router.include_router(router=user_router, prefix='/users')



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)



main_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)



main_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)