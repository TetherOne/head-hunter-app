Сайт находится в разработке, используется фреймворк FastAPI

- Валидация при помощи Pydantic
- Создание миграций через Alembic
- Контроль зависимостей через Poetry
- Написаны тесты при помощи Pytest-Asyncio
- Взаимодействие с бд с через асинхронную SQLAlchemy 2.0
- База данных: PostgreSQL + асинхронный движок asyncpg

Написано API для взаимодействия с резюме пользователей, регистрация и входа

![Image alt](https://github.com/TetherOne/head_hunter/raw/master/photoes_for_github/img_2.png)
![Image alt](https://github.com/TetherOne/head_hunter/raw/master/photoes_for_github/img_1.png)

Планируется добавить
- Кеширование через Redis
- Очереди задач celery[redis]
