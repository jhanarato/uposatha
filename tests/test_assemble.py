from datetime import date

import pytest

from uposatha.elements import SeasonName, MoonPhase
from uposatha.configure import get_default_configuration
from uposatha.assemble import create_season, season_names


@pytest.fixture
def first_season():
    config = get_default_configuration()
    return create_season(config, config.start_date, config.start_season)

def test_add_uposathas_to_season(first_season):
    assert len(first_season.uposathas) == 10

def test_first_uposatha_date(first_season):
    assert first_season.uposathas[0].falls_on == date(2010, 3, 15)

def test_last_uposatha_date(first_season):
    assert first_season.uposathas[-1].falls_on == date(2010, 7, 26)

def test_uposatha_number_in_season(first_season):
    assert first_season.uposathas[0].number_in_season == 1
    assert first_season.uposathas[-1].number_in_season == 10

def test_fourteen_day(first_season):
    assert first_season.uposathas[2].days_since_previous == 14

def test_fifteen_day(first_season):
    assert first_season.uposathas[0].days_since_previous == 15

def test_season_name(first_season):
    assert first_season.name == SeasonName.HOT

def test_first_day_of_season(first_season):
    assert first_season.first_day == date(2010, 3, 1)

def test_last_day_of_season(first_season):
    assert first_season.last_day == date(2010, 7, 26)

def test_uposatha_moon_phase(first_season):
    expected = [MoonPhase.NEW, MoonPhase.FULL] * 5
    actual = [uposatha.moon_phase for uposatha in first_season.uposathas]
    assert actual == expected

def test_first_half_moon_date(first_season):
    assert first_season.half_moons[0].falls_on == date(2010, 3, 8)

def test_last_half_moon_date(first_season):
    assert first_season.half_moons[-1].falls_on == date(2010, 7, 19)

def test_half_moon_phase(first_season):
    expected = [MoonPhase.WANING, MoonPhase.WAXING] * 5
    actual = [half_moon.moon_phase for half_moon in first_season.half_moons]
    assert actual == expected

@pytest.mark.parametrize(
    "start_name,next_name",
    [
        (SeasonName.RAINY, SeasonName.COLD),
        (SeasonName.COLD, SeasonName.HOT),
        (SeasonName.HOT, SeasonName.RAINY)
    ]
)
def test_season_name_generator(start_name, next_name):
    name_generator = season_names(start_name)
    assert next(name_generator) == start_name
    assert next(name_generator) == next_name