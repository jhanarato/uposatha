import pytest

@pytest.fixture
def normal_uposatha_sequence():
    return [15, 15, 14, 15, 15, 15, 14, 15]

@pytest.fixture
def extra_month_uposatha_sequence():
    return [15, 15, 14, 15, 15, 15, 14, 15, 15, 15]

@pytest.fixture
def extra_day_uposatha_sequence():
    return [15, 15, 14, 15, 15, 15, 15, 15]
