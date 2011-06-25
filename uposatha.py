import datetime
from datetime import date, timedelta

class Uposatha:
    rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]
    weekNum = 0 # Current week index
    
    nextWeekStartDate = None # initialised by calcWeekDates
    nextWeekEndDate = datetime.date(2011, 07, 15) # Uposatha prior to season

    out = None
    
    # Must be called before originalScript
    def setOutput(self, fileName):
        self.out = open(fileName, 'w')
        
    # A simple formatting method
    def formatWeek(self):
        return "Week %02d: %s TO %s" % (self.weekNum,
                                        self.nextWeekStartDate.isoformat(),
                                        self.nextWeekEndDate.isoformat())

    # Calculate the beginning and end of the next week
    def calcWeekDates(self, lastWeekEndDate):
        self.nextWeekStartDate = lastWeekEndDate + timedelta(1)
        self.nextWeekEndDate   = lastWeekEndDate + timedelta(self.rainsWeeks[self.weekNum])

    def nextWeek(self):
        self.calcWeekDates(self.nextWeekEndDate)
        self.weekNum = self.weekNum + 1

    # The original script, now being refactored
    def originalScript(self):
        for week in range(1, 12):
            self.nextWeek()
            self.out.write(self.formatWeek() + "\n")

        self.nextWeek()
        self.out.write(self.formatWeek()) # Last line has no line feed
        self.out.close()
