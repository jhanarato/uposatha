#!/usr/bin/env python3

from datetime import date, timedelta

class Uposatha:
    def __init__(self, filename):
        self.rainsWeeks = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]
        self.weekNo = 0 # Current week index
        self.nextA = None # initialised by advance()
        self.nextB = date(2011, 07, 15) # Uposatha prior to season
    
    def getWeek(self):
        return "Week {no:02d}: {start} -> {end}".format(
            no=self.weekNo,
            start=self.nextA.isoformat(),
            end=self.nextB.isoformat()
        )
    
    def advance(self):
        lastB = self.nextB
        self.nextA = lastB + timedelta(1)
        self.nextB = lastB + timedelta(self.rainsWeeks[self.weekNo])
        self.weekNo += 1
    
    def calendar(self):
        for i in range(1, 12):
            self.advance()
            print(self.getWeek())
        self.advance()
        print(self.getWeek()) # Last line has no line feed

# Main
u = Uposatha("out.txt")
u.calendar()
