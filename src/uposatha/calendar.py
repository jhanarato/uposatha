from uposatha.configure import get_default_configuration
from uposatha.generate import get_seasons

class Calendar:
    def __init__(self):
        self.config = get_default_configuration()
        self.seasons = get_seasons(self.config)