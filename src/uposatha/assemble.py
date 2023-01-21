from typing import List, Tuple
from datetime import date, timedelta
from uposatha.configure import Configuration
from uposatha.elements import Season, SeasonName, Uposatha
from uposatha.sequence import SequenceSelector

def get_seasons(config: Configuration) -> List[Season]:
    return [create_season(config, config.start_date, SeasonName.COLD)]

def create_season(config: Configuration, day_before: date, season_name: SeasonName) -> Season:
    selector = SequenceSelector(config.extra_month_years, config.extra_day_years)
    return Season(
        uposathas=uposathas_in_season(selector, day_before, season_name)
    )

def uposathas_in_season(selector: SequenceSelector,
                        day_before: date,
                        season_name: SeasonName) -> Tuple[Uposatha, ...]:
    sequence = selector.uposathas(season_name, day_before.year)
    deltas = [timedelta(days) for days in sequence]

    uposathas = create_uposatha(day_before, deltas)

    return tuple(uposathas)


def create_uposatha(day_before, deltas):
    uposathas = []
    next_date = day_before
    for delta in deltas:
        next_date = next_date + delta

        uposathas.append(
            Uposatha(
                falls_on=next_date
            )
        )
    return uposathas

