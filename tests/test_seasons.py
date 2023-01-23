from datetime import date

import pytest

from uposatha.configure import Configuration
from uposatha.assemble import get_seasons, is_last_season
from uposatha.elements import Season, SeasonName


def test_three_seasons(three_seasons):
    assert len(three_seasons) == 3


@pytest.fixture
def three_seasons():
    # Rainy  2011-07-16 2011-11-10
    # Cold   2011-11-11 2012-03-07
    # Hot    2012-03-08 2012-08-02

    config = Configuration(
        start_date=date(2011, 7, 15),
        start_season=SeasonName.RAINY,
        end_season=SeasonName.HOT,
        end_year=2012,
        extra_month_years=[2010, 2012, 2015, 2018, 2021, 2023, 2026, 2029],
        extra_day_years=[2016, 2020, 2025, 2030]
    )
    return get_seasons(config)

@pytest.mark.parametrize(
    "index,first_day",
    [
        (0, date(2011, 7, 16)),
        (1, date(2011, 11, 11)),
        (2, date(2012, 3, 8))
    ]
)
def test_three_seasons_first_day(three_seasons, index, first_day):
    assert three_seasons[index].first_day == first_day


@pytest.mark.parametrize(
    "index,last_day",
    [
        (0, date(2011, 11, 10)),
        (1, date(2012, 3, 7)),
        (2, date(2012, 8, 2))
    ]
)
def test_three_seasons_last_day(three_seasons, index, last_day):
    assert three_seasons[index].last_day == last_day


@pytest.mark.parametrize(
    "index,season_name",
    [
        (0, SeasonName.RAINY),
        (1, SeasonName.COLD),
        (2, SeasonName.HOT)
    ]
)
def test_three_seasons_name(three_seasons, index, season_name):
    assert three_seasons[index].name == season_name

def test_is_last_season():
    config = Configuration(
        start_date=date(1977, 1, 1),
        start_season=SeasonName.RAINY,
        end_season=SeasonName.HOT,
        end_year=2012,
        extra_month_years=[],
        extra_day_years=[]
    )

    season = Season(
        name=SeasonName.HOT,
        first_day=date(2012, 3, 1),
        last_day=date(2012, 7, 1),
        uposathas=(),
        half_moons=()
    )

    assert is_last_season(config, season)
