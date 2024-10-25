import logging

from fastapi import APIRouter

from calculator.models.calculate_request import (
    CalculateRequest,
    Operation
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=['Calculate'])


def do_operation(a, b, op):
    match op:
        case Operation.add:
            c = a + b
        case Operation.subtract:
            c = a - b
        case Operation.multiply:
            c = a * b
        case Operation.divide:
            c = a / b
        case _:
            raise ValueError
    return c

@router.post(path='/calculate')
def calculate(
    r: CalculateRequest
):
    logger.info('%s', r)

    return do_operation(r.a, r.b, r.operation)
