from uposatha.assemble import UposathaSequence

def test_uposatha_sequence():
    seq = UposathaSequence()
    assert seq.days == [15, 15, 14, 15, 15, 15, 14, 15]
