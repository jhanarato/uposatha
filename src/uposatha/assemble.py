class UposathaSequence:
    def __init__(self):
        self.add_month = False
        self.add_day = False
        self.positions = 8
        self.fourteen_days = [3, 7]
        self.extra_day_position = 6

    def _duration_at_position(self, position):
        if position in self.fourteen_days:
            return 14
        else:
            return 15

    @property
    def days(self):
        if self.add_month:
            self.positions += 2

        if self.add_day:
            self.fourteen_days.remove(7)

        positions = range(1, self.positions + 1)
        return [self._duration_at_position(position) for position in positions]
