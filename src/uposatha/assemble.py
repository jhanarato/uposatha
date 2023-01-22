from typing import List, Tuple
from datetime import date, timedelta
from itertools import accumulate

from uposatha.configure import Configuration
from uposatha.elements import Season, SeasonName, Uposatha, OfTheDay
from uposatha.sequence import SequenceSelector

def get_seasons(config: Configuration) -> List[Season]:
    return [create_season(config, config.start_date, SeasonName.COLD)]

def create_season(config: Configuration, day_before: date, season_name: SeasonName) -> Season:
    selector = SequenceSelector(config.extra_month_years, config.extra_day_years)
    uposathas = uposathas_in_season(selector, day_before, season_name)
    first_day = day_before + timedelta(1)
    last_day = uposathas[-1].falls_on

    return Season(
        name=season_name,
        first_day=first_day,
        last_day=last_day,
        uposathas=uposathas
    )

def uposathas_in_season(selector: SequenceSelector,
                        day_before: date,
                        season_name: SeasonName) -> Tuple[Uposatha, ...]:
    sequence = selector.uposathas(season_name, day_before.year)

    uposathas = []
    delta = timedelta(0)
    for position, days in enumerate(sequence):
        if days == 14:
            of_the_day = OfTheDay.FOURTEEN
        else:
            of_the_day = OfTheDay.FIFTEEN

        delta += timedelta(days)

        uposathas.append(
            Uposatha(
                falls_on=day_before + delta,
                number_in_season=position + 1,
                of_the_day=of_the_day
            )
        )
    return tuple(uposathas)
