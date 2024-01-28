from pydantic_settings import BaseSettings

from pydantic import BaseModel

from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


# BASE_DIR = Path(__file__).parent.parent
#
# DB_PATH = BASE_DIR / 'db.sqlite3'

class DbSettings(BaseModel):
    # url: str = f'sqlite+aiosqlite:///{DB_PATH}'

    url: str = f'postgresql+asyncpg://postgres:qwerty@localhost:5432/head_hunter'
    echo: bool = False


class Settings(BaseSettings):
    api_v1_prefix: str = '/api/v1'

    db: DbSettings = DbSettings()



settings = Settings()

engine = create_async_engine(settings.db.url)
async_session_maker = async_sessionmaker(engine)