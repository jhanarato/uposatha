from datetime import date

import pytest

from uposatha.calendar import Calendar

@pytest.fixture
def calendar():
    return Calendar()

@pytest.mark.parametrize(
    "today,next_falls_on",
    [
        (date(2010, 3, 1), date(2010, 3, 15)),
        (date(2010, 3, 15), date(2010, 3, 15)),
    ]
)
def test_next_uposatha(calendar, today, next_falls_on):
    next_uposatha = calendar.next_uposatha(today=today)
    assert next_uposatha.falls_on == next_falls_on

@pytest.mark.parametrize(
    "today,first_day",
    [
        (date(2010, 3, 1), date(2010, 3, 1)),
        (date(2010, 7, 26), date(2010, 3, 1)),
    ]
)
def test_current_season(calendar, today, first_day):
    calendar = Calendar()
    assert calendar.current_season(today=today).first_day == first_day
