from datetime import date

from uposatha.calendar import Calendar
from uposatha.elements import HolidayName


def test_get_holiday_from_uposatha():
    asalha_puja = date(2023, 8, 1)
    calendar = Calendar()
    uposatha = calendar.next_uposatha(asalha_puja)
    holiday = uposatha.holiday

    assert holiday.uposatha.falls_on == date(2023, 8, 1)
    assert holiday.name == HolidayName.ASALHA
