from enum import Enum, auto

class SeasonName(Enum):
    COLD = "Cold"
    HOT = "Hot"
    RAINY = "Rainy"

class SeasonType(Enum):
    NORMAL = "Normal"
    EXTRA_MONTH = "Extra Month"
    EXTRA_DAY = "Extra Day"
