from fastapi import APIRouter

from .resume.views import router as resume_router



router = APIRouter()
router.include_router(router=resume_router)