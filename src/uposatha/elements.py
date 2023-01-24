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

class MoonPhase(Enum):
    WANING = "Waning"
    NEW = "New"
    WAXING = "Waxing"
    FULL = "Full"

class HolidayName(Enum):
    PAVARANA = "Pavarana Day"

@dataclass(frozen=True)
class Uposatha:
    falls_on: date
    number_in_season: int
    days_since_previous: int
    moon_phase: MoonPhase

@dataclass(frozen=True)
class HalfMoon:
    falls_on: date
    moon_phase: MoonPhase

@dataclass(frozen=True)
class Holiday:
    name: HolidayName
    # falls_on: date
    # uposatha: Uposatha

@dataclass(frozen=True)
class Season:
    name: SeasonName
    uposathas: Tuple[Uposatha, ...]
    half_moons: Tuple[HalfMoon, ...]
    holidays: Tuple[Holiday, ...]
    first_day: date
    last_day: date
