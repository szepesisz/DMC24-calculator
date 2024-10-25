import logging
from typing import Self
from enum import StrEnum

from pydantic import BaseModel, model_validator

logger = logging.getLogger(__name__)


class Operation(StrEnum):
    add = 'add'
    subtract = 'sub'
    multiply = 'mul'
    divide = 'div'
    # root = 'sqrt'

class CalculateRequest(BaseModel):
    operation: Operation
    a: float
    b: float

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.operation == Operation.divide and self.b == 0:
            raise ValueError('Zero division')
        return self