FROM python:3.11.4-slim


RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .





#RUN chmod a+x docker/*.sh

#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000


#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]