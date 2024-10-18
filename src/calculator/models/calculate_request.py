import logging

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class CalculateRequest(BaseModel):
    operation: str
    a: float
    b: float