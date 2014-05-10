Buddhist Moon Days
==================
This is a Python API for calculating the moon days for the Buddhist lunar
calendar during the rains retreat given the previous Uposatha day before the
rains.

Example output:

    $ python3 uposatha.py 2014/07/11
    +---------+------------+------------+
    |  Week   |   Start    |    End     |
    +---------+------------+------------+
    | Week  1 | 2014-07-12 | 2014-07-19 |
    | Week  2 | 2014-07-20 | 2014-07-26 |
    | Week  3 | 2014-07-27 | 2014-08-03 |
    | Week  4 | 2014-08-04 | 2014-08-10 |
    | Week  5 | 2014-08-11 | 2014-08-17 |
    | Week  6 | 2014-08-18 | 2014-08-24 |
    | Week  7 | 2014-08-25 | 2014-09-01 |
    | Week  8 | 2014-09-02 | 2014-09-08 |
    | Week  9 | 2014-09-09 | 2014-09-16 |
    | Week 10 | 2014-09-17 | 2014-09-23 |
    | Week 11 | 2014-09-24 | 2014-10-01 |
    | Week 12 | 2014-10-02 | 2014-10-08 |
    +---------+------------+------------+

Authors
-------
* Bhante Jhanarato, Bodhinyana Monastery
* Ryan O'Connell

Changelog
=========

2.0.0
-----

* converted to Python 3
* argparse added for passing the initial date, rather than have it hard-coded
* output is heavily processed with format() to resemble a table
* variable and method names shortened

1.0.0
-----
* Initial version
