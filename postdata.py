from pydantic import BaseModel
from typing import Optional


class LevelData(BaseModel):
    data: int
