from fastapi import APIRouter

from starlette import status
from starlette.responses import JSONResponse

from fastapi_versioning import version

common_router = APIRouter()


@common_router.get("/health")
@version(1)
def health():
    return JSONResponse(
        content={"message": "APIBeez are buzzing...."}, status_code=status.HTTP_200_OK
    )
