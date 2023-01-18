from typing import List
from uposatha.elements import SeasonName, SeasonType

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
        if self._is_extra_month(season_name, begins_in_year):
            return extra_month_uposatha_sequence

        if self._is_extra_day(season_name, begins_in_year):
            return extra_day_uposatha_sequence

        return normal_uposatha_sequence

    def half_moons(self, season_name: SeasonName, begins_in_year: int) -> List[int]:
        if self._is_extra_month(season_name, begins_in_year):
            return extra_month_half_moon_sequence

        if self._is_extra_day(season_name, begins_in_year):
            return extra_day_half_moon_sequence

        return normal_half_moon_sequence

    def _is_extra_month(self, season_name: SeasonName, begins_in_year: int) -> bool:
        return season_name == SeasonName.HOT and begins_in_year in self._extra_month_years

    def _is_extra_day(self, season_name: SeasonName, begins_in_year: int) -> bool:
        return season_name == SeasonName.HOT and begins_in_year in self._extra_day_years
