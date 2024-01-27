from .resume.views import router as resume_router

from fastapi import APIRouter



router = APIRouter()
router.include_router(router=resume_router)