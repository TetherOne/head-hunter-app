[![Python 3.6](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/downloads/release/python-360/)
![Django 3.0](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)

# Описание проекта:


    При разработке проекта использовался фреймворк FastAPI,
    было написано Api для сайта по поиску кандидатов на работу
    (взаимодействия с резюме, пользователями (регистрация, аутентификация при
    помощи JWT токена), реализован полный CRUD). Написаны юнит тесты 
    с использованием библиотеки PyTest.

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
## 4. Перейдите в браузер по ссылке:
```
http://127.0.0.1:8000/docs
```


