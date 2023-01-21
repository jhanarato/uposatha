from typing import List

from uposatha.elements import Season
from uposatha.configure import Configuration


def get_seasons(config: Configuration) -> List[Season]:
    return [create_season(config)]

def create_season(config: Configuration) -> Season:
    return Season()
