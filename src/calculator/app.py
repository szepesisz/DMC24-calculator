import logging

from fastapi import FastAPI
import uvicorn

from calculator.routers.calculate import router as calc_router

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s: %(message)s'
    )
    logger.info('Starting Calculator')
    app = FastAPI(title='Calculator')

    app.include_router(calc_router)

    uvicorn.run(app, log_config=None)