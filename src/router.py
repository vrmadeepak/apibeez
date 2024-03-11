from enum import Enum
from fastapi import APIRouter

from src.common.router import common_router
from src.user.router import user_router

router = APIRouter()

class Tags(Enum):
    common = "common"
    users = "users"


router.include_router(common_router, prefix="", tags=[Tags.common])
router.include_router(user_router, prefix="/users", tags=[Tags.users])