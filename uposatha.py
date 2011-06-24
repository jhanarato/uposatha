import datetime
from datetime import date, timedelta

dayBeforeRains = datetime.date(2011, 07, 15) # First day of rains, after uposatha
week1start = dayBeforeRains + timedelta(1)
week1end = dayBeforeRains + timedelta(8)

print "Week 01: " + week1start.isoformat() + " TO " + week1end.isoformat()

week2start = week1end + timedelta(1)
week2end =   week1end + timedelta(7)

print "Week 02: " + week2start.isoformat() + " TO " + week2end.isoformat()

week3start = week2end + timedelta(1)
week3end =   week2end + timedelta(8)

print "Week 03: " + week3start.isoformat() + " TO " + week3end.isoformat()

week4start = week3end + timedelta(1)
week4end =   week3end + timedelta(7)

print "Week 04: " + week4start.isoformat() + " TO " + week4end.isoformat()

week5start = week4end + timedelta(1)
week5end =   week4end + timedelta(7)

print "Week 05: " + week5start.isoformat() + " TO " + week5end.isoformat()

week6start = week5end + timedelta(1)
week6end =   week5end + timedelta(7)

print "Week 06: " + week6start.isoformat() + " TO " + week6end.isoformat()

week7start = week6end + timedelta(1)
week7end =   week6end + timedelta(8)

print "Week 07: " + week7start.isoformat() + " TO " + week7end.isoformat()

week8start = week7end + timedelta(1)
week8end =   week7end + timedelta(7)

print "Week 08: " + week8start.isoformat() + " TO " + week8end.isoformat()

week9start = week8end + timedelta(1)
week9end =   week8end + timedelta(8)

print "Week 09: " + week9start.isoformat() + " TO " + week9end.isoformat()

week10start = week9end + timedelta(1)
week10end =   week9end + timedelta(7)

print "Week 10: " + week10start.isoformat() + " TO " + week10end.isoformat()

week11start = week10end + timedelta(1)
week11end =   week10end + timedelta(8)

print "Week 11: " + week11start.isoformat() + " TO " + week11end.isoformat()

week12start = week11end + timedelta(1)
week12end =   week11end + timedelta(7)

print "Week 12: " + week12start.isoformat() + " TO " + week12end.isoformat()
