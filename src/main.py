from fastapi import FastAPI

from router import router
from fastapi_versioning import VersionedFastAPI, version

from src.database.service import engine
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def buzzzzzz():
    # include router
    app.include_router(router)

    return app


app = VersionedFastAPI(
    buzzzzzz(),
    version_format="{major}",
    prefix_format="/api/v{major}",
    description="Greet users with a nice message",
    # middleware=[
    #     Middleware(SessionMiddleware, secret_key='mysecretkey')
    # ]
)
