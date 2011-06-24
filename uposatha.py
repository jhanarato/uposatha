import datetime
from datetime import date, timedelta

class Uposatha:
    rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]

    lastWeekEndDate = datetime.date(2011, 07, 15)
    nextWeekStartDate = None # initialised by doNextWeek
    nextWeekEndDate = None   # initialised by doNextWeek
    
    # A simple formatting method
    def formatWeek(self, weekNum, startDate, endDate):
        return "Week %02d: %s TO %s" % (weekNum, startDate.isoformat(), endDate.isoformat())

    # Method extracted to avoid repertition
    def doNextWeek(self, weekNum, lastWeekEndDate):
        self.nextWeekStartDate = lastWeekEndDate + timedelta(1)
        self.nextWeekEndDate   = lastWeekEndDate + timedelta(self.rainsWeeks[weekNum - 1])
    
    # The original script, now being refactored
    def originalScript(self, outputFile):  
        dayBeforeRains = datetime.date(2011, 07, 15) # Uposatha prior to first day of rains,
                                                     # after uposatha
        
        week1start = dayBeforeRains + timedelta(1)
        week1end = dayBeforeRains + timedelta(self.rainsWeeks[0])

        out = open(outputFile, 'w')
        
        out.write(self.formatWeek(1, week1start, week1end) + "\n")

        week2start = week1end + timedelta(1)
        week2end =   week1end + timedelta(self.rainsWeeks[1])

        out.write(self.formatWeek(2, week2start, week2end) + "\n")

        week3start = week2end + timedelta(1)
        week3end =   week2end + timedelta(self.rainsWeeks[2])

        out.write(self.formatWeek(3, week3start, week3end) + "\n")

        week4start = week3end + timedelta(1)
        week4end =   week3end + timedelta(self.rainsWeeks[3])

        out.write(self.formatWeek(4, week4start, week4end) + "\n")

        week5start = week4end + timedelta(1)
        week5end =   week4end + timedelta(self.rainsWeeks[4])

        out.write(self.formatWeek(5, week5start, week5end) + "\n")

        week6start = week5end + timedelta(1)
        week6end =   week5end + timedelta(self.rainsWeeks[5])

        out.write(self.formatWeek(6, week6start, week6end) + "\n")

        week7start = week6end + timedelta(1)
        week7end =   week6end + timedelta(self.rainsWeeks[6])

        out.write(self.formatWeek(7, week7start, week7end) + "\n")

        week8start = week7end + timedelta(1)
        week8end =   week7end + timedelta(self.rainsWeeks[7])

        out.write(self.formatWeek(8, week8start, week8end) + "\n")

        week9start = week8end + timedelta(1)
        week9end =   week8end + timedelta(self.rainsWeeks[8])

        out.write(self.formatWeek(9, week9start, week9end) + "\n")

        week10start = week9end + timedelta(1)
        week10end =   week9end + timedelta(self.rainsWeeks[9])

        out.write(self.formatWeek(10, week10start, week10end) + "\n")

        week11start = week10end + timedelta(1)
        week11end =   week10end + timedelta(self.rainsWeeks[10])

        out.write(self.formatWeek(11, week11start, week11end) + "\n")

        week12start = week11end + timedelta(1)
        week12end =   week11end + timedelta(self.rainsWeeks[11])

        out.write(self.formatWeek(12, week12start, week12end))
