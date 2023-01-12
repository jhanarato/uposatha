from uposatha.assemble import UposathaSequence

def test_uposatha_sequence():
    seq = UposathaSequence()
    assert seq.days == [15, 15, 14, 15, 15, 15, 14, 15]

def test_add_month():
    seq = UposathaSequence()
    seq.add_month = True
    assert seq.days == [15, 15, 14, 15, 15, 15, 14, 15, 15, 15]

def test_add_day():
    seq = UposathaSequence()
    seq.add_day = True
    assert seq.days == [15, 15, 14, 15, 15, 15, 15, 15]
