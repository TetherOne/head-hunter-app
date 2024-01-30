from fastapi_users import fastapi_users

from api_v1.auth.auth import auth_backend
from api_v1.auth.manager import get_user_manager
from api_v1.auth.schemas import UserRead, UserCreate
from api_v1.demo_auth.views import demo_auth_router
from api_v1.resume.views import resume_router

from api_v1.users.views import user_router

from fastapi import APIRouter



main_router = APIRouter()



main_router.include_router(router=resume_router, prefix='/resume')
main_router.include_router(router=user_router, prefix='/users')
main_router.include_router(router=demo_auth_router)
# main_router.include_router(router=fastapi_users.get_register_router(get_user_manager, UserRead, UserCreate), prefix="/auth", response_model=None)
# main_router.include_router(router=fastapi_users.get_auth_router(get_user_manager, auth_backend),  prefix="/auth/jwt")

# fastapi_users = FastAPIUsers(
#     get_user_manager,
#     [auth_backend],
# )
#
#
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )