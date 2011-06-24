import datetime
from datetime import date, timedelta

class Uposatha:
    rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]

    lastWeekEndDate = datetime.date(2011, 07, 15)
    nextWeekStartDate = None # initialised by doNextWeek
    nextWeekEndDate = None   # initialised by doNextWeek
    
    # A simple formatting method
    def formatWeek(self, weekNum, startDate, endDate):
        return "Week %02d: %s TO %s" % (weekNum,
                                        self.nextWeekStartDate.isoformat(),
                                        self.nextWeekEndDate.isoformat())

    # Method extracted to avoid repertition
    def doNextWeek(self, weekNum, lastWeekEndDate):
        self.nextWeekStartDate = lastWeekEndDate + timedelta(1)
        self.nextWeekEndDate   = lastWeekEndDate + timedelta(self.rainsWeeks[weekNum - 1])
    
    # The original script, now being refactored
    def originalScript(self, outputFile):  
        dayBeforeRains = datetime.date(2011, 07, 15) # Uposatha prior to first day of rains,
                                                     # after uposatha

        self.doNextWeek(1, dayBeforeRains)

        out = open(outputFile, 'w')
        
        out.write(self.formatWeek(1, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(2, self.nextWeekEndDate)
        
        out.write(self.formatWeek(2, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(3, self.nextWeekEndDate)      

        out.write(self.formatWeek(3, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(4, self.nextWeekEndDate)
        
        out.write(self.formatWeek(4, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(5, self.nextWeekEndDate)
        
        out.write(self.formatWeek(5, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(6, self.nextWeekEndDate)
        
        out.write(self.formatWeek(6, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(7, self.nextWeekEndDate)
        
        out.write(self.formatWeek(7, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(8, self.nextWeekEndDate)
        
        out.write(self.formatWeek(8, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(9, self.nextWeekEndDate)
        
        out.write(self.formatWeek(9, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(10, self.nextWeekEndDate)
        
        out.write(self.formatWeek(10, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(11, self.nextWeekEndDate)
        
        out.write(self.formatWeek(11, self.nextWeekStartDate, self.nextWeekEndDate) + "\n")

        self.doNextWeek(12, self.nextWeekEndDate)
        
        out.write(self.formatWeek(12, self.nextWeekStartDate, self.nextWeekEndDate))
