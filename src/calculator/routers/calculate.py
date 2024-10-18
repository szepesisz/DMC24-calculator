import logging

from fastapi import APIRouter

from calculator.models.calculate_request import (
    CalculateRequest
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=['Calculate'])


@router.post(path='/calculate')
def calculate(
    r: CalculateRequest
):
    logger.info('%s', r)

    match r.operation:
        case 'add':
            resp = r.a + r.b
        case _:
            resp = None

    return resp