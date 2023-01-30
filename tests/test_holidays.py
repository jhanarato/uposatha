from datetime import date

import pytest

from uposatha.calendar import Calendar
from uposatha.elements import HolidayName, SeasonName

def test_pavarana_day_name(rainy_season):
    assert rainy_season.holidays[0].name == HolidayName.PAVARANA

def test_pavarana_day_date(rainy_season):
    assert rainy_season.holidays[0].uposatha.falls_on == date(2010, 10, 23)

def test_magha_puja_when_next_season_long_with_extra_month(cold_before_extra_month_season):
    holidays = cold_before_extra_month_season.holidays
    magha_pujas = [holiday for holiday in holidays if holiday.name == HolidayName.MAGHA]
    assert len(magha_pujas) == 1
    assert magha_pujas[0].uposatha.number_in_season == 8
    assert magha_pujas[0].uposatha.falls_on == date(2012, 3, 7)

@pytest.mark.parametrize(
    "holiday_date",
    [
        "2011-02-18", "2012-03-07", "2013-02-25", "2014-02-14", "2015-03-04", "2016-02-22",
        "2017-02-11", "2018-03-01", "2019-02-19", "2020-02-08", "2021-02-26", "2022-02-16",
        "2023-03-06", "2024-02-24", "2025-02-12", "2026-03-03", "2027-02-21", "2028-02-10",
        "2029-02-27", "2030-02-17"
    ]
)
def test_all_magha_puja_dates(holiday_date):
    calendar = Calendar()
    holidays = []
    for season in calendar.seasons:
        holidays.extend(holiday for holiday in season.holidays if holiday.name == HolidayName.MAGHA)

    holiday_dates = [holiday.uposatha.falls_on for holiday in holidays]
    assert date.fromisoformat(holiday_date) in holiday_dates
