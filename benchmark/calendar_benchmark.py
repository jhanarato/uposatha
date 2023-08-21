from uposatha.calendar import Calendar


def test_initialise_calendar(benchmark):
    benchmark(Calendar)
