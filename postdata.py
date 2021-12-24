from pydantic import BaseModel
from typing import Optional


class LevelData(BaseModel):
    canlevelup: bool
    level: int
    levelup: int
    mainstat: str
    mainstat_value: float
    substats: list
    substats_count: int
    type: str

