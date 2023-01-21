from datetime import date

import pytest

from uposatha.configure import get_default_configuration
from uposatha.assemble import create_season

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
