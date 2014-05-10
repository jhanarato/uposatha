from datetime import date, timedelta

class Uposatha:
    def __init__(self, filename):
        self.rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]
        self.weekNum = 0 # Current week index
        self.nextWeekStartDate = None # initialised by nextWeek()
        self.nextWeekEndDate = date(2011, 07, 15) # Uposatha prior to season
    
    def formatWeek(self):
        return "Week %02d: %s TO %s" % (
            self.weekNum,
            self.nextWeekStartDate.isoformat(),
            self.nextWeekEndDate.isoformat()
        )
    
    def nextWeek(self):
        lastWeekEndDate = self.nextWeekEndDate
        self.nextWeekStartDate = lastWeekEndDate + timedelta(1)
        self.nextWeekEndDate = lastWeekEndDate + timedelta(self.rainsWeeks[self.weekNum])
        self.weekNum += 1
    
    def calendar(self):
        for week in range(1, 12):
            self.nextWeek()
            print(self.formatWeek() + "\n")
        self.nextWeek()
        print(self.formatWeek()) # Last line has no line feed

class UposathaWriter:
    def formatWeek(self, weekNum, startDate, endDate):
        return "Week %02d: %s TO %s" % (
            self.weekNum,
            startDate.isoformat(),
            endDate.isoformat()
        )

# Main
u = Uposatha("out.txt")
u.calendar()
