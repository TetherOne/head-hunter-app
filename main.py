
from fastapi_cache.backends.redis import RedisBackend

from api_v1 import main_router as router_v1

from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache

from redis import asyncio as aioredis

from core.config import settings

from fastapi import Request, BackgroundTasks
from fastapi import FastAPI

import uvicorn

# from tasks.tasks import sum_num


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(lifespan=lifespan)



redis = aioredis.from_url("redis://127.0.0.1:6379", encoding="utf-8", decode_responses=True)
FastAPICache.init(RedisBackend(redis), prefix="Head-Hunter-cache")



app.include_router(router=router_v1, prefix=settings.api_v1_prefix)






@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



# @app.get('/ping')
# async def ping(background_tasks: BackgroundTasks):
#     a = 11
#     b = 5
#     background_tasks.add_task(sum_num, a, b)
#     return {'message': 'pong'}




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)