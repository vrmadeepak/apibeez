from fastapi import FastAPI

from router import router
from fastapi_versioning import VersionedFastAPI, version

from src.database.service import engine


app = FastAPI(
    title="CardReferral",
    terms_of_service="https://",
    contact=dict(name="Deepak Verma", url="https://", email="dpkvrm999@gmail.com"),
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
    version="0.0.1",
    # middleware=[
    #     Middleware(SessionMiddleware, secret_key='mysecretkey')
    # ]
)
