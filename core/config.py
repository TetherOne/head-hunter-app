from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic_settings import BaseSettings

from pydantic import BaseModel



class DbSettings(BaseModel):

    url: str = f'postgresql+asyncpg://head_hunter_test:UWZoR2KhgtWiUJjHQzcGOqCbMyEbbXx3@dpg-cn28bm2cn0vc738u4k50-a:5432/head_hunter_ugob'
    echo: bool = False



class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db: DbSettings = DbSettings()



settings = Settings()



engine = create_async_engine(settings.db.url)
async_session_maker = async_sessionmaker(engine)