import time
from celery import Celery



celery = Celery('tasks', broker='redis://127.0.0.1:6379')


@celery.task
def sum_task(x, y):
    time.sleep(5)
    return x + y