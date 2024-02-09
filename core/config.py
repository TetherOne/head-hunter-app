
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic_settings import BaseSettings

from pydantic import BaseModel




class DbSettings(BaseModel):

    url: str = f'postgresql+asyncpg://head_hunter_test:35Koz4lWiUu87GggjaON6N12OzrFyX4j@dpg-cn3428vqd2ns73eelg6g-a:5432/35Koz4lWiUu87GggjaON6N12OzrFyX4j'
    echo: bool = False



class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db: DbSettings = DbSettings()



settings = Settings()



engine = create_async_engine(settings.db.url)
async_session_maker = async_sessionmaker(engine)
