# import time
#
# from celery import Celery
#
# celery = Celery('tasks', broker='redis://127.0.0.1:6379')
#
#
# @celery.task
# def sum_num(a, b):
#     time.sleep(5)
#     result = a + b
#     return result