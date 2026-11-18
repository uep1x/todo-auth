from app.api.endpoints import auth, item
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(item.router, prefix="/item")
