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

        self.doNextWeek(1, dayBeforeRains)
        
        week1start = self.nextWeekStartDate
        week1end = self.nextWeekEndDate

        out = open(outputFile, 'w')
        
        out.write(self.formatWeek(1, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(2, self.nextWeekEndDate)
        
        week2start = self.nextWeekStartDate
        week2end = self.nextWeekEndDate

        out.write(self.formatWeek(2, week2start, week2end) + "\n")

        self.doNextWeek(3, self.nextWeekEndDate)
        
        week3start = self.nextWeekStartDate
        week3end = self.nextWeekEndDate

        out.write(self.formatWeek(3, week3start, week3end) + "\n")

        self.doNextWeek(4, self.nextWeekEndDate)
        
        week4start = self.nextWeekStartDate
        week4end = self.nextWeekEndDate

        out.write(self.formatWeek(4, week4start, week4end) + "\n")

        self.doNextWeek(5, self.nextWeekEndDate)
        
        week5start = self.nextWeekStartDate
        week5end = self.nextWeekEndDate

        out.write(self.formatWeek(5, week5start, week5end) + "\n")

        self.doNextWeek(6, self.nextWeekEndDate)
        
        week6start = self.nextWeekStartDate
        week6end = self.nextWeekEndDate

        out.write(self.formatWeek(6, week6start, week6end) + "\n")

        self.doNextWeek(7, self.nextWeekEndDate)
        
        week7start = self.nextWeekStartDate
        week7end = self.nextWeekEndDate
        
        out.write(self.formatWeek(7, week7start, week7end) + "\n")

        self.doNextWeek(8, self.nextWeekEndDate)
        
        week8start = self.nextWeekStartDate
        week8end = self.nextWeekEndDate

        out.write(self.formatWeek(8, week8start, week8end) + "\n")

        self.doNextWeek(9, self.nextWeekEndDate)
        
        week9start = self.nextWeekStartDate
        week9end = self.nextWeekEndDate

        out.write(self.formatWeek(9, week9start, week9end) + "\n")

        self.doNextWeek(10, self.nextWeekEndDate)
        
        week10start = self.nextWeekStartDate
        week10end = self.nextWeekEndDate

        out.write(self.formatWeek(10, week10start, week10end) + "\n")

        self.doNextWeek(11, self.nextWeekEndDate)
        
        week11start = self.nextWeekStartDate
        week11end = self.nextWeekEndDate

        out.write(self.formatWeek(11, week11start, week11end) + "\n")

        self.doNextWeek(12, self.nextWeekEndDate)
        
        week12start = self.nextWeekStartDate
        week12end = self.nextWeekEndDate

        out.write(self.formatWeek(12, week12start, week12end))
