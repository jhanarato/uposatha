from typing import List, Tuple, Generator
from datetime import date, timedelta
from itertools import cycle, dropwhile, accumulate, islice
from dataclasses import dataclass

from uposatha.configure import Configuration
from uposatha.elements import Season, SeasonName, Uposatha, MoonPhase, HalfMoon, Holiday, HolidayName, SeasonType
from uposatha.elements import days_between_uposathas, days_between_half_moons


def get_seasons(config: Configuration) -> List[Season]:
    names = season_names(config.start_season)
    season = create_season(config, config.start_date, next(names))

    seasons = [season]

    while not is_last_season(config, season):
        season = create_season(config, season.last_day, next(names))
        seasons.append(season)

    return seasons

def create_season(config: Configuration, day_before: date, season_name: SeasonName) -> Season:
    season_type = get_season_type(config.extra_month_years, config.extra_day_years, season_name, day_before.year)

    uposatha_sequence = days_between_uposathas[season_type]
    half_moon_sequence = days_between_half_moons[season_type]

    uposathas = uposathas_in_season(uposatha_sequence, day_before)
    half_moons = half_moons_in_season(half_moon_sequence, day_before)
    holidays = holidays_in_season(season_name, season_type, uposathas)

    return Season(
        name=season_name,
        type=season_type,
        first_day=day_before + timedelta(1),
        last_day=uposathas[-1].falls_on,
        uposathas=uposathas,
        half_moons=half_moons,
        holidays=holidays
    )

def date_sequence(sequence: Tuple[int, ...], day_before: date) -> Tuple[date, ...]:
    return tuple(day_before + timedelta(days) for days in accumulate(sequence))

def position_sequence(length: int):
    return tuple(range(1, length + 1))

def phase_sequence(length: int, phases: List[MoonPhase]) -> Tuple[MoonPhase]:
    p = phases
    p = cycle(p)
    p = islice(p, length)
    return tuple(p)

def uposathas_in_season(sequence: Tuple[int, ...], day_before: date) -> Tuple[Uposatha, ...]:
    dates = iter(date_sequence(sequence, day_before))
    position = iter(position_sequence(len(sequence)))
    days_since_previous = iter(sequence)
    phases = iter(phase_sequence(len(sequence), [MoonPhase.NEW, MoonPhase.FULL]))

    uposathas = []

    for days in sequence:
        uposathas.append(
            Uposatha(
                falls_on=next(dates),
                number_in_season=next(position),
                days_since_previous=next(days_since_previous),
                moon_phase=next(phases)
            )
        )
    return tuple(uposathas)

def half_moons_in_season(sequence: Tuple[int, ...], day_before: date) -> Tuple[HalfMoon, ...]:
    phases = cycle([MoonPhase.WANING, MoonPhase.WAXING])
    delta = timedelta(0)
    half_moons = []

    for position, days in enumerate(sequence):
        delta += timedelta(days)

        half_moons.append(
            HalfMoon(
                falls_on=day_before + delta,
                moon_phase=next(phases)
            )
        )

    return tuple(half_moons)

@dataclass(frozen=True)
class HolidayLocation:
    name: HolidayName
    season: SeasonName
    normal_position: int
    extra_month_position: int

def holidays_in_season(season_name: SeasonName,
                       season_type: SeasonType,
                       uposathas: Tuple[Uposatha, ...]) -> Tuple[Holiday]:
    pavarana = HolidayLocation(
        name=HolidayName.PAVARANA,
        season=SeasonName.RAINY,
        normal_position=6,
        extra_month_position=6
    )

    return Holiday(name=HolidayName.PAVARANA),

def season_names(start_name: SeasonName) -> Generator[SeasonName, None, None]:
    names_in_order = [SeasonName.RAINY, SeasonName.COLD, SeasonName.HOT]
    names_looped = cycle(names_in_order)
    skipped_to_start = dropwhile(lambda name: name != start_name, names_looped)

    while True:
        yield next(skipped_to_start)

def is_last_season(config: Configuration, season: Season) -> bool:
    is_end_year = config.end_year == season.last_day.year
    is_end_season = config.end_season == season.name
    return is_end_season and is_end_year

def get_season_type(extra_month_years: List[int], extra_day_years: List[int],
                    season_name: SeasonName, begins_in_year: int) -> SeasonType:
    if season_name == SeasonName.HOT:
        if begins_in_year in extra_month_years:
            return SeasonType.EXTRA_MONTH
        if begins_in_year in extra_day_years:
            return SeasonType.EXTRA_DAY
    return SeasonType.NORMAL
