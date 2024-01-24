from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import async_scoped_session

from asyncio import current_task

from core.config import settings



class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):

        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )

        return session

    async def scoped_session_dependency(self) -> AsyncSession:

        session = self.get_scoped_session()
        yield session
        await session.close()



db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)