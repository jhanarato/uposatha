class UposathaSequence:
    def __init__(self):
        self.positions = range(1, 9)
        self.fourteen_days = [3, 7]

    def _duration_at_position(self, position):
        if position in self.fourteen_days:
            return 14
        else:
            return 15

    @property
    def days(self):
        return [self._duration_at_position(position) for position in self.positions]