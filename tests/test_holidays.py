from datetime import date

import pytest

from uposatha.elements import HolidayName

def test_pavarana_day_name(rainy_season):
    assert rainy_season.holidays[0].name == HolidayName.PAVARANA

# def test_pavarana_day_date(rainy_season):
#     assert rainy_season.holidays[0].falls_on == date(2010, 10, 23)
