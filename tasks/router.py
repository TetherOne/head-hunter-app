from fastapi import BackgroundTasks
from fastapi import APIRouter

from tasks.tasks import send_email



email_router = APIRouter(prefix="/report")



@email_router.get("/email")
def get_dashboard_report(background_tasks: BackgroundTasks):
    send_email.apply_async(['pashajobber@gmail.com'], countdown=10)
    return {
        "status": 200,
        "data": "Письмо будет отправлено через 10 секунд",
        "details": None
    }