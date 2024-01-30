from api_v1.auth.manager import get_user_manager

from fastapi.templating import Jinja2Templates

from api_v1 import main_router as router_v1

from contextlib import asynccontextmanager

from api_v1.auth.auth import auth_backend

from api_v1.auth.schemas import UserCreate
from api_v1.auth.schemas import UserRead

from fastapi_users import FastAPIUsers

from core.config import settings

from fastapi import Request
from fastapi import FastAPI

import uvicorn

from core.models import User



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)



app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)



templates = Jinja2Templates(directory='templates')



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)