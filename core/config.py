from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic_settings import BaseSettings

from pydantic import BaseModel



class DbSettings(BaseModel):

    url: str = f'postgresql+asyncpg://postgres_user:7xfGzDrT0rD9N560L1D7tvauHobN8adT@dpg-cn2a4aed3nmc739bo3sg-a:5432/postgres_hh'
    echo: bool = False



class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db: DbSettings = DbSettings()



settings = Settings()



engine = create_async_engine(settings.db.url)
async_session_maker = async_sessionmaker(engine)