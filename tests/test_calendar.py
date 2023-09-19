from datetime import date

import pytest

from uposatha.calendar import Calendar


def test_calendar_has_config():
    calendar = Calendar()
    assert calendar.config.end_year == 2030


def test_calendar_has_seasons():
    calendar = Calendar()
    assert calendar.seasons


def test_end_date():
    calendar = Calendar()
    assert calendar.seasons[-1].last_day == date(2030, 11, 10)


@pytest.mark.parametrize(
    "out_of_bounds",
    [date(2030, 11, 11), date(2010, 2, 28)]
)
def test_current_season_out_of_bounds(out_of_bounds):
    calendar = Calendar()
    with pytest.raises(ValueError):
        calendar.current_season(out_of_bounds)


@pytest.mark.parametrize(
    "out_of_bounds",
    [date(2030, 11, 11), date(2010, 2, 28)]
)
def test_next_uposatha_out_of_bounds(out_of_bounds):
    calendar = Calendar()
    with pytest.raises(ValueError):
        calendar.next_uposatha(out_of_bounds)


@pytest.mark.parametrize(
    "valid_date,uposatha_falls_on",
    [
        (date(2023, 9, 19), date(2023, 9, 29)),
        (date(2023, 9, 28), date(2023, 9, 29)),
        (date(2023, 9, 29), date(2023, 9, 29)),
        (date(2023, 9, 30), date(2023, 10, 14)),
    ]
)
def test_valid_next_uposatha(valid_date, uposatha_falls_on):
    calendar = Calendar()
    assert calendar.next_uposatha(valid_date).falls_on == uposatha_falls_on
