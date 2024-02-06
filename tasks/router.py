from fastapi import APIRouter, BackgroundTasks

from tasks.tasks import sum_task

sum_router = APIRouter(prefix="/report")

@sum_router.get("/sum")
def get_dashboard_report(background_tasks: BackgroundTasks):
    sum_task(1, 7)
    background_tasks.add_task(sum_task, 1, 7)
    sum_task.delay(1, 7)
    return {
        "status": 200,
        "data": "Сумма получена",
        "details": None
    }