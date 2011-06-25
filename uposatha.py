import datetime
from datetime import date, timedelta

class Uposatha:
    rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]

    nextWeekStartDate = None # initialised by calcWeekDates
    nextWeekEndDate = datetime.date(2011, 07, 15) # Uposatha prior to season

    out = None
    
    # Must be called before originalScript
    def setOutput(self, fileName):
        self.out = open(fileName, 'w')
        
    # A simple formatting method
    def formatWeek(self, weekNum):
        return "Week %02d: %s TO %s" % (weekNum,
                                        self.nextWeekStartDate.isoformat(),
                                        self.nextWeekEndDate.isoformat())

    # Calculate the beginning and end of the next week
    def calcWeekDates(self, weekNum, lastWeekEndDate):
        self.nextWeekStartDate = lastWeekEndDate + timedelta(1)
        self.nextWeekEndDate   = lastWeekEndDate + timedelta(self.rainsWeeks[weekNum - 1])

    def nextWeek(self, weekNum):
        self.calcWeekDates(weekNum, self.nextWeekEndDate)
        self.out.write(self.formatWeek(weekNum))
        
    # The original script, now being refactored
    def originalScript(self):
        self.nextWeek(1)
        self.out.write("\n")
        self.nextWeek(2)
        self.out.write("\n")
        self.nextWeek(3)
        self.out.write("\n")
        self.nextWeek(4)
        self.out.write("\n")
        self.nextWeek(5)
        self.out.write("\n")
        self.nextWeek(6)
        self.out.write("\n")
        self.nextWeek(7)
        self.out.write("\n")
        self.nextWeek(8)
        self.out.write("\n")
        self.nextWeek(9)
        self.out.write("\n")
        self.nextWeek(10)
        self.out.write("\n")
        self.nextWeek(11)
        self.out.write("\n")
        self.nextWeek(12)
        self.out.close()
        
