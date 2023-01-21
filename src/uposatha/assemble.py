from typing import List, Tuple
from datetime import date, timedelta
from itertools import accumulate

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

    uposathas = []
    for position, days in enumerate(accumulate(sequence)):
        uposathas.append(
            Uposatha(
                falls_on=day_before + timedelta(days),
                number_in_season=position + 1
            )
        )
    return tuple(uposathas)
