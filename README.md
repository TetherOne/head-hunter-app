Сайт находится в разработке, используется фреймворк FastAPI

- Валидация --> Pydantic
- Создание миграций --> Alembic
- Написаны тесты --> Pytest
- Контроль зависимостей --> Poetry
- Взаимодействие с бд с через асинхронную SQLAlchemy 2.0
- База данных: PostgreSQL + асинхронный движок asyncpg

Написано API для взаимодействия с резюме пользователей, регистрация и входа

![Image alt](https://github.com/TetherOne/head_hunter/raw/master/photoes_for_github/img_2.png)
![Image alt](https://github.com/TetherOne/head_hunter/raw/master/photoes_for_github/img_1.png)

Планируется добавить
- Кеширование через Redis
- Очереди задач celery[redis]
