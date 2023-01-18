from typing import List
from uposatha.elements import SeasonNames

normal_uposatha_sequence = [15, 15, 14, 15, 15, 15, 14, 15]
extra_month_uposatha_sequence = [15, 15, 14, 15, 15, 15, 14, 15, 15, 15]
extra_day_uposatha_sequence = [15, 15, 14, 15, 15, 15, 15, 15]

class SequenceSelector:
    def __init__(self, extra_month_years: List[int], extra_day_years: List[int]) -> None:
        self._extra_month_years = extra_month_years
        self._extra_day_years = extra_day_years

    def uposathas(self, season_name: SeasonNames, begins_in_year: int) -> List[int]:
        if self._is_extra_month(begins_in_year, season_name):
            return extra_month_uposatha_sequence

        if self._is_extra_day(begins_in_year, season_name):
            return extra_day_uposatha_sequence

        return normal_uposatha_sequence

    def _is_extra_month(self, begins_in_year, season_name):
        return season_name == SeasonNames.HOT and begins_in_year in self._extra_month_years

    def _is_extra_day(self, begins_in_year, season_name):
        return season_name == SeasonNames.HOT and begins_in_year in self._extra_day_years
