import time
from contextlib import asynccontextmanager
from fastapi import Request, FastAPI

from core.config import get_settings
from core.logger import logger
from db.database import initialize_db
from db.seeding import seed_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_db()

    if get_settings().seeding_enabled:
        logger.info("Seeding enabled: Seeding the DB.")
        await seed_db()
    else:
        logger.info("Seeding disabled: skipping initial seeding.")

    yield

    logger.info("Application shutting down...")


settings = get_settings()

app = FastAPI(
    lifespan=lifespan,
    title=settings.app_name,
)


# app.include_router(router)

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
