import time
from contextlib import asynccontextmanager
from fastapi import Request, FastAPI

from core.config import get_settings
from core.logger import logger
from db.seeding import seed_db

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    if get_settings().seeding_enabled:
        logger.info("Seeding enabled: Seeding the DB.")
        await seed_db()




@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000

    logger.info(
        f"Method: {request.method} Path: {request.url.path} "
        f"Status: {response.status_code} Duration: {process_time:.2f}ms"
    )

    return response


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "time": time.time(),
    }
