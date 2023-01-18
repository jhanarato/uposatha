import pytest

from uposatha.sequence import SequenceSelector
from uposatha.elements import SeasonNames

@pytest.fixture
def selector():
    return SequenceSelector(
        extra_month_years=[2010, 2012, 2015, 2018, 2021, 2023, 2026, 2029],
        extra_day_years=[2016, 2020, 2025, 2030]
    )

@pytest.mark.parametrize(
    "season_name,year",
    [
        (SeasonNames.COLD, 2011),
        (SeasonNames.RAINY, 2011),
        (SeasonNames.HOT, 2011)
    ]
)
def test_normal_year(selector, normal_uposatha_sequence, season_name, year):
    assert selector.uposathas(season_name, year) == normal_uposatha_sequence
