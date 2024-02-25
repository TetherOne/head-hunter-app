FROM python:3.11.4-slim

RUN mkdir /fastapi-app

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

<<<<<<< HEAD
=======
RUN alembic upgrade head

CMD gunicorn main:app --workers 3 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
>>>>>>> 5bb9238c3c58aec6f1d099b363fe222e058e3910
