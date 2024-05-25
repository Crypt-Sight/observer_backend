from fastapi import FastAPI, status
from app.config import config

if config.mode == "DEV":
    app = FastAPI(title="Observer Backend")
else:
    app = FastAPI(
        title="Observer Backend",
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )


@app.get("/debug/healthcheck", tags=["Debug"], status_code=status.HTTP_200_OK)
async def healthcheck():
    return {"status": "OK"}
