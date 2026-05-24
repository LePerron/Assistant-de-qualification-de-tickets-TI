import time
from fastapi import Request, FastAPI

from core.logger import logger

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "time": time.time(),
    }


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
