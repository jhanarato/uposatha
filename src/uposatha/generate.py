from typing import List, Tuple, Generator
from datetime import date, timedelta
from itertools import cycle, dropwhile, accumulate, islice
from dataclasses import dataclass

from uposatha.configure import Configuration
from uposatha.elements import YearType, SeasonType
from uposatha.elements import Season, SeasonName, Uposatha, MoonPhase, HalfMoon, Holiday, HolidayName
from uposatha.elements import days_between_uposathas, days_between_half_moons


def generate_seasons(config: Configuration) -> List[Season]:
    names = season_names(config.start_season)
    season = generate_season(config.extra_month_years, config.extra_day_years, config.start_date, next(names))

    seasons = [season]

    while not is_last_season(config, season):
        season = generate_season(config.extra_month_years, config.extra_day_years, season.last_day, next(names))
        seasons.append(season)

    return seasons

def generate_season(extra_month_years: List[int],
                    extra_day_years: List[int],
                    day_before: date,
                    season_name: SeasonName) -> Season:
    begins_in_year_type = year_type_of_date(extra_month_years, extra_day_years, day_before)
    season_type = get_season_type(season_name, begins_in_year_type)

    uposatha_sequence = days_between_uposathas[season_type]
    half_moon_sequence = days_between_half_moons[season_type]

    uposathas = generate_uposathas(uposatha_sequence, day_before)
    half_moons = generate_half_moons(half_moon_sequence, day_before)

    last_day_in_season = uposathas[-1].falls_on

    # Magha Puja uposatha depends on whether the next hot season has an extra month.
    # Since we haven't generated the next month yet we'll need to know what sort of
    # year the cold season ends in.
    ends_in_year_type = year_type_of_date(extra_month_years, extra_day_years, last_day_in_season)
    holidays = generate_holidays(season_name, ends_in_year_type, uposathas)

    return Season(
        name=season_name,
        type=season_type,
        first_day=day_before + timedelta(1),
        last_day=last_day_in_season,
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
                      ends_in_year_type: YearType,
                      uposathas: Tuple[Uposatha, ...]) -> Tuple[Holiday]:
    match (season_name, ends_in_year_type):
        case (SeasonName.RAINY, _):
            holidays = (
                Holiday(name=HolidayName.PAVARANA, uposatha=uposathas[5]),
            )
        case (SeasonName.COLD, YearType.NORMAL) | (SeasonName.COLD, YearType.EXTRA_DAY):
            holidays = (
                Holiday(name=HolidayName.MAGHA, uposatha=uposathas[5]),
            )
        case (SeasonName.COLD, YearType.EXTRA_MONTH):
            holidays = (
                Holiday(name=HolidayName.MAGHA, uposatha=uposathas[7]),
            )
        case (SeasonName.HOT, YearType.NORMAL) | (SeasonName.HOT, YearType.EXTRA_DAY):
            holidays = (
                Holiday(name=HolidayName.VESAK, uposatha=uposathas[3]),
                Holiday(name=HolidayName.ASALHA, uposatha=uposathas[7])
            )
        case (SeasonName.HOT, YearType.EXTRA_MONTH):
            holidays = (
                Holiday(name=HolidayName.VESAK, uposatha=uposathas[5]),
                Holiday(name=HolidayName.ASALHA, uposatha=uposathas[9])
            )
        case _:
            holidays = ()
    return holidays

def is_last_season(config: Configuration, season: Season) -> bool:
    is_end_year = config.end_year == season.last_day.year
    is_end_season = config.end_season == season.name
    return is_end_season and is_end_year

def get_season_type(season_name: SeasonName, year_type: YearType) -> SeasonType:
    match (season_name, year_type):
        case (SeasonName.HOT, YearType.EXTRA_MONTH):
            season_type = SeasonType.EXTRA_MONTH
        case (SeasonName.HOT, YearType.EXTRA_DAY):
            season_type = SeasonType.EXTRA_DAY
        case _:
            season_type = SeasonType.NORMAL
    return season_type

def year_type_of_date(extra_month_years: List[int],
                      extra_day_years: List[int],
                      date_: date) -> YearType:
    if date_.year in extra_month_years:
        return YearType.EXTRA_MONTH
    if date_.year in extra_day_years:
        return YearType.EXTRA_DAY
    return YearType.NORMAL

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