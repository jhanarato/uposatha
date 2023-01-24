import pytest

from uposatha.elements import HolidayName

def test_pavarana_day(rainy_season):
    assert rainy_season.holidays[0].name == HolidayName.PAVARANA
