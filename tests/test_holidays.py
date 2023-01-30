from datetime import date
from typing import List
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

def holiday_dates(holiday_name: HolidayName) -> List[date]:
    calendar = Calendar()
    holidays = []
    for season in calendar.seasons:
        holidays.extend(holiday for holiday in season.holidays if holiday.name == holiday_name)

    return [holiday.uposatha.falls_on for holiday in holidays]

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
    dates = holiday_dates(HolidayName.MAGHA)
    assert date.fromisoformat(holiday_date) in dates

@pytest.mark.parametrize(
    "holiday_date",
    [
        "2010-10-23", "2011-10-12", "2012-10-30", "2013-10-19", "2014-10-08", "2015-10-27",
        "2016-10-16", "2017-10-05", "2018-10-24", "2019-10-13", "2020-10-02", "2021-10-21",
        "2022-10-10", "2023-10-29", "2024-10-17", "2025-10-07", "2026-10-26", "2027-10-15",
        "2028-10-03", "2029-10-22", "2030-10-12"]
)
def test_all_pavarana_dates(holiday_date):
    dates = holiday_dates(HolidayName.PAVARANA)
    assert date.fromisoformat(holiday_date) in dates
