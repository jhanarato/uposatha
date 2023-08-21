from datetime import date

import pytest

from uposatha.elements import HolidayName, Uposatha, MoonPhase, Holiday
from uposatha.elements import add_to_lookup, lookup_holiday, clear_lookup


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
