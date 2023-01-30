from datetime import date

import pytest

from uposatha.elements import SeasonName
from uposatha.generate import generate_season
from uposatha.configure import get_default_configuration
from uposatha.calendar import Calendar

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
    calendar = Calendar()
    return calendar.seasons[0]

@pytest.fixture
def rainy_season():
    calendar = Calendar()
    return calendar.seasons[1]

@pytest.fixture
def cold_season():
    calendar = Calendar()
    return calendar.seasons[2]

@pytest.fixture
def cold_before_extra_month_season():
    calendar = Calendar()
    return calendar.seasons[5]
