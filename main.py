
from fastapi_cache.backends.redis import RedisBackend

from api_v1 import main_router as router_v1

from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache

from redis import asyncio as aioredis

from core.config import settings

from fastapi import Request
from fastapi import FastAPI

import uvicorn

from tasks.router import email_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(lifespan=lifespan)



redis = aioredis.from_url("redis://red-cn2832gl5elc73ea76g0:6379", encoding="utf-8", decode_responses=True)
FastAPICache.init(RedisBackend(redis), prefix="Head-Hunter-cache")



app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(email_router, prefix=settings.api_v1_prefix)



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)