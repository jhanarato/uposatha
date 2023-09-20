from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class SeasonName(Enum):
    COLD = "Cold"
    HOT = "Hot"
    RAINY = "Rainy"


class SeasonType(Enum):
    NORMAL = "Normal"
    EXTRA_MONTH = "Extra Month"
    EXTRA_DAY = "Extra Day"


class YearType(Enum):
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
    VESAK = "Vesak Day"
    MAGHA = "Magha Puja"
    ASALHA = "Asalha Puja"


@dataclass(frozen=True)
class Uposatha:
    falls_on: date
    number_in_season: int
    days_since_previous: int
    moon_phase: MoonPhase

    @property
    def holiday(self) -> "Holiday | None":
        return lookup_holiday(self)


@dataclass(frozen=True)
class HalfMoon:
    falls_on: date
    moon_phase: MoonPhase


@dataclass(frozen=True)
class Holiday:
    name: HolidayName
    uposatha: Uposatha


@dataclass(frozen=True)
class Season:
    name: SeasonName
    type: SeasonType
    uposathas: tuple[Uposatha, ...]
    half_moons: tuple[HalfMoon, ...]
    holidays: tuple[Holiday, ...]
    first_day: date
    last_day: date


_holiday_lookup: dict[Uposatha, Holiday] = dict()


def clear_lookup() -> None:
    _holiday_lookup.clear()


def add_to_lookup(uposatha: Uposatha, holiday: Holiday) -> None:
    _holiday_lookup[uposatha] = holiday


def lookup_holiday(uposatha: Uposatha) -> Optional[Holiday]:
    return _holiday_lookup.get(uposatha)


days_between_uposathas = {
    SeasonType.NORMAL: (15, 15, 14, 15, 15, 15, 14, 15),
    SeasonType.EXTRA_MONTH: (15, 15, 14, 15, 15, 15, 14, 15, 15, 15),
    SeasonType.EXTRA_DAY: (15, 15, 14, 15, 15, 15, 15, 15)
}

days_between_half_moons = {
    SeasonType.NORMAL: (8, 15, 15, 14, 15, 15, 15, 14),
    SeasonType.EXTRA_MONTH: (8, 15, 15, 14, 15, 15, 15, 14, 15, 15),
    SeasonType.EXTRA_DAY: (8, 15, 15, 14, 15, 15, 15, 15)
}
