from datetime import date

import pytest

from uposatha.elements import HolidayName

def test_pavarana_day_name(rainy_season):
    assert rainy_season.holidays[0].name == HolidayName.PAVARANA

def test_pavarana_day_date(rainy_season):
    assert rainy_season.holidays[0].uposatha.falls_on == date(2010, 10, 23)

def test_magha_puja(cold_season):
    pass