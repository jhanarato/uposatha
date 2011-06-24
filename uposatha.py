import datetime
from datetime import date, timedelta

class Uposatha:
    # A simple formatting method
    def formatWeek(self, weekNum, startDate, endDate):
        return "Week %02d: %s TO %s\n" % (weekNum, startDate.isoformat(), endDate.isoformat() + "\n")

    # The original script, now being refactored
    def originalScript(self, outputFile):  
        dayBeforeRains = datetime.date(2011, 07, 15) # First day of rains, after uposatha
        week1start = dayBeforeRains + timedelta(1)
        week1end = dayBeforeRains + timedelta(8)

        out = open(outputFile, 'w')
        
        out.write("Week 01: " + week1start.isoformat() + " TO " + week1end.isoformat() + "\n")

        week2start = week1end + timedelta(1)
        week2end =   week1end + timedelta(7)

        out.write("Week 02: " + week2start.isoformat() + " TO " + week2end.isoformat() + "\n")

        week3start = week2end + timedelta(1)
        week3end =   week2end + timedelta(8)

        out.write("Week 03: " + week3start.isoformat() + " TO " + week3end.isoformat() + "\n")

        week4start = week3end + timedelta(1)
        week4end =   week3end + timedelta(7)

        out.write("Week 04: " + week4start.isoformat() + " TO " + week4end.isoformat() + "\n")

        week5start = week4end + timedelta(1)
        week5end =   week4end + timedelta(7)

        out.write("Week 05: " + week5start.isoformat() + " TO " + week5end.isoformat() + "\n")

        week6start = week5end + timedelta(1)
        week6end =   week5end + timedelta(7)

        out.write("Week 06: " + week6start.isoformat() + " TO " + week6end.isoformat() + "\n")

        week7start = week6end + timedelta(1)
        week7end =   week6end + timedelta(8)

        out.write("Week 07: " + week7start.isoformat() + " TO " + week7end.isoformat() + "\n")

        week8start = week7end + timedelta(1)
        week8end =   week7end + timedelta(7)

        out.write("Week 08: " + week8start.isoformat() + " TO " + week8end.isoformat() + "\n")

        week9start = week8end + timedelta(1)
        week9end =   week8end + timedelta(8)

        out.write("Week 09: " + week9start.isoformat() + " TO " + week9end.isoformat() + "\n")

        week10start = week9end + timedelta(1)
        week10end =   week9end + timedelta(7)

        out.write("Week 10: " + week10start.isoformat() + " TO " + week10end.isoformat() + "\n")

        week11start = week10end + timedelta(1)
        week11end =   week10end + timedelta(8)

        out.write("Week 11: " + week11start.isoformat() + " TO " + week11end.isoformat() + "\n")

        week12start = week11end + timedelta(1)
        week12end =   week11end + timedelta(7)

        out.write( "Week 12: " + week12start.isoformat() + " TO " + week12end.isoformat())
