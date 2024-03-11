from fastapi import FastAPI

from src.router import router
from fastapi_versioning import VersionedFastAPI, version

from src.config import settings
from src.database.service import engine


app = FastAPI(
    title=settings.PROJECT_NAME,
    terms_of_service="https://",
    contact=dict(name=settings.PROJECT_AUTHOR, url="https://", email="dpkvrm999@gmail.com"),
    # docs_url="/"
)


def buzzzzzz():
    # include router
    app.include_router(router)

    return app


app = VersionedFastAPI(
    buzzzzzz(),
    version_format="{major}",
    prefix_format="/api/v{major}",
    description="hello there",
    version=settings.PROJECT_VERSION,
    # middleware=[
    #     Middleware(SessionMiddleware, secret_key='mysecretkey')
    # ]
)
