from datetime import date

from uposatha.calendar import Calendar
from uposatha.elements import HolidayName, Uposatha, MoonPhase, Holiday
from uposatha.elements import add_to_lookup, lookup_holiday


def test_get_holiday_from_uposatha():
    asalha_puja = date(2023, 8, 1)
    calendar = Calendar()
    uposatha = calendar.next_uposatha(asalha_puja)
    holiday = uposatha.holiday

    assert holiday.uposatha.falls_on == date(2023, 8, 1)
    assert holiday.name == HolidayName.ASALHA


def test_add_to_lookup():
    uposatha = Uposatha(
        falls_on=date(2023, 8, 1),
        number_in_season=10,
        days_since_previous=15,
        moon_phase=MoonPhase.FULL)

    holiday = Holiday(
        name=HolidayName.ASALHA,
        uposatha=uposatha
    )

    add_to_lookup(uposatha, holiday)

    assert lookup_holiday(uposatha) == holiday
