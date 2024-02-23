FROM python:3.11.4-slim

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN alembic upgrade head

CMD gunicorn main:app --workers 1 --    worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000