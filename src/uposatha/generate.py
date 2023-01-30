from typing import List, Tuple, Generator
from datetime import date, timedelta
from itertools import cycle, dropwhile, accumulate, islice
from dataclasses import dataclass

from uposatha.configure import Configuration
from uposatha.elements import Season, SeasonName, Uposatha, MoonPhase, HalfMoon, Holiday, HolidayName, SeasonType
from uposatha.elements import days_between_uposathas, days_between_half_moons


def generate_seasons(config: Configuration) -> List[Season]:
    names = season_names(config.start_season)
    season = generate_season(config, config.start_date, next(names))

    seasons = [season]

    while not is_last_season(config, season):
        season = generate_season(config, season.last_day, next(names))
        seasons.append(season)

    return seasons

def generate_season(config: Configuration, day_before: date, season_name: SeasonName) -> Season:
    season_type_ = season_type(config.extra_month_years, config.extra_day_years, season_name, day_before.year)
    uposatha_sequence = days_between_uposathas[season_type_]
    half_moon_sequence = days_between_half_moons[season_type_]

    uposathas = generate_uposathas(uposatha_sequence, day_before)
    half_moons = generate_half_moons(half_moon_sequence, day_before)
    holidays = generate_holidays(season_name, season_type_, uposathas)

    return Season(
        name=season_name,
        type=season_type_,
        first_day=day_before + timedelta(1),
        last_day=uposathas[-1].falls_on,
        uposathas=uposathas,
        half_moons=half_moons,
        holidays=holidays
    )

def generate_uposathas(sequence: Tuple[int, ...],
                       day_before: date) -> Tuple[Uposatha, ...]:
    return tuple(
        map(Uposatha,
            seq_to_date(sequence, day_before),
            seq_to_position(len(sequence)),
            sequence,
            phases(
                len(sequence),
                [MoonPhase.NEW, MoonPhase.FULL]
            )
        )
    )

def generate_half_moons(sequence: Tuple[int, ...],
                        day_before: date) -> Tuple[HalfMoon, ...]:
    return tuple(
        map(HalfMoon,
            seq_to_date(sequence, day_before),
            phases(
                len(sequence),
                [MoonPhase.WANING, MoonPhase.WAXING]
            )
        )
    )

def generate_holidays(season_name: SeasonName,
                      season_type_: SeasonType,
                      uposathas: Tuple[Uposatha, ...]) -> Tuple[Holiday]:
    holidays = []

    match (season_name, season_type_):
        case (SeasonName.RAINY, _):
            holidays.append(
                Holiday(name=HolidayName.PAVARANA,
                        uposatha=uposathas[5])
            )

    return tuple(holidays)

def is_last_season(config: Configuration, season: Season) -> bool:
    is_end_year = config.end_year == season.last_day.year
    is_end_season = config.end_season == season.name
    return is_end_season and is_end_year

def season_type(extra_month_years: List[int], extra_day_years: List[int],
                season_name: SeasonName, begins_in_year: int) -> SeasonType:
    if season_name == SeasonName.HOT:
        if begins_in_year in extra_month_years:
            return SeasonType.EXTRA_MONTH
        if begins_in_year in extra_day_years:
            return SeasonType.EXTRA_DAY
    return SeasonType.NORMAL

def season_names(start_name: SeasonName) -> Generator[SeasonName, None, None]:
    names_in_order = [SeasonName.RAINY, SeasonName.COLD, SeasonName.HOT]
    names_looped = cycle(names_in_order)
    skipped_to_start = dropwhile(lambda name: name != start_name, names_looped)

    while True:
        yield next(skipped_to_start)

def seq_to_date(sequence: Tuple[int, ...], day_before: date) -> Tuple[date, ...]:
    return tuple(day_before + timedelta(days) for days in accumulate(sequence))

def seq_to_position(length: int):
    return tuple(range(1, length + 1))

def phases(length: int, p: List[MoonPhase]) -> Tuple[MoonPhase]:
    p = cycle(p)
    p = islice(p, length)
    return tuple(p)