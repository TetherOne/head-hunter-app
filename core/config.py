from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic_settings import BaseSettings

from pydantic import BaseModel

from dotenv import load_dotenv

import os



load_dotenv()



class DbSettings(BaseModel):

    url: str = f'postgresql+asyncpg://{os.environ.get("POSTGRES_USERNAME")}:{os.environ.get("POSTGRES_PASSWORD")}:@{os.environ.get("POSTGRES_HOSTNAME")}:5432/{os.environ.get("POSTGRES_DATABASE")}'
    echo: bool = False



class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db: DbSettings = DbSettings()



settings = Settings()



engine = create_async_engine(settings.db.url)
async_session_maker = async_sessionmaker(engine)
