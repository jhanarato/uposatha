from datetime import date

import pytest

from uposatha.calendar import Calendar
from uposatha.elements import HolidayName, Uposatha, MoonPhase, Holiday, Season, SeasonName, SeasonType
from uposatha.elements import add_to_lookup, lookup_holiday, clear_lookup
from uposatha.generate import uposatha_holidays


@pytest.fixture
def holiday_uposatha():
    return Uposatha(
        falls_on=date(2023, 8, 1),
        number_in_season=10,
        days_since_previous=15,
        moon_phase=MoonPhase.FULL)


@pytest.fixture
def holiday(holiday_uposatha):
    yield Holiday(
        name=HolidayName.ASALHA,
        uposatha=holiday_uposatha
    )


@pytest.fixture
def lookup_available(holiday_uposatha, holiday):
    add_to_lookup(holiday_uposatha, holiday)
    yield
    clear_lookup()


def test_add_to_lookup(holiday_uposatha, holiday, lookup_available):
    assert lookup_holiday(holiday_uposatha) == holiday


def test_uposatha_retrieves_holiday(holiday_uposatha, holiday, lookup_available):
    assert holiday_uposatha.holiday == holiday


def test_uposatha_holiday_chain(holiday_uposatha, holiday, lookup_available):
    assert holiday_uposatha.holiday.uposatha == holiday_uposatha


def test_missing_holiday_is_none(holiday_uposatha, holiday):
    assert holiday_uposatha.holiday is None


def test_uposatha_holidays_in_season(holiday_uposatha, holiday):
    seasons = [Season(
        name=SeasonName.HOT,
        type=SeasonType.EXTRA_MONTH,
        first_day=date(2023, 3, 7),
        last_day=date(2023, 8, 1),
        half_moons=(),
        uposathas=(holiday_uposatha,),
        holidays=(holiday,)
    )]

    assert next(uposatha_holidays(seasons)) == (holiday_uposatha, holiday)


def test_calendar_populates_lookup():
    cal = Calendar()
    asalha_uposatha = cal.next_uposatha(date(2023, 8, 1))
    assert asalha_uposatha.holiday.name == HolidayName.ASALHA

