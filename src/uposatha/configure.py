# Configure the calendar model.
from dataclasses import dataclass
from enum import Enum, auto
import datetime
from typing import List

class SeasonNames(Enum):
    COLD = "Cold"
    HOT = "Hot"
    RAINY = "Rainy"

@dataclass(frozen=True)
class Configuration:
    start_date: datetime.date
    start_season: SeasonNames
    end_year: int
    end_season: SeasonNames
    hot_season_years: List[int]
    extra_day_years: List[int]

def get_default_configuration():
    return Configuration(
        start_date=datetime.date(2010, 2, 28),
        start_season=SeasonNames.HOT,
        end_season=SeasonNames.RAINY,
        end_year=2030,
        hot_season_years=[2010, 2012, 2015, 2018, 2021, 2023, 2026, 2029],
        extra_day_years=[2016, 2020, 2025, 2030]
    )
