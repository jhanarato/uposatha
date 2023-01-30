from datetime import date

import pytest

from uposatha.elements import HolidayName, SeasonName

def test_pavarana_day_name(rainy_season):
    assert rainy_season.holidays[0].name == HolidayName.PAVARANA

def test_pavarana_day_date(rainy_season):
    assert rainy_season.holidays[0].uposatha.falls_on == date(2010, 10, 23)

def test_magha_puja_when_next_season_long_with_extra_month(cold_before_extra_month_season):
    holidays = cold_before_extra_month_season.holidays
    magha_pujas = [holiday for holiday in holidays if holiday.name == HolidayName.MAGHA_PUJA]
    assert len(magha_pujas) == 1
    assert magha_pujas[0].uposatha.number_in_season == 8
    assert magha_pujas[0].uposatha.falls_on == date(2012, 3, 7)