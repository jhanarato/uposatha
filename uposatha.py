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
        
        self.calcWeekDates(2, self.nextWeekEndDate)
        out.write(self.formatWeek(2) + "\n")
        
        self.calcWeekDates(3, self.nextWeekEndDate)      
        out.write(self.formatWeek(3) + "\n")

        self.calcWeekDates(4, self.nextWeekEndDate)
        out.write(self.formatWeek(4) + "\n")

        self.calcWeekDates(5, self.nextWeekEndDate)
        out.write(self.formatWeek(5) + "\n")

        self.calcWeekDates(6, self.nextWeekEndDate)
        out.write(self.formatWeek(6) + "\n")

        self.calcWeekDates(7, self.nextWeekEndDate)
        out.write(self.formatWeek(7) + "\n")

        self.calcWeekDates(8, self.nextWeekEndDate)
        out.write(self.formatWeek(8) + "\n")

        self.calcWeekDates(9, self.nextWeekEndDate)
        out.write(self.formatWeek(9) + "\n")

        self.calcWeekDates(10, self.nextWeekEndDate)
        out.write(self.formatWeek(10) + "\n")

        self.calcWeekDates(11, self.nextWeekEndDate)
        out.write(self.formatWeek(11) + "\n")

        self.calcWeekDates(12, self.nextWeekEndDate)
        out.write(self.formatWeek(12))
