from typing import Tuple
from dataclasses import dataclass
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

class OfTheDay(Enum):
    FOURTEEN = 14,
    FIFTEEN = 15

@dataclass
class Uposatha:
    falls_on: date
    number_in_season: int
    of_the_day: OfTheDay

@dataclass
class Season:
    name: SeasonName
    uposathas: Tuple[Uposatha, ...]
