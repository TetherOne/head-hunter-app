from email.mime.text import MIMEText

from email.header import Header

from dotenv import load_dotenv

from celery import Celery

import smtplib

import os



load_dotenv()



celery = Celery('tasks', broker='redis://redis_hh:6379')



@celery.task
def send_email(recipients_emails):

    login = 'hh-adm1nistrator@yandex.ru'
    password = os.getenv("PASSWORD_EMAIL")

    message = MIMEText('Привет', 'plain', 'utf-8')
    message['Subject'] = Header(f'Сообщение доставлено', 'utf-8')
    message['From'] = login
    message['To'] = ', '.join(recipients_emails)

    email = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)

    try:
        email.starttls()
        email.login(login, password)
        email.sendmail(message['From'], recipients_emails, message.as_string())

    except Exception as ex:
        print(ex)

    finally:
        email.quit()