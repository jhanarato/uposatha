from uposatha.sequence import UposathaSequence, get_sequence
from uposatha.configure import SeasonNames

def test_uposatha_sequence(normal_sequence):
    seq = UposathaSequence()
    assert seq.days == normal_sequence

def test_add_month(long_hot_season_sequence):
    seq = UposathaSequence()
    seq.add_month = True
    assert seq.days == long_hot_season_sequence

def test_add_day(extra_day_sequence):
    seq = UposathaSequence()
    seq.add_day = True
    assert seq.days == extra_day_sequence

def test_get_sequence(normal_sequence):
    normal_year = 2011
    season_name = SeasonNames.COLD
    long_years = [2010]
    extra_day_years = [2012]
    sequence = get_sequence(long_years, extra_day_years, normal_year, season_name)
    assert sequence == normal_sequence
