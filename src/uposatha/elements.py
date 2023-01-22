from typing import Literal, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import date

class SeasonName(Enum):
    COLD = "Cold"
    HOT = "Hot"
    RAINY = "Rainy"

class SeasonType(Enum):
    NORMAL = "Normal"
    EXTRA_MONTH = "Extra Month"
    EXTRA_DAY = "Extra Day"

@dataclass(frozen=True)
class Uposatha:
    falls_on: date
    number_in_season: int
    days_since_previous: int

@dataclass(frozen=True)
class Season:
    name: SeasonName
    uposathas: Tuple[Uposatha, ...]
    first_day: date
    last_day: date
