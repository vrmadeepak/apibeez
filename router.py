from fastapi import APIRouter

from src.common.router import common_router
from src.user.router import user_router

router = APIRouter()

router.include_router(common_router, prefix="", tags=["common"])
router.include_router(user_router, prefix="/user", tags=["user"])