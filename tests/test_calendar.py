from uposatha.calendar import Calendar

def test_calendar_has_config():
    calendar = Calendar()
    assert calendar.config.end_year == 2030

def test_calendar_has_seasons():
    calendar = Calendar()
    assert calendar.seasons