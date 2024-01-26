from contextlib import asynccontextmanager

from api_v1 import router as router_v1

from core.models import db_helper

from core.config import settings

from core.models import Base

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