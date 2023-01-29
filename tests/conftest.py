from datetime import date

import pytest

from uposatha.elements import SeasonName
from uposatha.assemble import create_season
from uposatha.configure import get_default_configuration

@pytest.fixture
def normal_uposatha_sequence():
    return 15, 15, 14, 15, 15, 15, 14, 15

@pytest.fixture
def extra_month_uposatha_sequence():
    return 15, 15, 14, 15, 15, 15, 14, 15, 15, 15

@pytest.fixture
def extra_day_uposatha_sequence():
    return 15, 15, 14, 15, 15, 15, 15, 15

@pytest.fixture
def normal_half_moon_sequence():
    return 8, 15, 15, 14, 15, 15, 15, 14

@pytest.fixture
def extra_month_half_moon_sequence():
    return 8, 15, 15, 14, 15, 15, 15, 14, 15, 15

@pytest.fixture
def extra_day_half_moon_sequence():
    return 8, 15, 15, 14, 15, 15, 15, 15

@pytest.fixture
def long_hot_season():
    config = get_default_configuration()
    return create_season(config, date(2010, 2, 28), SeasonName.HOT)

@pytest.fixture
def rainy_season():
    config = get_default_configuration()
    return create_season(config, date(2010, 7, 26), SeasonName.RAINY)

@pytest.fixture
def cold_season():
    config = get_default_configuration()
    return create_season(config, date(2010, 11, 18), SeasonName.COLD)
