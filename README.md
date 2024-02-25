# Описание проекта:


    При разработке проекта использовался фреймворк FastAPI,
    было написано Api для сайта по поиску кандидатов на работу
    (взаимодействия с резюме, пользователями (регистрация, аутентификация), 
    реализован полный CRUD).

![Image alt](https://github.com/TetherOne/head_hunter/raw/master/github_pages/img_3.png)


# Техническая информация:

  - Кэширование: Redis
  - Валидация: Pydantic
  - Тестирование: Pytest
  - Очереди задач: Celery[redis]
  - Создание миграций: Alembic
  - Взаимодействие с бд: асинхронная SQLAlchemy 2.0
  - База данных: PostgreSQL + асинхронный движок asyncpg

# Запуск проекта:

## 1. Клонируйте репозиторий:
```
git clone https://github.com/TetherOne/head-hunter
```
## 2. Соберите docker-compose:
```
docker compose build
```
## 3. Запустите docker-compose:
```
docker compose up
```



