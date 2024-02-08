from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic_settings import BaseSettings

from pydantic import BaseModel



class DbSettings(BaseModel):

    url: str = f'postgresql+asyncpg://head_hunter_test:Wrb27C2l13aG8c1un6gbXwtKyqa8sISa@dpg-cn281sol6cac739b7e40-a:5432/head_hunter'
    echo: bool = False



class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db: DbSettings = DbSettings()



settings = Settings()



engine = create_async_engine(settings.db.url)
async_session_maker = async_sessionmaker(engine)