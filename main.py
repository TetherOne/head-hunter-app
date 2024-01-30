

from api_v1 import main_router as router_v1, fastapi_users

from contextlib import asynccontextmanager

from core.config import settings

from fastapi import Request, Depends
from fastapi import FastAPI

import uvicorn

from core.models import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, i dont know who are you"



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)