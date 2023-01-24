from typing import List, Tuple
from uposatha.elements import SeasonName, SeasonType, days_between_uposathas, days_between_half_moons


class SequenceSelector:
    def __init__(self, extra_month_years: List[int], extra_day_years: List[int]) -> None:
        self._extra_month_years = extra_month_years
        self._extra_day_years = extra_day_years

    def uposathas(self, season_name: SeasonName, begins_in_year: int) -> Tuple[int, ...]:
        s_type = get_season_type(self._extra_month_years, self._extra_day_years, season_name, begins_in_year)
        return days_between_uposathas[s_type]

    def half_moons(self, season_name: SeasonName, begins_in_year: int) -> Tuple[int, ...]:
        s_type = get_season_type(self._extra_month_years, self._extra_day_years, season_name, begins_in_year)
        return days_between_half_moons[s_type]

def get_season_type(extra_month_years: List[int], extra_day_years: List[int],
                    season_name: SeasonName, begins_in_year: int) -> SeasonType:
    if season_name == SeasonName.HOT:
        if begins_in_year in extra_month_years:
            return SeasonType.EXTRA_MONTH
        if begins_in_year in extra_day_years:
            return SeasonType.EXTRA_DAY
    return SeasonType.NORMAL
