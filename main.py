from fastapi_cache import FastAPICache

from api_v1 import main_router as router_v1

from contextlib import asynccontextmanager
from fastapi_cache.backends.redis import RedisBackend
from core.config import settings
from redis import asyncio as aioredis
from fastapi import Request
from fastapi import FastAPI

import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(lifespan=lifespan)



redis = aioredis.from_url("redis://127.0.0.1:6379", encoding="utf-8", decode_responses=True)
FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")



app.include_router(router=router_v1, prefix=settings.api_v1_prefix)



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)