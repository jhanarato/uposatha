import datetime
from datetime import date, timedelta

class Uposatha:
    rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]
    weekNum = 1 # Current week index
    
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

    def nextWeek(self):
        self.calcWeekDates(self.weekNum, self.nextWeekEndDate)
        self.out.write(self.formatWeek(self.weekNum))
        self.weekNum = self.weekNum + 1
        
    # The original script, now being refactored
    def originalScript(self):
        for foo in range(1, 12):
            self.nextWeek()
            self.out.write("\n")

        self.nextWeek() # Last line has no line feed
        self.out.close()
