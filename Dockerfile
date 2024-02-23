FROM python:3.11.4-slim

RUN mkdir /fastapi_app

RUN pip install poetry

WORKDIR /fastapi_app

COPY . .

RUN poetry install

RUN alembic upgrade head

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000