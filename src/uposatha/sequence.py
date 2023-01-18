from typing import List
from uposatha.elements import SeasonNames

class SequenceSelector:
    def __init__(self, extra_month_years: List[int], extra_day_years: List[int]) -> None:
        self._extra_month_years = extra_month_years
        self._extra_day_years = extra_day_years

    def uposathas(self, season_name: SeasonNames, begins_in_year: int) -> List[int]:
        return [15, 15, 14, 15, 15, 15, 14, 15]