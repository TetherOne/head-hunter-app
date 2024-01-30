from api_v1 import main_router as router_v1

from contextlib import asynccontextmanager

from core.config import settings

from fastapi import Request
from fastapi import FastAPI

import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)