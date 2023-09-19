import datetime
from typing import Generator, Tuple

from uposatha.configure import get_default_configuration
from uposatha.generate import generate_seasons, uposatha_holidays
from uposatha.elements import Season, Uposatha, add_to_lookup


class Calendar:
    def __init__(self):
        self.config = get_default_configuration()
        self.seasons = generate_seasons(self.config)
        self.start_date = self.seasons[0].first_day
        self.end_date = self.seasons[-1].last_day
        self._populate_holiday_lookup()

    def _populate_holiday_lookup(self) -> None:
        for up, hol in uposatha_holidays(self.seasons):
            add_to_lookup(up, hol)

    def current_season(self, today: datetime.date = datetime.date.today()) -> Season:
        current = None

        for season in self.seasons:
            if season.first_day <= today <= season.last_day:
                current = season

        if not current:
            raise ValueError("Nothing available for this date.")

        return current

    def next_uposatha(self, today: datetime.date = datetime.date.today()) -> Uposatha:
        next_uposatha = None
        season = self.current_season(today=today)
        future_uposathas = [uposatha for uposatha in season.uposathas
                            if uposatha.falls_on >= today]

        if future_uposathas:
            next_uposatha = future_uposathas[0]
        else:
            raise ValueError("Nothing available for this date.")

        return next_uposatha
