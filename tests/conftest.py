import pytest

@pytest.fixture
def normal_sequence():
    return [15, 15, 14, 15, 15, 15, 14, 15]

@pytest.fixture
def long_hot_season_sequence():
    return [15, 15, 14, 15, 15, 15, 14, 15, 15, 15]

@pytest.fixture
def extra_day_sequence():
    return [15, 15, 14, 15, 15, 15, 15, 15]
