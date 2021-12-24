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


"""
{
    "canlevelup": true,
    "type": "Goblet of Eonothem",
    "mainstat": "Hydro DMG Bonus%",
    "mainstat_value": 7,
    "substats": [
        [
            "CRIT DMG%",
            6.99
        ],
        [
            "Elemental Mastery",
            23.31
        ],
        [
            "HP%",
            4.66
        ]
    ],
    "substats_count": 3,
    "level": 0,
    "levelup": 1
}
"""
