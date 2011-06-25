import datetime
from datetime import date, timedelta

class Uposatha:
    rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]

    nextWeekStartDate = None # initialised by calcWeekDates
    nextWeekEndDate = datetime.date(2011, 07, 15) # Uposatha prior to season
    
    # A simple formatting method
    def formatWeek(self, weekNum):
        return "Week %02d: %s TO %s" % (weekNum,
                                        self.nextWeekStartDate.isoformat(),
                                        self.nextWeekEndDate.isoformat())

    # Calculate the beginning and end of the next week
    def calcWeekDates(self, weekNum, lastWeekEndDate):
        self.nextWeekStartDate = lastWeekEndDate + timedelta(1)
        self.nextWeekEndDate   = lastWeekEndDate + timedelta(self.rainsWeeks[weekNum - 1])

    def nextWeek(self, out, weekNum):
        self.calcWeekDates(weekNum, self.nextWeekEndDate)
        out.write(self.formatWeek(weekNum))
        
    # The original script, now being refactored
    def originalScript(self, outputFile):  
        
        out = open(outputFile, 'w')
        
        self.nextWeek(out, 1)
        out.write("\n")
        self.nextWeek(out, 2)
        out.write("\n")
        self.nextWeek(out, 3)
        out.write("\n")
        self.nextWeek(out, 4)
        out.write("\n")
        self.nextWeek(out, 5)
        out.write("\n")
        self.nextWeek(out, 6)
        out.write("\n")
        self.nextWeek(out, 7)
        out.write("\n")
        self.nextWeek(out, 8)
        out.write("\n")
        self.nextWeek(out, 9)
        out.write("\n")
        self.nextWeek(out, 10)
        out.write("\n")
        self.nextWeek(out, 11)
        out.write("\n")
        self.nextWeek(out, 12)
        
