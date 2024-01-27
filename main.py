from contextlib import asynccontextmanager

import aiosignal
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from api_v1 import main_router as router_v1

from core.config import settings

from fastapi import FastAPI

import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


  
@app.get('/')
def hello_world():
    return {
        'message': 'hellow world'
    }



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)