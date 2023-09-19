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


def test_current_season_out_of_bounds():
    calendar = Calendar()
    with pytest.raises(ValueError):
        calendar.current_season(date(2030, 11, 11))