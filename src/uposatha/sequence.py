from typing import List
from uposatha.elements import SeasonName, SeasonType

days_between_uposathas = {
    SeasonType.NORMAL: [15, 15, 14, 15, 15, 15, 14, 15],
    SeasonType.EXTRA_MONTH: [15, 15, 14, 15, 15, 15, 14, 15, 15, 15],
    SeasonType.EXTRA_DAY: [15, 15, 14, 15, 15, 15, 15, 15]
}

days_between_half_moons = {
    SeasonType.NORMAL: [8, 15, 15, 14, 15, 15, 15, 14],
    SeasonType.EXTRA_MONTH: [8, 15, 15, 14, 15, 15, 15, 14, 15, 15],
    SeasonType.EXTRA_DAY: [8, 15, 15, 14, 15, 15, 15, 15]
}

normal_uposatha_sequence = [15, 15, 14, 15, 15, 15, 14, 15]
extra_month_uposatha_sequence = [15, 15, 14, 15, 15, 15, 14, 15, 15, 15]
extra_day_uposatha_sequence = [15, 15, 14, 15, 15, 15, 15, 15]

normal_half_moon_sequence = [8, 15, 15, 14, 15, 15, 15, 14]
extra_month_half_moon_sequence = [8, 15, 15, 14, 15, 15, 15, 14, 15, 15]
extra_day_half_moon_sequence = [8, 15, 15, 14, 15, 15, 15, 15]

class SequenceSelector:
    def __init__(self, extra_month_years: List[int], extra_day_years: List[int]) -> None:
        self._extra_month_years = extra_month_years
        self._extra_day_years = extra_day_years

    def uposathas(self, season_name: SeasonName, begins_in_year: int) -> List[int]:
        season_type = self._season_type(season_name, begins_in_year)
        return days_between_uposathas[season_type]

    def half_moons(self, season_name: SeasonName, begins_in_year: int) -> List[int]:
        season_type = self._season_type(season_name, begins_in_year)
        return days_between_half_moons[season_type]

    def _season_type(self, season_name: SeasonName, begins_in_year: int) -> SeasonType:
        if season_name == SeasonName.HOT:
            if begins_in_year in self._extra_month_years:
                return SeasonType.EXTRA_MONTH
            if begins_in_year in self._extra_day_years:
                return SeasonType.EXTRA_DAY

        return SeasonType.NORMAL
