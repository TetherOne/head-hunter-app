from contextlib import asynccontextmanager

from api_v1 import main_router as router_v1

from core.config import settings
from fastapi import Request
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.testclient import TestClient



@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

templates = Jinja2Templates(directory='templates')



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)