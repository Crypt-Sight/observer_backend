from fastapi import Depends, FastAPI, status

from app.config import config
from app.dependencies import bearer_auth

if config.mode == "DEV":
    app = FastAPI(title="Observer Backend")
else:
    app = FastAPI(title="Observer Backend", docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/debug/healthcheck", tags=["Debug"], status_code=status.HTTP_200_OK)
async def healthcheck():
    return {"status": "OK"}


@app.get("/debug/auth", dependencies=[Depends(bearer_auth)], tags=["Auth"], status_code=status.HTTP_200_OK)
async def auth():
    return
