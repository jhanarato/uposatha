from datetime import date

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
