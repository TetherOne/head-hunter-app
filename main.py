from contextlib import asynccontextmanager

from fastapi_users import fastapi_users, FastAPIUsers

from api_v1 import main_router as router_v1
from api_v1.auth.auth import auth_backend
from api_v1.auth.manager import get_user_manager
from api_v1.auth.schemas import UserRead, UserCreate

from core.config import settings
from fastapi import Request
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.testclient import TestClient

from core.models import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
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

current_user = fastapi_users.current_user()


templates = Jinja2Templates(directory='templates')



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)