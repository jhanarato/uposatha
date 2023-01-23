from typing import List, Tuple, Generator
from datetime import date, timedelta
from itertools import cycle, dropwhile

from uposatha.configure import Configuration
from uposatha.elements import Season, SeasonName, Uposatha, MoonPhase, HalfMoon
from uposatha.sequence import SequenceSelector

def get_seasons(config: Configuration) -> List[Season]:
    first = create_season(config, config.start_date, SeasonName.RAINY)
    second = create_season(config, first.last_day, SeasonName.COLD)
    third = create_season(config, second.last_day, SeasonName.HOT)
    return [first, second, third]

def create_season(config: Configuration, day_before: date, season_name: SeasonName) -> Season:
    selector = SequenceSelector(config.extra_month_years, config.extra_day_years)
    uposathas = uposathas_in_season(selector, day_before, season_name)
    half_moons = half_moons_in_season(selector, day_before, season_name)
    first_day = day_before + timedelta(1)
    last_day = uposathas[-1].falls_on

    return Season(
        name=season_name,
        first_day=first_day,
        last_day=last_day,
        uposathas=uposathas,
        half_moons=half_moons
    )

def season_names(start_name: SeasonName) -> Generator[SeasonName, None, None]:
    names_in_order = [SeasonName.RAINY, SeasonName.COLD, SeasonName.HOT]
    names_looped = cycle(names_in_order)
    skipped_to_start = dropwhile(lambda name: name != start_name, names_looped)

    while True:
        yield next(skipped_to_start)

def uposathas_in_season(selector: SequenceSelector,
                        day_before: date,
                        season_name: SeasonName) -> Tuple[Uposatha, ...]:
    sequence = selector.uposathas(season_name, day_before.year)
    phases = cycle([MoonPhase.NEW, MoonPhase.FULL])
    delta = timedelta(0)
    uposathas = []

    for position, days in enumerate(sequence):
        delta += timedelta(days)

        uposathas.append(
            Uposatha(
                falls_on=day_before + delta,
                number_in_season=position + 1,
                days_since_previous=days,
                moon_phase=next(phases)
            )
        )
    return tuple(uposathas)

def half_moons_in_season(selector: SequenceSelector,
                         day_before: date,
                         season_name: SeasonName) -> Tuple[HalfMoon, ...]:
    sequence = selector.half_moons(season_name, day_before.year)
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
